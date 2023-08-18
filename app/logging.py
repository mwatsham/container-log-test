import sys, platform, time
from datetime import datetime
 
stdout_txt = "{} - This is STDOUT from {}"
stderr_txt = "{} - This is STDERR from {}"
host = platform.node()
 
while True:
  dateTimeObj = datetime.now()
  timestamp = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
 
  print (stdout_txt.format(timestamp,host))
  print (stderr_txt.format(timestamp,host))
 
  time.sleep(1)
 
exit()
