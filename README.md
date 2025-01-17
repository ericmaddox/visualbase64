# VisualBase64

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Tkinter](https://img.shields.io/badge/Tkinter-Installed-brightgreen)
![Issues](https://img.shields.io/github/issues/ericmaddox/visualbase64)
![Last Commit](https://img.shields.io/github/last-commit/ericmaddox/visualbase64)


<table>
  <tr>
    <td style="vertical-align: top; padding-right: 20px;">
      A sleek and professional tool for converting images to Base64 strings with ease. Drag, drop, encode, and copy—<b>VisualBase64</b> makes it simple.
    </td>
    <td>
      <img src="https://github.com/ericmaddox/visualbase64/blob/main/media/visual_base64_1.JPEG" width="300"/>
    </td>
  </tr>
</table>






## Overview

The Image to Base64 Converter is a graphical user interface (GUI) application that allows users to convert image files to Base64 strings. The application provides a drag and drop area for easy file selection, displays the converted Base64 string, and includes a button to copy the Base64 string to the clipboard.

## Features

- Drag and drop support for image file selection
- Converts image files to Base64 strings
- Displays the converted Base64 string in a text widget
- Button to copy the Base64 string to the clipboard
- Supports common image formats: PNG, JPEG, BMP, GIF, TIFF

## Requirements

- Python 3.x
- tkinter
- tkinterdnd2

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ericmaddox/visualbase64.git
   cd visualbase64
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:

   ```bash
   python visual_base64.py
   ```

2. Drag and drop an image file into the specified area in the GUI.

3. The converted Base64 string will be displayed in the text widget.

4. To copy the Base64 string to the clipboard, click the "Copy to Clipboard" button.

## Getting Started

Follow these steps to get your development environment set up:

1. Ensure you have Python 3.x installed.
2. Install the required packages using the provided `requirements.txt` file.
3. Run the application and start converting your images to Base64!

## Screenshots

<table>
  <tr>
    <td><img src="https://github.com/ericmaddox/visualbase64/blob/main/media/example_image1.JPG" width="400"/></td>
    <td><img src="https://github.com/ericmaddox/visualbase64/blob/main/media/example_image3.JPG" width="400"/></td>
  </tr>
  <tr>
    <td><img src="https://github.com/ericmaddox/visualbase64/blob/main/media/example_image2.JPG" width="400"/></td>
    <td><img src="https://github.com/ericmaddox/visualbase64/blob/main/media/example_image4.JPG" width="400"/></td>
  </tr>
</table>

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss any changes or improvements.

## Acknowledgements

- [tkinter](https://docs.python.org/3/library/tkinter.html) - The standard GUI toolkit for Python
- [tkinterdnd2](https://github.com/pmgagne/tkinterdnd2) - A drag-and-drop support library for tkinter
