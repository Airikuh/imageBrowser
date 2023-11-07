import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QFileDialog, QWidget
from PyQt5.QtGui import QPixmap

class ImageBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.image_label = QLabel()
        self.layout.addWidget(self.image_label)

        self.load_button = QPushButton("Load Image")
        self.load_button.clicked.connect(self.load_image)
        self.layout.addWidget(self.load_button)

        self.central_widget.setLayout(self.layout)

    def load_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image", "", \
            "Image Files (*.png *.jpg *.jpeg *.gif *.bmp *.ico);;All Files (*)", \
            options=options)

        if file_name:
            pixmap = QPixmap(file_name)
            self.image_label.setPixmap(pixmap)
            self.image_label.setScaledContents(True)

def main():
    app = QApplication(sys.argv)
    window = ImageBrowser()
    window.setGeometry(100, 100, 800, 600)
    window.setWindowTitle("Image Browser")
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
