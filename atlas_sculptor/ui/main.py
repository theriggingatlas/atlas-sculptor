# -*- coding: utf-8 -*-
""" UI class to create module from atlas sculptor

Author: Clement Daures
Company: The Rigging Atlas
Website: theriggingatlas.com
Created: 2025

# ---------- LICENSE ----------

Copyright 2025 Clement Daures - The Rigging Atlas

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# ---------- IMPORT ----------

import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                               QHBoxLayout, QPushButton, QLabel, QSpinBox,
                               QLineEdit, QComboBox, QFrame, QGroupBox, QMenuBar)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette, QColor, QAction
from shiboken6 import wrapInstance
import maya.OpenMayaUI as omui

# ---------- MAYA UI ----------

def get_maya_main_window():
    """Return Maya's main window as a QWidget."""
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr), QWidget)

# ---------- UI BUILDER ----------

class AtlasShotSculptorUi(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Atlas Sculptor 1.0.0 - Maya")
        self.setGeometry(100, 100, 320, 480)
        self.setStyleSheet("""
            QWidget {
                background-color: #303030;
                color: #ddd;
                font-family: Segoe UI;
                font-size: 8pt;
            }
            QMenuBar:item:selected {
                background-color: #7a53cf;
                color: #ffffff;
            }
            QMenu::item:selected {
                background-color: #7a53cf;
                color: #fff;
            }
            QPushButton {
                background-color: #404040;
                border: 1px solid #262626;
                border-radius: 4px;
                padding: 4px 8px;
            }
            QPushButton:hover {
                background-color: #404040;
                border: 1px solid #7a53cf;
                border-radius: 4px;
                padding: 4px 8px;
            }
            QComboBox QAbstractItemView {
                selection-background-color: #7a53cf;  
                selection-color: #ffffff;              
                background-color: #262626;            
            }
            QComboBox:hover {
                border: 1px solid #7a53cf;
            }
            QDoubleSpinBox:hover {
                border: 1px solid #7a53cf;
            }
            QLineEdit, QComboBox, QDoubleSpinBox {
                background-color: #404040;
                border: 1px solid #555;
                border-radius: 3px;
                padding: 2px;
            }
            QGroupBox {
                border: 1px solid #7a53cf;
                border-radius: 5px;
                margin-top: 6px;
                padding: 4px;
                font-weight: bold;
            }
            QFrame#line {
                background-color: #303030;
                border: 1px solid #303030;
            }
        """)

        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(8, 8, 8, 8)
        main_layout.setSpacing(10)

        # === Menu Bar ===
        menubar = QMenuBar()
        file_menu = menubar.addMenu("Edit")
        help_menu = menubar.addMenu("Help")
        file_menu.addAction(QAction("Save settings", self))
        file_menu.addAction(QAction("Reset settings", self))
        help_menu.addAction(QAction("Help on Atlas Autorig", self))
        main_layout.setMenuBar(menubar)

        # Button section
        btn_layout = QVBoxLayout()
        btn_layout.setContentsMargins(5, 5, 5, 5)
        btn_layout.setSpacing(2)

        # Create/Delete Shot Sculpt Group buttons
        create_group_btn = QPushButton("Create Shot Sculpt Group")
        btn_layout.addWidget(create_group_btn)

        delete_node_btn = QPushButton("Delete Shot Sculpt Node")
        btn_layout.addWidget(delete_node_btn)

        main_layout.addLayout(btn_layout)

        # Create/Delete Sculpt Frame buttons
        frame_btn_layout = QHBoxLayout()
        frame_btn_layout.setContentsMargins(5, 5, 5, 5)
        frame_btn_layout.setSpacing(2)

        create_frame_btn = QPushButton("Create Sculpt Frame")
        create_frame_btn.setStyleSheet("""
            QPushButton {
                background-color: #3C7837;
                color: white;
                border: none;
                padding: 8px;
                font-size: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #3d7f3d;
            }
        """)
        frame_btn_layout.addWidget(create_frame_btn)

        delete_frame_btn = QPushButton("Delete Sculpt Frame")
        delete_frame_btn.setStyleSheet("""
            QPushButton {
                background-color: #C44848;
                color: white;
                border: none;
                padding: 8px;
                font-size: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #8d4040;
            }
        """)
        frame_btn_layout.addWidget(delete_frame_btn)

        main_layout.addLayout(frame_btn_layout)

        # Large display area
        display_frame = QFrame()
        display_frame.setMinimumHeight(150)
        display_frame.setStyleSheet("""
            QFrame {
                background-color: #262626;
                border: 1px solid #7a53cf;
                margin: 5px;
            }
        """)
        main_layout.addWidget(display_frame)

        # Edit Frame button
        edit_frame_layout = QHBoxLayout()
        edit_frame_layout.setContentsMargins(5, 5, 5, 5)

        edit_frame_btn = QPushButton("Edit Frame")
        edit_frame_layout.addWidget(edit_frame_btn)

        main_layout.addLayout(edit_frame_layout)

        # Animation Settings Group
        settings_group = QGroupBox("Animation Settings")
        settings_group.setStyleSheet("""
            QGroupBox {
                color: #cccccc;
                border: 1px solid #7a53cf;
                border-radius: 5px;
                margin-top: 10px;
                padding: 4px;
                font-weight: bold;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px;
            }
        """)
        settings_layout = QVBoxLayout()

        # Ease In/Out, Hold In/Out controls
        controls_layout = QHBoxLayout()

        # Labels row
        labels_layout = QHBoxLayout()
        labels = ["Ease In:", "Ease Out:", "Hold In:", "Hold Out:"]
        for label_text in labels:
            label = QLabel(label_text)
            label.setStyleSheet("color: #cccccc; font-size: 10px;")
            labels_layout.addWidget(label)

        settings_layout.addLayout(labels_layout)

        # Spinboxes row
        spinboxes_layout = QHBoxLayout()
        for i, default_val in enumerate([1, 1, 0, 0]):
            spinbox = QSpinBox()
            spinbox.setValue(default_val)
            spinbox.setMinimum(0)
            spinbox.setMaximum(999)
            spinbox.setStyleSheet("""
                QSpinBox {
                    background-color: #3a3a3a;
                    color: white;
                    border: 1px solid #555555;
                    padding: 3px;
                    font-size: 8px;
                }
            """)
            spinboxes_layout.addWidget(spinbox)

        settings_layout.addLayout(spinboxes_layout)
        settings_layout.addSpacing(10)

        # Key Type dropdown
        key_type_layout = QHBoxLayout()
        key_type_label = QLabel("Key Type:")
        key_type_label.setStyleSheet("color: #cccccc; font-size: 10px;")
        key_type_layout.addWidget(key_type_label)

        key_type_combo = QComboBox()
        key_type_combo.addItems(["linear", "smooth", "step"])
        key_type_combo.setStyleSheet("""
            QComboBox {
                background-color: #3a3a3a;
                color: white;
                border: 1px solid #555555;
                padding: 3px;
                font-size: 10px;
            }
            QComboBox::drop-down {
                border: none;
            }
        """)
        key_type_layout.addWidget(key_type_combo)

        settings_layout.addLayout(key_type_layout)

        settings_group.setLayout(settings_layout)
        main_layout.addWidget(settings_group)

        # Frame name input and rename button
        rename_layout = QHBoxLayout()
        rename_layout.setContentsMargins(5, 5, 5, 5)

        frame_name_input = QLineEdit()
        frame_name_input.setPlaceholderText("New frame name...")
        frame_name_input.setStyleSheet("""
            QLineEdit {
                background-color: #262626;
                color: white;
                border: 1px solid #555555;
                padding: 5px;
                font-size: 10px;
            }
        """)
        rename_layout.addWidget(frame_name_input, stretch=1)

        rename_btn = QPushButton("Rename Frame")
        rename_layout.addWidget(rename_btn, stretch=1)

        main_layout.addLayout(rename_layout)

        # Status label
        status_label = QLabel("No frame selected")
        status_label.setStyleSheet("""
            QLabel {
                color: #888888;
                padding: 5px;
                font-size: 10px;
            }
        """)
        main_layout.addWidget(status_label)

        main_layout.addStretch()

if __name__ == "__main__":
    import sys

    global atlas_sculptor_ui
    try:
        atlas_sculptor_ui.close()
        atlas_sculptor_ui.deleteLater()
    except:
        pass

    atlas_sculptor_ui = AtlasShotSculptorUi(parent=get_maya_main_window())
    atlas_sculptor_ui.setWindowFlags(Qt.Window)
    atlas_sculptor_ui.show()