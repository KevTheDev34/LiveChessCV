#!/usr/bin/env python3
import os

# kinda worked, created the files as 'Assets#.jpg' in the same directory as the Assets folder, not within it. Manually moved them in
def rename_imgs():
    directory = "Assets"
    for ind, entry in enumerate(os.scandir(directory)):
        path = entry.path
        new_path = remove_reverse(path, '/')
        new_path = new_path + f"{ind}.jpg"
        os.rename(path, new_path)


def remove_reverse(text, char):
    index = text.rfind(char)
    if index != -1:
        return text[:index]
    return text

def check_cv_on_assets():
    # ret,img = cap.read()	
	img = cv2.imread('./Assets/chessboard_1.jpg', 1)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	land = land_cascade.detectMultiScale(gray, 10, 10) #If abrupt detections are made change (gray, 10, 10) to (gray, 20, 20) if more and more wrong detections are made, (gray, 1, 1) if none detections are made and you may change it as per your wish

