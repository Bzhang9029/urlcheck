import sys
from wsgiref.util import application_uri
import re
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit
from PyQt5.QtCore import Qt
import VirusTotalClient


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.url_label = QLabel("Enter the URL",self)
        self.url_insert = QLineEdit(self)
        self.decision = QLabel(self)
        self.get_decision_button = QPushButton("Scan URL", self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("CheckURL")
        self.setGeometry(500, 200, 400, 400)

        vbox = QVBoxLayout()
        vbox.addWidget(self.url_label)
        vbox.addWidget(self.url_insert)
        vbox.addSpacing(20)
        vbox.addWidget(self.get_decision_button)

        vbox.addWidget(self.decision)

        self.setLayout(vbox)
        self.url_label.setAlignment(Qt.AlignCenter)
        self.url_insert.setAlignment(Qt.AlignCenter)
        self.decision.setAlignment(Qt.AlignCenter)

        self.url_insert.setObjectName('url_insert')
        self.url_label.setObjectName('url_label')
        self.get_decision_button.setObjectName('get_decision_button')
        self.decision.setObjectName('decision')

        self.setStyleSheet("""
            QLabel{
            font-size: 20px;
            font-family: calibiri;
            }
            
            #url_insert{
            padding: 10px;
            font-size:20px
            }
            
            #url_label{
            font-size:40px;
            font-family: italtic;
            }
            
            QPushButton{
            font-size:20px;
            font-family: calibiri;
            background-color: #4CAF50;
            }
            
            QPushButton:hover{
            font-size:17px;
            background-color: #45a049;
            }
            
            QPushButton:pressed{
            font-size:20px;
            background-color: #2e7031;
            }
        """)

        self.get_decision_button.clicked.connect(self.get_decision)

    def get_decision(self):
        input= self.url_insert.text()
        id = VirusTotalClient.scan_url(input)
        url_report = (VirusTotalClient.get_url_report(id))
        self.display_decision(url_report)

    def display_decision(self,url_report):
        if url_report["data"]["attributes"]["stats"]["malicious"] > 0:
            self.decision.setText(" ☣️Malicious URL")
            self.decision.setStyleSheet("color: red;"
                                        "font-size: 30px;"
                                        "bold: true;")
        elif url_report["data"]["attributes"]["stats"]["suspicious"] > 0:
            self.decision.setText(" ⚠️Suspicious URL")
            self.decision.setStyleSheet("color: yellow; font-size: 30px;bold: true;")
        elif url_report["data"]["attributes"]["stats"]["harmless"] > 0:
            self.decision.setText(" ✅Harmless URL")
            self.decision.setStyleSheet("color: green; font-size: 30px;bold:true;")
        else:
            self.decision.setText("❓ <b>Unknown result</b>")
            self.decision.setStyleSheet("""
                   color: gray;
                   font-size: 28px;
                   font-weight: bold;
            """)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
