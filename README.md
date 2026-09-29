# Open-CV-Basics

Beginner-level OpenCV examples in Python, covering images, drawing, mouse events and webcam video, plus a small mouse-driven image cropping tool built with the same basic commands.

## What's covered

`main.py` goes through these steps one window at a time (press any key to move to the next one):

- Reading an image and printing its shape
- Showing an image
- Converting a color image to grayscale
- Splitting the blue, green and red channels and showing them side by side
- Resizing an image to 500x500 and to half size (the half-size result is shown)
- Flipping an image vertically, horizontally and both (the combined flip is shown)
- Cropping an image with array slicing
- Saving a cropped image to `fruits_small.png`
- Drawing a rectangle, circle, line and text on a blank canvas
- Live drawing with mouse events: click to draw circles, then click and drag to draw filled rectangles (press `x` to close each canvas)

`video.py` works with the webcam:

- Shows the live webcam feed in grayscale
- Records the grayscale feed to `output.avi`
- Plays `output.avi` back

Press `x` to stop each part and move to the next one.

## Cropping tool

`croppingtool.py` opens an image in a window. Click and drag with the left mouse button to select an area. When you release the button, the selection is outlined on the image and the cropped part opens in a separate window. You can make as many selections as you like. Press `x` to quit.

## Tech stack

- Python 3
- OpenCV (`opencv-python`)
- NumPy

## Project structure

```
Open-CV-Basics/
├── main.py            # image basics, drawing and mouse events
├── video.py           # webcam feed, recording and playback
├── croppingtool.py    # mouse-based cropping tool
└── requirements.txt
```

## Setup

```bash
git clone https://github.com/Hamza-Tahirr/Open-CV-Basics.git
cd Open-CV-Basics
python -m venv venv
venv\Scripts\activate        # on macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
```

The image scripts read `img/fruits.jpg` by default. The image is not included in the repo, so create an `img` folder and put any photo there with that name, or pass the path of another image as an argument.

## Usage

Run the scripts from the project folder:

```bash
python main.py                      # uses img/fruits.jpg
python main.py path/to/image.jpg
python croppingtool.py
python croppingtool.py path/to/image.jpg
python video.py                     # needs a webcam
```

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
