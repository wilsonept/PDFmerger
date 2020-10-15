import smtplib
import ssl
import os
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

print('If it fails check your google settings at: \
https://myaccount.google.com/lesssecureapps\
or at: \
https://myaccount.google.com/apppasswords')

def send_mail(send_from, send_to, subject, text, basedir, files=None, password, server='smtp.gmail.com', port=465):
	assert isinstance(send_to, list)

	os.chdir(basedir)

	msg = MIMEMultipart()
	msg['From'] = send_from
	msg['To'] = COMMASPACE.join(send_to)
	msg['Date'] = formatdate(localtime=True)
	msg['Subject'] = subject

	msg.attach(MIMEText(text))

	for f in files or []:
		with open(f, "rb") as fil:
			part = MIMEApplication(
				fil.read(),
				Name=basename(f)
				)

		# After the file is closed
		part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
		msg.attach(part)
		
	context = ssl.create_default_context()
	conn = smtplib.SMTP_SSL('smtp.gmail.com', port, context=context)
	conn.login(send_from, password)
	conn.sendmail(send_from, send_to, msg.as_string())
	conn.close()

	print('Message have been sent')

