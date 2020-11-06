from flask_mail import Message
from app import mail,app
from flask import render_template
from threading import Thread

#防止應用變慢 使用python的一部方法 啟動一個後臺progress將比開始一個全新的progress需要資源少得多
#手動創建應用的context 因為要使用progress
#因為FLASK-MAIL的config儲存在app.config裡面
def send_async_mail(app, msg):
    #使用with app.app_context()調用創建的應用上下文，
    #使應用實例可以透過來自FLASK的current_app變量進行訪問
    with app.app_context():
        mail.send(msg)

def send_mail(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    # mail.send(msg)
    #改成異步方法 開啟progress,電子郵件會在progress中運行
    #progress完成時 progress會自行清理
    Thread(target=send_async_mail, args=(app, msg)).start()

def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email('[Microblog] Reset Your Password',
               sender=app.config['ADMINS'][0],
               recipients=[user.email],
               text_body=render_template('email/reset_password.txt',
                                         user=user, token=token),
               html_body=render_template('email/reset_password.html',
                                         user=user, token=token))