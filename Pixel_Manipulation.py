import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel,
    QLineEdit, QRadioButton, QFileDialog, QMessageBox
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PIL import Image
import numpy as np

class ImageEncryptionApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Image Encryption Tool')

        layout = QVBoxLayout()

        self.key_label = QLabel('Enter Key (Integer 0-255):')
        layout.addWidget(self.key_label)

        self.key_entry = QLineEdit(self)
        layout.addWidget(self.key_entry)

        self.method_label = QLabel('Encryption Method:')
        layout.addWidget(self.method_label)

        self.add_method = QRadioButton('Add Value')
        self.add_method.setChecked(True)
        layout.addWidget(self.add_method)

        self.swap_method = QRadioButton('Swap Pixels')
        layout.addWidget(self.swap_method)

        # Buttons for selecting input and output images
        self.input_button = QPushButton('Select Input Image', self)
        self.input_button.clicked.connect(self.select_input_file)
        layout.addWidget(self.input_button)

        # Label to display the input file path
        self.input_path_label = QLabel('Input file location:')
        layout.addWidget(self.input_path_label)

        self.output_button = QPushButton('Select Output Image', self)
        self.output_button.clicked.connect(self.select_output_file)
        layout.addWidget(self.output_button)

        # Label to display the output file path
        self.output_path_label = QLabel('Output file location:')
        layout.addWidget(self.output_path_label)

        # Encryption and Decryption buttons
        self.encrypt_button = QPushButton('Encrypt Image', self)
        self.encrypt_button.clicked.connect(self.encrypt_image)
        layout.addWidget(self.encrypt_button)

        self.decrypt_button = QPushButton('Decrypt Image', self)
        self.decrypt_button.clicked.connect(self.decrypt_image)
        layout.addWidget(self.decrypt_button)

        # Image display label with a larger size
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setMinimumSize(600, 400)  # Set minimum size for the image
        layout.addWidget(self.image_label)

        self.setLayout(layout)
        self.setGeometry(100, 100, 500, 700)  # Adjust the window size to accommodate the larger image

        # Variables to store file paths
        self.input_path = None
        self.output_path = None

    def select_input_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select Input Image", "", "Image Files (*.png *.jpg *.jpeg)"
        )
        if file_path:
            self.input_path = file_path
            self.input_path_label.setText(f'Input file location: {file_path}')  # Display the input file path
            self.load_image(file_path)

    def select_output_file(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save Output Image", "", "PNG files (*.png)"
        )
        if file_path:
            self.output_path = file_path
            self.output_path_label.setText(f'Output file location: {file_path}')  # Display the output file path

    def load_image(self, path):
        pixmap = QPixmap(path)
        self.image_label.setPixmap(pixmap.scaled(
            self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def swap_pixels(self, pixels):
        height, width, _ = pixels.shape
        for i in range(0, height - 1, 2):
            for j in range(0, width - 1, 2):
                if i + 1 < height and j + 1 < width:
                    pixels[i, j], pixels[i + 1, j + 1] = pixels[i + 1, j + 1], pixels[i, j]
        return pixels

    def add_value(self, pixels, value):
        return np.clip(pixels + value, 0, 255)

    def subtract_value(self, pixels, value):
        return np.clip(pixels - value, 0, 255)

    def encrypt_image(self):
        if not self.input_path:
            QMessageBox.warning(self, "Input Error", "Please select an input image.")
            return
        if not self.output_path:
            QMessageBox.warning(self, "Output Error", "Please select an output path.")
            return
        try:
            key = int(self.key_entry.text())
            method = "add" if self.add_method.isChecked() else "swap"
            self.process_image(self.input_path, self.output_path, key, method, True)
            self.load_image(self.output_path)
            QMessageBox.information(self, "Success", "Image encrypted successfully!")
        except Exception as e:
            QMessageBox.critical(self, "Error", "Enter key integer 0-255")

    def decrypt_image(self):
        if not self.input_path:
            QMessageBox.warning(self, "Input Error", "Please select an input image.")
            return
        if not self.output_path:
            QMessageBox.warning(self, "Output Error", "Please select an output image.")
            return
        try:
            key = int(self.key_entry.text())
            method = "add" if self.add_method.isChecked() else "swap"
            self.process_image(self.input_path, self.output_path, key, method, False)
            self.load_image(self.output_path)
            QMessageBox.information(self, "Success", "Image decrypted successfully!")
        except Exception as e:
            QMessageBox.critical(self, "Error", "Enter key integer 0-255")

    def process_image(self, input_path, output_path, key, method, encrypt):
        image = Image.open(input_path)
        pixels = np.array(image)
        if method == "swap":
            if encrypt:
                pixels = self.swap_pixels(pixels)
                pixels = self.add_value(pixels, key)
            else:
                pixels = self.subtract_value(pixels, key)
                pixels = self.swap_pixels(pixels)
        elif method == "add":
            if encrypt:
                pixels = self.add_value(pixels, key)
            else:
                pixels = self.subtract_value(pixels, key)
        processed_image = Image.fromarray(pixels.astype(np.uint8))
        processed_image.save(output_path)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImageEncryptionApp()
    ex.show()
    sys.exit(app.exec_())
