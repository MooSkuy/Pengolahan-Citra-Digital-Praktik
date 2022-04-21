import cv2 as cv
import numpy as np

blank = np.zeros((500, 1000, 3), dtype='uint8')
# cv.imshow('Blank', blank)

#Bagian Mesin
cv.rectangle(blank, (250,300), (500,200), (0, 255, 0), thickness=-1)
# cv.imshow('Bagian Mesin', blank)


#Bagian Masinis
cv.rectangle(blank, (500,300), (600,125), (22, 211, 224), thickness=-1)
# cv.imshow('Bagian Masinis', blank)

#Bagian Jendela
cv.rectangle(blank, (515,200), (585,140), (0,0,255), thickness=-1)
# cv.imshow('Bagian Jendela', blank)

#Bagian Depan

pt1 = (250, 200)
pt2 = (150, 300)
pt3 = (250, 300)

cv.circle(blank, pt1, 1, (179,85,18), -1)
cv.circle(blank, pt2, 1, (179,85,18), -1)
cv.circle(blank, pt3, 1, (179,85,18), -1)


triangle_cnt = np.array( [pt1, pt2, pt3] )

cv.drawContours(blank, [triangle_cnt], 0, (179,85,18), -1)

# cv.imshow('Bagian Depan', blank)

#Bagian Cerobong Asap
cv.rectangle(blank, (300,200), (340,140), (179,85,18), thickness=-1)
# cv.imshow('Bagian Cerobong Asap', blank)

cv.rectangle(blank, (290,140), (350,115), (0,255,0), thickness=-1)
# cv.imshow('Bagian Cerobong Asap', blank)

cv.rectangle(blank, (310, 115), (330,100), (179,85,18), thickness=-1)
# cv.imshow('Bagian Cerobong Asap', blank)

pt4 = (330,100)
pt5 = (330,115)
pt6 = (350,115)

cv.circle(blank, pt4, 1, (179,85,18), -1)
cv.circle(blank, pt5, 1, (179,85,18), -1)
cv.circle(blank, pt6, 1, (179,85,18), -1)

triangle_cnt = np.array( [pt4, pt5, pt6] )

cv.drawContours(blank, [triangle_cnt], 0, (179,85,18), -1)

# cv.imshow('Bagian Cerobong Asap', blank)

pt7 = (310,100)
pt8 = (290,115)
pt9 = (310,115)

cv.circle(blank, pt7, 1, (179,85,18), -1)
cv.circle(blank, pt8, 1, (179,85,18), -1)
cv.circle(blank, pt9, 1, (179,85,18), -1)

triangle_cnt = np.array( [pt7, pt8, pt9] )

cv.drawContours(blank, [triangle_cnt], 0, (179,85,18), -1)

# cv.imshow('Bagian Cerobong Asap', blank)

#Bagian Roda
cv.circle(blank, (300,330), 30, (179,85,18), -1)
# cv.imshow('Bagian Roda', blank)

cv.circle(blank, (400, 330), 30, (179,85,18), -1)
# cv.imshow('Bagian Roda', blank)

cv.circle(blank, (550, 320), 45, (0,0, 255), -1)
# cv.imshow('Bagian Roda', blank)

cv.circle(blank, (550, 320), 30, (0,255,0), -1)
# cv.imshow('Bagian Roda', blank)

# Bagian Garis
cv.line(blank, (300,330), (580,330), (255,255,255), thickness=3)
# cv.imshow('Bagian Garis', blank)

#Bagian nama
cv.putText(blank, 'Pramadika Egamo', (600,450), cv.FONT_HERSHEY_DUPLEX,
            1.0, (255,255,255), 1)
# cv.imshow('Bagian Nama', blank)

cv.imshow('My Shinkanzen', blank)

cv.waitKey(0)