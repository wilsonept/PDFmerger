from merger import merge
from sender import send_mail
from receiver import receive_mail

import io, os, imapclient, pyzmail, smtplib, ssl, PyPDF2
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
import config
from config import get_conf

conf_data = get_conf(config)
email = conf_data['email']
password = conf_data['password']
server = conf_data['server']
port = conf_data['port']

subject = 'RE:OCR'
text = 'Check your file at attachment\n\nCreated by automatic python merger\n\nPython Power by Dimkin'
basedir = 'c:\\!git\\PDFmerger\\process\\'
files = ['C:\\!git\\PDFmerger\\process\\combined.pdf']
to = [receive_mail(email, password, basedir)]


merge(basedir)
send_mail(email, to, subject, text, basedir, files, password, server, port)