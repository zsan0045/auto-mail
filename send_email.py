import os
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header
from email.mime.multipart import MIMEMultipart

# 设置接收人
receiver1 = 'zsan45@163.com'

#发件账号
sender='2013403390@qq.com'

# 此处填写QQ邮箱授权码
password = os.getenv('PASSEORD')

# 设置主题
subject = '测试数据'

# 构建邮件内容
msg = MIMEMultipart()
msg['From'] = formataddr(["测试邮件33", sender])  # 发送人直接在这里设置
msg['To'] = formataddr(["zsan", receiver1])
msg['Subject'] = Header(subject, 'utf-8')

# 邮件正文
msg.attach(MIMEText('这是菜鸟教程Python 邮件发送测试……', 'plain', 'utf-8'))

# 登录邮箱并发送邮件
username = sender


smtp_server = 'smtp.qq.com'
smtp_port = 587
smtp = smtplib.SMTP(smtp_server, smtp_port)
smtp.starttls()

smtp.login(username, password)
smtp.sendmail(username, receiver1, msg.as_string())  # 直接使用登录的用户名发送邮件
smtp.quit()

print("邮件已发送成功")
