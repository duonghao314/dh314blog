from sender import Mail, Message


class EMail:
    def __init__(self):
        self.mail = Mail(host='smtp.gmail.com',
                         port=465,
                         username='nhatquang.nv14@gmail.com',
                         password='loveyougirl',
                         use_tls=False,
                         use_ssl=True,
                         debug_level=True)


    def createMail(self, name,comment, email):
        msg = Message()
        sub = 'Comment From dh314Blog '
        msg.fromaddr = ('Đường Hạo', 'nhatquang.nv14@gmail.com')
        msg.subject = sub
        contentE = 'Bạn nhận được một comments từ dh314Blog \n Từ: '+str(name)+'\nEmail: '+str(email)+'\nNội dung: '+str(comment)
        msg.body = contentE
        msg.to = 'nhatquang.nv14@gmail.com'

        return msg
    def sendMail(self, name,comment,email):

            msg = self.createMail(name,comment,email)
            self.mail.send(msg)
            return 'Gửi thành công'

