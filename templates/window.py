from threading import Thread

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtWidgets import (QFrame, QLineEdit, QPushButton,
                               QVBoxLayout)

from utils import generate_qrcode


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 250)
        Form.setMinimumSize(QSize(400, 250))
        Form.setMaximumSize(QSize(400, 250))
        Form.setStyleSheet(u"QFrame {\n"
"	background-color: #bbd4ce;\n"
"}")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QLineEdit {\n"
"	height: 50px;\n"
"	border: solid;\n"
"	border-width: 2px;\n"
"	border-color: #264e70;\n"
"	border-radius: 25px;\n"
"	background-color: #679186;\n"
"	color: #f9b4ab;\n"
"	font-family: \"Arial\";\n"
"	font-style: bold;\n"
"	font-size: 40px;\n"
"}\n"
"QPushButton {\n"
"	height: 50px;\n"
"	border: solid;\n"
"	border-width: 2px;\n"
"	border-color: #264e70;\n"
"	border-radius: 25px;\n"
"	background-color: #679186;\n"
"	color: #f9b4ab;\n"
"	font-family: \"Arial\";\n"
"	font-style: bold;\n"
"	font-size: 40px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.clicked.connect(self._generate)

        self.verticalLayout_2.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"GENERATE", None))
    # retranslateUi

    def _generate(self):
        payload = self.lineEdit.text()
        thread = Thread(target=generate_qrcode, args=(payload, ))
        thread.start()

