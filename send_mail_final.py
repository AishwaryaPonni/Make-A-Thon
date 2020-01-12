import random
import smtplib
from PIL import Image
import PIL
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

import xlrd
workbook = xlrd.open_workbook('data.xls')
sheet = workbook.sheet_by_index(0)
name ="Aishu"
email1 = ""
for i in [0, 1, 2, 3]:
	retname = sheet.cell_value(i,0)
	if name == retname:
		email1 = str(sheet.cell_value(i,1))

import os
import qrcode
import os.path
from os import path
img=qrcode.make('Room1')

img=img.save('room_1.jpg')
img_data=open('room_1.jpg','rb').read()
image=MIMEImage(img_data,name=os.path.basename('room_1.jpg'))
msg=MIMEMultipart()
msg.attach(image)
print(path.exists("room_1.jpg"))


s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login("lightwood1298@gmail.com","indu@1234")

s.sendmail("lightwood1298@gmail.com",email1,msg.as_string())
s.quit()




