


import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login("lightwood1298@gmail.com","indu@1234")
message="Hello";
s.sendmail("lightwood1298@gmail.com","aishuponni2k@gmail.com",message)
s.quit()
