## pip install yagmail
## https://www.cnblogs.com/fnng/p/7967213.html

import yagmail

# 链接邮箱服务器
yag = yagmail.SMTP(user="user@126.com", password="1234", host='smtp.126.com')
# 收件人
mail_to = ["ccccc@qq.com", "ddddd@qq.com"]
# 邮箱标题
subject = ['我是标题']
# 邮箱正文
contents = [
    '我是正文', 'You can find an audio file attached.', '/local/path/song.mp3'
]
# 邮箱附件
extra_file = ['/tmp/readme.md', '/tmp/test.txt']

# 发送邮件
yag.send(mail_to, subject, contents, extra_file)
