# Color Converter Application

## Description
This is a color conversion application created using Python, Tkinter, and Pillow. It allows users to convert and visualize colors across three color models — RGB, CMYK, and HLS. The app provides a friendly interface to select colors and modify their components in real-time across all models.

## Features
- Convert between RGB, CMYK, and HLS color models.
- Adjust individual color components through sliders.
- Select colors using a color palette.
- Automatic updates of other color models when a value is changed.
- Rounds out-of-bounds values and shows warning if adjustments are needed.

## Requirements
- Python 3.x
- Tkinter (included with Python standard library)
- Pillow (Install via `pip install pillow`)

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/color-converter-app.git
   cd color-converter-app
Install required packages:
bash
Copy code
pip install pillow
Usage

The application includes:

Color Conversion Functions: Functions to convert RGB ↔ CMYK ↔ HLS.
Update Functions: When values in one color model are changed, all other color model values update accordingly.
Interface: Tkinter-based GUI with labels, sliders, and buttons for interacting with the application.
