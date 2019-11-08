import cv2
from config import *

#########################
### Final function
###
###

def crop_and_paste(original_path, result_path, crop_left_bottom, crop_right_top, paste_left_bottom, color_hex='#FFD966', thickness=3, paste_ratio=1):

	print('*****************')
	print(f'Start process: {original_path}')
	h = color_hex.lstrip('#')
	color_BGR = tuple(int(h[i:i+2], 16) for i in (4, 2, 0))

	####
	# read original image
	original = cv2.imread(original_path)
	print(f'Original image shape: {original.shape}')
	x1 = crop_left_bottom[0]
	x2 = crop_right_top[0]
	y1 = original.shape[0]-crop_right_top[1]
	y2 = original.shape[0]-crop_left_bottom[1]
	
	####
	# crop small image and add border
	crop_img = original[y1:y2, x1:x2,:]
	crop_img = cv2.copyMakeBorder(crop_img, thickness, thickness, thickness, thickness, cv2.BORDER_CONSTANT,value = list(color_BGR))
	
	print(f'Crop image at {crop_left_bottom} | {crop_right_top}')
	print(f'Crop image shape: {crop_img.shape}')
	
	####
	# draw rectangle on original image
	start_point = (x1, y1) 
	end_point = (x2, y2) 
	original = cv2.rectangle(original, start_point, end_point, color_BGR, thickness) 

	# ####
	# # resize crop image with ratio
	new_w = int(crop_img.shape[1]*paste_ratio)
	new_h = int(crop_img.shape[0]*paste_ratio)
	crop_img = cv2.resize(crop_img, (new_w, new_h), interpolation=cv2.INTER_LINEAR)
	print(f'Ratio: {paste_ratio}')
	print(f'Crop image shape after resize: {crop_img.shape}')

	# ####
	# # paste crop image to original
	print(f'Paste to {paste_left_bottom}')
	x1 = paste_left_bottom[0]
	x2 = paste_left_bottom[0]+crop_img.shape[1]
	y1 = paste_left_bottom[1]
	y2 = paste_left_bottom[1]+crop_img.shape[0]
	y1 = original.shape[0]-paste_left_bottom[1]-crop_img.shape[0]
	y2 = original.shape[0]-paste_left_bottom[1]

	original[y1:y2,x1:x2,0] = crop_img[:,:,0]
	original[y1:y2,x1:x2,1] = crop_img[:,:,1]
	original[y1:y2,x1:x2,2] = crop_img[:,:,2]

	cv2.imwrite(result_path, original)





if __name__ == '__main__':

	##########################
	### Process single img
	### 
	### 
	###########################	

	original_path = ORIGINAL_PATH
	result_path = RESULT_PATH
	color_hex = COLOR_HEX
	crop_left_bottom = CROP_LEFT_BOTTOM
	crop_right_top = CROP_RIGHT_TOP
	paste_ratio = PASTE_RATIO
	thickness=THICKNESS
	paste_left_bottom = PASTE_LEFT_BOTTOM
	
	

	

	try:
		crop_and_paste(original_path, result_path, crop_left_bottom, crop_right_top, paste_left_bottom, color_hex, thickness, paste_ratio)
	except Exception as e:
		print(str(e))