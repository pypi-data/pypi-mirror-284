from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys, os, json
import numpy as np
from functools import partial
from snub.gui.utils import IntervalIndex, CheckBox, CustomContextMenu
from snub.gui.stacks import PanelStack, TrackStack
from snub.gui.tracks import TracePlot
from snub.gui.help import HelpMenu

WIDGET_NAMES = [
    "annotator",
    "heatmap",
    "video",
    "traceplot",
    "spikeplot",
    "roiplot",
    "scatter",
    "pose3D",
]


def set_style(app):
    # https://www.wenzhaodesign.com/devblog/python-pyside2-simple-dark-theme
    # button from here https://github.com/persepolisdm/persepolis/blob/master/persepolis/gui/palettes.py
    app.setStyle(QStyleFactory.create("Fusion"))

    darktheme = QPalette()
    darktheme.setColor(QPalette.Window, QColor(45, 45, 45))
    darktheme.setColor(QPalette.WindowText, QColor(222, 222, 222))
    darktheme.setColor(QPalette.Button, QColor(45, 45, 45))
    darktheme.setColor(QPalette.ButtonText, QColor(222, 222, 222))
    darktheme.setColor(QPalette.AlternateBase, QColor(222, 222, 222))
    # darktheme.setColor(QPalette.AlternateBase, QColor(0, 222, 0))
    darktheme.setColor(QPalette.ToolTipBase, QColor(222, 222, 222))
    darktheme.setColor(QPalette.Highlight, QColor(45, 45, 45))
    darktheme.setColor(QPalette.Disabled, QPalette.Light, QColor(60, 60, 60))
    darktheme.setColor(QPalette.Disabled, QPalette.Shadow, QColor(50, 50, 50))
    darktheme.setColor(QPalette.Disabled, QPalette.ButtonText, QColor(111, 111, 111))
    darktheme.setColor(QPalette.Disabled, QPalette.Text, QColor(122, 118, 113))
    darktheme.setColor(QPalette.Disabled, QPalette.WindowText, QColor(122, 118, 113))
    darktheme.setColor(QPalette.Disabled, QPalette.Base, QColor(32, 32, 32))
    app.setPalette(darktheme)
    return app


class ProjectTab(QWidget):
    """
    Return the most important thing about a person.
    Parameters
    ----------
    your_name
        A string indicating the name of the person.
    """

    new_current_position = pyqtSignal(int)

    def __init__(self, project_directory):
        super().__init__()
        # load config
        self.project_directory = project_directory
        self.name = project_directory.strip(os.path.sep).split(os.path.sep)[-1]
        self.layout_mode = None
        config_path = os.path.join(self.project_directory, "config.json")
        config = json.load(open(config_path, "r"))
        config, error_messages = self.validate_and_autofill_config(config)
        if len(error_messages) > 0:
            self.config_error(config_path, error_messages)
            return

        # initialize state variables
        self.playing = False
        self.bounds = config["bounds"]
        self.layout_mode = config["layout_mode"]
        self.current_time = config["init_current_time"]
        self.play_speed = config["initial_playspeed"]
        self.animation_step = 1 / config["animation_fps"]
        self.track_playhead = config["track_playhead"]

        # keep track of current selection
        self.selected_intervals = IntervalIndex(min_step=config["min_step"])

        # create major gui elements
        self.panelStack = PanelStack(config, self.selected_intervals)
        self.trackStack = TrackStack(config, self.selected_intervals)

        # timer for live play
        self.timer = QTimer(self)

        # controls along bottom row
        self.play_button = QPushButton()
        self.speed_slider = QSlider(Qt.Horizontal)
        self.speed_label = QLabel()
        self.track_playhead_checkbox = CheckBox(self.track_playhead)
        self.track_playhead_checkbox.stateChanged.connect(self.update_track_playhead)

        # connect signals and slots
        self.speed_slider.valueChanged.connect(self.change_play_speed)
        self.play_button.clicked.connect(self.toggle_play_state)
        self.trackStack.new_current_time.connect(self.update_current_time)
        self.trackStack.selection_change.connect(self.update_selected_intervals)
        for panel in self.panelStack.widgets:
            panel.new_current_time.connect(self.update_current_time)
            panel.selection_change.connect(self.update_selected_intervals)
        for track in self.trackStack.tracks_flat():
            track.new_current_time.connect(self.update_current_time)
            if isinstance(track, TracePlot):
                if track.bound_rois is not None:
                    track.bind_rois(self.panelStack.get_by_name(track.bound_rois))
        self.timer.timeout.connect(self.increment_current_time)

        # initialize layout
        self.initUI()
        self.trackStack.update_current_range()
        self.update_current_time(self.current_time)

    def initUI(self):
        self.splitter = QSplitter(Qt.Horizontal)
        self.splitter.addWidget(self.panelStack)
        self.splitter.addWidget(self.trackStack)

        self.play_icon = QIcon(
            QPixmap(
                os.path.join(
                    os.path.dirname(os.path.realpath(__file__)), "icons", "play.png"
                )
            )
        )
        self.pause_icon = QIcon(
            QPixmap(
                os.path.join(
                    os.path.dirname(os.path.realpath(__file__)), "icons", "pause.png"
                )
            )
        )
        self.play_button.setIcon(self.play_icon)
        self.play_button.setIconSize(QSize(12, 12))

        self.speed_label.setText("{}X".format(self.play_speed))
        self.speed_label.setMinimumWidth(35)
        self.speed_slider.setMinimum(0 - 2)
        self.speed_slider.setMaximum(7)
        self.speed_slider.setValue(0)
        self.speed_slider.setTickPosition(QSlider.TicksBothSides)
        self.speed_slider.setTickInterval(1)
        self.speed_slider.setMaximumWidth(150)

        buttons = QHBoxLayout()
        buttons.addStretch(0)
        buttons.addWidget(self.play_button)
        buttons.addSpacing(10)
        label = QLabel("Playback Speed:")
        label.setFixedHeight(25)
        buttons.addWidget(label)
        buttons.addWidget(self.speed_slider)
        buttons.addWidget(self.speed_label)
        buttons.addSpacing(20)
        buttons.addWidget(self.track_playhead_checkbox)
        label = QLabel("Track Playhead")
        label.setFixedHeight(25)
        buttons.addWidget(label)
        buttons.addStretch(0)

        layout = QVBoxLayout(self)
        layout.addWidget(self.splitter)
        layout.addLayout(buttons)
        self.change_layout_mode(self.layout_mode)

    def update_track_playhead(self, checkstate):
        self.track_playhead = checkstate
        if self.track_playhead:
            self.trackStack.center_at_time(self.current_time)

    def validate_and_autofill_config(self, config):
        error_messages = []

        # check for required global keys
        for k in ["bounds"]:
            if not k in config:
                error_messages.append('config is missing the key "{}"'.format(k))

        # initialize current time if not provided
        if not "init_current_time" in config:
            if "bounds" in config:
                config["init_current_time"] = config["bounds"][0]
            else:
                config["init_current_time"] = 0

        # autofill missing keys
        default_config = {
            "layout_mode": "columns",
            "min_step": 1 / 30,
            "zoom_gain": 0.003,
            "min_range": 0.01,
            "initial_playspeed": 1,
            "animation_fps": 30,
            "track_playhead": True,
            "panels_size_ratio": 1,
            "tracks_size_ratio": 2,
            "spikeplot": [],
            "traceplot": [],
            "roiplot": [],
            "scatter": [],
            "heatmap": [],
            "annotator": [],
            "pose3D": [],
            "video": [],
            "markers": {},
        }
        for key, value in default_config.items():
            if not key in config:
                config[key] = value

        # check for required keys in each widget
        for widget_name, requred_keys in {
            "heatmap": ["name", "data_path", "intervals_path", "add_traceplot"],
            "annotator": ["name", "data_path"],
            "video": ["name", "video_path", "timestamps_path"],
            "traceplot": ["name", "data_path"],
            "spikeplot": ["name", "heatmap_path", "spikes_path", "intervals_path"],
            "roiplot": ["name", "video_paths", "rois_path", "timestamps_path"],
            "scatter": ["name", "data_path"],
        }.items():
            for props in config[widget_name]:
                for k in requred_keys:
                    if not k in props:
                        error_messages.append(
                            '{} is missing the key "{}"'.format(widget_name, k)
                        )

        # resolve paths
        for widget_name in WIDGET_NAMES:
            for widget_config in config[widget_name]:
                for k, v in widget_config.items():
                    if k.endswith("_path"):
                        if not os.path.isabs(v):
                            widget_config[k] = os.path.join(self.project_directory, v)

        return config, error_messages

    def config_error(self, config_path, error_messages):
        title = QLabel("The following config file is incomplete")
        path = QLabel("   " + config_path)
        errors = QLabel(
            "<html><ul><li>" + "</li><li>".join(error_messages) + "</li></ul></html>"
        )

        title.setFont(QFont("Arial", 24, QFont.Bold))
        font = QFont("Arial", 16)
        font.setItalic(True)
        path.setFont(font)
        errors.setFont(QFont("Arial", 18))

        text_layout = QVBoxLayout()
        text_layout.setSpacing(10)
        text_layout.addStretch(0)
        text_layout.addWidget(title)
        text_layout.addWidget(path)
        text_layout.addWidget(errors)
        text_layout.addStretch(0)
        layout = QHBoxLayout(self)
        layout.addStretch(0)
        layout.addLayout(text_layout)
        layout.addStretch(0)

    def change_layout_mode(self, layout_mode):
        self.splitter.setOrientation(
            {"columns": Qt.Horizontal, "rows": Qt.Vertical}[layout_mode]
        )
        self.panelStack.change_layout_mode(layout_mode)
        self.trackStack.change_layout_mode(layout_mode)

    def change_play_speed(self, log2_speed):
        self.play_speed = round(2**log2_speed, 2)
        self.speed_label.setText("{}X".format(self.play_speed))

    def deselect_all(self):
        self.selected_intervals.clear()
        self.update_selected_intervals([], [])

    def update_selected_intervals(self, intervals, is_selected):
        for (start, end), sel in zip(intervals, is_selected):
            if sel:
                self.selected_intervals.add_interval(start, end)
            else:
                self.selected_intervals.remove_interval(start, end)
        self.trackStack.update_selected_intervals()
        self.panelStack.update_selected_intervals()

    def update_current_time(self, current_time):
        self.current_time = current_time
        self.trackStack.update_current_time(current_time)
        self.panelStack.update_current_time(current_time)

    def increment_current_time(self):
        new_time = self.current_time + self.play_speed * self.animation_step
        if new_time >= self.bounds[1]:
            new_time = self.bounds[0]
        self.update_current_time(new_time)
        if self.track_playhead:
            if (
                self.current_time > self.trackStack.current_range[1]
                or self.current_time < self.trackStack.current_range[0]
            ):
                self.trackStack.center_at_time(self.current_time)

    def toggle_play_state(self):
        if self.playing:
            self.pause()
        else:
            self.play()

    def play(self):
        self.timer.start(1000 * self.animation_step)
        self.play_button.setIcon(self.pause_icon)
        self.playing = True

    def pause(self):
        self.timer.stop()
        self.play_button.setIcon(self.play_icon)
        self.playing = False

    def copy_tab_name(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.name)


class CustomTabBar(QTabBar):
    def __init__(self, parent=None):
        super(CustomTabBar, self).__init__(parent)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)

    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            self.showContextMenu(event.pos())
        else:
            super(CustomTabBar, self).mousePressEvent(event)

    def showContextMenu(self, pos):
        global_pos = self.mapToGlobal(pos)
        index = self.tabAt(pos)
        if index != -1:
            contextMenu = CustomContextMenu(self)
            close_action = contextMenu.add_item(
                "Close Tab", lambda: self.parent().removeTab(index)
            )
            copy_action = contextMenu.add_item(
                "Copy Name", lambda: self.copyTabName(index)
            )
            contextMenu.exec_(global_pos)

    def copyTabName(self, index):
        clipboard = QApplication.clipboard()
        tab_name = self.tabText(index)
        clipboard.setText(tab_name)


class MainWindow(QMainWindow):
    """
    Main window that contains menu bar and tab widget. Contains methods for
    opening, reloading, and closing project tabs.
    """

    def __init__(self, args):
        super().__init__()
        self.tabs = QTabWidget()
        self.tabs.setTabBar(CustomTabBar(self.tabs))
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.tabs.currentChanged.connect(self.tab_changed)
        self.setCentralWidget(self.tabs)
        self.setWindowTitle("Systems Neuro Browser")

        open_project = QAction("&Open Project", self)
        open_project.setShortcut("Ctrl+O")
        open_project.triggered.connect(self.open)

        reload_data = QAction("&Reload Data", self)
        reload_data.setShortcut("Ctrl+R")
        reload_data.triggered.connect(self.reload_data)

        save_selection = QAction("Save Selection", self)
        save_selection.triggered.connect(self.save_selection)

        load_selection = QAction("Load Selection", self)
        load_selection.triggered.connect(self.load_selection)

        deselect_all = QAction("&Deselect All", self)
        deselect_all.triggered.connect(self.deselect_all)

        self.set_layout_to_rows = QAction("&Rows", self)
        self.set_layout_to_cols = QAction("&Columns", self)
        self.set_layout_to_rows.setCheckable(True)
        self.set_layout_to_cols.setCheckable(True)
        self.set_layout_to_rows.triggered.connect(
            partial(self.change_layout_mode, "rows")
        )
        self.set_layout_to_cols.triggered.connect(
            partial(self.change_layout_mode, "columns")
        )

        mainMenu = self.menuBar()
        mainMenu.setNativeMenuBar(False)

        fileMenu = mainMenu.addMenu("&File")
        fileMenu.addAction(open_project)
        fileMenu.addAction(reload_data)
        fileMenu.addAction(save_selection)
        fileMenu.addAction(load_selection)

        editMenu = mainMenu.addMenu("&Edit")
        editMenu.addAction(deselect_all)

        windowMenu = mainMenu.addMenu("&Window")
        layoutMenu = windowMenu.addMenu("&Layout...")
        layoutMenu.addAction(self.set_layout_to_cols)
        layoutMenu.addAction(self.set_layout_to_rows)

        helpMenu = HelpMenu(self)
        mainMenu.addMenu(helpMenu.get_menu())

        # try to open projects that are passed as command line arguments
        self.open(project_directories=args)

    def deselect_all(self):
        self.tabs.currentWidget().deselect_all()

    def change_layout_mode(self, layout_mode):
        current_tab = self.tabs.currentWidget()
        current_tab.change_layout_mode(layout_mode)
        self.set_layout_to_cols.setChecked(layout_mode == "columns")
        self.set_layout_to_rows.setChecked(layout_mode == "rows")

    def tab_changed(self, i):
        if i >= 0:
            current_tab = self.tabs.widget(i)
            self.set_layout_to_cols.setChecked(current_tab.layout_mode == "columns")
            self.set_layout_to_rows.setChecked(current_tab.layout_mode == "rows")

    def close_tab(self, i):
        self.tabs.removeTab(i)

    def open(self, *args, project_directories=None):
        if project_directories is None:
            project_directories = self.getExistingDirectories()
        error_directories = []
        for project_dir in project_directories:
            if len(project_dir) > 0:
                if os.path.exists(os.path.join(project_dir, "config.json")):
                    self.load_project(project_dir)
                else:
                    error_directories.append(project_dir)
        if len(error_directories) > 0:
            QMessageBox.about(
                self,
                "",
                "\n\n".join(
                    ["The following directories lack a config file."]
                    + error_directories
                ),
            )

    def reload_data(self):
        current_index = self.tabs.currentIndex()
        if current_index == -1:
            return  # no tab
        current_tab = self.tabs.currentWidget()
        project_dir = current_tab.project_directory
        self.close_tab(current_index)
        self.load_project(project_dir)

    def load_project(self, project_directory):
        project_tab = ProjectTab(project_directory)
        self.tabs.addTab(project_tab, project_tab.name)
        self.tabs.setCurrentWidget(project_tab)

    def getExistingDirectories(self):
        """
        Workaround for selecting multiple directories
        adopted from http://www.qtcentre.org/threads/34226-QFileDialog-select-multiple-directories?p=158482#post158482
        This also give control about hidden folders
        """
        dlg = QFileDialog(self)
        dlg.setOption(dlg.DontUseNativeDialog, True)
        dlg.setOption(dlg.HideNameFilterDetails, True)
        dlg.setFileMode(dlg.Directory)
        dlg.setOption(dlg.ShowDirsOnly, True)
        dlg.findChildren(QListView)[0].setSelectionMode(
            QAbstractItemView.ExtendedSelection
        )
        dlg.findChildren(QTreeView)[0].setSelectionMode(
            QAbstractItemView.ExtendedSelection
        )
        if dlg.exec_() == QDialog.Accepted:
            return dlg.selectedFiles()
        return [
            str(),
        ]

    def load_selection(self):
        current_index = self.tabs.currentIndex()
        if current_index == -1:
            QMessageBox.warning(self, "Error: No project is open")
            return  # no tab

        # get path of file to load
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Load Selection",
            "",
            "All Files (*);;CSV Files (*.csv)",
            options=options,
        )

        if file_name:
            try:
                self.deselect_all()
                intervals = np.loadtxt(file_name, delimiter=",", skiprows=1)
                if len(intervals) > 0:
                    is_selected = np.ones(len(intervals)) > 0
                    self.tabs.currentWidget().update_selected_intervals(
                        intervals, is_selected
                    )
            except Exception as e:
                QMessageBox.warning(
                    self, "Error", f"Failed to load selection: {str(e)}"
                )

    def save_selection(self):
        current_index = self.tabs.currentIndex()
        if current_index == -1:
            QMessageBox.warning(self, "Error: No project is open")
            return  # no tab

        selected_intervals = self.tabs.currentWidget().selected_intervals.intervals
        if len(selected_intervals) == 0:
            QMessageBox.warning(self, "Error: Nothing is selected")
            return  # no tab

        # get path of file to save
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getSaveFileName(
            self, "Save Selection", "", "CSV Files (*.csv)", options=options
        )

        if file_name:

            if not file_name.lower().endswith(".csv"):
                file_name += ".csv"

            try:
                # generate csv text
                text = ["start,end"]
                for s, e in selected_intervals:
                    text.append(f"{s},{e}")
                text = "\n".join(text) + "\n"

                # write to file
                with open(file_name, "w") as file:
                    file.write(text)
            except Exception as e:
                QMessageBox.warning(
                    self, "Error", f"Failed to save selection: {str(e)}"
                )


def run():
    app = QApplication(sys.argv)
    app = set_style(app)
    icon_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "icons", "app_icon.png"
    )
    app.setWindowIcon(QIcon(icon_path))

    window = MainWindow(sys.argv[1:])
    window.resize(1500, 900)

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    run()
