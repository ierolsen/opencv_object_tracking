This repository contains a part of code that is part of my project and will track red objects with the servo motor.

## Here are some functions I used

* **cv2.rectangle()** draws a box 
	```python
	cv2.rectangle(image, start_point, end_point, color, thickness)
	```
* **cv2.cvtColor()** converts from a color to another color
	```python
	cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	```
* **cv2.line()** draws a line
	```python
	cv2.line(image, start_point, end_point, color, thickness)
	```
* **cv2.inRange()** creates a mask of red
	```python
	cv2.inRange(hsv_frame, low_red, high_red)
	```
* **cv2.findContours()** finds contours of moving object

* **cv2.boundingRect()** returns the 4 points of the bounding box


## when the code works:
![middle_point](https://user-images.githubusercontent.com/30235603/74566304-3fa0c680-4f84-11ea-8045-f019609c73b2.png)
