import io, os, imapclient, pyzmail

def receive_mail(email, password, basedir):

	os.chdir(basedir)

	conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
	conn.login(email, password)
	conn.select_folder(r'INBOX')
	UIDs = conn.gmail_search('has:attachment subject:OCR')

	# принимает только последнее полученое сообщение ! ! !
	rawMessage = conn.fetch([UIDs[-1]], ['BODY[]', 'FLAGS'])
	message = pyzmail.PyzMessage.factory(rawMessage[UIDs[-1]][b'BODY[]'])
	received_from = message.get_address('from')
	attachmentCount = len(message.get_payload())

	for i in range(1, attachmentCount):
		attachment = message.get_payload(i)
		filename = attachment.get_filename()
		newfile = io.open(filename, 'wb')
		newfile.write(message.get_payload(i).get_payload(decode=True))
		newfile.close()
	conn.logout()
	return received_from[0]