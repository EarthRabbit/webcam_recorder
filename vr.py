import cv2 as cv

video = cv.VideoCapture(0)

if video.isOpened():
    fps = video.get(cv.CAP_PROP_FPS) 
    valid, img = video.read()
    
    if valid:
        h, w, *_ = img.shape
        # Choosing your own format, fourcc for your recordings
        format, fourcc = input("Choose your recording's format and fourcc. For .avi, choose XVID. For .mp4, choose H264\n").split(' ')
        
        is_color = (img.ndim > 2) and (img.shape[2] > 1)
        target_file = 'Recordings.' + format
        target = cv.VideoWriter(target_file, cv.VideoWriter_fourcc(*fourcc), fps, (w, h), is_color)
        
        frame = 0
        A = 1
        
        while True:
            valid, img = video.read()
            if not valid:
                break

            display_img = img.copy()
            recorder_status = "Recorder: Running" if A == 1 else "Recorder: Preview"
            cv.putText(display_img, f'{(frame/30):.2f}', (10, 25), cv.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)
            cv.putText(display_img, f'{recorder_status}', (10, 60), cv.FONT_HERSHEY_COMPLEX, 0.8, (255, 0, 0), 2)
            
            if(A == 1):
                target.write(img)
            
            frame += 1
            
            cv.imshow('video recorder', display_img)
            
            key = cv.waitKey(1)
            if key == 32:
                A = 0 if A == 1 else 1
                
                display_img = img.copy()
                recorder_status = "Recorder: Running" if A == 1 else "Recorder: Preview"
                cv.putText(display_img, f'{(frame/30):.2f}', (10, 25), cv.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)
                cv.putText(display_img, f'{recorder_status}', (10, 60), cv.FONT_HERSHEY_COMPLEX, 0.8, (255, 0, 0), 2)
                cv.imshow('video recorder', display_img)
                
                while True:
                    key = cv.waitKey(0)
                    if key == 32 or key == 27:
                        A = 0 if A == 1 else 1
                        break

            if key == 27:
                break

    target.release()

video.release()
cv.destroyAllWindows()