#coding=utf-8
import smtplib
import datetime
import time
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.utils import parseaddr, formataddr

def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr(( \
		Header(name, 'utf-8').encode(), \
		addr.encode('utf-8') if isinstance(addr, unicode) else addr))

sender = '191543154@qq.com' #发件人的邮件地址
password='ctxsqwdenulsbieh'#发件人的客户端密码
host='smtp.qq.com'#发件人用的邮件服务器
receivers = ['21530084@zju.edu.cn']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

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

file1 = "test.jpg"
fp = open(file1, 'rb')
image = MIMEImage(fp.read());
fp.close()
image.add_header('Content-ID', '<image1>')
message.attach(image)
while True:
	hour=23
	minute = 12
	second = 00
	current_time = time.localtime(time.time()) 
	if ((current_time.tm_hour == hour) and \
			(current_time.tm_min == minute) and \
			 (current_time.tm_sec == second)):

		try:
			smtpObj = smtplib.SMTP_SSL()#这个点要注意
			smtpObj.connect(host)
			smtpObj.login(sender,password) #邮箱登录
			smtpObj.sendmail(sender, receivers, message.as_string())
			print ("邮件发送成功")
		except smtplib.SMTPException as e:
			print ("Error: 发送邮件产生错误")
			print(e)
	time.sleep(1)
smtpObj.close()

