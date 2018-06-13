#coding=utf-8
import ConfigParser
import os
import smtplib
import datetime
import time
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.utils import parseaddr, formataddr

def get_config(section, key):
	config = ConfigParser.ConfigParser()
	path = os.path.split(os.path.realpath(__file__))[0] + '/info.conf'
	config.read(path)
	return config.get(section, key)

sender = get_config('address', 'sender')
key = get_config('address', 'key')
host = get_config('address', 'host')
receiver = get_config('address', 'receiver') 

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEMultipart('related') 
message['From'] = Header("章先生~", 'utf-8').encode()#内容中显示的发件人
message['To'] =  Header("收件人哦~", 'utf-8').encode()#内容中显示的收件人
message['Subject'] = Header('I Love You~', 'utf-8').encode()#邮件的题目

msgAlternative = MIMEMultipart('alternative')
message.attach(msgAlternative)
mail_msg = """
<p><p>i love you测试...</p>
<p>图片演示：</p>
<p><img src="cid:image1"></p>
"""
msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))

filename = get_config('image', 'path') + get_config('image', 'name') + '.jpg'
fp = open(filename, 'rb')
image = MIMEImage(fp.read());
fp.close()
image.add_header('Content-ID', '<image1>')
message.attach(image)


while True:
	hour = get_config('time', 'hour')
	minute = get_config('time', 'minute') 
	second = get_config('time', 'second') 
	current_time = time.localtime(time.time()) 
	if ((current_time.tm_hour == int(hour)) and (current_time.tm_min == int(minute)) and (current_time.tm_sec == int(second))):
		try:
			smtpObj = smtplib.SMTP_SSL()#这个点要注意
			smtpObj.connect(host)
			smtpObj.login(sender, key) #邮箱登录
			smtpObj.sendmail(sender, receiver, message.as_string())
			print ("邮件发送成功")
		except smtplib.SMTPException as e:
			print ("Error: 发送邮件产生错误")
			print(e)
	time.sleep(1)
smtpObj.close()
