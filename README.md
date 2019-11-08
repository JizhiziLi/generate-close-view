# generate-close-view

This repository is created to generate close view of original image and paste it to the original one.

Can be used in paper writing or slides making.

****
Required config(can be changed in config.py):

* **original_path**: path to load the original image
* **result_path**: path to save the result
* **colo_hex**: color to draw the border(hex format)
* **crop_left_bottom**: coordinate of the left bottom point, denoted as *(x1, y1)* in following image
* **crop_right_top**: coordinate of the right top point, denoted as *(x2, y2)* in following image
* **paste_ratio**: ratio to resize the crop_img
* **thickness**: thickness of the border
* **paste_left_bottom**: coordinate of the left bottom point to paste crop_img, denoted as *(x3, y3)* in following image

****
Required: python3, cv2
Output: an image with close-view at any location with any ratio and any color of border.

****
How to run: 
* Edit config.py for any paths/settings
* run `python crop_and_paste.py`

<img src="src_img/index.png" width="500" height="500" title="Result Image" />
