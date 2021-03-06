# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/krl1to5/Work/FULL/Sequence-ToolKit/2016/resources/ui/gensec/process/posl.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_process(object):
    def setupUi(self, process):
        process.setObjectName("process")
        process.resize(819, 228)
        process.setMinimumSize(QtCore.QSize(0, 228))
        process.setMaximumSize(QtCore.QSize(16777215, 228))
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(process)
        self.horizontalLayout_18.setSpacing(12)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.form_area = QtWidgets.QFrame(process)
        self.form_area.setFrameShape(QtWidgets.QFrame.Box)
        self.form_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.form_area.setObjectName("form_area")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.form_area)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName("verticalLayout")
        self.layout = QtWidgets.QHBoxLayout()
        self.layout.setSpacing(15)
        self.layout.setObjectName("layout")
        self.layout_2 = QtWidgets.QHBoxLayout()
        self.layout_2.setObjectName("layout_2")
        self.ligth_source_label = QtWidgets.QLabel(self.form_area)
        self.ligth_source_label.setObjectName("ligth_source_label")
        self.layout_2.addWidget(self.ligth_source_label)
        self.ligth_source = QtWidgets.QComboBox(self.form_area)
        self.ligth_source.setMinimumSize(QtCore.QSize(58, 28))
        self.ligth_source.setMaximumSize(QtCore.QSize(58, 16777215))
        self.ligth_source.setObjectName("ligth_source")
        self.ligth_source.addItem("")
        self.ligth_source.addItem("")
        self.ligth_source.addItem("")
        self.layout_2.addWidget(self.ligth_source)
        self.layout.addLayout(self.layout_2)
        self.layout_3 = QtWidgets.QHBoxLayout()
        self.layout_3.setObjectName("layout_3")
        self.optical_power_label = QtWidgets.QLabel(self.form_area)
        self.optical_power_label.setObjectName("optical_power_label")
        self.layout_3.addWidget(self.optical_power_label)
        self.optical_power = QtWidgets.QSpinBox(self.form_area)
        self.optical_power.setMinimumSize(QtCore.QSize(55, 28))
        self.optical_power.setMaximumSize(QtCore.QSize(55, 16777215))
        self.optical_power.setMaximum(100)
        self.optical_power.setObjectName("optical_power")
        self.layout_3.addWidget(self.optical_power)
        self.layout.addLayout(self.layout_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.layout)
        self.line = QtWidgets.QFrame(self.form_area)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.layout_4 = QtWidgets.QHBoxLayout()
        self.layout_4.setSpacing(15)
        self.layout_4.setObjectName("layout_4")
        self.layout_5 = QtWidgets.QHBoxLayout()
        self.layout_5.setObjectName("layout_5")
        self.channels_label = QtWidgets.QLabel(self.form_area)
        self.channels_label.setObjectName("channels_label")
        self.layout_5.addWidget(self.channels_label)
        self.channels = QtWidgets.QLabel(self.form_area)
        self.channels.setObjectName("channels")
        self.layout_5.addWidget(self.channels)
        spacerItem1 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_5.addItem(spacerItem1)
        self.layout_4.addLayout(self.layout_5)
        self.layout_6 = QtWidgets.QHBoxLayout()
        self.layout_6.setObjectName("layout_6")
        self.time_per_channel_label = QtWidgets.QLabel(self.form_area)
        self.time_per_channel_label.setObjectName("time_per_channel_label")
        self.layout_6.addWidget(self.time_per_channel_label)
        self.time_per_channel = QtWidgets.QLabel(self.form_area)
        self.time_per_channel.setObjectName("time_per_channel")
        self.layout_6.addWidget(self.time_per_channel)
        spacerItem2 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_6.addItem(spacerItem2)
        self.layout_4.addLayout(self.layout_6)
        self.layout_7 = QtWidgets.QHBoxLayout()
        self.layout_7.setObjectName("layout_7")
        self.number_of_scan_label = QtWidgets.QLabel(self.form_area)
        self.number_of_scan_label.setObjectName("number_of_scan_label")
        self.layout_7.addWidget(self.number_of_scan_label)
        self.number_of_scan = QtWidgets.QSpinBox(self.form_area)
        self.number_of_scan.setMinimumSize(QtCore.QSize(55, 28))
        self.number_of_scan.setMaximumSize(QtCore.QSize(55, 16777215))
        self.number_of_scan.setMaximum(100)
        self.number_of_scan.setObjectName("number_of_scan")
        self.layout_7.addWidget(self.number_of_scan)
        self.layout_4.addLayout(self.layout_7)
        self.layout_8 = QtWidgets.QHBoxLayout()
        self.layout_8.setObjectName("layout_8")
        self.time_label = QtWidgets.QLabel(self.form_area)
        self.time_label.setObjectName("time_label")
        self.layout_8.addWidget(self.time_label)
        self.layout_9 = QtWidgets.QHBoxLayout()
        self.layout_9.setSpacing(0)
        self.layout_9.setObjectName("layout_9")
        self.time = QtWidgets.QDoubleSpinBox(self.form_area)
        self.time.setMinimumSize(QtCore.QSize(80, 28))
        self.time.setMaximumSize(QtCore.QSize(80, 16777215))
        self.time.setMaximum(99999.0)
        self.time.setObjectName("time")
        self.layout_9.addWidget(self.time)
        self.time_measurement = QtWidgets.QComboBox(self.form_area)
        self.time_measurement.setMinimumSize(QtCore.QSize(48, 28))
        self.time_measurement.setMaximumSize(QtCore.QSize(48, 16777215))
        self.time_measurement.setObjectName("time_measurement")
        self.time_measurement.addItem("")
        self.time_measurement.addItem("")
        self.time_measurement.addItem("")
        self.layout_9.addWidget(self.time_measurement)
        self.layout_8.addLayout(self.layout_9)
        self.layout_4.addLayout(self.layout_8)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_4.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.layout_4)
        self.layout_10 = QtWidgets.QHBoxLayout()
        self.layout_10.setSpacing(15)
        self.layout_10.setObjectName("layout_10")
        self.layout_11 = QtWidgets.QHBoxLayout()
        self.layout_11.setObjectName("layout_11")
        self.before_stimulation_label = QtWidgets.QLabel(self.form_area)
        self.before_stimulation_label.setObjectName("before_stimulation_label")
        self.layout_11.addWidget(self.before_stimulation_label)
        self.before_stimulation = QtWidgets.QSpinBox(self.form_area)
        self.before_stimulation.setMinimumSize(QtCore.QSize(55, 28))
        self.before_stimulation.setMaximumSize(QtCore.QSize(55, 16777215))
        self.before_stimulation.setMaximum(512)
        self.before_stimulation.setObjectName("before_stimulation")
        self.layout_11.addWidget(self.before_stimulation)
        self.layout_10.addLayout(self.layout_11)
        self.layout_12 = QtWidgets.QHBoxLayout()
        self.layout_12.setObjectName("layout_12")
        self.during_stimulation_label = QtWidgets.QLabel(self.form_area)
        self.during_stimulation_label.setObjectName("during_stimulation_label")
        self.layout_12.addWidget(self.during_stimulation_label)
        self.during_stimulation = QtWidgets.QSpinBox(self.form_area)
        self.during_stimulation.setMinimumSize(QtCore.QSize(55, 28))
        self.during_stimulation.setMaximumSize(QtCore.QSize(55, 16777215))
        self.during_stimulation.setMaximum(512)
        self.during_stimulation.setObjectName("during_stimulation")
        self.layout_12.addWidget(self.during_stimulation)
        self.layout_10.addLayout(self.layout_12)
        self.layout_13 = QtWidgets.QHBoxLayout()
        self.layout_13.setObjectName("layout_13")
        self.after_stimulation_label = QtWidgets.QLabel(self.form_area)
        self.after_stimulation_label.setObjectName("after_stimulation_label")
        self.layout_13.addWidget(self.after_stimulation_label)
        self.after_stimulation = QtWidgets.QSpinBox(self.form_area)
        self.after_stimulation.setMinimumSize(QtCore.QSize(55, 28))
        self.after_stimulation.setMaximumSize(QtCore.QSize(55, 16777215))
        self.after_stimulation.setMaximum(512)
        self.after_stimulation.setObjectName("after_stimulation")
        self.layout_13.addWidget(self.after_stimulation)
        self.layout_10.addLayout(self.layout_13)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_10.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.layout_10)
        self.line_2 = QtWidgets.QFrame(self.form_area)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.layout_14 = QtWidgets.QHBoxLayout()
        self.layout_14.setSpacing(15)
        self.layout_14.setObjectName("layout_14")
        self.layout_15 = QtWidgets.QHBoxLayout()
        self.layout_15.setObjectName("layout_15")
        self.final_temperature_label = QtWidgets.QLabel(self.form_area)
        self.final_temperature_label.setObjectName("final_temperature_label")
        self.layout_15.addWidget(self.final_temperature_label)
        self.final_temperature = QtWidgets.QDoubleSpinBox(self.form_area)
        self.final_temperature.setMinimumSize(QtCore.QSize(80, 28))
        self.final_temperature.setMaximumSize(QtCore.QSize(80, 16777215))
        self.final_temperature.setMaximum(600.0)
        self.final_temperature.setObjectName("final_temperature")
        self.layout_15.addWidget(self.final_temperature)
        self.layout_14.addLayout(self.layout_15)
        self.layout_16 = QtWidgets.QHBoxLayout()
        self.layout_16.setObjectName("layout_16")
        self.heating_rate_label = QtWidgets.QLabel(self.form_area)
        self.heating_rate_label.setObjectName("heating_rate_label")
        self.layout_16.addWidget(self.heating_rate_label)
        self.heating_rate = QtWidgets.QDoubleSpinBox(self.form_area)
        self.heating_rate.setMinimumSize(QtCore.QSize(80, 28))
        self.heating_rate.setMaximumSize(QtCore.QSize(80, 16777215))
        self.heating_rate.setMinimum(0.1)
        self.heating_rate.setMaximum(20.0)
        self.heating_rate.setObjectName("heating_rate")
        self.layout_16.addWidget(self.heating_rate)
        self.layout_14.addLayout(self.layout_16)
        self.layout_17 = QtWidgets.QHBoxLayout()
        self.layout_17.setObjectName("layout_17")
        self.stabilization_label = QtWidgets.QLabel(self.form_area)
        self.stabilization_label.setObjectName("stabilization_label")
        self.layout_17.addWidget(self.stabilization_label)
        self.stabilization = QtWidgets.QDoubleSpinBox(self.form_area)
        self.stabilization.setMinimumSize(QtCore.QSize(80, 28))
        self.stabilization.setMaximumSize(QtCore.QSize(80, 16777215))
        self.stabilization.setMaximum(99999.0)
        self.stabilization.setObjectName("stabilization")
        self.layout_17.addWidget(self.stabilization)
        self.layout_14.addLayout(self.layout_17)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_14.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.layout_14)
        self.horizontalLayout_18.addWidget(self.form_area)
        self.buttons_area = QtWidgets.QFrame(process)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttons_area.sizePolicy().hasHeightForWidth())
        self.buttons_area.setSizePolicy(sizePolicy)
        self.buttons_area.setMinimumSize(QtCore.QSize(0, 0))
        self.buttons_area.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.buttons_area.setFrameShape(QtWidgets.QFrame.Box)
        self.buttons_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttons_area.setObjectName("buttons_area")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.buttons_area)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.push_button_accept = QtWidgets.QPushButton(self.buttons_area)
        self.push_button_accept.setMinimumSize(QtCore.QSize(100, 32))
        self.push_button_accept.setShortcut("Return")
        self.push_button_accept.setObjectName("push_button_accept")
        self.verticalLayout_2.addWidget(self.push_button_accept)
        self.push_button_cancel = QtWidgets.QPushButton(self.buttons_area)
        self.push_button_cancel.setMinimumSize(QtCore.QSize(100, 32))
        self.push_button_cancel.setShortcut("Esc")
        self.push_button_cancel.setObjectName("push_button_cancel")
        self.verticalLayout_2.addWidget(self.push_button_cancel)
        self.push_button_information = QtWidgets.QPushButton(self.buttons_area)
        self.push_button_information.setMinimumSize(QtCore.QSize(100, 32))
        self.push_button_information.setObjectName("push_button_information")
        self.verticalLayout_2.addWidget(self.push_button_information)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem6)
        self.horizontalLayout_18.addWidget(self.buttons_area)

        self.retranslateUi(process)
        QtCore.QMetaObject.connectSlotsByName(process)

    def retranslateUi(self, process):
        _translate = QtCore.QCoreApplication.translate
        process.setWindowTitle(_translate("process", "POSL"))
        self.ligth_source_label.setText(_translate("process", "Ligth Source"))
        self.ligth_source.setItemText(0, _translate("process", "Blue"))
        self.ligth_source.setItemText(1, _translate("process", "IR"))
        self.ligth_source.setItemText(2, _translate("process", "AUX"))
        self.optical_power_label.setText(_translate("process", "Optical Power (%)"))
        self.channels_label.setText(_translate("process", "Channels:"))
        self.channels.setText(_translate("process", "0"))
        self.time_per_channel_label.setText(_translate("process", "Time per Channel:"))
        self.time_per_channel.setText(_translate("process", "0 ms"))
        self.number_of_scan_label.setText(_translate("process", "Number of Scan"))
        self.time_label.setText(_translate("process", "Time"))
        self.time_measurement.setItemText(0, _translate("process", "ms"))
        self.time_measurement.setItemText(1, _translate("process", "s"))
        self.time_measurement.setItemText(2, _translate("process", "us"))
        self.before_stimulation_label.setText(_translate("process", "Before Stimulation"))
        self.during_stimulation_label.setText(_translate("process", "During Stimulation"))
        self.after_stimulation_label.setText(_translate("process", "After Stimulation"))
        self.final_temperature_label.setText(_translate("process", "Final Temperature (°C)"))
        self.heating_rate_label.setText(_translate("process", "Heating Rate (°C/s)"))
        self.stabilization_label.setText(_translate("process", "Stabilization (s)"))
        self.push_button_accept.setText(_translate("process", "Accept"))
        self.push_button_cancel.setText(_translate("process", "Cancel"))
        self.push_button_information.setText(_translate("process", "Information"))

