# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'am_i_dot2_V2kvyWWm.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLayout,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QStatusBar,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1772, 772)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/icons/media/gui_icons/ma_logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.actionWing_1 = QAction(MainWindow)
        self.actionWing_1.setObjectName(u"actionWing_1")
        self.actionWing_2 = QAction(MainWindow)
        self.actionWing_2.setObjectName(u"actionWing_2")
        self.actionNewFile = QAction(MainWindow)
        self.actionNewFile.setObjectName(u"actionNewFile")
        icon1 = QIcon()
        icon1.addFile(u":/icons/media/gui_icons/new_file.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionNewFile.setIcon(icon1)
        self.actionOpenFile = QAction(MainWindow)
        self.actionOpenFile.setObjectName(u"actionOpenFile")
        icon2 = QIcon()
        icon2.addFile(u":/icons/media/gui_icons/open_file.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionOpenFile.setIcon(icon2)
        self.actionCloseFile = QAction(MainWindow)
        self.actionCloseFile.setObjectName(u"actionCloseFile")
        icon3 = QIcon()
        icon3.addFile(u":/icons/media/gui_icons/close_file.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionCloseFile.setIcon(icon3)
        self.actionQuitApp = QAction(MainWindow)
        self.actionQuitApp.setObjectName(u"actionQuitApp")
        icon4 = QIcon()
        icon4.addFile(u":/icons/media/gui_icons/quit_app.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionQuitApp.setIcon(icon4)
        self.actionViewWing1 = QAction(MainWindow)
        self.actionViewWing1.setObjectName(u"actionViewWing1")
        self.actionViewWing1.setCheckable(True)
        self.actionViewWing1.setChecked(True)
        self.actionViewWing2 = QAction(MainWindow)
        self.actionViewWing2.setObjectName(u"actionViewWing2")
        self.actionViewWing2.setCheckable(True)
        self.actionViewWing2.setChecked(True)
        self.actionPreferences = QAction(MainWindow)
        self.actionPreferences.setObjectName(u"actionPreferences")
        icon5 = QIcon()
        icon5.addFile(u":/icons/media/gui_icons/settings.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionPreferences.setIcon(icon5)
        self.actionProfiles = QAction(MainWindow)
        self.actionProfiles.setObjectName(u"actionProfiles")
        icon6 = QIcon()
        icon6.addFile(u":/icons/media/gui_icons/profiles.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionProfiles.setIcon(icon6)
        self.actionGithub = QAction(MainWindow)
        self.actionGithub.setObjectName(u"actionGithub")
        icon7 = QIcon()
        icon7.addFile(u":/icons/media/gui_icons/github_logo.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionGithub.setIcon(icon7)
        self.actionConfiguring_Am_I_Dot_2 = QAction(MainWindow)
        self.actionConfiguring_Am_I_Dot_2.setObjectName(u"actionConfiguring_Am_I_Dot_2")
        icon8 = QIcon()
        icon8.addFile(u":/icons/media/gui_icons/configure_am_i_dot2.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionConfiguring_Am_I_Dot_2.setIcon(icon8)
        self.actionCreate_a_profile = QAction(MainWindow)
        self.actionCreate_a_profile.setObjectName(u"actionCreate_a_profile")
        self.actionCreate_a_profile.setIcon(icon6)
        self.actionRefresh_GUI = QAction(MainWindow)
        self.actionRefresh_GUI.setObjectName(u"actionRefresh_GUI")
        icon9 = QIcon()
        icon9.addFile(u":/icons/media/gui_icons/refresh.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionRefresh_GUI.setIcon(icon9)
        self.actionRefresh_Profile = QAction(MainWindow)
        self.actionRefresh_Profile.setObjectName(u"actionRefresh_Profile")
        self.actionRefresh_Profile.setIcon(icon9)
        self.actionContact_Help = QAction(MainWindow)
        self.actionContact_Help.setObjectName(u"actionContact_Help")
        icon10 = QIcon()
        icon10.addFile(u":/icons/media/gui_icons/help.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionContact_Help.setIcon(icon10)
        self.actionConfig_Mode = QAction(MainWindow)
        self.actionConfig_Mode.setObjectName(u"actionConfig_Mode")
        self.actionConfig_Mode.setCheckable(True)
        self.actionWing_1_Enabled = QAction(MainWindow)
        self.actionWing_1_Enabled.setObjectName(u"actionWing_1_Enabled")
        self.actionWing_1_Enabled.setCheckable(True)
        self.actionWing_1_Enabled.setChecked(True)
        self.actionWing_2_Enabled = QAction(MainWindow)
        self.actionWing_2_Enabled.setObjectName(u"actionWing_2_Enabled")
        self.actionWing_2_Enabled.setCheckable(True)
        self.actionWing_2_Enabled.setChecked(True)
        self.Wing1_dock = QWidget(MainWindow)
        self.Wing1_dock.setObjectName(u"Wing1_dock")
        sizePolicy.setHeightForWidth(self.Wing1_dock.sizePolicy().hasHeightForWidth())
        self.Wing1_dock.setSizePolicy(sizePolicy)
        self.Wing1_dock.setProperty(u"floating", False)
        self.gridLayout = QGridLayout(self.Wing1_dock)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, -1, 0, -1)
        self.wing_1 = QWidget(self.Wing1_dock)
        self.wing_1.setObjectName(u"wing_1")
        self.gridLayout_3 = QGridLayout(self.wing_1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, -1, 0, -1)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.button36_4 = QPushButton(self.wing_1)
        self.button36_4.setObjectName(u"button36_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.button36_4.sizePolicy().hasHeightForWidth())
        self.button36_4.setSizePolicy(sizePolicy1)
        self.button36_4.setMinimumSize(QSize(88, 44))
        self.button36_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button36_4, 3, 5, 1, 1)

        self.button61_4 = QPushButton(self.wing_1)
        self.button61_4.setObjectName(u"button61_4")
        sizePolicy1.setHeightForWidth(self.button61_4.sizePolicy().hasHeightForWidth())
        self.button61_4.setSizePolicy(sizePolicy1)
        self.button61_4.setMinimumSize(QSize(88, 44))
        self.button61_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button61_4, 0, 6, 1, 1)

        self.button45_4 = QPushButton(self.wing_1)
        self.button45_4.setObjectName(u"button45_4")
        sizePolicy1.setHeightForWidth(self.button45_4.sizePolicy().hasHeightForWidth())
        self.button45_4.setSizePolicy(sizePolicy1)
        self.button45_4.setMinimumSize(QSize(88, 44))
        self.button45_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button45_4, 2, 6, 1, 1)

        self.button44_4 = QPushButton(self.wing_1)
        self.button44_4.setObjectName(u"button44_4")
        sizePolicy1.setHeightForWidth(self.button44_4.sizePolicy().hasHeightForWidth())
        self.button44_4.setSizePolicy(sizePolicy1)
        self.button44_4.setMinimumSize(QSize(88, 44))
        self.button44_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button44_4, 2, 5, 1, 1)

        self.button8_4 = QPushButton(self.wing_1)
        self.button8_4.setObjectName(u"button8_4")
        sizePolicy1.setHeightForWidth(self.button8_4.sizePolicy().hasHeightForWidth())
        self.button8_4.setSizePolicy(sizePolicy1)
        self.button8_4.setMinimumSize(QSize(88, 44))
        self.button8_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button8_4, 6, 1, 1, 1)

        self.button116_layout_4 = QGridLayout()
        self.button116_layout_4.setObjectName(u"button116_layout_4")
        self.button116_layout_4.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.button116_4 = QPushButton(self.wing_1)
        self.button116_4.setObjectName(u"button116_4")
        self.button116_4.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.button116_4.sizePolicy().hasHeightForWidth())
        self.button116_4.setSizePolicy(sizePolicy1)
        self.button116_4.setMinimumSize(QSize(28, 28))
        self.button116_4.setMaximumSize(QSize(28, 28))
        font = QFont()
        font.setPointSize(6)
        self.button116_4.setFont(font)

        self.button116_layout_4.addWidget(self.button116_4, 0, 0, 1, 1)


        self.gridLayout_5.addLayout(self.button116_layout_4, 4, 10, 1, 1)

        self.button16_4 = QPushButton(self.wing_1)
        self.button16_4.setObjectName(u"button16_4")
        sizePolicy1.setHeightForWidth(self.button16_4.sizePolicy().hasHeightForWidth())
        self.button16_4.setSizePolicy(sizePolicy1)
        self.button16_4.setMinimumSize(QSize(88, 44))
        self.button16_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button16_4, 5, 1, 1, 1)

        self.button12_4 = QPushButton(self.wing_1)
        self.button12_4.setObjectName(u"button12_4")
        sizePolicy1.setHeightForWidth(self.button12_4.sizePolicy().hasHeightForWidth())
        self.button12_4.setSizePolicy(sizePolicy1)
        self.button12_4.setMinimumSize(QSize(88, 44))
        self.button12_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button12_4, 6, 5, 1, 1)

        self.button10_4 = QPushButton(self.wing_1)
        self.button10_4.setObjectName(u"button10_4")
        sizePolicy1.setHeightForWidth(self.button10_4.sizePolicy().hasHeightForWidth())
        self.button10_4.setSizePolicy(sizePolicy1)
        self.button10_4.setMinimumSize(QSize(88, 44))
        self.button10_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button10_4, 6, 3, 1, 1)

        self.button49_4 = QPushButton(self.wing_1)
        self.button49_4.setObjectName(u"button49_4")
        sizePolicy1.setHeightForWidth(self.button49_4.sizePolicy().hasHeightForWidth())
        self.button49_4.setSizePolicy(sizePolicy1)
        self.button49_4.setMinimumSize(QSize(88, 44))
        self.button49_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button49_4, 1, 2, 1, 1)

        self.button30_4 = QPushButton(self.wing_1)
        self.button30_4.setObjectName(u"button30_4")
        sizePolicy1.setHeightForWidth(self.button30_4.sizePolicy().hasHeightForWidth())
        self.button30_4.setSizePolicy(sizePolicy1)
        self.button30_4.setMinimumSize(QSize(88, 44))
        self.button30_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button30_4, 4, 7, 1, 1)

        self.button113_layout_4 = QGridLayout()
        self.button113_layout_4.setObjectName(u"button113_layout_4")
        self.button113_layout_4.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.button113_4 = QPushButton(self.wing_1)
        self.button113_4.setObjectName(u"button113_4")
        self.button113_4.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.button113_4.sizePolicy().hasHeightForWidth())
        self.button113_4.setSizePolicy(sizePolicy1)
        self.button113_4.setMinimumSize(QSize(28, 28))
        self.button113_4.setMaximumSize(QSize(28, 28))
        self.button113_4.setFont(font)

        self.button113_layout_4.addWidget(self.button113_4, 0, 0, 1, 1)


        self.gridLayout_5.addLayout(self.button113_layout_4, 1, 10, 1, 1)

        self.button104_layout_4 = QGridLayout()
        self.button104_layout_4.setObjectName(u"button104_layout_4")
        self.button104_4 = QPushButton(self.wing_1)
        self.button104_4.setObjectName(u"button104_4")
        self.button104_4.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.button104_4.sizePolicy().hasHeightForWidth())
        self.button104_4.setSizePolicy(sizePolicy1)
        self.button104_4.setMinimumSize(QSize(28, 28))
        self.button104_4.setMaximumSize(QSize(28, 28))
        self.button104_4.setFont(font)

        self.button104_layout_4.addWidget(self.button104_4, 0, 0, 1, 1)


        self.gridLayout_5.addLayout(self.button104_layout_4, 8, 5, 1, 1)

        self.button25_4 = QPushButton(self.wing_1)
        self.button25_4.setObjectName(u"button25_4")
        sizePolicy1.setHeightForWidth(self.button25_4.sizePolicy().hasHeightForWidth())
        self.button25_4.setSizePolicy(sizePolicy1)
        self.button25_4.setMinimumSize(QSize(88, 44))
        self.button25_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button25_4, 4, 2, 1, 1)

        self.button63_4 = QPushButton(self.wing_1)
        self.button63_4.setObjectName(u"button63_4")
        sizePolicy1.setHeightForWidth(self.button63_4.sizePolicy().hasHeightForWidth())
        self.button63_4.setSizePolicy(sizePolicy1)
        self.button63_4.setMinimumSize(QSize(88, 44))
        self.button63_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button63_4, 0, 8, 1, 1)

        self.button122_layout_4 = QGridLayout()
        self.button122_layout_4.setObjectName(u"button122_layout_4")
        self.button122_layout_4.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.button122_4 = QPushButton(self.wing_1)
        self.button122_4.setObjectName(u"button122_4")
        self.button122_4.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.button122_4.sizePolicy().hasHeightForWidth())
        self.button122_4.setSizePolicy(sizePolicy1)
        self.button122_4.setMinimumSize(QSize(28, 28))
        self.button122_4.setMaximumSize(QSize(28, 28))
        self.button122_4.setFont(font)

        self.button122_layout_4.addWidget(self.button122_4, 0, 0, 1, 1)


        self.gridLayout_5.addLayout(self.button122_layout_4, 8, 10, 1, 1)

        self.button48_4 = QPushButton(self.wing_1)
        self.button48_4.setObjectName(u"button48_4")
        sizePolicy1.setHeightForWidth(self.button48_4.sizePolicy().hasHeightForWidth())
        self.button48_4.setSizePolicy(sizePolicy1)
        self.button48_4.setMinimumSize(QSize(88, 44))
        self.button48_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button48_4, 1, 1, 1, 1)

        self.button31_4 = QPushButton(self.wing_1)
        self.button31_4.setObjectName(u"button31_4")
        sizePolicy1.setHeightForWidth(self.button31_4.sizePolicy().hasHeightForWidth())
        self.button31_4.setSizePolicy(sizePolicy1)
        self.button31_4.setMinimumSize(QSize(88, 44))
        self.button31_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button31_4, 4, 8, 1, 1)

        self.button7_4 = QPushButton(self.wing_1)
        self.button7_4.setObjectName(u"button7_4")
        sizePolicy1.setHeightForWidth(self.button7_4.sizePolicy().hasHeightForWidth())
        self.button7_4.setSizePolicy(sizePolicy1)
        self.button7_4.setMinimumSize(QSize(88, 44))
        self.button7_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button7_4, 7, 8, 1, 1)

        self.button4_4 = QPushButton(self.wing_1)
        self.button4_4.setObjectName(u"button4_4")
        sizePolicy1.setHeightForWidth(self.button4_4.sizePolicy().hasHeightForWidth())
        self.button4_4.setSizePolicy(sizePolicy1)
        self.button4_4.setMinimumSize(QSize(88, 44))
        self.button4_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button4_4, 7, 5, 1, 1)

        self.button35_4 = QPushButton(self.wing_1)
        self.button35_4.setObjectName(u"button35_4")
        sizePolicy1.setHeightForWidth(self.button35_4.sizePolicy().hasHeightForWidth())
        self.button35_4.setSizePolicy(sizePolicy1)
        self.button35_4.setMinimumSize(QSize(88, 44))
        self.button35_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button35_4, 3, 4, 1, 1)

        self.button39_4 = QPushButton(self.wing_1)
        self.button39_4.setObjectName(u"button39_4")
        sizePolicy1.setHeightForWidth(self.button39_4.sizePolicy().hasHeightForWidth())
        self.button39_4.setSizePolicy(sizePolicy1)
        self.button39_4.setMinimumSize(QSize(88, 44))
        self.button39_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button39_4, 3, 8, 1, 1)

        self.button24_4 = QPushButton(self.wing_1)
        self.button24_4.setObjectName(u"button24_4")
        sizePolicy1.setHeightForWidth(self.button24_4.sizePolicy().hasHeightForWidth())
        self.button24_4.setSizePolicy(sizePolicy1)
        self.button24_4.setMinimumSize(QSize(88, 44))
        self.button24_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button24_4, 4, 1, 1, 1)

        self.button3_4 = QPushButton(self.wing_1)
        self.button3_4.setObjectName(u"button3_4")
        sizePolicy1.setHeightForWidth(self.button3_4.sizePolicy().hasHeightForWidth())
        self.button3_4.setSizePolicy(sizePolicy1)
        self.button3_4.setMinimumSize(QSize(88, 44))
        self.button3_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button3_4, 7, 4, 1, 1)

        self.button46_4 = QPushButton(self.wing_1)
        self.button46_4.setObjectName(u"button46_4")
        sizePolicy1.setHeightForWidth(self.button46_4.sizePolicy().hasHeightForWidth())
        self.button46_4.setSizePolicy(sizePolicy1)
        self.button46_4.setMinimumSize(QSize(88, 44))
        self.button46_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button46_4, 2, 7, 1, 1)

        self.button40_4 = QPushButton(self.wing_1)
        self.button40_4.setObjectName(u"button40_4")
        sizePolicy1.setHeightForWidth(self.button40_4.sizePolicy().hasHeightForWidth())
        self.button40_4.setSizePolicy(sizePolicy1)
        self.button40_4.setMinimumSize(QSize(88, 44))
        self.button40_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button40_4, 2, 1, 1, 1)

        self.button55_4 = QPushButton(self.wing_1)
        self.button55_4.setObjectName(u"button55_4")
        sizePolicy1.setHeightForWidth(self.button55_4.sizePolicy().hasHeightForWidth())
        self.button55_4.setSizePolicy(sizePolicy1)
        self.button55_4.setMinimumSize(QSize(88, 44))
        self.button55_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button55_4, 1, 8, 1, 1)

        self.button9_4 = QPushButton(self.wing_1)
        self.button9_4.setObjectName(u"button9_4")
        sizePolicy1.setHeightForWidth(self.button9_4.sizePolicy().hasHeightForWidth())
        self.button9_4.setSizePolicy(sizePolicy1)
        self.button9_4.setMinimumSize(QSize(88, 44))
        self.button9_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button9_4, 6, 2, 1, 1)

        self.button5_4 = QPushButton(self.wing_1)
        self.button5_4.setObjectName(u"button5_4")
        sizePolicy1.setHeightForWidth(self.button5_4.sizePolicy().hasHeightForWidth())
        self.button5_4.setSizePolicy(sizePolicy1)
        self.button5_4.setMinimumSize(QSize(88, 44))
        self.button5_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button5_4, 7, 6, 1, 1)

        self.button38_4 = QPushButton(self.wing_1)
        self.button38_4.setObjectName(u"button38_4")
        sizePolicy1.setHeightForWidth(self.button38_4.sizePolicy().hasHeightForWidth())
        self.button38_4.setSizePolicy(sizePolicy1)
        self.button38_4.setMinimumSize(QSize(88, 44))
        self.button38_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button38_4, 3, 7, 1, 1)

        self.button100_layout_4 = QGridLayout()
        self.button100_layout_4.setObjectName(u"button100_layout_4")
        self.button100_4 = QPushButton(self.wing_1)
        self.button100_4.setObjectName(u"button100_4")
        self.button100_4.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.button100_4.sizePolicy().hasHeightForWidth())
        self.button100_4.setSizePolicy(sizePolicy1)
        self.button100_4.setMinimumSize(QSize(28, 28))
        self.button100_4.setMaximumSize(QSize(28, 28))
        self.button100_4.setFont(font)
        self.button100_4.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.button100_4.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.button100_4.setAutoDefault(False)

        self.button100_layout_4.addWidget(self.button100_4, 0, 0, 1, 1)


        self.gridLayout_5.addLayout(self.button100_layout_4, 8, 1, 1, 1)

        self.button119_layout_4 = QGridLayout()
        self.button119_layout_4.setObjectName(u"button119_layout_4")
        self.button119_layout_4.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.button119_4 = QPushButton(self.wing_1)
        self.button119_4.setObjectName(u"button119_4")
        self.button119_4.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.button119_4.sizePolicy().hasHeightForWidth())
        self.button119_4.setSizePolicy(sizePolicy1)
        self.button119_4.setMinimumSize(QSize(28, 28))
        self.button119_4.setMaximumSize(QSize(28, 28))
        self.button119_4.setFont(font)

        self.button119_layout_4.addWidget(self.button119_4, 0, 0, 1, 1)


        self.gridLayout_5.addLayout(self.button119_layout_4, 7, 10, 1, 1)

        self.button52_4 = QPushButton(self.wing_1)
        self.button52_4.setObjectName(u"button52_4")
        sizePolicy1.setHeightForWidth(self.button52_4.sizePolicy().hasHeightForWidth())
        self.button52_4.setSizePolicy(sizePolicy1)
        self.button52_4.setMinimumSize(QSize(88, 44))
        self.button52_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button52_4, 1, 5, 1, 1)

        self.button51_4 = QPushButton(self.wing_1)
        self.button51_4.setObjectName(u"button51_4")
        sizePolicy1.setHeightForWidth(self.button51_4.sizePolicy().hasHeightForWidth())
        self.button51_4.setSizePolicy(sizePolicy1)
        self.button51_4.setMinimumSize(QSize(88, 44))
        self.button51_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button51_4, 1, 4, 1, 1)

        self.button60_4 = QPushButton(self.wing_1)
        self.button60_4.setObjectName(u"button60_4")
        sizePolicy1.setHeightForWidth(self.button60_4.sizePolicy().hasHeightForWidth())
        self.button60_4.setSizePolicy(sizePolicy1)
        self.button60_4.setMinimumSize(QSize(88, 44))
        self.button60_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button60_4, 0, 5, 1, 1)

        self.button13_4 = QPushButton(self.wing_1)
        self.button13_4.setObjectName(u"button13_4")
        sizePolicy1.setHeightForWidth(self.button13_4.sizePolicy().hasHeightForWidth())
        self.button13_4.setSizePolicy(sizePolicy1)
        self.button13_4.setMinimumSize(QSize(88, 44))
        self.button13_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button13_4, 6, 6, 1, 1)

        self.button14_4 = QPushButton(self.wing_1)
        self.button14_4.setObjectName(u"button14_4")
        sizePolicy1.setHeightForWidth(self.button14_4.sizePolicy().hasHeightForWidth())
        self.button14_4.setSizePolicy(sizePolicy1)
        self.button14_4.setMinimumSize(QSize(88, 44))
        self.button14_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button14_4, 6, 7, 1, 1)

        self.button6_4 = QPushButton(self.wing_1)
        self.button6_4.setObjectName(u"button6_4")
        sizePolicy1.setHeightForWidth(self.button6_4.sizePolicy().hasHeightForWidth())
        self.button6_4.setSizePolicy(sizePolicy1)
        self.button6_4.setMinimumSize(QSize(88, 44))
        self.button6_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button6_4, 7, 7, 1, 1)

        self.button26_4 = QPushButton(self.wing_1)
        self.button26_4.setObjectName(u"button26_4")
        sizePolicy1.setHeightForWidth(self.button26_4.sizePolicy().hasHeightForWidth())
        self.button26_4.setSizePolicy(sizePolicy1)
        self.button26_4.setMinimumSize(QSize(88, 44))
        self.button26_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button26_4, 4, 3, 1, 1)

        self.button1_4 = QPushButton(self.wing_1)
        self.button1_4.setObjectName(u"button1_4")
        sizePolicy1.setHeightForWidth(self.button1_4.sizePolicy().hasHeightForWidth())
        self.button1_4.setSizePolicy(sizePolicy1)
        self.button1_4.setMinimumSize(QSize(88, 44))
        self.button1_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button1_4, 7, 2, 1, 1)

        self.button34_4 = QPushButton(self.wing_1)
        self.button34_4.setObjectName(u"button34_4")
        sizePolicy1.setHeightForWidth(self.button34_4.sizePolicy().hasHeightForWidth())
        self.button34_4.setSizePolicy(sizePolicy1)
        self.button34_4.setMinimumSize(QSize(88, 44))
        self.button34_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button34_4, 3, 3, 1, 1)

        self.button117_layout_4 = QGridLayout()
        self.button117_layout_4.setObjectName(u"button117_layout_4")
        self.button117_layout_4.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.button117_4 = QPushButton(self.wing_1)
        self.button117_4.setObjectName(u"button117_4")
        self.button117_4.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.button117_4.sizePolicy().hasHeightForWidth())
        self.button117_4.setSizePolicy(sizePolicy1)
        self.button117_4.setMinimumSize(QSize(28, 28))
        self.button117_4.setMaximumSize(QSize(28, 28))
        self.button117_4.setFont(font)

        self.button117_layout_4.addWidget(self.button117_4, 0, 0, 1, 1)


        self.gridLayout_5.addLayout(self.button117_layout_4, 5, 10, 1, 1)

        self.button115_layout_4 = QGridLayout()
        self.button115_layout_4.setObjectName(u"button115_layout_4")
        self.button115_layout_4.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.button115_4 = QPushButton(self.wing_1)
        self.button115_4.setObjectName(u"button115_4")
        self.button115_4.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.button115_4.sizePolicy().hasHeightForWidth())
        self.button115_4.setSizePolicy(sizePolicy1)
        self.button115_4.setMinimumSize(QSize(28, 28))
        self.button115_4.setMaximumSize(QSize(28, 28))
        self.button115_4.setFont(font)

        self.button115_layout_4.addWidget(self.button115_4, 0, 0, 1, 1)


        self.gridLayout_5.addLayout(self.button115_layout_4, 3, 10, 1, 1)

        self.button62_4 = QPushButton(self.wing_1)
        self.button62_4.setObjectName(u"button62_4")
        sizePolicy1.setHeightForWidth(self.button62_4.sizePolicy().hasHeightForWidth())
        self.button62_4.setSizePolicy(sizePolicy1)
        self.button62_4.setMinimumSize(QSize(88, 44))
        self.button62_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button62_4, 0, 7, 1, 1)

        self.button58_4 = QPushButton(self.wing_1)
        self.button58_4.setObjectName(u"button58_4")
        sizePolicy1.setHeightForWidth(self.button58_4.sizePolicy().hasHeightForWidth())
        self.button58_4.setSizePolicy(sizePolicy1)
        self.button58_4.setMinimumSize(QSize(88, 44))
        self.button58_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button58_4, 0, 3, 1, 1)

        self.button29_4 = QPushButton(self.wing_1)
        self.button29_4.setObjectName(u"button29_4")
        sizePolicy1.setHeightForWidth(self.button29_4.sizePolicy().hasHeightForWidth())
        self.button29_4.setSizePolicy(sizePolicy1)
        self.button29_4.setMinimumSize(QSize(88, 44))
        self.button29_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button29_4, 4, 6, 1, 1)

        self.button21_4 = QPushButton(self.wing_1)
        self.button21_4.setObjectName(u"button21_4")
        sizePolicy1.setHeightForWidth(self.button21_4.sizePolicy().hasHeightForWidth())
        self.button21_4.setSizePolicy(sizePolicy1)
        self.button21_4.setMinimumSize(QSize(88, 44))
        self.button21_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button21_4, 5, 6, 1, 1)

        self.button43_4 = QPushButton(self.wing_1)
        self.button43_4.setObjectName(u"button43_4")
        sizePolicy1.setHeightForWidth(self.button43_4.sizePolicy().hasHeightForWidth())
        self.button43_4.setSizePolicy(sizePolicy1)
        self.button43_4.setMinimumSize(QSize(88, 44))
        self.button43_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button43_4, 2, 4, 1, 1)

        self.button15_4 = QPushButton(self.wing_1)
        self.button15_4.setObjectName(u"button15_4")
        sizePolicy1.setHeightForWidth(self.button15_4.sizePolicy().hasHeightForWidth())
        self.button15_4.setSizePolicy(sizePolicy1)
        self.button15_4.setMinimumSize(QSize(88, 44))
        self.button15_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button15_4, 6, 8, 1, 1)

        self.right_padding2_4 = QSpacerItem(0, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.right_padding2_4, 7, 11, 1, 1)

        self.button32_4 = QPushButton(self.wing_1)
        self.button32_4.setObjectName(u"button32_4")
        sizePolicy1.setHeightForWidth(self.button32_4.sizePolicy().hasHeightForWidth())
        self.button32_4.setSizePolicy(sizePolicy1)
        self.button32_4.setMinimumSize(QSize(88, 44))
        self.button32_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button32_4, 3, 1, 1, 1)

        self.button59_4 = QPushButton(self.wing_1)
        self.button59_4.setObjectName(u"button59_4")
        sizePolicy1.setHeightForWidth(self.button59_4.sizePolicy().hasHeightForWidth())
        self.button59_4.setSizePolicy(sizePolicy1)
        self.button59_4.setMinimumSize(QSize(88, 44))
        self.button59_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button59_4, 0, 4, 1, 1)

        self.button118_layout_4 = QGridLayout()
        self.button118_layout_4.setObjectName(u"button118_layout_4")
        self.button118_layout_4.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.button118_4 = QPushButton(self.wing_1)
        self.button118_4.setObjectName(u"button118_4")
        self.button118_4.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.button118_4.sizePolicy().hasHeightForWidth())
        self.button118_4.setSizePolicy(sizePolicy1)
        self.button118_4.setMinimumSize(QSize(28, 28))
        self.button118_4.setMaximumSize(QSize(28, 28))
        self.button118_4.setFont(font)

        self.button118_layout_4.addWidget(self.button118_4, 0, 0, 1, 1)


        self.gridLayout_5.addLayout(self.button118_layout_4, 6, 10, 1, 1)

        self.button22_4 = QPushButton(self.wing_1)
        self.button22_4.setObjectName(u"button22_4")
        sizePolicy1.setHeightForWidth(self.button22_4.sizePolicy().hasHeightForWidth())
        self.button22_4.setSizePolicy(sizePolicy1)
        self.button22_4.setMinimumSize(QSize(88, 44))
        self.button22_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button22_4, 5, 7, 1, 1)

        self.button42_4 = QPushButton(self.wing_1)
        self.button42_4.setObjectName(u"button42_4")
        sizePolicy1.setHeightForWidth(self.button42_4.sizePolicy().hasHeightForWidth())
        self.button42_4.setSizePolicy(sizePolicy1)
        self.button42_4.setMinimumSize(QSize(88, 44))
        self.button42_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button42_4, 2, 3, 1, 1)

        self.button107_layout_4 = QGridLayout()
        self.button107_layout_4.setObjectName(u"button107_layout_4")
        self.button107_4 = QPushButton(self.wing_1)
        self.button107_4.setObjectName(u"button107_4")
        self.button107_4.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.button107_4.sizePolicy().hasHeightForWidth())
        self.button107_4.setSizePolicy(sizePolicy1)
        self.button107_4.setMinimumSize(QSize(28, 28))
        self.button107_4.setMaximumSize(QSize(28, 28))
        self.button107_4.setFont(font)

        self.button107_layout_4.addWidget(self.button107_4, 0, 0, 1, 1)


        self.gridLayout_5.addLayout(self.button107_layout_4, 8, 8, 1, 1)

        self.right_padding_4 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_5.addItem(self.right_padding_4, 8, 11, 1, 1)

        self.button27_4 = QPushButton(self.wing_1)
        self.button27_4.setObjectName(u"button27_4")
        sizePolicy1.setHeightForWidth(self.button27_4.sizePolicy().hasHeightForWidth())
        self.button27_4.setSizePolicy(sizePolicy1)
        self.button27_4.setMinimumSize(QSize(88, 44))
        self.button27_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button27_4, 4, 4, 1, 1)

        self.frame_fader52_4 = QFrame(self.wing_1)
        self.frame_fader52_4.setObjectName(u"frame_fader52_4")
        self.frame_fader52_4.setMinimumSize(QSize(88, 250))
        self.frame_fader52_4.setMaximumSize(QSize(88, 250))
        self.frame_fader52_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_fader52_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_40 = QGridLayout(self.frame_fader52_4)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.gridLayout_40.setContentsMargins(0, 0, 0, 0)
        self.below_button_layout_fader52_4 = QGridLayout()
        self.below_button_layout_fader52_4.setSpacing(0)
        self.below_button_layout_fader52_4.setObjectName(u"below_button_layout_fader52_4")
        self.fader52_layout_4 = QGridLayout()
        self.fader52_layout_4.setObjectName(u"fader52_layout_4")
        self.fader52_4 = QSlider(self.frame_fader52_4)
        self.fader52_4.setObjectName(u"fader52_4")
        sizePolicy1.setHeightForWidth(self.fader52_4.sizePolicy().hasHeightForWidth())
        self.fader52_4.setSizePolicy(sizePolicy1)
        self.fader52_4.setMinimumSize(QSize(0, 190))
        self.fader52_4.setMaximumSize(QSize(15, 190))
        self.fader52_4.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.fader52_4.setAutoFillBackground(False)
        self.fader52_4.setMaximum(127)
        self.fader52_4.setSliderPosition(0)
        self.fader52_4.setOrientation(Qt.Orientation.Vertical)
        self.fader52_4.setInvertedAppearance(False)
        self.fader52_4.setInvertedControls(False)

        self.fader52_layout_4.addWidget(self.fader52_4, 0, 0, 1, 1)


        self.below_button_layout_fader52_4.addLayout(self.fader52_layout_4, 0, 0, 1, 1)

        self.pushButton_fader52_4 = QPushButton(self.frame_fader52_4)
        self.pushButton_fader52_4.setObjectName(u"pushButton_fader52_4")

        self.below_button_layout_fader52_4.addWidget(self.pushButton_fader52_4, 2, 0, 1, 1)

        self.verticalSpacer_28 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.below_button_layout_fader52_4.addItem(self.verticalSpacer_28, 1, 0, 1, 1)


        self.gridLayout_40.addLayout(self.below_button_layout_fader52_4, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_fader52_4, 10, 5, 1, 1)

        self.button17_4 = QPushButton(self.wing_1)
        self.button17_4.setObjectName(u"button17_4")
        sizePolicy1.setHeightForWidth(self.button17_4.sizePolicy().hasHeightForWidth())
        self.button17_4.setSizePolicy(sizePolicy1)
        self.button17_4.setMinimumSize(QSize(88, 44))
        self.button17_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button17_4, 5, 2, 1, 1)

        self.frame_fader53_4 = QFrame(self.wing_1)
        self.frame_fader53_4.setObjectName(u"frame_fader53_4")
        self.frame_fader53_4.setMinimumSize(QSize(88, 250))
        self.frame_fader53_4.setMaximumSize(QSize(88, 250))
        self.frame_fader53_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_fader53_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_41 = QGridLayout(self.frame_fader53_4)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.gridLayout_41.setContentsMargins(0, 0, 0, 0)
        self.below_button_layout_fader53_4 = QGridLayout()
        self.below_button_layout_fader53_4.setSpacing(0)
        self.below_button_layout_fader53_4.setObjectName(u"below_button_layout_fader53_4")
        self.fader53_layout_4 = QGridLayout()
        self.fader53_layout_4.setObjectName(u"fader53_layout_4")
        self.fader53_4 = QSlider(self.frame_fader53_4)
        self.fader53_4.setObjectName(u"fader53_4")
        sizePolicy1.setHeightForWidth(self.fader53_4.sizePolicy().hasHeightForWidth())
        self.fader53_4.setSizePolicy(sizePolicy1)
        self.fader53_4.setMinimumSize(QSize(0, 190))
        self.fader53_4.setMaximumSize(QSize(15, 190))
        self.fader53_4.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.fader53_4.setAutoFillBackground(False)
        self.fader53_4.setMaximum(127)
        self.fader53_4.setSliderPosition(0)
        self.fader53_4.setOrientation(Qt.Orientation.Vertical)
        self.fader53_4.setInvertedAppearance(False)
        self.fader53_4.setInvertedControls(False)

        self.fader53_layout_4.addWidget(self.fader53_4, 0, 0, 1, 1)


        self.below_button_layout_fader53_4.addLayout(self.fader53_layout_4, 0, 0, 1, 1)

        self.pushButton_fader53_4 = QPushButton(self.frame_fader53_4)
        self.pushButton_fader53_4.setObjectName(u"pushButton_fader53_4")

        self.below_button_layout_fader53_4.addWidget(self.pushButton_fader53_4, 2, 0, 1, 1)

        self.verticalSpacer_29 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.below_button_layout_fader53_4.addItem(self.verticalSpacer_29, 1, 0, 1, 1)


        self.gridLayout_41.addLayout(self.below_button_layout_fader53_4, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_fader53_4, 10, 6, 1, 1)

        self.frame_fader49_4 = QFrame(self.wing_1)
        self.frame_fader49_4.setObjectName(u"frame_fader49_4")
        self.frame_fader49_4.setMinimumSize(QSize(88, 250))
        self.frame_fader49_4.setMaximumSize(QSize(88, 250))
        self.frame_fader49_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_fader49_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_42 = QGridLayout(self.frame_fader49_4)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.gridLayout_42.setContentsMargins(0, 0, 0, 0)
        self.below_button_layout_fader49_4 = QGridLayout()
        self.below_button_layout_fader49_4.setSpacing(0)
        self.below_button_layout_fader49_4.setObjectName(u"below_button_layout_fader49_4")
        self.pushButton_fader49_4 = QPushButton(self.frame_fader49_4)
        self.pushButton_fader49_4.setObjectName(u"pushButton_fader49_4")

        self.below_button_layout_fader49_4.addWidget(self.pushButton_fader49_4, 2, 0, 1, 1)

        self.fader49_layout_4 = QGridLayout()
        self.fader49_layout_4.setObjectName(u"fader49_layout_4")
        self.fader49_4 = QSlider(self.frame_fader49_4)
        self.fader49_4.setObjectName(u"fader49_4")
        sizePolicy1.setHeightForWidth(self.fader49_4.sizePolicy().hasHeightForWidth())
        self.fader49_4.setSizePolicy(sizePolicy1)
        self.fader49_4.setMinimumSize(QSize(0, 190))
        self.fader49_4.setMaximumSize(QSize(15, 190))
        self.fader49_4.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.fader49_4.setAutoFillBackground(False)
        self.fader49_4.setMaximum(127)
        self.fader49_4.setSliderPosition(0)
        self.fader49_4.setOrientation(Qt.Orientation.Vertical)
        self.fader49_4.setInvertedAppearance(False)
        self.fader49_4.setInvertedControls(False)

        self.fader49_layout_4.addWidget(self.fader49_4, 0, 0, 1, 1)


        self.below_button_layout_fader49_4.addLayout(self.fader49_layout_4, 0, 0, 1, 1)

        self.verticalSpacer_30 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.below_button_layout_fader49_4.addItem(self.verticalSpacer_30, 1, 0, 1, 1)


        self.gridLayout_42.addLayout(self.below_button_layout_fader49_4, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_fader49_4, 10, 2, 1, 1)

        self.button37_4 = QPushButton(self.wing_1)
        self.button37_4.setObjectName(u"button37_4")
        sizePolicy1.setHeightForWidth(self.button37_4.sizePolicy().hasHeightForWidth())
        self.button37_4.setSizePolicy(sizePolicy1)
        self.button37_4.setMinimumSize(QSize(88, 44))
        self.button37_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button37_4, 3, 6, 1, 1)

        self.button41_4 = QPushButton(self.wing_1)
        self.button41_4.setObjectName(u"button41_4")
        sizePolicy1.setHeightForWidth(self.button41_4.sizePolicy().hasHeightForWidth())
        self.button41_4.setSizePolicy(sizePolicy1)
        self.button41_4.setMinimumSize(QSize(88, 44))
        self.button41_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button41_4, 2, 2, 1, 1)

        self.button0_4 = QPushButton(self.wing_1)
        self.button0_4.setObjectName(u"button0_4")
        sizePolicy1.setHeightForWidth(self.button0_4.sizePolicy().hasHeightForWidth())
        self.button0_4.setSizePolicy(sizePolicy1)
        self.button0_4.setMinimumSize(QSize(88, 44))
        self.button0_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button0_4, 7, 1, 1, 1)

        self.left_padding_7 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_5.addItem(self.left_padding_7, 7, 0, 1, 1)

        self.button56_4 = QPushButton(self.wing_1)
        self.button56_4.setObjectName(u"button56_4")
        sizePolicy1.setHeightForWidth(self.button56_4.sizePolicy().hasHeightForWidth())
        self.button56_4.setSizePolicy(sizePolicy1)
        self.button56_4.setMinimumSize(QSize(88, 44))
        self.button56_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button56_4, 0, 1, 1, 1)

        self.button23_4 = QPushButton(self.wing_1)
        self.button23_4.setObjectName(u"button23_4")
        sizePolicy1.setHeightForWidth(self.button23_4.sizePolicy().hasHeightForWidth())
        self.button23_4.setSizePolicy(sizePolicy1)
        self.button23_4.setMinimumSize(QSize(88, 44))
        self.button23_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button23_4, 5, 8, 1, 1)

        self.button54_4 = QPushButton(self.wing_1)
        self.button54_4.setObjectName(u"button54_4")
        sizePolicy1.setHeightForWidth(self.button54_4.sizePolicy().hasHeightForWidth())
        self.button54_4.setSizePolicy(sizePolicy1)
        self.button54_4.setMinimumSize(QSize(88, 44))
        self.button54_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button54_4, 1, 7, 1, 1)

        self.frame_fader48_4 = QFrame(self.wing_1)
        self.frame_fader48_4.setObjectName(u"frame_fader48_4")
        self.frame_fader48_4.setMinimumSize(QSize(88, 250))
        self.frame_fader48_4.setMaximumSize(QSize(88, 250))
        self.frame_fader48_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_fader48_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_43 = QGridLayout(self.frame_fader48_4)
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.gridLayout_43.setContentsMargins(0, 0, 0, 0)
        self.below_button_layout_fader48_4 = QGridLayout()
        self.below_button_layout_fader48_4.setSpacing(0)
        self.below_button_layout_fader48_4.setObjectName(u"below_button_layout_fader48_4")
        self.fader48_layout_4 = QGridLayout()
        self.fader48_layout_4.setObjectName(u"fader48_layout_4")
        self.fader48_4 = QSlider(self.frame_fader48_4)
        self.fader48_4.setObjectName(u"fader48_4")
        sizePolicy1.setHeightForWidth(self.fader48_4.sizePolicy().hasHeightForWidth())
        self.fader48_4.setSizePolicy(sizePolicy1)
        self.fader48_4.setMinimumSize(QSize(0, 190))
        self.fader48_4.setMaximumSize(QSize(15, 190))
        self.fader48_4.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.fader48_4.setAutoFillBackground(False)
        self.fader48_4.setMaximum(127)
        self.fader48_4.setSliderPosition(0)
        self.fader48_4.setOrientation(Qt.Orientation.Vertical)
        self.fader48_4.setInvertedAppearance(False)
        self.fader48_4.setInvertedControls(False)

        self.fader48_layout_4.addWidget(self.fader48_4, 0, 0, 1, 1)


        self.below_button_layout_fader48_4.addLayout(self.fader48_layout_4, 0, 0, 1, 1)

        self.pushButton_fader48_4 = QPushButton(self.frame_fader48_4)
        self.pushButton_fader48_4.setObjectName(u"pushButton_fader48_4")

        self.below_button_layout_fader48_4.addWidget(self.pushButton_fader48_4, 2, 0, 1, 1)

        self.verticalSpacer_31 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.below_button_layout_fader48_4.addItem(self.verticalSpacer_31, 1, 0, 1, 1)


        self.gridLayout_43.addLayout(self.below_button_layout_fader48_4, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_fader48_4, 10, 1, 1, 1)

        self.button106_layout_4 = QGridLayout()
        self.button106_layout_4.setObjectName(u"button106_layout_4")
        self.button106_4 = QPushButton(self.wing_1)
        self.button106_4.setObjectName(u"button106_4")
        self.button106_4.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.button106_4.sizePolicy().hasHeightForWidth())
        self.button106_4.setSizePolicy(sizePolicy1)
        self.button106_4.setMinimumSize(QSize(28, 28))
        self.button106_4.setMaximumSize(QSize(28, 28))
        self.button106_4.setFont(font)

        self.button106_layout_4.addWidget(self.button106_4, 0, 0, 1, 1)


        self.gridLayout_5.addLayout(self.button106_layout_4, 8, 7, 1, 1)

        self.button33_4 = QPushButton(self.wing_1)
        self.button33_4.setObjectName(u"button33_4")
        sizePolicy1.setHeightForWidth(self.button33_4.sizePolicy().hasHeightForWidth())
        self.button33_4.setSizePolicy(sizePolicy1)
        self.button33_4.setMinimumSize(QSize(88, 44))
        self.button33_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button33_4, 3, 2, 1, 1)

        self.button28_4 = QPushButton(self.wing_1)
        self.button28_4.setObjectName(u"button28_4")
        sizePolicy1.setHeightForWidth(self.button28_4.sizePolicy().hasHeightForWidth())
        self.button28_4.setSizePolicy(sizePolicy1)
        self.button28_4.setMinimumSize(QSize(88, 44))
        self.button28_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button28_4, 4, 5, 1, 1)

        self.button2_4 = QPushButton(self.wing_1)
        self.button2_4.setObjectName(u"button2_4")
        sizePolicy1.setHeightForWidth(self.button2_4.sizePolicy().hasHeightForWidth())
        self.button2_4.setSizePolicy(sizePolicy1)
        self.button2_4.setMinimumSize(QSize(88, 44))
        self.button2_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button2_4, 7, 3, 1, 1)

        self.button11_4 = QPushButton(self.wing_1)
        self.button11_4.setObjectName(u"button11_4")
        sizePolicy1.setHeightForWidth(self.button11_4.sizePolicy().hasHeightForWidth())
        self.button11_4.setSizePolicy(sizePolicy1)
        self.button11_4.setMinimumSize(QSize(88, 44))
        self.button11_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button11_4, 6, 4, 1, 1)

        self.button102_layout_4 = QGridLayout()
        self.button102_layout_4.setObjectName(u"button102_layout_4")
        self.button102_4 = QPushButton(self.wing_1)
        self.button102_4.setObjectName(u"button102_4")
        self.button102_4.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.button102_4.sizePolicy().hasHeightForWidth())
        self.button102_4.setSizePolicy(sizePolicy1)
        self.button102_4.setMinimumSize(QSize(28, 28))
        self.button102_4.setMaximumSize(QSize(28, 28))
        self.button102_4.setFont(font)

        self.button102_layout_4.addWidget(self.button102_4, 0, 0, 1, 1)


        self.gridLayout_5.addLayout(self.button102_layout_4, 8, 3, 1, 1)

        self.button18_4 = QPushButton(self.wing_1)
        self.button18_4.setObjectName(u"button18_4")
        sizePolicy1.setHeightForWidth(self.button18_4.sizePolicy().hasHeightForWidth())
        self.button18_4.setSizePolicy(sizePolicy1)
        self.button18_4.setMinimumSize(QSize(88, 44))
        self.button18_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button18_4, 5, 3, 1, 1)

        self.button19_4 = QPushButton(self.wing_1)
        self.button19_4.setObjectName(u"button19_4")
        sizePolicy1.setHeightForWidth(self.button19_4.sizePolicy().hasHeightForWidth())
        self.button19_4.setSizePolicy(sizePolicy1)
        self.button19_4.setMinimumSize(QSize(88, 44))
        self.button19_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button19_4, 5, 4, 1, 1)

        self.button47_4 = QPushButton(self.wing_1)
        self.button47_4.setObjectName(u"button47_4")
        sizePolicy1.setHeightForWidth(self.button47_4.sizePolicy().hasHeightForWidth())
        self.button47_4.setSizePolicy(sizePolicy1)
        self.button47_4.setMinimumSize(QSize(88, 44))
        self.button47_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button47_4, 2, 8, 1, 1)

        self.button53_4 = QPushButton(self.wing_1)
        self.button53_4.setObjectName(u"button53_4")
        sizePolicy1.setHeightForWidth(self.button53_4.sizePolicy().hasHeightForWidth())
        self.button53_4.setSizePolicy(sizePolicy1)
        self.button53_4.setMinimumSize(QSize(88, 44))
        self.button53_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button53_4, 1, 6, 1, 1)

        self.button112_layout_4 = QGridLayout()
        self.button112_layout_4.setObjectName(u"button112_layout_4")
        self.button112_layout_4.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.button112_4 = QPushButton(self.wing_1)
        self.button112_4.setObjectName(u"button112_4")
        self.button112_4.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.button112_4.sizePolicy().hasHeightForWidth())
        self.button112_4.setSizePolicy(sizePolicy1)
        self.button112_4.setMinimumSize(QSize(28, 28))
        self.button112_4.setMaximumSize(QSize(28, 28))
        self.button112_4.setFont(font)

        self.button112_layout_4.addWidget(self.button112_4, 0, 0, 1, 1)


        self.gridLayout_5.addLayout(self.button112_layout_4, 0, 10, 1, 1)

        self.button114_layout_4 = QGridLayout()
        self.button114_layout_4.setObjectName(u"button114_layout_4")
        self.button114_layout_4.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.button114_4 = QPushButton(self.wing_1)
        self.button114_4.setObjectName(u"button114_4")
        self.button114_4.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.button114_4.sizePolicy().hasHeightForWidth())
        self.button114_4.setSizePolicy(sizePolicy1)
        self.button114_4.setMinimumSize(QSize(28, 28))
        self.button114_4.setMaximumSize(QSize(28, 28))
        self.button114_4.setFont(font)

        self.button114_layout_4.addWidget(self.button114_4, 0, 0, 1, 1)


        self.gridLayout_5.addLayout(self.button114_layout_4, 2, 10, 1, 1)

        self.button50_4 = QPushButton(self.wing_1)
        self.button50_4.setObjectName(u"button50_4")
        sizePolicy1.setHeightForWidth(self.button50_4.sizePolicy().hasHeightForWidth())
        self.button50_4.setSizePolicy(sizePolicy1)
        self.button50_4.setMinimumSize(QSize(88, 44))
        self.button50_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button50_4, 1, 3, 1, 1)

        self.left_padding_8 = QSpacerItem(0, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.left_padding_8, 8, 0, 1, 1)

        self.frame_fader51_4 = QFrame(self.wing_1)
        self.frame_fader51_4.setObjectName(u"frame_fader51_4")
        self.frame_fader51_4.setMinimumSize(QSize(88, 250))
        self.frame_fader51_4.setMaximumSize(QSize(88, 250))
        self.frame_fader51_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_fader51_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_44 = QGridLayout(self.frame_fader51_4)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.gridLayout_44.setContentsMargins(0, 0, 0, 0)
        self.below_button_layout_fader51_4 = QGridLayout()
        self.below_button_layout_fader51_4.setSpacing(0)
        self.below_button_layout_fader51_4.setObjectName(u"below_button_layout_fader51_4")
        self.fader51_layout_4 = QGridLayout()
        self.fader51_layout_4.setObjectName(u"fader51_layout_4")
        self.fader51_4 = QSlider(self.frame_fader51_4)
        self.fader51_4.setObjectName(u"fader51_4")
        sizePolicy1.setHeightForWidth(self.fader51_4.sizePolicy().hasHeightForWidth())
        self.fader51_4.setSizePolicy(sizePolicy1)
        self.fader51_4.setMinimumSize(QSize(0, 190))
        self.fader51_4.setMaximumSize(QSize(15, 190))
        self.fader51_4.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.fader51_4.setAutoFillBackground(False)
        self.fader51_4.setMaximum(127)
        self.fader51_4.setSliderPosition(0)
        self.fader51_4.setOrientation(Qt.Orientation.Vertical)
        self.fader51_4.setInvertedAppearance(False)
        self.fader51_4.setInvertedControls(False)

        self.fader51_layout_4.addWidget(self.fader51_4, 0, 0, 1, 1)


        self.below_button_layout_fader51_4.addLayout(self.fader51_layout_4, 0, 0, 1, 1)

        self.pushButton_fader51_4 = QPushButton(self.frame_fader51_4)
        self.pushButton_fader51_4.setObjectName(u"pushButton_fader51_4")

        self.below_button_layout_fader51_4.addWidget(self.pushButton_fader51_4, 2, 0, 1, 1)

        self.verticalSpacer_32 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.below_button_layout_fader51_4.addItem(self.verticalSpacer_32, 1, 0, 1, 1)


        self.gridLayout_44.addLayout(self.below_button_layout_fader51_4, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_fader51_4, 10, 4, 1, 1)

        self.frame_fader50_4 = QFrame(self.wing_1)
        self.frame_fader50_4.setObjectName(u"frame_fader50_4")
        self.frame_fader50_4.setMinimumSize(QSize(88, 250))
        self.frame_fader50_4.setMaximumSize(QSize(88, 250))
        self.frame_fader50_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_fader50_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_45 = QGridLayout(self.frame_fader50_4)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.gridLayout_45.setContentsMargins(0, 0, 0, 0)
        self.below_button_layout_fader50_4 = QGridLayout()
        self.below_button_layout_fader50_4.setSpacing(0)
        self.below_button_layout_fader50_4.setObjectName(u"below_button_layout_fader50_4")
        self.pushButton_fader50_4 = QPushButton(self.frame_fader50_4)
        self.pushButton_fader50_4.setObjectName(u"pushButton_fader50_4")

        self.below_button_layout_fader50_4.addWidget(self.pushButton_fader50_4, 2, 0, 1, 1)

        self.fader50_layout_4 = QGridLayout()
        self.fader50_layout_4.setObjectName(u"fader50_layout_4")
        self.fader50_4 = QSlider(self.frame_fader50_4)
        self.fader50_4.setObjectName(u"fader50_4")
        sizePolicy1.setHeightForWidth(self.fader50_4.sizePolicy().hasHeightForWidth())
        self.fader50_4.setSizePolicy(sizePolicy1)
        self.fader50_4.setMinimumSize(QSize(0, 190))
        self.fader50_4.setMaximumSize(QSize(15, 190))
        self.fader50_4.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.fader50_4.setAutoFillBackground(False)
        self.fader50_4.setMaximum(127)
        self.fader50_4.setSliderPosition(0)
        self.fader50_4.setOrientation(Qt.Orientation.Vertical)
        self.fader50_4.setInvertedAppearance(False)
        self.fader50_4.setInvertedControls(False)

        self.fader50_layout_4.addWidget(self.fader50_4, 0, 0, 1, 1)


        self.below_button_layout_fader50_4.addLayout(self.fader50_layout_4, 0, 0, 1, 1)

        self.verticalSpacer_33 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.below_button_layout_fader50_4.addItem(self.verticalSpacer_33, 1, 0, 1, 1)


        self.gridLayout_45.addLayout(self.below_button_layout_fader50_4, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_fader50_4, 10, 3, 1, 1)

        self.button105_layout_4 = QGridLayout()
        self.button105_layout_4.setObjectName(u"button105_layout_4")
        self.button105_4 = QPushButton(self.wing_1)
        self.button105_4.setObjectName(u"button105_4")
        self.button105_4.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.button105_4.sizePolicy().hasHeightForWidth())
        self.button105_4.setSizePolicy(sizePolicy1)
        self.button105_4.setMinimumSize(QSize(28, 28))
        self.button105_4.setMaximumSize(QSize(28, 28))
        self.button105_4.setFont(font)

        self.button105_layout_4.addWidget(self.button105_4, 0, 0, 1, 1)


        self.gridLayout_5.addLayout(self.button105_layout_4, 8, 6, 1, 1)

        self.button20_4 = QPushButton(self.wing_1)
        self.button20_4.setObjectName(u"button20_4")
        sizePolicy1.setHeightForWidth(self.button20_4.sizePolicy().hasHeightForWidth())
        self.button20_4.setSizePolicy(sizePolicy1)
        self.button20_4.setMinimumSize(QSize(88, 44))
        self.button20_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button20_4, 5, 5, 1, 1)

        self.button101_layout_4 = QGridLayout()
        self.button101_layout_4.setObjectName(u"button101_layout_4")
        self.button101_4 = QPushButton(self.wing_1)
        self.button101_4.setObjectName(u"button101_4")
        self.button101_4.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.button101_4.sizePolicy().hasHeightForWidth())
        self.button101_4.setSizePolicy(sizePolicy1)
        self.button101_4.setMinimumSize(QSize(28, 28))
        self.button101_4.setMaximumSize(QSize(28, 28))
        self.button101_4.setFont(font)

        self.button101_layout_4.addWidget(self.button101_4, 0, 0, 1, 1)


        self.gridLayout_5.addLayout(self.button101_layout_4, 8, 2, 1, 1)

        self.button103_layout_4 = QGridLayout()
        self.button103_layout_4.setObjectName(u"button103_layout_4")
        self.button103_4 = QPushButton(self.wing_1)
        self.button103_4.setObjectName(u"button103_4")
        self.button103_4.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.button103_4.sizePolicy().hasHeightForWidth())
        self.button103_4.setSizePolicy(sizePolicy1)
        self.button103_4.setMinimumSize(QSize(28, 28))
        self.button103_4.setMaximumSize(QSize(28, 28))
        self.button103_4.setFont(font)

        self.button103_layout_4.addWidget(self.button103_4, 0, 0, 1, 1)


        self.gridLayout_5.addLayout(self.button103_layout_4, 8, 4, 1, 1)

        self.button57_4 = QPushButton(self.wing_1)
        self.button57_4.setObjectName(u"button57_4")
        sizePolicy1.setHeightForWidth(self.button57_4.sizePolicy().hasHeightForWidth())
        self.button57_4.setSizePolicy(sizePolicy1)
        self.button57_4.setMinimumSize(QSize(88, 44))
        self.button57_4.setMaximumSize(QSize(88, 44))

        self.gridLayout_5.addWidget(self.button57_4, 0, 2, 1, 1)

        self.frame_fader54_4 = QFrame(self.wing_1)
        self.frame_fader54_4.setObjectName(u"frame_fader54_4")
        self.frame_fader54_4.setMinimumSize(QSize(88, 250))
        self.frame_fader54_4.setMaximumSize(QSize(88, 250))
        self.frame_fader54_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_fader54_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_46 = QGridLayout(self.frame_fader54_4)
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.gridLayout_46.setContentsMargins(0, 0, 0, 0)
        self.below_button_layout_fader54_4 = QGridLayout()
        self.below_button_layout_fader54_4.setSpacing(0)
        self.below_button_layout_fader54_4.setObjectName(u"below_button_layout_fader54_4")
        self.pushButton_fader54_4 = QPushButton(self.frame_fader54_4)
        self.pushButton_fader54_4.setObjectName(u"pushButton_fader54_4")

        self.below_button_layout_fader54_4.addWidget(self.pushButton_fader54_4, 2, 0, 1, 1)

        self.fader54_layout_4 = QGridLayout()
        self.fader54_layout_4.setObjectName(u"fader54_layout_4")
        self.fader54_4 = QSlider(self.frame_fader54_4)
        self.fader54_4.setObjectName(u"fader54_4")
        sizePolicy1.setHeightForWidth(self.fader54_4.sizePolicy().hasHeightForWidth())
        self.fader54_4.setSizePolicy(sizePolicy1)
        self.fader54_4.setMinimumSize(QSize(0, 190))
        self.fader54_4.setMaximumSize(QSize(15, 190))
        self.fader54_4.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.fader54_4.setAutoFillBackground(False)
        self.fader54_4.setMaximum(127)
        self.fader54_4.setSliderPosition(0)
        self.fader54_4.setOrientation(Qt.Orientation.Vertical)
        self.fader54_4.setInvertedAppearance(False)
        self.fader54_4.setInvertedControls(False)

        self.fader54_layout_4.addWidget(self.fader54_4, 0, 0, 1, 1)


        self.below_button_layout_fader54_4.addLayout(self.fader54_layout_4, 0, 0, 1, 1)

        self.verticalSpacer_34 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.below_button_layout_fader54_4.addItem(self.verticalSpacer_34, 1, 0, 1, 1)


        self.gridLayout_46.addLayout(self.below_button_layout_fader54_4, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_fader54_4, 10, 7, 1, 1)

        self.frame_fader55_4 = QFrame(self.wing_1)
        self.frame_fader55_4.setObjectName(u"frame_fader55_4")
        self.frame_fader55_4.setMinimumSize(QSize(88, 250))
        self.frame_fader55_4.setMaximumSize(QSize(88, 250))
        self.frame_fader55_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_fader55_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_47 = QGridLayout(self.frame_fader55_4)
        self.gridLayout_47.setObjectName(u"gridLayout_47")
        self.gridLayout_47.setContentsMargins(0, 0, 0, 0)
        self.below_button_layout_fader55_4 = QGridLayout()
        self.below_button_layout_fader55_4.setSpacing(0)
        self.below_button_layout_fader55_4.setObjectName(u"below_button_layout_fader55_4")
        self.fader55_layout_4 = QGridLayout()
        self.fader55_layout_4.setObjectName(u"fader55_layout_4")
        self.fader55_4 = QSlider(self.frame_fader55_4)
        self.fader55_4.setObjectName(u"fader55_4")
        sizePolicy1.setHeightForWidth(self.fader55_4.sizePolicy().hasHeightForWidth())
        self.fader55_4.setSizePolicy(sizePolicy1)
        self.fader55_4.setMinimumSize(QSize(0, 190))
        self.fader55_4.setMaximumSize(QSize(15, 190))
        self.fader55_4.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.fader55_4.setAutoFillBackground(False)
        self.fader55_4.setMaximum(127)
        self.fader55_4.setSliderPosition(0)
        self.fader55_4.setOrientation(Qt.Orientation.Vertical)
        self.fader55_4.setInvertedAppearance(False)
        self.fader55_4.setInvertedControls(False)

        self.fader55_layout_4.addWidget(self.fader55_4, 0, 0, 1, 1)


        self.below_button_layout_fader55_4.addLayout(self.fader55_layout_4, 0, 0, 1, 1)

        self.pushButton_fader55_4 = QPushButton(self.frame_fader55_4)
        self.pushButton_fader55_4.setObjectName(u"pushButton_fader55_4")

        self.below_button_layout_fader55_4.addWidget(self.pushButton_fader55_4, 2, 0, 1, 1)

        self.verticalSpacer_35 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.below_button_layout_fader55_4.addItem(self.verticalSpacer_35, 1, 0, 1, 1)


        self.gridLayout_47.addLayout(self.below_button_layout_fader55_4, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_fader55_4, 10, 8, 1, 1)

        self.frame_fader56_4 = QFrame(self.wing_1)
        self.frame_fader56_4.setObjectName(u"frame_fader56_4")
        self.frame_fader56_4.setMinimumSize(QSize(88, 250))
        self.frame_fader56_4.setMaximumSize(QSize(88, 250))
        self.frame_fader56_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_fader56_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_48 = QGridLayout(self.frame_fader56_4)
        self.gridLayout_48.setObjectName(u"gridLayout_48")
        self.gridLayout_48.setContentsMargins(0, 0, 0, 0)
        self.below_button_layout_fader56_4 = QGridLayout()
        self.below_button_layout_fader56_4.setSpacing(0)
        self.below_button_layout_fader56_4.setObjectName(u"below_button_layout_fader56_4")
        self.fader56_layout_4 = QGridLayout()
        self.fader56_layout_4.setObjectName(u"fader56_layout_4")
        self.fader56_4 = QSlider(self.frame_fader56_4)
        self.fader56_4.setObjectName(u"fader56_4")
        sizePolicy1.setHeightForWidth(self.fader56_4.sizePolicy().hasHeightForWidth())
        self.fader56_4.setSizePolicy(sizePolicy1)
        self.fader56_4.setMinimumSize(QSize(0, 190))
        self.fader56_4.setMaximumSize(QSize(15, 190))
        self.fader56_4.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.fader56_4.setAutoFillBackground(False)
        self.fader56_4.setMaximum(127)
        self.fader56_4.setSliderPosition(0)
        self.fader56_4.setOrientation(Qt.Orientation.Vertical)
        self.fader56_4.setInvertedAppearance(False)
        self.fader56_4.setInvertedControls(False)

        self.fader56_layout_4.addWidget(self.fader56_4, 0, 0, 1, 1)


        self.below_button_layout_fader56_4.addLayout(self.fader56_layout_4, 0, 0, 1, 1)

        self.pushButton_fader56_4 = QPushButton(self.frame_fader56_4)
        self.pushButton_fader56_4.setObjectName(u"pushButton_fader56_4")

        self.below_button_layout_fader56_4.addWidget(self.pushButton_fader56_4, 2, 0, 1, 1)

        self.verticalSpacer_36 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.below_button_layout_fader56_4.addItem(self.verticalSpacer_36, 1, 0, 1, 1)


        self.gridLayout_48.addLayout(self.below_button_layout_fader56_4, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_fader56_4, 10, 10, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_5, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.wing_1, 0, 0, 1, 1)

        self.wing_2 = QWidget(self.Wing1_dock)
        self.wing_2.setObjectName(u"wing_2")
        self.wing_2.setEnabled(True)
        self.gridLayout_6 = QGridLayout(self.wing_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, -1, 0, -1)
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.button114_layout_6 = QGridLayout()
        self.button114_layout_6.setObjectName(u"button114_layout_6")
        self.button114_layout_6.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.button114_6 = QPushButton(self.wing_2)
        self.button114_6.setObjectName(u"button114_6")
        self.button114_6.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.button114_6.sizePolicy().hasHeightForWidth())
        self.button114_6.setSizePolicy(sizePolicy1)
        self.button114_6.setMinimumSize(QSize(28, 28))
        self.button114_6.setMaximumSize(QSize(28, 28))
        self.button114_6.setFont(font)

        self.button114_layout_6.addWidget(self.button114_6, 0, 0, 1, 1)


        self.gridLayout_7.addLayout(self.button114_layout_6, 2, 10, 1, 1)

        self.button20_6 = QPushButton(self.wing_2)
        self.button20_6.setObjectName(u"button20_6")
        sizePolicy1.setHeightForWidth(self.button20_6.sizePolicy().hasHeightForWidth())
        self.button20_6.setSizePolicy(sizePolicy1)
        self.button20_6.setMinimumSize(QSize(44, 44))
        self.button20_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button20_6, 5, 5, 1, 1)

        self.button22_6 = QPushButton(self.wing_2)
        self.button22_6.setObjectName(u"button22_6")
        sizePolicy1.setHeightForWidth(self.button22_6.sizePolicy().hasHeightForWidth())
        self.button22_6.setSizePolicy(sizePolicy1)
        self.button22_6.setMinimumSize(QSize(44, 44))
        self.button22_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button22_6, 5, 7, 1, 1)

        self.button50_6 = QPushButton(self.wing_2)
        self.button50_6.setObjectName(u"button50_6")
        sizePolicy1.setHeightForWidth(self.button50_6.sizePolicy().hasHeightForWidth())
        self.button50_6.setSizePolicy(sizePolicy1)
        self.button50_6.setMinimumSize(QSize(44, 44))
        self.button50_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button50_6, 1, 3, 1, 1)

        self.button113_layout_6 = QGridLayout()
        self.button113_layout_6.setObjectName(u"button113_layout_6")
        self.button113_layout_6.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.button113_6 = QPushButton(self.wing_2)
        self.button113_6.setObjectName(u"button113_6")
        self.button113_6.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.button113_6.sizePolicy().hasHeightForWidth())
        self.button113_6.setSizePolicy(sizePolicy1)
        self.button113_6.setMinimumSize(QSize(28, 28))
        self.button113_6.setMaximumSize(QSize(28, 28))
        self.button113_6.setFont(font)

        self.button113_layout_6.addWidget(self.button113_6, 0, 0, 1, 1)


        self.gridLayout_7.addLayout(self.button113_layout_6, 1, 10, 1, 1)

        self.button47_6 = QPushButton(self.wing_2)
        self.button47_6.setObjectName(u"button47_6")
        sizePolicy1.setHeightForWidth(self.button47_6.sizePolicy().hasHeightForWidth())
        self.button47_6.setSizePolicy(sizePolicy1)
        self.button47_6.setMinimumSize(QSize(44, 44))
        self.button47_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button47_6, 2, 8, 1, 1)

        self.button38_6 = QPushButton(self.wing_2)
        self.button38_6.setObjectName(u"button38_6")
        sizePolicy1.setHeightForWidth(self.button38_6.sizePolicy().hasHeightForWidth())
        self.button38_6.setSizePolicy(sizePolicy1)
        self.button38_6.setMinimumSize(QSize(44, 44))
        self.button38_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button38_6, 3, 7, 1, 1)

        self.button49_6 = QPushButton(self.wing_2)
        self.button49_6.setObjectName(u"button49_6")
        sizePolicy1.setHeightForWidth(self.button49_6.sizePolicy().hasHeightForWidth())
        self.button49_6.setSizePolicy(sizePolicy1)
        self.button49_6.setMinimumSize(QSize(44, 44))
        self.button49_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button49_6, 1, 2, 1, 1)

        self.button7_6 = QPushButton(self.wing_2)
        self.button7_6.setObjectName(u"button7_6")
        sizePolicy1.setHeightForWidth(self.button7_6.sizePolicy().hasHeightForWidth())
        self.button7_6.setSizePolicy(sizePolicy1)
        self.button7_6.setMinimumSize(QSize(44, 44))
        self.button7_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button7_6, 7, 8, 1, 1)

        self.button56_6 = QPushButton(self.wing_2)
        self.button56_6.setObjectName(u"button56_6")
        sizePolicy1.setHeightForWidth(self.button56_6.sizePolicy().hasHeightForWidth())
        self.button56_6.setSizePolicy(sizePolicy1)
        self.button56_6.setMinimumSize(QSize(44, 44))
        self.button56_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button56_6, 0, 1, 1, 1)

        self.button102_layout_6 = QGridLayout()
        self.button102_layout_6.setObjectName(u"button102_layout_6")
        self.button102_6 = QPushButton(self.wing_2)
        self.button102_6.setObjectName(u"button102_6")
        self.button102_6.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.button102_6.sizePolicy().hasHeightForWidth())
        self.button102_6.setSizePolicy(sizePolicy1)
        self.button102_6.setMinimumSize(QSize(28, 28))
        self.button102_6.setMaximumSize(QSize(28, 28))
        self.button102_6.setFont(font)

        self.button102_layout_6.addWidget(self.button102_6, 0, 0, 1, 1)


        self.gridLayout_7.addLayout(self.button102_layout_6, 8, 3, 1, 1)

        self.button11_6 = QPushButton(self.wing_2)
        self.button11_6.setObjectName(u"button11_6")
        sizePolicy1.setHeightForWidth(self.button11_6.sizePolicy().hasHeightForWidth())
        self.button11_6.setSizePolicy(sizePolicy1)
        self.button11_6.setMinimumSize(QSize(44, 44))
        self.button11_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button11_6, 6, 4, 1, 1)

        self.button112_layout_6 = QGridLayout()
        self.button112_layout_6.setObjectName(u"button112_layout_6")
        self.button112_layout_6.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.button112_6 = QPushButton(self.wing_2)
        self.button112_6.setObjectName(u"button112_6")
        self.button112_6.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.button112_6.sizePolicy().hasHeightForWidth())
        self.button112_6.setSizePolicy(sizePolicy1)
        self.button112_6.setMinimumSize(QSize(28, 28))
        self.button112_6.setMaximumSize(QSize(28, 28))
        self.button112_6.setFont(font)

        self.button112_layout_6.addWidget(self.button112_6, 0, 0, 1, 1)


        self.gridLayout_7.addLayout(self.button112_layout_6, 0, 10, 1, 1)

        self.button16_6 = QPushButton(self.wing_2)
        self.button16_6.setObjectName(u"button16_6")
        sizePolicy1.setHeightForWidth(self.button16_6.sizePolicy().hasHeightForWidth())
        self.button16_6.setSizePolicy(sizePolicy1)
        self.button16_6.setMinimumSize(QSize(44, 44))
        self.button16_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button16_6, 5, 1, 1, 1)

        self.button60_6 = QPushButton(self.wing_2)
        self.button60_6.setObjectName(u"button60_6")
        sizePolicy1.setHeightForWidth(self.button60_6.sizePolicy().hasHeightForWidth())
        self.button60_6.setSizePolicy(sizePolicy1)
        self.button60_6.setMinimumSize(QSize(44, 44))
        self.button60_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button60_6, 0, 5, 1, 1)

        self.button118_layout_6 = QGridLayout()
        self.button118_layout_6.setObjectName(u"button118_layout_6")
        self.button118_layout_6.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.button118_6 = QPushButton(self.wing_2)
        self.button118_6.setObjectName(u"button118_6")
        self.button118_6.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.button118_6.sizePolicy().hasHeightForWidth())
        self.button118_6.setSizePolicy(sizePolicy1)
        self.button118_6.setMinimumSize(QSize(28, 28))
        self.button118_6.setMaximumSize(QSize(28, 28))
        self.button118_6.setFont(font)

        self.button118_layout_6.addWidget(self.button118_6, 0, 0, 1, 1)


        self.gridLayout_7.addLayout(self.button118_layout_6, 6, 10, 1, 1)

        self.frame_fader51_6 = QFrame(self.wing_2)
        self.frame_fader51_6.setObjectName(u"frame_fader51_6")
        self.frame_fader51_6.setMinimumSize(QSize(88, 250))
        self.frame_fader51_6.setMaximumSize(QSize(88, 250))
        self.frame_fader51_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_fader51_6.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_62 = QGridLayout(self.frame_fader51_6)
        self.gridLayout_62.setObjectName(u"gridLayout_62")
        self.gridLayout_62.setContentsMargins(0, 0, 0, 0)
        self.below_button_layout_fader51_6 = QGridLayout()
        self.below_button_layout_fader51_6.setSpacing(0)
        self.below_button_layout_fader51_6.setObjectName(u"below_button_layout_fader51_6")
        self.fader51_layout_6 = QGridLayout()
        self.fader51_layout_6.setObjectName(u"fader51_layout_6")
        self.fader51_6 = QSlider(self.frame_fader51_6)
        self.fader51_6.setObjectName(u"fader51_6")
        sizePolicy1.setHeightForWidth(self.fader51_6.sizePolicy().hasHeightForWidth())
        self.fader51_6.setSizePolicy(sizePolicy1)
        self.fader51_6.setMinimumSize(QSize(0, 190))
        self.fader51_6.setMaximumSize(QSize(15, 190))
        self.fader51_6.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.fader51_6.setAutoFillBackground(False)
        self.fader51_6.setMaximum(127)
        self.fader51_6.setSliderPosition(0)
        self.fader51_6.setOrientation(Qt.Orientation.Vertical)
        self.fader51_6.setInvertedAppearance(False)
        self.fader51_6.setInvertedControls(False)

        self.fader51_layout_6.addWidget(self.fader51_6, 0, 0, 1, 1)


        self.below_button_layout_fader51_6.addLayout(self.fader51_layout_6, 0, 0, 1, 1)

        self.pushButton_fader51_6 = QPushButton(self.frame_fader51_6)
        self.pushButton_fader51_6.setObjectName(u"pushButton_fader51_6")

        self.below_button_layout_fader51_6.addWidget(self.pushButton_fader51_6, 2, 0, 1, 1)

        self.verticalSpacer_50 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.below_button_layout_fader51_6.addItem(self.verticalSpacer_50, 1, 0, 1, 1)


        self.gridLayout_62.addLayout(self.below_button_layout_fader51_6, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.frame_fader51_6, 10, 4, 1, 1)

        self.button48_6 = QPushButton(self.wing_2)
        self.button48_6.setObjectName(u"button48_6")
        sizePolicy1.setHeightForWidth(self.button48_6.sizePolicy().hasHeightForWidth())
        self.button48_6.setSizePolicy(sizePolicy1)
        self.button48_6.setMinimumSize(QSize(44, 44))
        self.button48_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button48_6, 1, 1, 1, 1)

        self.button58_6 = QPushButton(self.wing_2)
        self.button58_6.setObjectName(u"button58_6")
        sizePolicy1.setHeightForWidth(self.button58_6.sizePolicy().hasHeightForWidth())
        self.button58_6.setSizePolicy(sizePolicy1)
        self.button58_6.setMinimumSize(QSize(44, 44))
        self.button58_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button58_6, 0, 3, 1, 1)

        self.button53_6 = QPushButton(self.wing_2)
        self.button53_6.setObjectName(u"button53_6")
        sizePolicy1.setHeightForWidth(self.button53_6.sizePolicy().hasHeightForWidth())
        self.button53_6.setSizePolicy(sizePolicy1)
        self.button53_6.setMinimumSize(QSize(44, 44))
        self.button53_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button53_6, 1, 6, 1, 1)

        self.left_padding_11 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_7.addItem(self.left_padding_11, 7, 0, 1, 1)

        self.button35_6 = QPushButton(self.wing_2)
        self.button35_6.setObjectName(u"button35_6")
        sizePolicy1.setHeightForWidth(self.button35_6.sizePolicy().hasHeightForWidth())
        self.button35_6.setSizePolicy(sizePolicy1)
        self.button35_6.setMinimumSize(QSize(44, 44))
        self.button35_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button35_6, 3, 4, 1, 1)

        self.button122_layout_6 = QGridLayout()
        self.button122_layout_6.setObjectName(u"button122_layout_6")
        self.button122_layout_6.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.button122_6 = QPushButton(self.wing_2)
        self.button122_6.setObjectName(u"button122_6")
        self.button122_6.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.button122_6.sizePolicy().hasHeightForWidth())
        self.button122_6.setSizePolicy(sizePolicy1)
        self.button122_6.setMinimumSize(QSize(28, 28))
        self.button122_6.setMaximumSize(QSize(28, 28))
        self.button122_6.setFont(font)

        self.button122_layout_6.addWidget(self.button122_6, 0, 0, 1, 1)


        self.gridLayout_7.addLayout(self.button122_layout_6, 8, 10, 1, 1)

        self.button15_6 = QPushButton(self.wing_2)
        self.button15_6.setObjectName(u"button15_6")
        sizePolicy1.setHeightForWidth(self.button15_6.sizePolicy().hasHeightForWidth())
        self.button15_6.setSizePolicy(sizePolicy1)
        self.button15_6.setMinimumSize(QSize(44, 44))
        self.button15_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button15_6, 6, 8, 1, 1)

        self.frame_fader56_6 = QFrame(self.wing_2)
        self.frame_fader56_6.setObjectName(u"frame_fader56_6")
        self.frame_fader56_6.setMinimumSize(QSize(88, 250))
        self.frame_fader56_6.setMaximumSize(QSize(88, 250))
        self.frame_fader56_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_fader56_6.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_66 = QGridLayout(self.frame_fader56_6)
        self.gridLayout_66.setObjectName(u"gridLayout_66")
        self.gridLayout_66.setContentsMargins(0, 0, 0, 0)
        self.below_button_layout_fader56_6 = QGridLayout()
        self.below_button_layout_fader56_6.setSpacing(0)
        self.below_button_layout_fader56_6.setObjectName(u"below_button_layout_fader56_6")
        self.fader56_layout_6 = QGridLayout()
        self.fader56_layout_6.setObjectName(u"fader56_layout_6")
        self.fader56_6 = QSlider(self.frame_fader56_6)
        self.fader56_6.setObjectName(u"fader56_6")
        sizePolicy1.setHeightForWidth(self.fader56_6.sizePolicy().hasHeightForWidth())
        self.fader56_6.setSizePolicy(sizePolicy1)
        self.fader56_6.setMinimumSize(QSize(0, 190))
        self.fader56_6.setMaximumSize(QSize(15, 190))
        self.fader56_6.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.fader56_6.setAutoFillBackground(False)
        self.fader56_6.setMaximum(127)
        self.fader56_6.setSliderPosition(0)
        self.fader56_6.setOrientation(Qt.Orientation.Vertical)
        self.fader56_6.setInvertedAppearance(False)
        self.fader56_6.setInvertedControls(False)

        self.fader56_layout_6.addWidget(self.fader56_6, 0, 0, 1, 1)


        self.below_button_layout_fader56_6.addLayout(self.fader56_layout_6, 0, 0, 1, 1)

        self.pushButton_fader56_6 = QPushButton(self.frame_fader56_6)
        self.pushButton_fader56_6.setObjectName(u"pushButton_fader56_6")

        self.below_button_layout_fader56_6.addWidget(self.pushButton_fader56_6, 2, 0, 1, 1)

        self.verticalSpacer_54 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.below_button_layout_fader56_6.addItem(self.verticalSpacer_54, 1, 0, 1, 1)


        self.gridLayout_66.addLayout(self.below_button_layout_fader56_6, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.frame_fader56_6, 10, 10, 1, 1)

        self.button40_6 = QPushButton(self.wing_2)
        self.button40_6.setObjectName(u"button40_6")
        sizePolicy1.setHeightForWidth(self.button40_6.sizePolicy().hasHeightForWidth())
        self.button40_6.setSizePolicy(sizePolicy1)
        self.button40_6.setMinimumSize(QSize(44, 44))
        self.button40_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button40_6, 2, 1, 1, 1)

        self.button30_6 = QPushButton(self.wing_2)
        self.button30_6.setObjectName(u"button30_6")
        sizePolicy1.setHeightForWidth(self.button30_6.sizePolicy().hasHeightForWidth())
        self.button30_6.setSizePolicy(sizePolicy1)
        self.button30_6.setMinimumSize(QSize(44, 44))
        self.button30_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button30_6, 4, 7, 1, 1)

        self.button37_6 = QPushButton(self.wing_2)
        self.button37_6.setObjectName(u"button37_6")
        sizePolicy1.setHeightForWidth(self.button37_6.sizePolicy().hasHeightForWidth())
        self.button37_6.setSizePolicy(sizePolicy1)
        self.button37_6.setMinimumSize(QSize(44, 44))
        self.button37_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button37_6, 3, 6, 1, 1)

        self.button24_6 = QPushButton(self.wing_2)
        self.button24_6.setObjectName(u"button24_6")
        sizePolicy1.setHeightForWidth(self.button24_6.sizePolicy().hasHeightForWidth())
        self.button24_6.setSizePolicy(sizePolicy1)
        self.button24_6.setMinimumSize(QSize(44, 44))
        self.button24_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button24_6, 4, 1, 1, 1)

        self.right_padding_6 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_7.addItem(self.right_padding_6, 8, 11, 1, 1)

        self.button55_6 = QPushButton(self.wing_2)
        self.button55_6.setObjectName(u"button55_6")
        sizePolicy1.setHeightForWidth(self.button55_6.sizePolicy().hasHeightForWidth())
        self.button55_6.setSizePolicy(sizePolicy1)
        self.button55_6.setMinimumSize(QSize(44, 44))
        self.button55_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button55_6, 1, 8, 1, 1)

        self.button10_6 = QPushButton(self.wing_2)
        self.button10_6.setObjectName(u"button10_6")
        sizePolicy1.setHeightForWidth(self.button10_6.sizePolicy().hasHeightForWidth())
        self.button10_6.setSizePolicy(sizePolicy1)
        self.button10_6.setMinimumSize(QSize(44, 44))
        self.button10_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button10_6, 6, 3, 1, 1)

        self.button14_6 = QPushButton(self.wing_2)
        self.button14_6.setObjectName(u"button14_6")
        sizePolicy1.setHeightForWidth(self.button14_6.sizePolicy().hasHeightForWidth())
        self.button14_6.setSizePolicy(sizePolicy1)
        self.button14_6.setMinimumSize(QSize(44, 44))
        self.button14_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button14_6, 6, 7, 1, 1)

        self.button54_6 = QPushButton(self.wing_2)
        self.button54_6.setObjectName(u"button54_6")
        sizePolicy1.setHeightForWidth(self.button54_6.sizePolicy().hasHeightForWidth())
        self.button54_6.setSizePolicy(sizePolicy1)
        self.button54_6.setMinimumSize(QSize(44, 44))
        self.button54_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button54_6, 1, 7, 1, 1)

        self.button46_6 = QPushButton(self.wing_2)
        self.button46_6.setObjectName(u"button46_6")
        sizePolicy1.setHeightForWidth(self.button46_6.sizePolicy().hasHeightForWidth())
        self.button46_6.setSizePolicy(sizePolicy1)
        self.button46_6.setMinimumSize(QSize(44, 44))
        self.button46_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button46_6, 2, 7, 1, 1)

        self.frame_fader52_6 = QFrame(self.wing_2)
        self.frame_fader52_6.setObjectName(u"frame_fader52_6")
        self.frame_fader52_6.setMinimumSize(QSize(88, 250))
        self.frame_fader52_6.setMaximumSize(QSize(88, 250))
        self.frame_fader52_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_fader52_6.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_58 = QGridLayout(self.frame_fader52_6)
        self.gridLayout_58.setObjectName(u"gridLayout_58")
        self.gridLayout_58.setContentsMargins(0, 0, 0, 0)
        self.below_button_layout_fader52_6 = QGridLayout()
        self.below_button_layout_fader52_6.setSpacing(0)
        self.below_button_layout_fader52_6.setObjectName(u"below_button_layout_fader52_6")
        self.fader52_layout_6 = QGridLayout()
        self.fader52_layout_6.setObjectName(u"fader52_layout_6")
        self.fader52_6 = QSlider(self.frame_fader52_6)
        self.fader52_6.setObjectName(u"fader52_6")
        sizePolicy1.setHeightForWidth(self.fader52_6.sizePolicy().hasHeightForWidth())
        self.fader52_6.setSizePolicy(sizePolicy1)
        self.fader52_6.setMinimumSize(QSize(0, 190))
        self.fader52_6.setMaximumSize(QSize(15, 190))
        self.fader52_6.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.fader52_6.setAutoFillBackground(False)
        self.fader52_6.setMaximum(127)
        self.fader52_6.setSliderPosition(0)
        self.fader52_6.setOrientation(Qt.Orientation.Vertical)
        self.fader52_6.setInvertedAppearance(False)
        self.fader52_6.setInvertedControls(False)

        self.fader52_layout_6.addWidget(self.fader52_6, 0, 0, 1, 1)


        self.below_button_layout_fader52_6.addLayout(self.fader52_layout_6, 0, 0, 1, 1)

        self.pushButton_fader52_6 = QPushButton(self.frame_fader52_6)
        self.pushButton_fader52_6.setObjectName(u"pushButton_fader52_6")

        self.below_button_layout_fader52_6.addWidget(self.pushButton_fader52_6, 2, 0, 1, 1)

        self.verticalSpacer_46 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.below_button_layout_fader52_6.addItem(self.verticalSpacer_46, 1, 0, 1, 1)


        self.gridLayout_58.addLayout(self.below_button_layout_fader52_6, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.frame_fader52_6, 10, 5, 1, 1)

        self.button44_6 = QPushButton(self.wing_2)
        self.button44_6.setObjectName(u"button44_6")
        sizePolicy1.setHeightForWidth(self.button44_6.sizePolicy().hasHeightForWidth())
        self.button44_6.setSizePolicy(sizePolicy1)
        self.button44_6.setMinimumSize(QSize(44, 44))
        self.button44_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button44_6, 2, 5, 1, 1)

        self.left_padding_12 = QSpacerItem(0, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.left_padding_12, 8, 0, 1, 1)

        self.button17_6 = QPushButton(self.wing_2)
        self.button17_6.setObjectName(u"button17_6")
        sizePolicy1.setHeightForWidth(self.button17_6.sizePolicy().hasHeightForWidth())
        self.button17_6.setSizePolicy(sizePolicy1)
        self.button17_6.setMinimumSize(QSize(44, 44))
        self.button17_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button17_6, 5, 2, 1, 1)

        self.button117_layout_6 = QGridLayout()
        self.button117_layout_6.setObjectName(u"button117_layout_6")
        self.button117_layout_6.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.button117_6 = QPushButton(self.wing_2)
        self.button117_6.setObjectName(u"button117_6")
        self.button117_6.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.button117_6.sizePolicy().hasHeightForWidth())
        self.button117_6.setSizePolicy(sizePolicy1)
        self.button117_6.setMinimumSize(QSize(28, 28))
        self.button117_6.setMaximumSize(QSize(28, 28))
        self.button117_6.setFont(font)

        self.button117_layout_6.addWidget(self.button117_6, 0, 0, 1, 1)


        self.gridLayout_7.addLayout(self.button117_layout_6, 5, 10, 1, 1)

        self.button43_6 = QPushButton(self.wing_2)
        self.button43_6.setObjectName(u"button43_6")
        sizePolicy1.setHeightForWidth(self.button43_6.sizePolicy().hasHeightForWidth())
        self.button43_6.setSizePolicy(sizePolicy1)
        self.button43_6.setMinimumSize(QSize(44, 44))
        self.button43_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button43_6, 2, 4, 1, 1)

        self.button2_6 = QPushButton(self.wing_2)
        self.button2_6.setObjectName(u"button2_6")
        sizePolicy1.setHeightForWidth(self.button2_6.sizePolicy().hasHeightForWidth())
        self.button2_6.setSizePolicy(sizePolicy1)
        self.button2_6.setMinimumSize(QSize(44, 44))
        self.button2_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button2_6, 7, 3, 1, 1)

        self.button105_layout_6 = QGridLayout()
        self.button105_layout_6.setObjectName(u"button105_layout_6")
        self.button105_6 = QPushButton(self.wing_2)
        self.button105_6.setObjectName(u"button105_6")
        self.button105_6.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.button105_6.sizePolicy().hasHeightForWidth())
        self.button105_6.setSizePolicy(sizePolicy1)
        self.button105_6.setMinimumSize(QSize(28, 28))
        self.button105_6.setMaximumSize(QSize(28, 28))
        self.button105_6.setFont(font)

        self.button105_layout_6.addWidget(self.button105_6, 0, 0, 1, 1)


        self.gridLayout_7.addLayout(self.button105_layout_6, 8, 6, 1, 1)

        self.button103_layout_6 = QGridLayout()
        self.button103_layout_6.setObjectName(u"button103_layout_6")
        self.button103_6 = QPushButton(self.wing_2)
        self.button103_6.setObjectName(u"button103_6")
        self.button103_6.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.button103_6.sizePolicy().hasHeightForWidth())
        self.button103_6.setSizePolicy(sizePolicy1)
        self.button103_6.setMinimumSize(QSize(28, 28))
        self.button103_6.setMaximumSize(QSize(28, 28))
        self.button103_6.setFont(font)

        self.button103_layout_6.addWidget(self.button103_6, 0, 0, 1, 1)


        self.gridLayout_7.addLayout(self.button103_layout_6, 8, 4, 1, 1)

        self.button9_6 = QPushButton(self.wing_2)
        self.button9_6.setObjectName(u"button9_6")
        sizePolicy1.setHeightForWidth(self.button9_6.sizePolicy().hasHeightForWidth())
        self.button9_6.setSizePolicy(sizePolicy1)
        self.button9_6.setMinimumSize(QSize(44, 44))
        self.button9_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button9_6, 6, 2, 1, 1)

        self.button51_6 = QPushButton(self.wing_2)
        self.button51_6.setObjectName(u"button51_6")
        sizePolicy1.setHeightForWidth(self.button51_6.sizePolicy().hasHeightForWidth())
        self.button51_6.setSizePolicy(sizePolicy1)
        self.button51_6.setMinimumSize(QSize(44, 44))
        self.button51_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button51_6, 1, 4, 1, 1)

        self.button26_6 = QPushButton(self.wing_2)
        self.button26_6.setObjectName(u"button26_6")
        sizePolicy1.setHeightForWidth(self.button26_6.sizePolicy().hasHeightForWidth())
        self.button26_6.setSizePolicy(sizePolicy1)
        self.button26_6.setMinimumSize(QSize(44, 44))
        self.button26_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button26_6, 4, 3, 1, 1)

        self.button107_layout_6 = QGridLayout()
        self.button107_layout_6.setObjectName(u"button107_layout_6")
        self.button107_6 = QPushButton(self.wing_2)
        self.button107_6.setObjectName(u"button107_6")
        self.button107_6.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.button107_6.sizePolicy().hasHeightForWidth())
        self.button107_6.setSizePolicy(sizePolicy1)
        self.button107_6.setMinimumSize(QSize(28, 28))
        self.button107_6.setMaximumSize(QSize(28, 28))
        self.button107_6.setFont(font)

        self.button107_layout_6.addWidget(self.button107_6, 0, 0, 1, 1)


        self.gridLayout_7.addLayout(self.button107_layout_6, 8, 8, 1, 1)

        self.button13_6 = QPushButton(self.wing_2)
        self.button13_6.setObjectName(u"button13_6")
        sizePolicy1.setHeightForWidth(self.button13_6.sizePolicy().hasHeightForWidth())
        self.button13_6.setSizePolicy(sizePolicy1)
        self.button13_6.setMinimumSize(QSize(44, 44))
        self.button13_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button13_6, 6, 6, 1, 1)

        self.button0_6 = QPushButton(self.wing_2)
        self.button0_6.setObjectName(u"button0_6")
        sizePolicy1.setHeightForWidth(self.button0_6.sizePolicy().hasHeightForWidth())
        self.button0_6.setSizePolicy(sizePolicy1)
        self.button0_6.setMinimumSize(QSize(44, 44))
        self.button0_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button0_6, 7, 1, 1, 1)

        self.button59_6 = QPushButton(self.wing_2)
        self.button59_6.setObjectName(u"button59_6")
        sizePolicy1.setHeightForWidth(self.button59_6.sizePolicy().hasHeightForWidth())
        self.button59_6.setSizePolicy(sizePolicy1)
        self.button59_6.setMinimumSize(QSize(44, 44))
        self.button59_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button59_6, 0, 4, 1, 1)

        self.button119_layout_6 = QGridLayout()
        self.button119_layout_6.setObjectName(u"button119_layout_6")
        self.button119_layout_6.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.button119_6 = QPushButton(self.wing_2)
        self.button119_6.setObjectName(u"button119_6")
        self.button119_6.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.button119_6.sizePolicy().hasHeightForWidth())
        self.button119_6.setSizePolicy(sizePolicy1)
        self.button119_6.setMinimumSize(QSize(28, 28))
        self.button119_6.setMaximumSize(QSize(28, 28))
        self.button119_6.setFont(font)

        self.button119_layout_6.addWidget(self.button119_6, 0, 0, 1, 1)


        self.gridLayout_7.addLayout(self.button119_layout_6, 7, 10, 1, 1)

        self.button116_layout_6 = QGridLayout()
        self.button116_layout_6.setObjectName(u"button116_layout_6")
        self.button116_layout_6.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.button116_6 = QPushButton(self.wing_2)
        self.button116_6.setObjectName(u"button116_6")
        self.button116_6.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.button116_6.sizePolicy().hasHeightForWidth())
        self.button116_6.setSizePolicy(sizePolicy1)
        self.button116_6.setMinimumSize(QSize(28, 28))
        self.button116_6.setMaximumSize(QSize(28, 28))
        self.button116_6.setFont(font)

        self.button116_layout_6.addWidget(self.button116_6, 0, 0, 1, 1)


        self.gridLayout_7.addLayout(self.button116_layout_6, 4, 10, 1, 1)

        self.button1_6 = QPushButton(self.wing_2)
        self.button1_6.setObjectName(u"button1_6")
        sizePolicy1.setHeightForWidth(self.button1_6.sizePolicy().hasHeightForWidth())
        self.button1_6.setSizePolicy(sizePolicy1)
        self.button1_6.setMinimumSize(QSize(44, 44))
        self.button1_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button1_6, 7, 2, 1, 1)

        self.button39_6 = QPushButton(self.wing_2)
        self.button39_6.setObjectName(u"button39_6")
        sizePolicy1.setHeightForWidth(self.button39_6.sizePolicy().hasHeightForWidth())
        self.button39_6.setSizePolicy(sizePolicy1)
        self.button39_6.setMinimumSize(QSize(44, 44))
        self.button39_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button39_6, 3, 8, 1, 1)

        self.button61_6 = QPushButton(self.wing_2)
        self.button61_6.setObjectName(u"button61_6")
        sizePolicy1.setHeightForWidth(self.button61_6.sizePolicy().hasHeightForWidth())
        self.button61_6.setSizePolicy(sizePolicy1)
        self.button61_6.setMinimumSize(QSize(44, 44))
        self.button61_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button61_6, 0, 6, 1, 1)

        self.button12_6 = QPushButton(self.wing_2)
        self.button12_6.setObjectName(u"button12_6")
        self.button12_6.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.button12_6.sizePolicy().hasHeightForWidth())
        self.button12_6.setSizePolicy(sizePolicy1)
        self.button12_6.setMinimumSize(QSize(44, 44))
        self.button12_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button12_6, 6, 5, 1, 1)

        self.button45_6 = QPushButton(self.wing_2)
        self.button45_6.setObjectName(u"button45_6")
        sizePolicy1.setHeightForWidth(self.button45_6.sizePolicy().hasHeightForWidth())
        self.button45_6.setSizePolicy(sizePolicy1)
        self.button45_6.setMinimumSize(QSize(44, 44))
        self.button45_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button45_6, 2, 6, 1, 1)

        self.button4_6 = QPushButton(self.wing_2)
        self.button4_6.setObjectName(u"button4_6")
        sizePolicy1.setHeightForWidth(self.button4_6.sizePolicy().hasHeightForWidth())
        self.button4_6.setSizePolicy(sizePolicy1)
        self.button4_6.setMinimumSize(QSize(44, 44))
        self.button4_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button4_6, 7, 5, 1, 1)

        self.button104_layout_6 = QGridLayout()
        self.button104_layout_6.setObjectName(u"button104_layout_6")
        self.button104_6 = QPushButton(self.wing_2)
        self.button104_6.setObjectName(u"button104_6")
        self.button104_6.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.button104_6.sizePolicy().hasHeightForWidth())
        self.button104_6.setSizePolicy(sizePolicy1)
        self.button104_6.setMinimumSize(QSize(28, 28))
        self.button104_6.setMaximumSize(QSize(28, 28))
        self.button104_6.setFont(font)

        self.button104_layout_6.addWidget(self.button104_6, 0, 0, 1, 1)


        self.gridLayout_7.addLayout(self.button104_layout_6, 8, 5, 1, 1)

        self.button62_6 = QPushButton(self.wing_2)
        self.button62_6.setObjectName(u"button62_6")
        sizePolicy1.setHeightForWidth(self.button62_6.sizePolicy().hasHeightForWidth())
        self.button62_6.setSizePolicy(sizePolicy1)
        self.button62_6.setMinimumSize(QSize(44, 44))
        self.button62_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button62_6, 0, 7, 1, 1)

        self.button18_6 = QPushButton(self.wing_2)
        self.button18_6.setObjectName(u"button18_6")
        sizePolicy1.setHeightForWidth(self.button18_6.sizePolicy().hasHeightForWidth())
        self.button18_6.setSizePolicy(sizePolicy1)
        self.button18_6.setMinimumSize(QSize(44, 44))
        self.button18_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button18_6, 5, 3, 1, 1)

        self.button29_6 = QPushButton(self.wing_2)
        self.button29_6.setObjectName(u"button29_6")
        sizePolicy1.setHeightForWidth(self.button29_6.sizePolicy().hasHeightForWidth())
        self.button29_6.setSizePolicy(sizePolicy1)
        self.button29_6.setMinimumSize(QSize(44, 44))
        self.button29_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button29_6, 4, 6, 1, 1)

        self.frame_fader54_6 = QFrame(self.wing_2)
        self.frame_fader54_6.setObjectName(u"frame_fader54_6")
        self.frame_fader54_6.setMinimumSize(QSize(88, 250))
        self.frame_fader54_6.setMaximumSize(QSize(88, 250))
        self.frame_fader54_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_fader54_6.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_64 = QGridLayout(self.frame_fader54_6)
        self.gridLayout_64.setObjectName(u"gridLayout_64")
        self.gridLayout_64.setContentsMargins(0, 0, 0, 0)
        self.below_button_layout_fader54_6 = QGridLayout()
        self.below_button_layout_fader54_6.setSpacing(0)
        self.below_button_layout_fader54_6.setObjectName(u"below_button_layout_fader54_6")
        self.pushButton_fader54_6 = QPushButton(self.frame_fader54_6)
        self.pushButton_fader54_6.setObjectName(u"pushButton_fader54_6")

        self.below_button_layout_fader54_6.addWidget(self.pushButton_fader54_6, 2, 0, 1, 1)

        self.fader54_layout_6 = QGridLayout()
        self.fader54_layout_6.setObjectName(u"fader54_layout_6")
        self.fader54_6 = QSlider(self.frame_fader54_6)
        self.fader54_6.setObjectName(u"fader54_6")
        sizePolicy1.setHeightForWidth(self.fader54_6.sizePolicy().hasHeightForWidth())
        self.fader54_6.setSizePolicy(sizePolicy1)
        self.fader54_6.setMinimumSize(QSize(0, 190))
        self.fader54_6.setMaximumSize(QSize(15, 190))
        self.fader54_6.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.fader54_6.setAutoFillBackground(False)
        self.fader54_6.setMaximum(127)
        self.fader54_6.setSliderPosition(0)
        self.fader54_6.setOrientation(Qt.Orientation.Vertical)
        self.fader54_6.setInvertedAppearance(False)
        self.fader54_6.setInvertedControls(False)

        self.fader54_layout_6.addWidget(self.fader54_6, 0, 0, 1, 1)


        self.below_button_layout_fader54_6.addLayout(self.fader54_layout_6, 0, 0, 1, 1)

        self.verticalSpacer_52 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.below_button_layout_fader54_6.addItem(self.verticalSpacer_52, 1, 0, 1, 1)


        self.gridLayout_64.addLayout(self.below_button_layout_fader54_6, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.frame_fader54_6, 10, 7, 1, 1)

        self.button31_6 = QPushButton(self.wing_2)
        self.button31_6.setObjectName(u"button31_6")
        sizePolicy1.setHeightForWidth(self.button31_6.sizePolicy().hasHeightForWidth())
        self.button31_6.setSizePolicy(sizePolicy1)
        self.button31_6.setMinimumSize(QSize(44, 44))
        self.button31_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button31_6, 4, 8, 1, 1)

        self.button3_6 = QPushButton(self.wing_2)
        self.button3_6.setObjectName(u"button3_6")
        sizePolicy1.setHeightForWidth(self.button3_6.sizePolicy().hasHeightForWidth())
        self.button3_6.setSizePolicy(sizePolicy1)
        self.button3_6.setMinimumSize(QSize(44, 44))
        self.button3_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button3_6, 7, 4, 1, 1)

        self.frame_fader53_6 = QFrame(self.wing_2)
        self.frame_fader53_6.setObjectName(u"frame_fader53_6")
        self.frame_fader53_6.setMinimumSize(QSize(88, 250))
        self.frame_fader53_6.setMaximumSize(QSize(88, 250))
        self.frame_fader53_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_fader53_6.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_59 = QGridLayout(self.frame_fader53_6)
        self.gridLayout_59.setObjectName(u"gridLayout_59")
        self.gridLayout_59.setContentsMargins(0, 0, 0, 0)
        self.below_button_layout_fader53_6 = QGridLayout()
        self.below_button_layout_fader53_6.setSpacing(0)
        self.below_button_layout_fader53_6.setObjectName(u"below_button_layout_fader53_6")
        self.fader53_layout_6 = QGridLayout()
        self.fader53_layout_6.setObjectName(u"fader53_layout_6")
        self.fader53_6 = QSlider(self.frame_fader53_6)
        self.fader53_6.setObjectName(u"fader53_6")
        sizePolicy1.setHeightForWidth(self.fader53_6.sizePolicy().hasHeightForWidth())
        self.fader53_6.setSizePolicy(sizePolicy1)
        self.fader53_6.setMinimumSize(QSize(0, 190))
        self.fader53_6.setMaximumSize(QSize(15, 190))
        self.fader53_6.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.fader53_6.setAutoFillBackground(False)
        self.fader53_6.setMaximum(127)
        self.fader53_6.setSliderPosition(0)
        self.fader53_6.setOrientation(Qt.Orientation.Vertical)
        self.fader53_6.setInvertedAppearance(False)
        self.fader53_6.setInvertedControls(False)

        self.fader53_layout_6.addWidget(self.fader53_6, 0, 0, 1, 1)


        self.below_button_layout_fader53_6.addLayout(self.fader53_layout_6, 0, 0, 1, 1)

        self.pushButton_fader53_6 = QPushButton(self.frame_fader53_6)
        self.pushButton_fader53_6.setObjectName(u"pushButton_fader53_6")

        self.below_button_layout_fader53_6.addWidget(self.pushButton_fader53_6, 2, 0, 1, 1)

        self.verticalSpacer_47 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.below_button_layout_fader53_6.addItem(self.verticalSpacer_47, 1, 0, 1, 1)


        self.gridLayout_59.addLayout(self.below_button_layout_fader53_6, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.frame_fader53_6, 10, 6, 1, 1)

        self.button41_6 = QPushButton(self.wing_2)
        self.button41_6.setObjectName(u"button41_6")
        sizePolicy1.setHeightForWidth(self.button41_6.sizePolicy().hasHeightForWidth())
        self.button41_6.setSizePolicy(sizePolicy1)
        self.button41_6.setMinimumSize(QSize(44, 44))
        self.button41_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button41_6, 2, 2, 1, 1)

        self.button115_layout_6 = QGridLayout()
        self.button115_layout_6.setObjectName(u"button115_layout_6")
        self.button115_layout_6.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.button115_6 = QPushButton(self.wing_2)
        self.button115_6.setObjectName(u"button115_6")
        self.button115_6.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.button115_6.sizePolicy().hasHeightForWidth())
        self.button115_6.setSizePolicy(sizePolicy1)
        self.button115_6.setMinimumSize(QSize(28, 28))
        self.button115_6.setMaximumSize(QSize(28, 28))
        self.button115_6.setFont(font)

        self.button115_layout_6.addWidget(self.button115_6, 0, 0, 1, 1)


        self.gridLayout_7.addLayout(self.button115_layout_6, 3, 10, 1, 1)

        self.frame_fader49_6 = QFrame(self.wing_2)
        self.frame_fader49_6.setObjectName(u"frame_fader49_6")
        self.frame_fader49_6.setMinimumSize(QSize(88, 250))
        self.frame_fader49_6.setMaximumSize(QSize(88, 250))
        self.frame_fader49_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_fader49_6.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_60 = QGridLayout(self.frame_fader49_6)
        self.gridLayout_60.setObjectName(u"gridLayout_60")
        self.gridLayout_60.setContentsMargins(0, 0, 0, 0)
        self.below_button_layout_fader49_6 = QGridLayout()
        self.below_button_layout_fader49_6.setSpacing(0)
        self.below_button_layout_fader49_6.setObjectName(u"below_button_layout_fader49_6")
        self.pushButton_fader49_6 = QPushButton(self.frame_fader49_6)
        self.pushButton_fader49_6.setObjectName(u"pushButton_fader49_6")

        self.below_button_layout_fader49_6.addWidget(self.pushButton_fader49_6, 2, 0, 1, 1)

        self.fader49_layout_6 = QGridLayout()
        self.fader49_layout_6.setObjectName(u"fader49_layout_6")
        self.fader49_6 = QSlider(self.frame_fader49_6)
        self.fader49_6.setObjectName(u"fader49_6")
        sizePolicy1.setHeightForWidth(self.fader49_6.sizePolicy().hasHeightForWidth())
        self.fader49_6.setSizePolicy(sizePolicy1)
        self.fader49_6.setMinimumSize(QSize(0, 190))
        self.fader49_6.setMaximumSize(QSize(15, 190))
        self.fader49_6.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.fader49_6.setAutoFillBackground(False)
        self.fader49_6.setMaximum(127)
        self.fader49_6.setSliderPosition(0)
        self.fader49_6.setOrientation(Qt.Orientation.Vertical)
        self.fader49_6.setInvertedAppearance(False)
        self.fader49_6.setInvertedControls(False)

        self.fader49_layout_6.addWidget(self.fader49_6, 0, 0, 1, 1)


        self.below_button_layout_fader49_6.addLayout(self.fader49_layout_6, 0, 0, 1, 1)

        self.verticalSpacer_48 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.below_button_layout_fader49_6.addItem(self.verticalSpacer_48, 1, 0, 1, 1)


        self.gridLayout_60.addLayout(self.below_button_layout_fader49_6, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.frame_fader49_6, 10, 2, 1, 1)

        self.button106_layout_6 = QGridLayout()
        self.button106_layout_6.setObjectName(u"button106_layout_6")
        self.button106_6 = QPushButton(self.wing_2)
        self.button106_6.setObjectName(u"button106_6")
        self.button106_6.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.button106_6.sizePolicy().hasHeightForWidth())
        self.button106_6.setSizePolicy(sizePolicy1)
        self.button106_6.setMinimumSize(QSize(28, 28))
        self.button106_6.setMaximumSize(QSize(28, 28))
        self.button106_6.setFont(font)

        self.button106_layout_6.addWidget(self.button106_6, 0, 0, 1, 1)


        self.gridLayout_7.addLayout(self.button106_layout_6, 8, 7, 1, 1)

        self.button57_6 = QPushButton(self.wing_2)
        self.button57_6.setObjectName(u"button57_6")
        sizePolicy1.setHeightForWidth(self.button57_6.sizePolicy().hasHeightForWidth())
        self.button57_6.setSizePolicy(sizePolicy1)
        self.button57_6.setMinimumSize(QSize(44, 44))
        self.button57_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button57_6, 0, 2, 1, 1)

        self.button21_6 = QPushButton(self.wing_2)
        self.button21_6.setObjectName(u"button21_6")
        sizePolicy1.setHeightForWidth(self.button21_6.sizePolicy().hasHeightForWidth())
        self.button21_6.setSizePolicy(sizePolicy1)
        self.button21_6.setMinimumSize(QSize(44, 44))
        self.button21_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button21_6, 5, 6, 1, 1)

        self.button19_6 = QPushButton(self.wing_2)
        self.button19_6.setObjectName(u"button19_6")
        sizePolicy1.setHeightForWidth(self.button19_6.sizePolicy().hasHeightForWidth())
        self.button19_6.setSizePolicy(sizePolicy1)
        self.button19_6.setMinimumSize(QSize(44, 44))
        self.button19_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button19_6, 5, 4, 1, 1)

        self.button101_layout_6 = QGridLayout()
        self.button101_layout_6.setObjectName(u"button101_layout_6")
        self.button101_6 = QPushButton(self.wing_2)
        self.button101_6.setObjectName(u"button101_6")
        self.button101_6.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.button101_6.sizePolicy().hasHeightForWidth())
        self.button101_6.setSizePolicy(sizePolicy1)
        self.button101_6.setMinimumSize(QSize(28, 28))
        self.button101_6.setMaximumSize(QSize(28, 28))
        self.button101_6.setFont(font)

        self.button101_layout_6.addWidget(self.button101_6, 0, 0, 1, 1)


        self.gridLayout_7.addLayout(self.button101_layout_6, 8, 2, 1, 1)

        self.button100_layout_6 = QGridLayout()
        self.button100_layout_6.setObjectName(u"button100_layout_6")
        self.button100_6 = QPushButton(self.wing_2)
        self.button100_6.setObjectName(u"button100_6")
        self.button100_6.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.button100_6.sizePolicy().hasHeightForWidth())
        self.button100_6.setSizePolicy(sizePolicy1)
        self.button100_6.setMinimumSize(QSize(28, 28))
        self.button100_6.setMaximumSize(QSize(28, 28))
        self.button100_6.setFont(font)
        self.button100_6.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.button100_6.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.button100_6.setAutoDefault(False)

        self.button100_layout_6.addWidget(self.button100_6, 0, 0, 1, 1)


        self.gridLayout_7.addLayout(self.button100_layout_6, 8, 1, 1, 1)

        self.button23_6 = QPushButton(self.wing_2)
        self.button23_6.setObjectName(u"button23_6")
        sizePolicy1.setHeightForWidth(self.button23_6.sizePolicy().hasHeightForWidth())
        self.button23_6.setSizePolicy(sizePolicy1)
        self.button23_6.setMinimumSize(QSize(44, 44))
        self.button23_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button23_6, 5, 8, 1, 1)

        self.button27_6 = QPushButton(self.wing_2)
        self.button27_6.setObjectName(u"button27_6")
        sizePolicy1.setHeightForWidth(self.button27_6.sizePolicy().hasHeightForWidth())
        self.button27_6.setSizePolicy(sizePolicy1)
        self.button27_6.setMinimumSize(QSize(44, 44))
        self.button27_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button27_6, 4, 4, 1, 1)

        self.frame_fader55_6 = QFrame(self.wing_2)
        self.frame_fader55_6.setObjectName(u"frame_fader55_6")
        self.frame_fader55_6.setMinimumSize(QSize(88, 250))
        self.frame_fader55_6.setMaximumSize(QSize(88, 250))
        self.frame_fader55_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_fader55_6.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_65 = QGridLayout(self.frame_fader55_6)
        self.gridLayout_65.setObjectName(u"gridLayout_65")
        self.gridLayout_65.setContentsMargins(0, 0, 0, 0)
        self.below_button_layout_fader55_6 = QGridLayout()
        self.below_button_layout_fader55_6.setSpacing(0)
        self.below_button_layout_fader55_6.setObjectName(u"below_button_layout_fader55_6")
        self.fader55_layout_6 = QGridLayout()
        self.fader55_layout_6.setObjectName(u"fader55_layout_6")
        self.fader55_6 = QSlider(self.frame_fader55_6)
        self.fader55_6.setObjectName(u"fader55_6")
        sizePolicy1.setHeightForWidth(self.fader55_6.sizePolicy().hasHeightForWidth())
        self.fader55_6.setSizePolicy(sizePolicy1)
        self.fader55_6.setMinimumSize(QSize(0, 190))
        self.fader55_6.setMaximumSize(QSize(15, 190))
        self.fader55_6.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.fader55_6.setAutoFillBackground(False)
        self.fader55_6.setMaximum(127)
        self.fader55_6.setSliderPosition(0)
        self.fader55_6.setOrientation(Qt.Orientation.Vertical)
        self.fader55_6.setInvertedAppearance(False)
        self.fader55_6.setInvertedControls(False)

        self.fader55_layout_6.addWidget(self.fader55_6, 0, 0, 1, 1)


        self.below_button_layout_fader55_6.addLayout(self.fader55_layout_6, 0, 0, 1, 1)

        self.pushButton_fader55_6 = QPushButton(self.frame_fader55_6)
        self.pushButton_fader55_6.setObjectName(u"pushButton_fader55_6")

        self.below_button_layout_fader55_6.addWidget(self.pushButton_fader55_6, 2, 0, 1, 1)

        self.verticalSpacer_53 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.below_button_layout_fader55_6.addItem(self.verticalSpacer_53, 1, 0, 1, 1)


        self.gridLayout_65.addLayout(self.below_button_layout_fader55_6, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.frame_fader55_6, 10, 8, 1, 1)

        self.button8_6 = QPushButton(self.wing_2)
        self.button8_6.setObjectName(u"button8_6")
        sizePolicy1.setHeightForWidth(self.button8_6.sizePolicy().hasHeightForWidth())
        self.button8_6.setSizePolicy(sizePolicy1)
        self.button8_6.setMinimumSize(QSize(44, 44))
        self.button8_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button8_6, 6, 1, 1, 1)

        self.right_padding2_6 = QSpacerItem(0, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.right_padding2_6, 7, 11, 1, 1)

        self.button5_6 = QPushButton(self.wing_2)
        self.button5_6.setObjectName(u"button5_6")
        sizePolicy1.setHeightForWidth(self.button5_6.sizePolicy().hasHeightForWidth())
        self.button5_6.setSizePolicy(sizePolicy1)
        self.button5_6.setMinimumSize(QSize(44, 44))
        self.button5_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button5_6, 7, 6, 1, 1)

        self.button6_6 = QPushButton(self.wing_2)
        self.button6_6.setObjectName(u"button6_6")
        sizePolicy1.setHeightForWidth(self.button6_6.sizePolicy().hasHeightForWidth())
        self.button6_6.setSizePolicy(sizePolicy1)
        self.button6_6.setMinimumSize(QSize(44, 44))
        self.button6_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button6_6, 7, 7, 1, 1)

        self.frame_fader48_6 = QFrame(self.wing_2)
        self.frame_fader48_6.setObjectName(u"frame_fader48_6")
        self.frame_fader48_6.setMinimumSize(QSize(88, 250))
        self.frame_fader48_6.setMaximumSize(QSize(88, 250))
        self.frame_fader48_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_fader48_6.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_61 = QGridLayout(self.frame_fader48_6)
        self.gridLayout_61.setObjectName(u"gridLayout_61")
        self.gridLayout_61.setContentsMargins(0, 0, 0, 0)
        self.below_button_layout_fader48_6 = QGridLayout()
        self.below_button_layout_fader48_6.setSpacing(0)
        self.below_button_layout_fader48_6.setObjectName(u"below_button_layout_fader48_6")
        self.fader48_layout_6 = QGridLayout()
        self.fader48_layout_6.setObjectName(u"fader48_layout_6")
        self.fader48_6 = QSlider(self.frame_fader48_6)
        self.fader48_6.setObjectName(u"fader48_6")
        sizePolicy1.setHeightForWidth(self.fader48_6.sizePolicy().hasHeightForWidth())
        self.fader48_6.setSizePolicy(sizePolicy1)
        self.fader48_6.setMinimumSize(QSize(0, 190))
        self.fader48_6.setMaximumSize(QSize(15, 190))
        self.fader48_6.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.fader48_6.setAutoFillBackground(False)
        self.fader48_6.setMaximum(127)
        self.fader48_6.setSliderPosition(0)
        self.fader48_6.setOrientation(Qt.Orientation.Vertical)
        self.fader48_6.setInvertedAppearance(False)
        self.fader48_6.setInvertedControls(False)

        self.fader48_layout_6.addWidget(self.fader48_6, 0, 0, 1, 1)


        self.below_button_layout_fader48_6.addLayout(self.fader48_layout_6, 0, 0, 1, 1)

        self.pushButton_fader48_6 = QPushButton(self.frame_fader48_6)
        self.pushButton_fader48_6.setObjectName(u"pushButton_fader48_6")

        self.below_button_layout_fader48_6.addWidget(self.pushButton_fader48_6, 2, 0, 1, 1)

        self.verticalSpacer_49 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.below_button_layout_fader48_6.addItem(self.verticalSpacer_49, 1, 0, 1, 1)


        self.gridLayout_61.addLayout(self.below_button_layout_fader48_6, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.frame_fader48_6, 10, 1, 1, 1)

        self.button25_6 = QPushButton(self.wing_2)
        self.button25_6.setObjectName(u"button25_6")
        sizePolicy1.setHeightForWidth(self.button25_6.sizePolicy().hasHeightForWidth())
        self.button25_6.setSizePolicy(sizePolicy1)
        self.button25_6.setMinimumSize(QSize(44, 44))
        self.button25_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button25_6, 4, 2, 1, 1)

        self.button32_6 = QPushButton(self.wing_2)
        self.button32_6.setObjectName(u"button32_6")
        sizePolicy1.setHeightForWidth(self.button32_6.sizePolicy().hasHeightForWidth())
        self.button32_6.setSizePolicy(sizePolicy1)
        self.button32_6.setMinimumSize(QSize(44, 44))
        self.button32_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button32_6, 3, 1, 1, 1)

        self.button36_6 = QPushButton(self.wing_2)
        self.button36_6.setObjectName(u"button36_6")
        sizePolicy1.setHeightForWidth(self.button36_6.sizePolicy().hasHeightForWidth())
        self.button36_6.setSizePolicy(sizePolicy1)
        self.button36_6.setMinimumSize(QSize(44, 44))
        self.button36_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button36_6, 3, 5, 1, 1)

        self.frame_fader50_6 = QFrame(self.wing_2)
        self.frame_fader50_6.setObjectName(u"frame_fader50_6")
        self.frame_fader50_6.setMinimumSize(QSize(88, 250))
        self.frame_fader50_6.setMaximumSize(QSize(88, 250))
        self.frame_fader50_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_fader50_6.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_63 = QGridLayout(self.frame_fader50_6)
        self.gridLayout_63.setObjectName(u"gridLayout_63")
        self.gridLayout_63.setContentsMargins(0, 0, 0, 0)
        self.below_button_layout_fader50_6 = QGridLayout()
        self.below_button_layout_fader50_6.setSpacing(0)
        self.below_button_layout_fader50_6.setObjectName(u"below_button_layout_fader50_6")
        self.pushButton_fader50_6 = QPushButton(self.frame_fader50_6)
        self.pushButton_fader50_6.setObjectName(u"pushButton_fader50_6")

        self.below_button_layout_fader50_6.addWidget(self.pushButton_fader50_6, 2, 0, 1, 1)

        self.fader50_layout_6 = QGridLayout()
        self.fader50_layout_6.setObjectName(u"fader50_layout_6")
        self.fader50_6 = QSlider(self.frame_fader50_6)
        self.fader50_6.setObjectName(u"fader50_6")
        sizePolicy1.setHeightForWidth(self.fader50_6.sizePolicy().hasHeightForWidth())
        self.fader50_6.setSizePolicy(sizePolicy1)
        self.fader50_6.setMinimumSize(QSize(0, 190))
        self.fader50_6.setMaximumSize(QSize(15, 190))
        self.fader50_6.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.fader50_6.setAutoFillBackground(False)
        self.fader50_6.setMaximum(127)
        self.fader50_6.setSliderPosition(0)
        self.fader50_6.setOrientation(Qt.Orientation.Vertical)
        self.fader50_6.setInvertedAppearance(False)
        self.fader50_6.setInvertedControls(False)

        self.fader50_layout_6.addWidget(self.fader50_6, 0, 0, 1, 1)


        self.below_button_layout_fader50_6.addLayout(self.fader50_layout_6, 0, 0, 1, 1)

        self.verticalSpacer_51 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.below_button_layout_fader50_6.addItem(self.verticalSpacer_51, 1, 0, 1, 1)


        self.gridLayout_63.addLayout(self.below_button_layout_fader50_6, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.frame_fader50_6, 10, 3, 1, 1)

        self.button33_6 = QPushButton(self.wing_2)
        self.button33_6.setObjectName(u"button33_6")
        sizePolicy1.setHeightForWidth(self.button33_6.sizePolicy().hasHeightForWidth())
        self.button33_6.setSizePolicy(sizePolicy1)
        self.button33_6.setMinimumSize(QSize(44, 44))
        self.button33_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button33_6, 3, 2, 1, 1)

        self.button52_6 = QPushButton(self.wing_2)
        self.button52_6.setObjectName(u"button52_6")
        sizePolicy1.setHeightForWidth(self.button52_6.sizePolicy().hasHeightForWidth())
        self.button52_6.setSizePolicy(sizePolicy1)
        self.button52_6.setMinimumSize(QSize(44, 44))
        self.button52_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button52_6, 1, 5, 1, 1)

        self.button42_6 = QPushButton(self.wing_2)
        self.button42_6.setObjectName(u"button42_6")
        sizePolicy1.setHeightForWidth(self.button42_6.sizePolicy().hasHeightForWidth())
        self.button42_6.setSizePolicy(sizePolicy1)
        self.button42_6.setMinimumSize(QSize(44, 44))
        self.button42_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button42_6, 2, 3, 1, 1)

        self.button34_6 = QPushButton(self.wing_2)
        self.button34_6.setObjectName(u"button34_6")
        sizePolicy1.setHeightForWidth(self.button34_6.sizePolicy().hasHeightForWidth())
        self.button34_6.setSizePolicy(sizePolicy1)
        self.button34_6.setMinimumSize(QSize(44, 44))
        self.button34_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button34_6, 3, 3, 1, 1)

        self.button28_6 = QPushButton(self.wing_2)
        self.button28_6.setObjectName(u"button28_6")
        sizePolicy1.setHeightForWidth(self.button28_6.sizePolicy().hasHeightForWidth())
        self.button28_6.setSizePolicy(sizePolicy1)
        self.button28_6.setMinimumSize(QSize(44, 44))
        self.button28_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button28_6, 4, 5, 1, 1)

        self.button63_6 = QPushButton(self.wing_2)
        self.button63_6.setObjectName(u"button63_6")
        sizePolicy1.setHeightForWidth(self.button63_6.sizePolicy().hasHeightForWidth())
        self.button63_6.setSizePolicy(sizePolicy1)
        self.button63_6.setMinimumSize(QSize(44, 44))
        self.button63_6.setMaximumSize(QSize(88, 44))

        self.gridLayout_7.addWidget(self.button63_6, 0, 8, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_7, 0, 0, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_4, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.wing_2, 0, 3, 1, 1)

        MainWindow.setCentralWidget(self.Wing1_dock)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1772, 23))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuWings = QMenu(self.menubar)
        self.menuWings.setObjectName(u"menuWings")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuWings.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionNewFile)
        self.menuFile.addAction(self.actionOpenFile)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuitApp)
        self.menuWings.addAction(self.actionViewWing1)
        self.menuWings.addAction(self.actionViewWing2)
        self.menuWings.addSeparator()
        self.menuWings.addAction(self.actionWing_1_Enabled)
        self.menuWings.addAction(self.actionWing_2_Enabled)
        self.menuSettings.addAction(self.actionPreferences)
        self.menuSettings.addAction(self.actionProfiles)
        self.menuHelp.addAction(self.actionGithub)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionConfiguring_Am_I_Dot_2)
        self.menuHelp.addAction(self.actionCreate_a_profile)
        self.menuHelp.addAction(self.actionContact_Help)
        self.menuTools.addAction(self.actionRefresh_GUI)
        self.menuTools.addAction(self.actionRefresh_Profile)
        self.menuTools.addAction(self.actionConfig_Mode)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Am I Dot2 ? - The ultimate Akai-Dot2 Interface", None))
        self.actionWing_1.setText(QCoreApplication.translate("MainWindow", u"Wing-1", None))
        self.actionWing_2.setText(QCoreApplication.translate("MainWindow", u"Wing-2", None))
        self.actionNewFile.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionOpenFile.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionCloseFile.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.actionQuitApp.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionViewWing1.setText(QCoreApplication.translate("MainWindow", u"View Wing-1", None))
        self.actionViewWing1.setIconText(QCoreApplication.translate("MainWindow", u"View Wing-1", None))
#if QT_CONFIG(tooltip)
        self.actionViewWing1.setToolTip(QCoreApplication.translate("MainWindow", u"View Wing-1", None))
#endif // QT_CONFIG(tooltip)
        self.actionViewWing2.setText(QCoreApplication.translate("MainWindow", u"View Wing-2", None))
        self.actionPreferences.setText(QCoreApplication.translate("MainWindow", u"Preferences", None))
        self.actionProfiles.setText(QCoreApplication.translate("MainWindow", u"Profiles", None))
        self.actionGithub.setText(QCoreApplication.translate("MainWindow", u"Github", None))
        self.actionConfiguring_Am_I_Dot_2.setText(QCoreApplication.translate("MainWindow", u"Configuring Am I Dot-2", None))
        self.actionCreate_a_profile.setText(QCoreApplication.translate("MainWindow", u"How to manage profiles", None))
        self.actionRefresh_GUI.setText(QCoreApplication.translate("MainWindow", u"Refresh GUI", None))
        self.actionRefresh_Profile.setText(QCoreApplication.translate("MainWindow", u"Refresh Profile", None))
        self.actionContact_Help.setText(QCoreApplication.translate("MainWindow", u"Contact Help", None))
        self.actionConfig_Mode.setText(QCoreApplication.translate("MainWindow", u"Config Mode", None))
        self.actionWing_1_Enabled.setText(QCoreApplication.translate("MainWindow", u"Wing-1 Enabled", None))
        self.actionWing_2_Enabled.setText(QCoreApplication.translate("MainWindow", u"Wing-2 Enabled", None))
        self.Wing1_dock.setWindowTitle(QCoreApplication.translate("MainWindow", u"Wing-1", None))
        self.button36_4.setText(QCoreApplication.translate("MainWindow", u"36", None))
        self.button61_4.setText(QCoreApplication.translate("MainWindow", u"61", None))
        self.button45_4.setText(QCoreApplication.translate("MainWindow", u"45", None))
        self.button44_4.setText(QCoreApplication.translate("MainWindow", u"44", None))
        self.button8_4.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.button116_4.setText(QCoreApplication.translate("MainWindow", u"116", None))
        self.button16_4.setText(QCoreApplication.translate("MainWindow", u"16", None))
        self.button12_4.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.button10_4.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.button49_4.setText(QCoreApplication.translate("MainWindow", u"49", None))
        self.button30_4.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.button113_4.setText(QCoreApplication.translate("MainWindow", u"113", None))
        self.button104_4.setText(QCoreApplication.translate("MainWindow", u"104", None))
        self.button25_4.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.button63_4.setText(QCoreApplication.translate("MainWindow", u"63", None))
        self.button122_4.setText(QCoreApplication.translate("MainWindow", u"122", None))
        self.button48_4.setText(QCoreApplication.translate("MainWindow", u"48", None))
        self.button31_4.setText(QCoreApplication.translate("MainWindow", u"31", None))
        self.button7_4.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.button4_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.button35_4.setText(QCoreApplication.translate("MainWindow", u"35", None))
        self.button39_4.setText(QCoreApplication.translate("MainWindow", u"39", None))
        self.button24_4.setText(QCoreApplication.translate("MainWindow", u"24", None))
        self.button3_4.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.button46_4.setText(QCoreApplication.translate("MainWindow", u"46", None))
        self.button40_4.setText(QCoreApplication.translate("MainWindow", u"40", None))
        self.button55_4.setText(QCoreApplication.translate("MainWindow", u"55", None))
        self.button9_4.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.button5_4.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.button38_4.setText(QCoreApplication.translate("MainWindow", u"38", None))
        self.button100_4.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.button119_4.setText(QCoreApplication.translate("MainWindow", u"119", None))
        self.button52_4.setText(QCoreApplication.translate("MainWindow", u"52", None))
        self.button51_4.setText(QCoreApplication.translate("MainWindow", u"51", None))
        self.button60_4.setText(QCoreApplication.translate("MainWindow", u"60", None))
        self.button13_4.setText(QCoreApplication.translate("MainWindow", u"13", None))
        self.button14_4.setText(QCoreApplication.translate("MainWindow", u"14", None))
        self.button6_4.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.button26_4.setText(QCoreApplication.translate("MainWindow", u"26", None))
        self.button1_4.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.button34_4.setText(QCoreApplication.translate("MainWindow", u"34", None))
        self.button117_4.setText(QCoreApplication.translate("MainWindow", u"117", None))
        self.button115_4.setText(QCoreApplication.translate("MainWindow", u"115", None))
        self.button62_4.setText(QCoreApplication.translate("MainWindow", u"62", None))
        self.button58_4.setText(QCoreApplication.translate("MainWindow", u"58", None))
        self.button29_4.setText(QCoreApplication.translate("MainWindow", u"29", None))
        self.button21_4.setText(QCoreApplication.translate("MainWindow", u"21", None))
        self.button43_4.setText(QCoreApplication.translate("MainWindow", u"43", None))
        self.button15_4.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.button32_4.setText(QCoreApplication.translate("MainWindow", u"32", None))
        self.button59_4.setText(QCoreApplication.translate("MainWindow", u"59", None))
        self.button118_4.setText(QCoreApplication.translate("MainWindow", u"118", None))
        self.button22_4.setText(QCoreApplication.translate("MainWindow", u"22", None))
        self.button42_4.setText(QCoreApplication.translate("MainWindow", u"42", None))
        self.button107_4.setText(QCoreApplication.translate("MainWindow", u"107", None))
        self.button27_4.setText(QCoreApplication.translate("MainWindow", u"27", None))
        self.pushButton_fader52_4.setText(QCoreApplication.translate("MainWindow", u"button52", None))
        self.button17_4.setText(QCoreApplication.translate("MainWindow", u"17", None))
        self.pushButton_fader53_4.setText(QCoreApplication.translate("MainWindow", u"button53", None))
        self.pushButton_fader49_4.setText(QCoreApplication.translate("MainWindow", u"button49", None))
        self.button37_4.setText(QCoreApplication.translate("MainWindow", u"37", None))
        self.button41_4.setText(QCoreApplication.translate("MainWindow", u"41", None))
        self.button0_4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.button56_4.setText(QCoreApplication.translate("MainWindow", u"56", None))
        self.button23_4.setText(QCoreApplication.translate("MainWindow", u"23", None))
        self.button54_4.setText(QCoreApplication.translate("MainWindow", u"54", None))
        self.pushButton_fader48_4.setText(QCoreApplication.translate("MainWindow", u"button48", None))
        self.button106_4.setText(QCoreApplication.translate("MainWindow", u"106", None))
        self.button33_4.setText(QCoreApplication.translate("MainWindow", u"33", None))
        self.button28_4.setText(QCoreApplication.translate("MainWindow", u"28", None))
        self.button2_4.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.button11_4.setText(QCoreApplication.translate("MainWindow", u"11", None))
        self.button102_4.setText(QCoreApplication.translate("MainWindow", u"102", None))
        self.button18_4.setText(QCoreApplication.translate("MainWindow", u"18", None))
        self.button19_4.setText(QCoreApplication.translate("MainWindow", u"19", None))
        self.button47_4.setText(QCoreApplication.translate("MainWindow", u"47", None))
        self.button53_4.setText(QCoreApplication.translate("MainWindow", u"53", None))
        self.button112_4.setText(QCoreApplication.translate("MainWindow", u"112", None))
        self.button114_4.setText(QCoreApplication.translate("MainWindow", u"114", None))
        self.button50_4.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.pushButton_fader51_4.setText(QCoreApplication.translate("MainWindow", u"button51", None))
        self.pushButton_fader50_4.setText(QCoreApplication.translate("MainWindow", u"button50", None))
        self.button105_4.setText(QCoreApplication.translate("MainWindow", u"105", None))
        self.button20_4.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.button101_4.setText(QCoreApplication.translate("MainWindow", u"101", None))
        self.button103_4.setText(QCoreApplication.translate("MainWindow", u"103", None))
        self.button57_4.setText(QCoreApplication.translate("MainWindow", u"57", None))
        self.pushButton_fader54_4.setText(QCoreApplication.translate("MainWindow", u"button54", None))
        self.pushButton_fader55_4.setText(QCoreApplication.translate("MainWindow", u"button55", None))
        self.pushButton_fader56_4.setText(QCoreApplication.translate("MainWindow", u"button56", None))
        self.button114_6.setText(QCoreApplication.translate("MainWindow", u"114", None))
        self.button20_6.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.button22_6.setText(QCoreApplication.translate("MainWindow", u"22", None))
        self.button50_6.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.button113_6.setText(QCoreApplication.translate("MainWindow", u"113", None))
        self.button47_6.setText(QCoreApplication.translate("MainWindow", u"47", None))
        self.button38_6.setText(QCoreApplication.translate("MainWindow", u"38", None))
        self.button49_6.setText(QCoreApplication.translate("MainWindow", u"49", None))
        self.button7_6.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.button56_6.setText(QCoreApplication.translate("MainWindow", u"56", None))
        self.button102_6.setText(QCoreApplication.translate("MainWindow", u"102", None))
        self.button11_6.setText(QCoreApplication.translate("MainWindow", u"11", None))
        self.button112_6.setText(QCoreApplication.translate("MainWindow", u"112", None))
        self.button16_6.setText(QCoreApplication.translate("MainWindow", u"16", None))
        self.button60_6.setText(QCoreApplication.translate("MainWindow", u"60", None))
        self.button118_6.setText(QCoreApplication.translate("MainWindow", u"118", None))
        self.pushButton_fader51_6.setText(QCoreApplication.translate("MainWindow", u"button51", None))
        self.button48_6.setText(QCoreApplication.translate("MainWindow", u"48", None))
        self.button58_6.setText(QCoreApplication.translate("MainWindow", u"58", None))
        self.button53_6.setText(QCoreApplication.translate("MainWindow", u"53", None))
        self.button35_6.setText(QCoreApplication.translate("MainWindow", u"35", None))
        self.button122_6.setText(QCoreApplication.translate("MainWindow", u"122", None))
        self.button15_6.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.pushButton_fader56_6.setText(QCoreApplication.translate("MainWindow", u"button56", None))
        self.button40_6.setText(QCoreApplication.translate("MainWindow", u"40", None))
        self.button30_6.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.button37_6.setText(QCoreApplication.translate("MainWindow", u"37", None))
        self.button24_6.setText(QCoreApplication.translate("MainWindow", u"24", None))
        self.button55_6.setText(QCoreApplication.translate("MainWindow", u"55", None))
        self.button10_6.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.button14_6.setText(QCoreApplication.translate("MainWindow", u"14", None))
        self.button54_6.setText(QCoreApplication.translate("MainWindow", u"54", None))
        self.button46_6.setText(QCoreApplication.translate("MainWindow", u"46", None))
        self.pushButton_fader52_6.setText(QCoreApplication.translate("MainWindow", u"button52", None))
        self.button44_6.setText(QCoreApplication.translate("MainWindow", u"44", None))
        self.button17_6.setText(QCoreApplication.translate("MainWindow", u"17", None))
        self.button117_6.setText(QCoreApplication.translate("MainWindow", u"117", None))
        self.button43_6.setText(QCoreApplication.translate("MainWindow", u"43", None))
        self.button2_6.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.button105_6.setText(QCoreApplication.translate("MainWindow", u"105", None))
        self.button103_6.setText(QCoreApplication.translate("MainWindow", u"103", None))
        self.button9_6.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.button51_6.setText(QCoreApplication.translate("MainWindow", u"51", None))
        self.button26_6.setText(QCoreApplication.translate("MainWindow", u"26", None))
        self.button107_6.setText(QCoreApplication.translate("MainWindow", u"107", None))
        self.button13_6.setText(QCoreApplication.translate("MainWindow", u"13", None))
        self.button0_6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.button59_6.setText(QCoreApplication.translate("MainWindow", u"59", None))
        self.button119_6.setText(QCoreApplication.translate("MainWindow", u"119", None))
        self.button116_6.setText(QCoreApplication.translate("MainWindow", u"116", None))
        self.button1_6.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.button39_6.setText(QCoreApplication.translate("MainWindow", u"39", None))
        self.button61_6.setText(QCoreApplication.translate("MainWindow", u"61", None))
        self.button12_6.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.button45_6.setText(QCoreApplication.translate("MainWindow", u"45", None))
        self.button4_6.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.button104_6.setText(QCoreApplication.translate("MainWindow", u"104", None))
        self.button62_6.setText(QCoreApplication.translate("MainWindow", u"62", None))
        self.button18_6.setText(QCoreApplication.translate("MainWindow", u"18", None))
        self.button29_6.setText(QCoreApplication.translate("MainWindow", u"29", None))
        self.pushButton_fader54_6.setText(QCoreApplication.translate("MainWindow", u"button54", None))
        self.button31_6.setText(QCoreApplication.translate("MainWindow", u"31", None))
        self.button3_6.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_fader53_6.setText(QCoreApplication.translate("MainWindow", u"button53", None))
        self.button41_6.setText(QCoreApplication.translate("MainWindow", u"41", None))
        self.button115_6.setText(QCoreApplication.translate("MainWindow", u"115", None))
        self.pushButton_fader49_6.setText(QCoreApplication.translate("MainWindow", u"button49", None))
        self.button106_6.setText(QCoreApplication.translate("MainWindow", u"106", None))
        self.button57_6.setText(QCoreApplication.translate("MainWindow", u"57", None))
        self.button21_6.setText(QCoreApplication.translate("MainWindow", u"21", None))
        self.button19_6.setText(QCoreApplication.translate("MainWindow", u"19", None))
        self.button101_6.setText(QCoreApplication.translate("MainWindow", u"101", None))
        self.button100_6.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.button23_6.setText(QCoreApplication.translate("MainWindow", u"23", None))
        self.button27_6.setText(QCoreApplication.translate("MainWindow", u"27", None))
        self.pushButton_fader55_6.setText(QCoreApplication.translate("MainWindow", u"button55", None))
        self.button8_6.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.button5_6.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.button6_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_fader48_6.setText(QCoreApplication.translate("MainWindow", u"button48", None))
        self.button25_6.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.button32_6.setText(QCoreApplication.translate("MainWindow", u"32", None))
        self.button36_6.setText(QCoreApplication.translate("MainWindow", u"36", None))
        self.pushButton_fader50_6.setText(QCoreApplication.translate("MainWindow", u"button50", None))
        self.button33_6.setText(QCoreApplication.translate("MainWindow", u"33", None))
        self.button52_6.setText(QCoreApplication.translate("MainWindow", u"52", None))
        self.button42_6.setText(QCoreApplication.translate("MainWindow", u"42", None))
        self.button34_6.setText(QCoreApplication.translate("MainWindow", u"34", None))
        self.button28_6.setText(QCoreApplication.translate("MainWindow", u"28", None))
        self.button63_6.setText(QCoreApplication.translate("MainWindow", u"63", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuWings.setTitle(QCoreApplication.translate("MainWindow", u"Wings", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
    # retranslateUi

