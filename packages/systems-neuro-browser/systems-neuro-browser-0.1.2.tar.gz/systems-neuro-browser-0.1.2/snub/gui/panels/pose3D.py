from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import numpy as np
import os

from vispy.scene import SceneCanvas
from vispy.scene.visuals import Markers, Line

from snub.gui.panels import Panel
from snub.gui.utils import HeaderMixin


class Pose3DPanel(Panel, HeaderMixin):
    def __init__(
        self,
        config,
        data_path=None,
        labels_path=None,
        intervals_path=None,
        joint_colors_path=None,
        link_colors_path=None,
        links_path=None,
        joint_size=5,
        link_width=2,
        scaling=True,
        floor_bounds=None,
        floor_height=0,
        floor_spacing=10,
        floor_color=(1, 1, 1, 0.5),
        **kwargs
    ):
        super().__init__(config, **kwargs)

        self.data = np.load(data_path)
        self.intervals = np.load(intervals_path)

        if labels_path is None:
            self.labels = [str(i) for i in range(self.data.shape[0])]
        else:
            self.labels = open(labels_path, "r").read().split("\n")
        if links_path is None:
            self.link_indexes = np.zeros((0, 2), dtype=int)
        else:
            self.link_indexes = np.load(links_path).astype(int)
        if joint_colors_path is None:
            self.joint_colors = np.ones((self.data.shape[0], 3))
        else:
            self.joint_colors = np.load(joint_colors_path)

        if link_colors_path is None:
            self.link_colors = np.ones((len(self.links) * 2, 3))
        else:
            self.link_colors = np.repeat(np.load(link_colors_path), 2, axis=0)

        self.joint_size = joint_size
        self.link_width = link_width
        self.scaling = scaling

        self.canvas = SceneCanvas(keys="interactive", show=True)
        self.view = self.canvas.central_widget.add_view(camera="arcball")
        self.view.camera.scale_factor = 500
        self.joints = Markers(
            scaling=self.scaling, spherical=True, antialias=0, parent=self.view.scene
        )
        self.links = Line(
            width=self.link_width,
            connect="segments",
            method="gl",
            parent=self.view.scene,
        )

        if floor_bounds is not None:
            xs = np.arange(
                floor_bounds[0], floor_bounds[1] + floor_spacing, floor_spacing
            )
            ys = np.arange(
                floor_bounds[2], floor_bounds[3] + floor_spacing, floor_spacing
            )
            if len(xs) > 1 and len(ys) > 1:
                pos = np.vstack(
                    [
                        np.stack(
                            [
                                np.stack(
                                    [
                                        xs,
                                        ys.min() * np.ones_like(xs),
                                        floor_height * np.ones_like(xs),
                                    ],
                                    axis=1,
                                ),
                                np.stack(
                                    [
                                        xs,
                                        ys.max() * np.ones_like(xs),
                                        floor_height * np.ones_like(xs),
                                    ],
                                    axis=1,
                                ),
                            ],
                            axis=1,
                        ).reshape(-1, 3),
                        np.stack(
                            [
                                np.stack(
                                    [
                                        xs.min() * np.ones_like(ys),
                                        ys,
                                        floor_height * np.ones_like(ys),
                                    ],
                                    axis=1,
                                ),
                                np.stack(
                                    [
                                        xs.max() * np.ones_like(ys),
                                        ys,
                                        floor_height * np.ones_like(ys),
                                    ],
                                    axis=1,
                                ),
                            ],
                            axis=1,
                        ).reshape(-1, 3),
                    ]
                )

                self.floor = Line(
                    pos,
                    width=0.5,
                    color=floor_color,
                    connect="segments",
                    method="gl",
                    parent=self.view.scene,
                )

        # self.update_current_time(config['init_current_time'])
        self.initUI(**kwargs)

    def initUI(self, **kwargs):
        super().initUI(**kwargs)
        self.layout.addWidget(self.canvas.native, 1)

    def update_current_time(self, t):
        ix = self.intervals[:, 1].searchsorted(t)
        if (
            ix < self.intervals.shape[0]
            and self.intervals[ix, 0] <= t
            and t <= self.intervals[ix, 1]
        ):
            self.current_frame_index = ix
        else:
            self.current_frame_index = None
        if self.is_visible:
            self.update_plot()

    def update_plot(self):
        if self.current_frame_index is not None:
            self.joints.set_data(
                pos=self.data[self.current_frame_index],
                size=self.joint_size,
                face_color=self.joint_colors,
            )
            self.links.set_data(
                pos=self.data[self.current_frame_index, self.link_indexes.flat],
                color=self.link_colors,
            )

    def toggle_visiblity(self, *args):
        super().toggle_visiblity(*args)
        if self.is_visible:
            self.update_plot()
