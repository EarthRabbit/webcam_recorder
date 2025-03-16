# webcam_recorder
A video recorder using webcam

## using library
* cv2

## additional function for my own video recorder
changing fourcc and format for various type of recordings

* warnings: opencv doesn't provide H264 fourcc for .mp4 format.
* so if you want to use H264, you need to install [openH264](https://github.com/cisco/openh264).

### description for webcam-recorder
1. In advance, you need to check you don't have any web camera or you have more than 2 cameras.
2. You need to choose file format and file fourcc in advance and type with delimiter ' '.
* In this case, you need to change 0 from **video = cv.VideoCapture(0)** to 1, or something else.
3. Then your web camera will start recording. <img align="left" src="./image.png">

