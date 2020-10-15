from merger import merge
from sender import send_mail
from receiver import receive_mail

import io, os, imapclient, pyzmail, smtplib, ssl, PyPDF2
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate



email = 'wilsonept@gmail.com'
#to = ['wilsonept@gmail.com']
subject = 'RE:OCR'
text = 'Check your file at attachment\n\nCreated by automatic python merger\n\nPython Power by Dimkin'
basedir = 'c:\\!git\\PDFmerger\\process\\'
files = ['C:\\!git\\PDFmerger\\process\\combined.pdf']
password = 'wsrjejcckmkdmoug'
server = 'smtp.gmail.com'
port = 465


to = [receive_mail(email, password, basedir)]
merge(basedir)
send_mail(email, to, subject, text, basedir, files, password, server, port)