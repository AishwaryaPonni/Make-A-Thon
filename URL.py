
import urllib
#import urllib.request

output = "test.xls"
#url = "https://drive.google.com/file/d/1CPrdC94SOgOVsxLzsB6D1gv1j5z_Zm0b/view?usp=sharing"
#url= "https://drive.google.com/open?id=1CPrdC94SOgOVsxLzsB6D1gv1j5z_Zm0b"
url="https://docs.google.com/spreadsheets/u/1/d/1BLD4KTxpGOIQLWwkew9HDRvKGC4WNRbOscWAm-B1f80/edit?usp=drive_web&ouid=103311423293150964696"
urllib.urlretrieve(url,output)
