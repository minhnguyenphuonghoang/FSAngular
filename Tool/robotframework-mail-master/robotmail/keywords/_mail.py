from keywordgroup import KeywordGroup
import imaplib
import time
from bs4 import BeautifulSoup
import base64
import re

class _MailKeywords(KeywordGroup):

	def __init__(self):
		i = 0

	def open_mailbox(self, server, user, pwd, ssl=False, port=993):
		"""
		Connect to mailbox using given arguments.
		"""
		if ssl:
			self.mailbox = imaplib.IMAP4_SSL(server, port)
		else:
			self.mailbox = imaplib.IMAP4(server, port)
		self.mailbox.login(user, pwd)
		self.mailbox.select()

	def close_mailbox(self):
		self.mailbox.close()

	def get_unread_email(self, email=None):
		"""
		Gets unread mails send to mailbox from `email`. If `email` is 'None'
		it gets all unread emails.

		Returns list of numbers, you can use them to retrive data from emails with
		other keywords.
		"""
		return self._get_emails(email)

	def wait_for_mail(self, timeout=120,email=None):
		"""
		Waits until unread email(s) show up. Note that it will exit at once if there is a
		unread email already in mailbox.

		It will return number of first (ussualy oldest) unread mail.

		If it will reach `timeout` (`timeout` is in seconds) before unread email shows up it fails.

		It will check for new emails every 5 seconds. (However if left timeout is lower than 5 seconds
		it will wait for value of timeout)


		If `email` is given it checks from  emails send to mailbox from `email`. If `email` is 'None'
		it checks for all unread emails.
		"""
		

		timeout = int(timeout)

		

		while (timeout >= 5):
			self.mailbox.recent()
			emails = self._get_emails(email)
			if len(emails) > 0:
				return emails[0]
			time.sleep(5)
			timeout = timeout - 5

		if timeout > 0:
			time.sleep(timeout)


		self.mailbox.recent()
		emails = self._get_emails(email)
		if len(emails) > 0:
			return emails[0]

		raise AssertionError("No mail found. Timeleft: " + str(timeout))       



	def mark_email_as_read(self, email=None):
		"""
		Marks email(s) as read.

		If `email` is number it marks email with that number as read, 
		if `email` is 'None' then it marks all unread emails as read,otherwise
		it searches for emails recived from `email` and marks them as read.

		"""

		if isinstance(email, int) and email is not None: 
			self.mailbox.store(email,'+FLAGS','\Seen')
		else:
			emails = self._get_emails(email)
			for num in emails:
				self.mailbox.store(num,'+FLAGS','\Seen')
	

	def delete_all_emails(self):
		"""
		Delete email(s).
		Attention: this keyword will delete all emails!!!

		"""
		result, list_of_email_id = self.mailbox.search(None, 'ALL')
		
		list_of_email_id = list_of_email_id[0].split()
		
		for an_email_id in list_of_email_id:
			self.mailbox.store(an_email_id,'+FLAGS','\\Deleted')


	def get_all_links_from_email(self, email):
		"""
		Parses email in search of links and returns
		list of found links.

		It marks email as read in the proccess.
		"""
		links = []
		soup = BeautifulSoup(self.get_body_from_email(email))
		for link in soup.find_all('a'):
			links.append(link.get('href'))

		return links


	def get_body_from_email(self, email):
		"""
		Get email body from email. This function will 
		decode your email body if it was encoded.
		The return value will be email's html format.

		It marks email as read in the process.
		"""
		mail_body = self.mailbox.fetch(email, '(BODY[TEXT])')[1][0][1]
		
		if "Content-Transfer-Encoding: base64" in mail_body \
			or "Content-Transfer-Encoding:base64" in mail_body:
			
			mail_body = mail_body.replace('\r','')
			mail_body = mail_body.replace('\n','')
			mail_body = re.sub('(--===============[\d]*==[-]*)', '', mail_body)
			mail_body = re.sub('Content-Type:[\w\W]*Content-Transfer-Encoding:[\s]*base64', '', mail_body)
			mail_body = base64.b64decode(mail_body)

		return mail_body


	def get_text_from_email_body(self, email):
		"""
		Get text from mail body. This function will get mail body in html
		and convert to text using BeautifulSoup
		"""

		
		

	def _get_emails(self, email):
		if email is None:
			r, item = self.mailbox.search(None, 'UNSEEN')
		else:
			r, item = self.mailbox.search(None, 'UNSEEN', 'FROM', email)

		return   item[0].split()
