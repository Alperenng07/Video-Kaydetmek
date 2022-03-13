# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 14:09:20 2022

@author: alper
"""

import cv2

# "0" çalıştıracağınız kameranın indeksidir eğer harici farklı kameralar tanımlıysa "1" yazmalısınız.
cam = cv2.VideoCapture(0)


fourrc= cv2.VideoWriter_fourcc(*'XVID')
out= cv2.VideoWriter("droneGrey.avi",fourrc,30.0,(640,480))

while cam.isOpened():
    ret,frame=cam.read()
    
    if not ret:
        print("kameradan görüntü alınamadı")
        break
    
    out.write(frame)
#Kayıt başlamasına rağmen kameranın neyi gösterdiğini görmek için yazdım eğer siz istemezseniz bu satırı kaldırabilirsiniz
    cv2.imshow("kamera",frame)
    
    
   if cv2.waitKey(1)==ord("q"):
        print("videdan ayrıldınız")
        break
# İşlem tamamlandığında kayıttan sonra kamera ve tüm pencereler kapatılır.    
cam.release()
out.release()
cv2.destroyAllWindows()