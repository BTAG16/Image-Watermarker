# Image Watermarker

This is a simple image watermarking application built using Python's Tkinter library. It allows users to add either text or image watermarks to an image, preview the result, and save the watermarked image.

## Features

- **Choose an Image**: Select an image from your computer to watermark.
- **Text Watermark**: Add a custom text watermark to the image.
- **Image Watermark**: Add a watermark image on top of the original image.
- **Position Control**: Adjust the position of the watermark on the image with sliders for X and Y coordinates.
- **Preview Watermark**: View the watermarked image before saving.
- **Clear Watermark**: Remove all watermarks from the image and restore the original.
- **Save Watermarked Image**: Save the watermarked image to your computer.

## Tech Stack

- **Python**: The programming language used.
- **Tkinter**: For building the GUI.
- **Pillow (PIL)**: For image manipulation (loading, editing, and saving images).

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/image-watermarker.git
   cd image-watermarker
   ```

2. **Install dependencies**:
   Ensure you have Python 3.x installed. Install the necessary Python libraries by running:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   To start the application, run the `main.py` script:
   ```bash
   python main.py
   ```

## Usage

1. Click **Choose a Picture** to load an image.
2. Select either **Picture Watermark** or **Text Watermark**.
   - For **Text Watermark**, enter the desired text and adjust the position.
   - For **Picture Watermark**, choose an image file to use as the watermark and adjust its position.
3. Use the sliders to adjust the **Position X** and **Position Y** of the watermark.
4. Click **Add Watermark** to apply the watermark to the image.
5. Click **Clear Watermark** to reset to the original image.
6. Click **Save Picture** to save the final watermarked image.

## Requirements

- Python 3.x
- Tkinter (comes pre-installed with Python)
- Pillow (for image manipulation)

You can install the required libraries with:

```bash
pip install pillow
```

## License
This project is licensed under the MIT License.


Feel free to contribute, suggest improvements, or ask questions by opening an issue in this repository.
Ensure that you create a `requirements.txt` file containing the following:

```txt
pillow
```
