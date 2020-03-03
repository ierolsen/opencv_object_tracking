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


## when the version 1.1 works:
![middle_point](https://user-images.githubusercontent.com/30235603/74566304-3fa0c680-4f84-11ea-8045-f019609c73b2.png)

## and when the version 2.0 works:

![version2 0](https://user-images.githubusercontent.com/30235603/75790950-ed7de480-5d7c-11ea-98e3-c829494f7a13.png)

## what is the difference between version1.0 and version2.0 ?

I just added some morphological transformations to video. They are called erode and dilate. 

-> Erode 
it rodes away the boundaries of foreground object and used to diminish the features of the image.

-> Dilate
it increases the object area and used to accentuate features.

and then i defined another morphological functions which is called ``` cv2.MORPH_OPEN```, ```cv2.MORPH_CLOSE```

-> ``` cv2.MORPH_OPEN``` firstly, erosion operator is applied and then dilatation operator is applied. it means they work together.

-> ``` cv2.MORPH_CLOSE``` It is useful in closing small holes inside the foreground objects, or small black points on the object.


I think the important difference of the code is here:

morphologyEx() function takes the dilation which is created by ``` cv2.dilate ``` as a source. 
dilate function makes clean and big area therefore, the colorful object is found clearly.
and the finally, i gave to ``` cv2.findContours ``` as a source that is called closing and returned by ``` cv2.MORPH_CLOSE ``` function.

## Conclusion

the first version finds the colorful object traditional way. it means, only there were classical functions
but the version2.0 contains more morphological functions that finding out the area of colorful objects.
