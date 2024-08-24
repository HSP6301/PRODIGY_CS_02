# Pixel Manipulation Tool for Image Encryption

## Introduction

The **Pixel Manipulation Tool** is the Image Encryption Tool is a Python-based desktop application designed to provide a simple yet effective way to encrypt and decrypt images. Built using the PyQt5 library for the graphical user interface (GUI) and the Python Imaging Library (PIL) for image processing, this tool allows users to securely modify images using basic encryption techniques. Whether you're interested in protecting sensitive images or exploring fundamental encryption concepts, this tool offers a user-friendly interface for experimenting with image encryption.

## Features

- **GUI Interface**: The tool provides an intuitive GUI for users, making it easy to encrypt and decrypt images without needing to write any code.
- **Image Encryption & Decryption**: Supports encryption and decryption of images using pixel manipulation techniques.
- **Encryption Methods**:
  - **Add Value**: Adds a specified integer value to each pixel's RGB values.
  - **Swap Pixels**: Swaps pixels in a grid pattern to obscure the image.
- **File Selection**: Users can choose input and output image files through file dialogs.
- **File Path Display**: The paths of the selected input and output image files are shown within the interface, providing clarity on which files are being processed.
- **Image Display**: The application displays the selected input image and the processed output image within the GUI. The image display area is large and scalable, making it easy to view the results.
- **Error Handling**: Provides user feedback in case of invalid inputs or processing errors.
- **Cross-Platform**: The tool can run on any platform that supports Python and PyQt5, making it versatile and accessible to a wide range of users.

## Usage

1. **Run the Application**:
   - Run the Python script. The main window of the Image Encryption Tool will appear.

2. **Select Input Image**:
   - Click the "Input Image" button to open a file dialog and select the image you want to encrypt or decrypt.
   - The path of the selected image will be displayed next to the button.

3. **Select Output Image**:
   - Click the "Output Image" button to open a file dialog and specify where to save the processed image.
   - The path of the selected save location will be displayed next to the button.

4. **Enter Encryption Key**:
   - Input an integer key into the provided text field. This key will be used for encryption and decryption.

5. **Choose Encryption Method**:
   - Select one of the two methods:
     - **Add Value**: Encrypts or decrypts by adding or subtracting the key value to pixel RGB values.
     - **Swap Pixels**: Encrypts or decrypts by swapping pixels in a grid pattern.

6. **Encrypt or Decrypt Image**:
   - Click the "Encrypt Image" button to apply the selected encryption method to the input image and save it to the specified output location.
   - Click the "Decrypt Image" button to apply the selected decryption method to the input image and save it to the specified output location.

7. **View Processed Image**:
   - The processed image will be displayed in the application window.

## Error Handling

- **Input/Output File Selection**: If an input or output file is not selected, a warning message will appear prompting the user to select the necessary files.essage will be displayed.
- **No Output Location Specified**: If you try to encrypt or decrypt without specifying an output location, a warning message will be displayed.
- **Invalid Key Input**: If the key is not a valid integer, an error message will be shown.
- **Processing Errors**: Any errors during image processing will be reported with a descriptive error message.

## Requirements

To run this application, you need the following:

- **Python 3.x**: Make sure you have Python installed on your system.
- **PySide6**: This is the Python module used to create the GUI. You can install it using pip:

  ```bash
  pip install PyQt5
  
- **Pillow**: The Python Imaging Library (PIL) fork that supports opening, manipulating, and saving many different image file formats. Install it using pip:

  ```bash
  pip install Pillow

- **NumPy**: A fundamental package for scientific computing with Python, used here for efficient image data manipulation. Install it using pip:  

   ```bash
   pip install numpy

  
