# import cv2 as cv

# """ ------------------ Resize Citra ------------------"""
# img = cv.imread('resources/soccer_kid_large.jpg', cv.IMREAD_UNCHANGED)

# """ ------------------ 'shape' untuk mendaptkan dimensi citra ------------------"""
# print('Original Dimensions\t: ', img.shape)

# scale_percent = 60 # Scale 60% dari dimensi asli
# width = int(img.shape[1]  * scale_percent / 100)
# height = int(img.shape[0] * scale_percent / 100)

# """ Dimensi baru """

# dim = (width, height)

# """ 'resize' untuk mengubah dimensi citra """
# resized = cv.resize(img, dim, interpolation = cv.INTER_BITS)

# print('Resized Dimensons\t: ', resized.shape)

# """ Menyimpan hasil resize """
# cv.imwrite('resources/soccer_kid_small.jpg', resized)

# cv.imshow("Hasil resize citra", resized)
# cv.waitKey(0)
# cv.destroyAllWindows



################################################################

import cv2 as cv

img = cv.imread('resources/soccer_kid_small.jpg', cv.IMREAD_COLOR)

print(img.shape)

# cv.imshow('Cari Bola', img)
# cv.waitKey(0)
# cv.destroyAllWindows()

""" Mengambil Objek Bola """

ball = img[750:865, 785:895] 
print(ball.dtype)
print(ball.shape)

""" Memindahkan bola """
img[805:920, 60:170] = ball 

cv.putText(img, '5200411193', (1120,860), cv.FONT_HERSHEY_DUPLEX,
            1.0, (224,58,25), 1)

""" Membuat file baru dengan objek yang ditempel """
cv.imwrite('resources/soccer_kid_small_doubleBall.jpg', img)

cv.imshow('Hasil Akhir', img)
cv.waitKey(0)
cv.destroyAllWindows()