# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/krl1to5/Work/FULL/Sequence-ToolKit/2016/resources/ui/genrep/dialogs/setup.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_setup(object):
    def setupUi(self, setup):
        setup.setObjectName("setup")
        setup.resize(510, 607)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(setup.sizePolicy().hasHeightForWidth())
        setup.setSizePolicy(sizePolicy)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(setup)
        self.verticalLayout_8.setContentsMargins(-1, -1, -1, 9)
        self.verticalLayout_8.setSpacing(15)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.tab_widget = QtWidgets.QTabWidget(setup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_widget.sizePolicy().hasHeightForWidth())
        self.tab_widget.setSizePolicy(sizePolicy)
        self.tab_widget.setObjectName("tab_widget")
        self.curve_to_show = QtWidgets.QWidget()
        self.curve_to_show.setObjectName("curve_to_show")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.curve_to_show)
        self.verticalLayout_3.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_3.setSpacing(12)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.curve_1 = QtWidgets.QCheckBox(self.curve_to_show)
        self.curve_1.setChecked(True)
        self.curve_1.setObjectName("curve_1")
        self.verticalLayout_3.addWidget(self.curve_1)
        self.curve_2 = QtWidgets.QCheckBox(self.curve_to_show)
        self.curve_2.setObjectName("curve_2")
        self.verticalLayout_3.addWidget(self.curve_2)
        self.curve_3 = QtWidgets.QCheckBox(self.curve_to_show)
        self.curve_3.setObjectName("curve_3")
        self.verticalLayout_3.addWidget(self.curve_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.tab_widget.addTab(self.curve_to_show, "")
        self.for_tl = QtWidgets.QWidget()
        self.for_tl.setObjectName("for_tl")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.for_tl)
        self.verticalLayout_4.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_4.setSpacing(12)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.show_label = QtWidgets.QLabel(self.for_tl)
        self.show_label.setObjectName("show_label")
        self.verticalLayout_4.addWidget(self.show_label)
        self.curve_vs_time = QtWidgets.QRadioButton(self.for_tl)
        self.curve_vs_time.setChecked(True)
        self.curve_vs_time.setObjectName("curve_vs_time")
        self.verticalLayout_4.addWidget(self.curve_vs_time)
        self.curve_vs_temperature = QtWidgets.QRadioButton(self.for_tl)
        self.curve_vs_temperature.setObjectName("curve_vs_temperature")
        self.verticalLayout_4.addWidget(self.curve_vs_temperature)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.tab_widget.addTab(self.for_tl, "")
        self.format_horizontal_axis = QtWidgets.QWidget()
        self.format_horizontal_axis.setObjectName("format_horizontal_axis")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.format_horizontal_axis)
        self.verticalLayout_2.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.layout = QtWidgets.QHBoxLayout()
        self.layout.setSpacing(10)
        self.layout.setObjectName("layout")
        self.units_label = QtWidgets.QLabel(self.format_horizontal_axis)
        self.units_label.setObjectName("units_label")
        self.layout.addWidget(self.units_label)
        self.units = QtWidgets.QComboBox(self.format_horizontal_axis)
        self.units.setMinimumSize(QtCore.QSize(100, 28))
        self.units.setObjectName("units")
        self.units.addItem("")
        self.units.addItem("")
        self.layout.addWidget(self.units)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.layout)
        self.line = QtWidgets.QFrame(self.format_horizontal_axis)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.scale_area = QtWidgets.QGroupBox(self.format_horizontal_axis)
        self.scale_area.setObjectName("scale_area")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.scale_area)
        self.horizontalLayout_9.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lineal = QtWidgets.QRadioButton(self.scale_area)
        self.lineal.setChecked(True)
        self.lineal.setAutoRepeat(False)
        self.lineal.setObjectName("lineal")
        self.horizontalLayout_9.addWidget(self.lineal)
        self.log10 = QtWidgets.QRadioButton(self.scale_area)
        self.log10.setObjectName("log10")
        self.horizontalLayout_9.addWidget(self.log10)
        self.ln = QtWidgets.QRadioButton(self.scale_area)
        self.ln.setObjectName("ln")
        self.horizontalLayout_9.addWidget(self.ln)
        self.verticalLayout_2.addWidget(self.scale_area)
        self.axis_values_area = QtWidgets.QGroupBox(self.format_horizontal_axis)
        self.axis_values_area.setObjectName("axis_values_area")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.axis_values_area)
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.layout_2 = QtWidgets.QHBoxLayout()
        self.layout_2.setSpacing(10)
        self.layout_2.setObjectName("layout_2")
        self.minimum_label = QtWidgets.QLabel(self.axis_values_area)
        self.minimum_label.setObjectName("minimum_label")
        self.layout_2.addWidget(self.minimum_label)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_2.addItem(spacerItem3)
        self.group = QtWidgets.QGroupBox(self.axis_values_area)
        self.group.setTitle("")
        self.group.setFlat(True)
        self.group.setObjectName("group")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.group)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.automatic_minimum = QtWidgets.QRadioButton(self.group)
        self.automatic_minimum.setChecked(True)
        self.automatic_minimum.setObjectName("automatic_minimum")
        self.horizontalLayout.addWidget(self.automatic_minimum)
        self.fixed_minimum = QtWidgets.QRadioButton(self.group)
        self.fixed_minimum.setObjectName("fixed_minimum")
        self.horizontalLayout.addWidget(self.fixed_minimum)
        self.fixed_minimum_value = QtWidgets.QDoubleSpinBox(self.group)
        self.fixed_minimum_value.setMinimumSize(QtCore.QSize(0, 28))
        self.fixed_minimum_value.setMaximum(9999999.0)
        self.fixed_minimum_value.setObjectName("fixed_minimum_value")
        self.horizontalLayout.addWidget(self.fixed_minimum_value)
        self.layout_2.addWidget(self.group)
        self.verticalLayout.addLayout(self.layout_2)
        self.layout_3 = QtWidgets.QHBoxLayout()
        self.layout_3.setSpacing(10)
        self.layout_3.setObjectName("layout_3")
        self.maximum_label = QtWidgets.QLabel(self.axis_values_area)
        self.maximum_label.setObjectName("maximum_label")
        self.layout_3.addWidget(self.maximum_label)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_3.addItem(spacerItem4)
        self.group_1 = QtWidgets.QGroupBox(self.axis_values_area)
        self.group_1.setTitle("")
        self.group_1.setFlat(True)
        self.group_1.setObjectName("group_1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.group_1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.automatic_maximum = QtWidgets.QRadioButton(self.group_1)
        self.automatic_maximum.setChecked(True)
        self.automatic_maximum.setObjectName("automatic_maximum")
        self.horizontalLayout_2.addWidget(self.automatic_maximum)
        self.fixed_maximum = QtWidgets.QRadioButton(self.group_1)
        self.fixed_maximum.setObjectName("fixed_maximum")
        self.horizontalLayout_2.addWidget(self.fixed_maximum)
        self.fixed_maximum_value = QtWidgets.QDoubleSpinBox(self.group_1)
        self.fixed_maximum_value.setMinimumSize(QtCore.QSize(0, 28))
        self.fixed_maximum_value.setMaximum(9999999.0)
        self.fixed_maximum_value.setObjectName("fixed_maximum_value")
        self.horizontalLayout_2.addWidget(self.fixed_maximum_value)
        self.layout_3.addWidget(self.group_1)
        self.verticalLayout.addLayout(self.layout_3)
        self.layout_4 = QtWidgets.QHBoxLayout()
        self.layout_4.setSpacing(10)
        self.layout_4.setObjectName("layout_4")
        self.greater_label = QtWidgets.QLabel(self.axis_values_area)
        self.greater_label.setObjectName("greater_label")
        self.layout_4.addWidget(self.greater_label)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_4.addItem(spacerItem5)
        self.group_2 = QtWidgets.QGroupBox(self.axis_values_area)
        self.group_2.setTitle("")
        self.group_2.setFlat(True)
        self.group_2.setObjectName("group_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.group_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.automatic_greater = QtWidgets.QRadioButton(self.group_2)
        self.automatic_greater.setChecked(False)
        self.automatic_greater.setObjectName("automatic_greater")
        self.horizontalLayout_3.addWidget(self.automatic_greater)
        self.fixed_greater = QtWidgets.QRadioButton(self.group_2)
        self.fixed_greater.setChecked(True)
        self.fixed_greater.setObjectName("fixed_greater")
        self.horizontalLayout_3.addWidget(self.fixed_greater)
        self.fixed_greater_value = QtWidgets.QDoubleSpinBox(self.group_2)
        self.fixed_greater_value.setMinimumSize(QtCore.QSize(0, 28))
        self.fixed_greater_value.setMaximum(9999999.0)
        self.fixed_greater_value.setProperty("value", 20.0)
        self.fixed_greater_value.setObjectName("fixed_greater_value")
        self.horizontalLayout_3.addWidget(self.fixed_greater_value)
        self.layout_4.addWidget(self.group_2)
        self.verticalLayout.addLayout(self.layout_4)
        self.layout_5 = QtWidgets.QHBoxLayout()
        self.layout_5.setSpacing(10)
        self.layout_5.setObjectName("layout_5")
        self.smallest_label = QtWidgets.QLabel(self.axis_values_area)
        self.smallest_label.setObjectName("smallest_label")
        self.layout_5.addWidget(self.smallest_label)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_5.addItem(spacerItem6)
        self.group_3 = QtWidgets.QGroupBox(self.axis_values_area)
        self.group_3.setTitle("")
        self.group_3.setFlat(True)
        self.group_3.setObjectName("group_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.group_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.automatic_smallest = QtWidgets.QRadioButton(self.group_3)
        self.automatic_smallest.setChecked(False)
        self.automatic_smallest.setObjectName("automatic_smallest")
        self.horizontalLayout_4.addWidget(self.automatic_smallest)
        self.fixed_smallest = QtWidgets.QRadioButton(self.group_3)
        self.fixed_smallest.setChecked(True)
        self.fixed_smallest.setObjectName("fixed_smallest")
        self.horizontalLayout_4.addWidget(self.fixed_smallest)
        self.fixed_smallest_value = QtWidgets.QDoubleSpinBox(self.group_3)
        self.fixed_smallest_value.setMinimumSize(QtCore.QSize(0, 28))
        self.fixed_smallest_value.setMaximum(9999999.0)
        self.fixed_smallest_value.setProperty("value", 5.0)
        self.fixed_smallest_value.setObjectName("fixed_smallest_value")
        self.horizontalLayout_4.addWidget(self.fixed_smallest_value)
        self.layout_5.addWidget(self.group_3)
        self.verticalLayout.addLayout(self.layout_5)
        self.verticalLayout_2.addWidget(self.axis_values_area)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem7)
        self.tab_widget.addTab(self.format_horizontal_axis, "")
        self.format_vertical_axis = QtWidgets.QWidget()
        self.format_vertical_axis.setObjectName("format_vertical_axis")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.format_vertical_axis)
        self.verticalLayout_6.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_6.setSpacing(12)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.scale_area_2 = QtWidgets.QGroupBox(self.format_vertical_axis)
        self.scale_area_2.setObjectName("scale_area_2")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.scale_area_2)
        self.horizontalLayout_19.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_19.setSpacing(10)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.lineal_2 = QtWidgets.QRadioButton(self.scale_area_2)
        self.lineal_2.setChecked(True)
        self.lineal_2.setAutoRepeat(False)
        self.lineal_2.setObjectName("lineal_2")
        self.horizontalLayout_19.addWidget(self.lineal_2)
        self.log10_2 = QtWidgets.QRadioButton(self.scale_area_2)
        self.log10_2.setObjectName("log10_2")
        self.horizontalLayout_19.addWidget(self.log10_2)
        self.ln_2 = QtWidgets.QRadioButton(self.scale_area_2)
        self.ln_2.setObjectName("ln_2")
        self.horizontalLayout_19.addWidget(self.ln_2)
        self.verticalLayout_6.addWidget(self.scale_area_2)
        self.axis_values_area_2 = QtWidgets.QGroupBox(self.format_vertical_axis)
        self.axis_values_area_2.setObjectName("axis_values_area_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.axis_values_area_2)
        self.verticalLayout_5.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.layout_6 = QtWidgets.QHBoxLayout()
        self.layout_6.setSpacing(10)
        self.layout_6.setObjectName("layout_6")
        self.minimum_label_2 = QtWidgets.QLabel(self.axis_values_area_2)
        self.minimum_label_2.setObjectName("minimum_label_2")
        self.layout_6.addWidget(self.minimum_label_2)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_6.addItem(spacerItem8)
        self.group_4 = QtWidgets.QGroupBox(self.axis_values_area_2)
        self.group_4.setTitle("")
        self.group_4.setFlat(True)
        self.group_4.setObjectName("group_4")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.group_4)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(10)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.automatic_minimum_2 = QtWidgets.QRadioButton(self.group_4)
        self.automatic_minimum_2.setChecked(True)
        self.automatic_minimum_2.setObjectName("automatic_minimum_2")
        self.horizontalLayout_12.addWidget(self.automatic_minimum_2)
        self.fixed_minimum_2 = QtWidgets.QRadioButton(self.group_4)
        self.fixed_minimum_2.setObjectName("fixed_minimum_2")
        self.horizontalLayout_12.addWidget(self.fixed_minimum_2)
        self.fixed_minimum_value_2 = QtWidgets.QDoubleSpinBox(self.group_4)
        self.fixed_minimum_value_2.setMinimumSize(QtCore.QSize(0, 28))
        self.fixed_minimum_value_2.setMaximum(9999999.0)
        self.fixed_minimum_value_2.setObjectName("fixed_minimum_value_2")
        self.horizontalLayout_12.addWidget(self.fixed_minimum_value_2)
        self.layout_6.addWidget(self.group_4)
        self.verticalLayout_5.addLayout(self.layout_6)
        self.layout_7 = QtWidgets.QHBoxLayout()
        self.layout_7.setSpacing(10)
        self.layout_7.setObjectName("layout_7")
        self.maximum_label_2 = QtWidgets.QLabel(self.axis_values_area_2)
        self.maximum_label_2.setObjectName("maximum_label_2")
        self.layout_7.addWidget(self.maximum_label_2)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_7.addItem(spacerItem9)
        self.group_5 = QtWidgets.QGroupBox(self.axis_values_area_2)
        self.group_5.setTitle("")
        self.group_5.setFlat(True)
        self.group_5.setObjectName("group_5")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.group_5)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setSpacing(10)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.automatic_maximum_2 = QtWidgets.QRadioButton(self.group_5)
        self.automatic_maximum_2.setChecked(True)
        self.automatic_maximum_2.setObjectName("automatic_maximum_2")
        self.horizontalLayout_14.addWidget(self.automatic_maximum_2)
        self.fixed_maximum_2 = QtWidgets.QRadioButton(self.group_5)
        self.fixed_maximum_2.setObjectName("fixed_maximum_2")
        self.horizontalLayout_14.addWidget(self.fixed_maximum_2)
        self.fixed_maximum_value_2 = QtWidgets.QDoubleSpinBox(self.group_5)
        self.fixed_maximum_value_2.setMinimumSize(QtCore.QSize(0, 28))
        self.fixed_maximum_value_2.setMaximum(9999999.0)
        self.fixed_maximum_value_2.setObjectName("fixed_maximum_value_2")
        self.horizontalLayout_14.addWidget(self.fixed_maximum_value_2)
        self.layout_7.addWidget(self.group_5)
        self.verticalLayout_5.addLayout(self.layout_7)
        self.layout_8 = QtWidgets.QHBoxLayout()
        self.layout_8.setSpacing(10)
        self.layout_8.setObjectName("layout_8")
        self.greater_label_2 = QtWidgets.QLabel(self.axis_values_area_2)
        self.greater_label_2.setObjectName("greater_label_2")
        self.layout_8.addWidget(self.greater_label_2)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_8.addItem(spacerItem10)
        self.group_6 = QtWidgets.QGroupBox(self.axis_values_area_2)
        self.group_6.setTitle("")
        self.group_6.setFlat(True)
        self.group_6.setObjectName("group_6")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.group_6)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setSpacing(10)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.automatic_greater_2 = QtWidgets.QRadioButton(self.group_6)
        self.automatic_greater_2.setChecked(False)
        self.automatic_greater_2.setObjectName("automatic_greater_2")
        self.horizontalLayout_16.addWidget(self.automatic_greater_2)
        self.fixed_greater_2 = QtWidgets.QRadioButton(self.group_6)
        self.fixed_greater_2.setChecked(True)
        self.fixed_greater_2.setObjectName("fixed_greater_2")
        self.horizontalLayout_16.addWidget(self.fixed_greater_2)
        self.fixed_greater_value_2 = QtWidgets.QDoubleSpinBox(self.group_6)
        self.fixed_greater_value_2.setMinimumSize(QtCore.QSize(0, 28))
        self.fixed_greater_value_2.setMaximum(9999999.0)
        self.fixed_greater_value_2.setProperty("value", 5000.0)
        self.fixed_greater_value_2.setObjectName("fixed_greater_value_2")
        self.horizontalLayout_16.addWidget(self.fixed_greater_value_2)
        self.layout_8.addWidget(self.group_6)
        self.verticalLayout_5.addLayout(self.layout_8)
        self.layout_9 = QtWidgets.QHBoxLayout()
        self.layout_9.setSpacing(10)
        self.layout_9.setObjectName("layout_9")
        self.smallest_label_2 = QtWidgets.QLabel(self.axis_values_area_2)
        self.smallest_label_2.setObjectName("smallest_label_2")
        self.layout_9.addWidget(self.smallest_label_2)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_9.addItem(spacerItem11)
        self.group_7 = QtWidgets.QGroupBox(self.axis_values_area_2)
        self.group_7.setTitle("")
        self.group_7.setFlat(True)
        self.group_7.setObjectName("group_7")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.group_7)
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18.setSpacing(10)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.automatic_smallest_2 = QtWidgets.QRadioButton(self.group_7)
        self.automatic_smallest_2.setChecked(False)
        self.automatic_smallest_2.setObjectName("automatic_smallest_2")
        self.horizontalLayout_18.addWidget(self.automatic_smallest_2)
        self.fixed_smallest_2 = QtWidgets.QRadioButton(self.group_7)
        self.fixed_smallest_2.setChecked(True)
        self.fixed_smallest_2.setObjectName("fixed_smallest_2")
        self.horizontalLayout_18.addWidget(self.fixed_smallest_2)
        self.fixed_smallest_value_2 = QtWidgets.QDoubleSpinBox(self.group_7)
        self.fixed_smallest_value_2.setMinimumSize(QtCore.QSize(0, 28))
        self.fixed_smallest_value_2.setMaximum(9999999.0)
        self.fixed_smallest_value_2.setProperty("value", 500.0)
        self.fixed_smallest_value_2.setObjectName("fixed_smallest_value_2")
        self.horizontalLayout_18.addWidget(self.fixed_smallest_value_2)
        self.layout_9.addWidget(self.group_7)
        self.verticalLayout_5.addLayout(self.layout_9)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem12)
        self.verticalLayout_6.addWidget(self.axis_values_area_2)
        self.tab_widget.addTab(self.format_vertical_axis, "")
        self.cursors = QtWidgets.QWidget()
        self.cursors.setObjectName("cursors")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.cursors)
        self.verticalLayout_7.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_7.setSpacing(12)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.layout_10 = QtWidgets.QHBoxLayout()
        self.layout_10.setObjectName("layout_10")
        self.show_cursors_label = QtWidgets.QLabel(self.cursors)
        self.show_cursors_label.setObjectName("show_cursors_label")
        self.layout_10.addWidget(self.show_cursors_label)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_10.addItem(spacerItem13)
        self.default_position_label = QtWidgets.QLabel(self.cursors)
        self.default_position_label.setObjectName("default_position_label")
        self.layout_10.addWidget(self.default_position_label)
        self.verticalLayout_7.addLayout(self.layout_10)
        self.layout_11 = QtWidgets.QHBoxLayout()
        self.layout_11.setObjectName("layout_11")
        self.signal = QtWidgets.QCheckBox(self.cursors)
        self.signal.setChecked(True)
        self.signal.setObjectName("signal")
        self.layout_11.addWidget(self.signal)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_11.addItem(spacerItem14)
        self.layout_12 = QtWidgets.QHBoxLayout()
        self.layout_12.setObjectName("layout_12")
        self.st_signal_low_label = QtWidgets.QLabel(self.cursors)
        self.st_signal_low_label.setObjectName("st_signal_low_label")
        self.layout_12.addWidget(self.st_signal_low_label)
        self.signal_low = QtWidgets.QDoubleSpinBox(self.cursors)
        self.signal_low.setMinimumSize(QtCore.QSize(110, 28))
        self.signal_low.setMaximumSize(QtCore.QSize(110, 16777215))
        self.signal_low.setMinimum(1.0)
        self.signal_low.setMaximum(9999999.0)
        self.signal_low.setObjectName("signal_low")
        self.layout_12.addWidget(self.signal_low)
        self.layout_11.addLayout(self.layout_12)
        self.layout_13 = QtWidgets.QHBoxLayout()
        self.layout_13.setObjectName("layout_13")
        self.st_signal_high_label = QtWidgets.QLabel(self.cursors)
        self.st_signal_high_label.setObjectName("st_signal_high_label")
        self.layout_13.addWidget(self.st_signal_high_label)
        self.signal_high = QtWidgets.QDoubleSpinBox(self.cursors)
        self.signal_high.setMinimumSize(QtCore.QSize(110, 28))
        self.signal_high.setMaximumSize(QtCore.QSize(110, 16777215))
        self.signal_high.setMaximum(9999999.0)
        self.signal_high.setProperty("value", 10.0)
        self.signal_high.setObjectName("signal_high")
        self.layout_13.addWidget(self.signal_high)
        self.layout_11.addLayout(self.layout_13)
        self.verticalLayout_7.addLayout(self.layout_11)
        self.layout_14 = QtWidgets.QHBoxLayout()
        self.layout_14.setObjectName("layout_14")
        self.background = QtWidgets.QCheckBox(self.cursors)
        self.background.setChecked(True)
        self.background.setObjectName("background")
        self.layout_14.addWidget(self.background)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_14.addItem(spacerItem15)
        self.layout_15 = QtWidgets.QHBoxLayout()
        self.layout_15.setObjectName("layout_15")
        self.st_background_low_label = QtWidgets.QLabel(self.cursors)
        self.st_background_low_label.setObjectName("st_background_low_label")
        self.layout_15.addWidget(self.st_background_low_label)
        self.background_low = QtWidgets.QDoubleSpinBox(self.cursors)
        self.background_low.setMinimumSize(QtCore.QSize(110, 28))
        self.background_low.setMaximumSize(QtCore.QSize(110, 16777215))
        self.background_low.setMinimum(-9999999.0)
        self.background_low.setMaximum(0.0)
        self.background_low.setProperty("value", -10.0)
        self.background_low.setObjectName("background_low")
        self.layout_15.addWidget(self.background_low)
        self.layout_14.addLayout(self.layout_15)
        self.layout_16 = QtWidgets.QHBoxLayout()
        self.layout_16.setObjectName("layout_16")
        self.st_background_high_label = QtWidgets.QLabel(self.cursors)
        self.st_background_high_label.setObjectName("st_background_high_label")
        self.layout_16.addWidget(self.st_background_high_label)
        self.background_high = QtWidgets.QDoubleSpinBox(self.cursors)
        self.background_high.setMinimumSize(QtCore.QSize(110, 28))
        self.background_high.setMaximumSize(QtCore.QSize(110, 16777215))
        self.background_high.setMinimum(-9999999.0)
        self.background_high.setMaximum(0.0)
        self.background_high.setObjectName("background_high")
        self.layout_16.addWidget(self.background_high)
        self.layout_14.addLayout(self.layout_16)
        self.verticalLayout_7.addLayout(self.layout_14)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem16)
        self.tab_widget.addTab(self.cursors, "")
        self.verticalLayout_8.addWidget(self.tab_widget)
        self.line_2 = QtWidgets.QFrame(setup)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_8.addWidget(self.line_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem17 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem17)
        self.push_button_accept = QtWidgets.QPushButton(setup)
        self.push_button_accept.setMinimumSize(QtCore.QSize(100, 32))
        self.push_button_accept.setObjectName("push_button_accept")
        self.horizontalLayout_5.addWidget(self.push_button_accept)
        self.push_button_cancel = QtWidgets.QPushButton(setup)
        self.push_button_cancel.setMinimumSize(QtCore.QSize(100, 32))
        self.push_button_cancel.setObjectName("push_button_cancel")
        self.horizontalLayout_5.addWidget(self.push_button_cancel)
        self.verticalLayout_8.addLayout(self.horizontalLayout_5)
        spacerItem18 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem18)

        self.retranslateUi(setup)
        self.tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(setup)

    def retranslateUi(self, setup):
        _translate = QtCore.QCoreApplication.translate
        setup.setWindowTitle(_translate("setup", "SetUp"))
        self.curve_1.setText(_translate("setup", "Curve 1"))
        self.curve_2.setText(_translate("setup", "Curve 2"))
        self.curve_3.setText(_translate("setup", "Curve 3"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.curve_to_show), _translate("setup", "Curve to Show"))
        self.show_label.setText(_translate("setup", "Show"))
        self.curve_vs_time.setText(_translate("setup", "Curve vs time"))
        self.curve_vs_temperature.setText(_translate("setup", "Curve vs Temperature"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.for_tl), _translate("setup", "For TL"))
        self.units_label.setText(_translate("setup", "Units"))
        self.units.setItemText(0, _translate("setup", "channels"))
        self.units.setItemText(1, _translate("setup", "s"))
        self.scale_area.setTitle(_translate("setup", "Scale"))
        self.lineal.setText(_translate("setup", "Lineal"))
        self.log10.setText(_translate("setup", "Log10"))
        self.ln.setText(_translate("setup", "Ln"))
        self.axis_values_area.setTitle(_translate("setup", "Axis values"))
        self.minimum_label.setText(_translate("setup", "Minimum"))
        self.automatic_minimum.setText(_translate("setup", "Automatic"))
        self.fixed_minimum.setText(_translate("setup", "Fixed"))
        self.maximum_label.setText(_translate("setup", "Maximum"))
        self.automatic_maximum.setText(_translate("setup", "Automatic"))
        self.fixed_maximum.setText(_translate("setup", "Fixed"))
        self.greater_label.setText(_translate("setup", "Greater Unit"))
        self.automatic_greater.setText(_translate("setup", "Automatic"))
        self.fixed_greater.setText(_translate("setup", "Fixed"))
        self.smallest_label.setText(_translate("setup", "Smallest Unit"))
        self.automatic_smallest.setText(_translate("setup", "Automatic"))
        self.fixed_smallest.setText(_translate("setup", "Fixed"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.format_horizontal_axis), _translate("setup", "Format Horizontal Axis"))
        self.scale_area_2.setTitle(_translate("setup", "Scale"))
        self.lineal_2.setText(_translate("setup", "Lineal"))
        self.log10_2.setText(_translate("setup", "Log10"))
        self.ln_2.setText(_translate("setup", "Ln"))
        self.axis_values_area_2.setTitle(_translate("setup", "Axis values"))
        self.minimum_label_2.setText(_translate("setup", "Minimum"))
        self.automatic_minimum_2.setText(_translate("setup", "Automatic"))
        self.fixed_minimum_2.setText(_translate("setup", "Fixed"))
        self.maximum_label_2.setText(_translate("setup", "Maximum"))
        self.automatic_maximum_2.setText(_translate("setup", "Automatic"))
        self.fixed_maximum_2.setText(_translate("setup", "Fixed"))
        self.greater_label_2.setText(_translate("setup", "Greater Unit"))
        self.automatic_greater_2.setText(_translate("setup", "Automatic"))
        self.fixed_greater_2.setText(_translate("setup", "Fixed"))
        self.smallest_label_2.setText(_translate("setup", "Smallest Unit"))
        self.automatic_smallest_2.setText(_translate("setup", "Automatic"))
        self.fixed_smallest_2.setText(_translate("setup", "Fixed"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.format_vertical_axis), _translate("setup", "Format Vertical Axis"))
        self.show_cursors_label.setText(_translate("setup", "Show Cursors"))
        self.default_position_label.setText(_translate("setup", "Default Position"))
        self.signal.setText(_translate("setup", "Signal"))
        self.st_signal_low_label.setText(_translate("setup", "Low"))
        self.st_signal_high_label.setText(_translate("setup", "High"))
        self.background.setText(_translate("setup", "Background"))
        self.st_background_low_label.setText(_translate("setup", "Low"))
        self.st_background_high_label.setText(_translate("setup", "High"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.cursors), _translate("setup", "Cursors"))
        self.push_button_accept.setText(_translate("setup", "Accept"))
        self.push_button_cancel.setText(_translate("setup", "Cancel"))

