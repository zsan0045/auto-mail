import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
import schedule
import time

# 配置信息
SMTP_SERVER = 'smtp.example.com'  # SMTP 服务器地址，例如 'smtp.gmail.com'
SMTP_PORT = 587  # SMTP 端口号
EMAIL_ADDRESS = 'your_email@example.com'  # 发件人邮箱地址
EMAIL_PASSWORD = 'your_password'  # 发件人邮箱密码或授权码

# 定义发送邮件的函数
def send_email(to_address, subject, body):
    try:
        # 创建邮件
        msg = MIMEMultipart()
        msg['From'] = formataddr(("Your Name", EMAIL_ADDRESS))
        msg['To'] = to_address
        msg['Subject'] = subject

        # 邮件正文
        msg.attach(MIMEText(body, 'plain'))

        # 连接到 SMTP 服务器并发送邮件
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()

        print(f"邮件已成功发送到 {to_address}")
    except Exception as e:
        print(f"邮件发送失败: {e}")

# 定时任务示例：每天发送邮件
def schedule_email():
    to_address = 'recipient@example.com'  # 收件人邮箱
    subject = '每日问候'
    body = '这是自动发送的邮件内容。祝您有美好的一天！'

    send_email(to_address, subject, body)

# 设置定时任务：每天早上9点执行
schedule.every().day.at("09:00").do(schedule_email)

# 保持脚本运行
print("开始定时邮件服务...")
while True:
    schedule.run_pending()
    time.sleep(1)
