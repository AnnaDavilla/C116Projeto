import cv2

#lendo poster
img = cv2.imread("solar-system.jpg")


#texto
text_to_Sol = "Sol"
text_to_show1 = "Mercurio"
text_to_show2 = "Venus"
text_to_show3 = "Terra"
text_to_show4 = "Marte"
text_to_show5 = "jupter"
text_to_show6 = "Saturno."
text_to_show7 = "Urano"
text_to_show8 = "Netuno"


#metodo para mostrar texto na tela


cv2.putText(img,
            text_to_Sol,
            (100,80),
            fontFace=cv2.FONT_HERSHEY_PLAIN,
            fontScale=4,
            color = (0,0,255))

cv2.putText(img,
            text_to_show1,
            (109,180),
            fontFace=cv2.FONT_HERSHEY_PLAIN,
            fontScale=1,
            color = (255,255,255))

cv2.putText(img,
            text_to_show2,
            (200,270),
            fontFace=cv2.FONT_HERSHEY_PLAIN,
            fontScale=1,
            color = (255,255,255))

cv2.putText(img,
            text_to_show3,
            (290,270),
            fontFace=cv2.FONT_HERSHEY_PLAIN,
            fontScale=1,
            color = (255,255,255))

cv2.putText(img,
            text_to_show4,
            (380,270),
            fontFace=cv2.FONT_HERSHEY_PLAIN,
            fontScale=1,
            color = (255,255,255))

cv2.putText(img,
            text_to_show5,
            (450,100),
            fontFace=cv2.FONT_HERSHEY_PLAIN,
            fontScale=1,
            color = (255,255,255))

cv2.putText(img,
            text_to_show6,
            (750,90),
            fontFace=cv2.FONT_HERSHEY_PLAIN,
            fontScale=1,
            color = (255,255,255))

cv2.putText(img,
            text_to_show7,
            (970,130),
            fontFace=cv2.FONT_HERSHEY_PLAIN,
            fontScale=1,
            color = (255,255,255))

cv2.putText(img,
            text_to_show7,
            (1120,130),
            fontFace=cv2.FONT_HERSHEY_PLAIN,
            fontScale=1,
            color = (255,255,255))




cv2.imshow("resultado", img)


cv2.waitKey(0)
