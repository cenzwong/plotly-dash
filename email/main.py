import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

import imaplib
import base64
import os

from email.header import decode_header

class Email:

    """A simple example class"""
    subject = ""
    sender_email = ""
    sender_pass = ""
    receiver_email = ""
    body_text = ""

    def sendEmail_withAttachment(self,attachmet_path_image):
        # Create a multipart message and set headers
        #message = MIMEMultipart()
        message = MIMEMultipart("alternative")
        message["From"] = self.sender_email
        message["To"] = self.receiver_email
        message["Subject"] = self.subject

        # Add body to email
        message.attach(MIMEText(self.body_text, "plain"))
        
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(attachmet_path_image, "rb").read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename='+attachmet_path_image)
        message.attach(part)

        text = message.as_string()

        # Log in to server using secure context and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(self.sender_email, self.sender_pass)
            server.sendmail(self.sender_email, self.receiver_email, text)

    def sendMail(self):
        #Setup the MIME
        message = MIMEMultipart()
        message['From'] = self.sender_email
        message['To'] = self.receiver_email
        message['Subject'] = self.subject   #The subject line
        #The body and the attachments for the mail
        message.attach(MIMEText(self.body_text, 'plain'))
        #Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session.starttls() #enable security
        session.login(self.sender_email, self.sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(self.sender_email, self.receiver_email, text)
        session.quit()
    
    def dowloadAllAttachmentfrom(self, emailFolder):
        if emailFolder == "inbox":
            print("WARNING: INBOX is not allows because you will mess up your system")
            print("WARNING: recommend you open a folder call python to play around with")
            return 0
        port = 993
        email_user = self.sender_email
        email_pass = self.sender_pass
        mail = imaplib.IMAP4_SSL("imap.gmail.com",port)
        mail.login(email_user, email_pass)
        mail.select(emailFolder)

        status, data = mail.search(None, 'ALL')
        mail_ids = data[0]
        id_list = mail_ids.split()

        for num in data[0].split():
            typ, data = mail.fetch(num, '(RFC822)' )
            raw_email = data[0][1]
        # converts byte literal to string removing b''
            raw_email_string = raw_email.decode('utf-8')
            email_message = email.message_from_string(raw_email_string)
        # downloading attachments
            for part in email_message.walk():
                # this part comes from the snipped I don't understand yet... 
                if part.get_content_maintype() == 'multipart':
                    continue
                if part.get('Content-Disposition') is None:
                    continue
                fileName = part.get_filename()
                if bool(fileName):
                    filePath = os.path.join('./', fileName)
                    if not os.path.isfile(filePath) :
                        fp = open(filePath, 'wb')
                        fp.write(part.get_payload(decode=True))
                        fp.close()
                    subject = str(email_message).split("Subject: ", 1)[1].split("\nTo:", 1)[0]
                    # print('Downloaded "{file}" from email titled "{subject}".'.format(file=fileName, subject=subject))

    def deleteAllMailfrom(self, emailFolder):
        if emailFolder == "inbox":
            print("WARNING: INBOX is not allows because you will mess up your system")
            print("WARNING: recommend you open a folder call python to play around with")
            return 0
        # create an IMAP4 class with SSL 
        imap = imaplib.IMAP4_SSL("imap.gmail.com")
        # authenticate
        imap.login(self.sender_email, self.sender_pass)

        # select the mailbox I want to delete in
        # if you want SPAM, use imap.select("SPAM") instead
        imap.select(emailFolder)

        # to get all mails
        status, messages = imap.search(None, "ALL")
        messages = messages[0].split(b' ')

        for mail in messages:
            _, msg = imap.fetch(mail, "(RFC822)")
            # you can delete the for loop for performance if you have a long list of emails
            # because it is only for printing the SUBJECT of target email to delete
            for response in msg:
                if isinstance(response, tuple):
                    msg = email.message_from_bytes(response[1])
                    # decode the email subject
                    subject = decode_header(msg["Subject"])[0][0]
                    if isinstance(subject, bytes):
                        # if it's a bytes type, decode to str
                        subject = subject.decode()
                    print("Deleting", subject)
            # mark the mail as deleted
            imap.store(mail, "+FLAGS", "\\Deleted")

        # permanently remove mails that are marked as deleted
        # from the selected mailbox (in this case, INBOX)
        imap.expunge()
        # close the mailbox
        imap.close()
        # logout from the account
        imap.logout()
        
        
        
        
# ===== Program Start ======
myMail = Email()
myMail.subject = "This is my Subject"
myMail.receiver_email = "myMail@gmail.com"
myMail.sender_email = "myMail@gmail.com"
myMail.sender_pass = "12345678"
myMail.body_text = "This is the Body Text"
# myMail.sendEmail_withAttachment("image4.png")
# myMail.sendMail()

myMail.dowloadAllAttachmentfrom("python")
myMail.deleteAllMailfrom("python")
