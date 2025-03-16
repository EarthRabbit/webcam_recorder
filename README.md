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
3. Then your web camera will start recording.
  
  ![Image](https://github.com/user-attachments/assets/23c5b276-6f88-4175-a714-558a6413722c)

4. If you want to stop recording for a while, just press spacebar.

![Image](https://github.com/user-attachments/assets/6cbc10d8-e901-4e70-9f1a-4d61fd1b57c8)

Do the same to resume recording.
6. if you want to finish recording, just press esc key. Then your recording will be saved as Recordings.***(your choice for format).

##
