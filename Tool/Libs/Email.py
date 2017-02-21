
import imaplib
import email
import re
from email.header import decode_header
import time 

class Email:
    def __init__(self):
        self.conn = None

    def connect_to_email(self, username, password, domain = 'imap.gmail.com'):
        self.conn = imaplib.IMAP4_SSL(domain)
        self.conn.login(username, password)

    def close_connection (self):
        self.conn.close()
        self.conn.logout()
        
    def get_all_links(self, index=-1, label='inbox'):        
        #select label
        self.conn.list()
        self.conn.select(label)

        result, data = self.conn.uid('search', None, "ALL")      
        try:
            email_uid = data[0].split()[index]
        except IndexError:
            return None 
        result, email_data = self.conn.uid('fetch', email_uid, '(RFC822)')
        raw_email = email_data[0][1]
        
        raw_email_string = raw_email.decode('utf-8')
        email_message = email.message_from_string(raw_email_string)
        for part in email_message.walk():
            if part.get_content_type() == "text/html":
                body = part.get_payload(decode=True)
                save_string = ""
                save_string+=body.decode('utf-8')
            else:
                continue

        urls = re.findall(r'href=[\'"]?([^\'" >]+)', save_string)
        return urls


    def get_body_content(self, index=-1, label='inbox'):
        #select label
        self.conn.list()
        self.conn.select(label)

        result, data = self.conn.uid('search', None, "ALL")      
        try:
            email_uid = data[0].split()[index]
        except IndexError:
            return None 
        result, email_data = self.conn.uid('fetch', email_uid, '(RFC822)')
        raw_email = email_data[0][1]
        
        raw_email_string = raw_email.decode('utf-8')
        email_message = email.message_from_string(raw_email_string)
        for part in email_message.walk():
            if part.get_content_type() == "text/html":
                body = part.get_payload(decode=True)
                save_string = ""
                save_string+=body.decode('utf-8')
            else:
                continue      
        return save_string

    def get_email_subject(self, index=-1, label='inbox'):
        #select label
        self.conn.list()
        self.conn.select(label)

        result, data = self.conn.uid('search', None, "ALL")
        try:
            email_uid = data[0].split()[index]
        except IndexError:
            return None
        result, email_data = self.conn.uid('fetch', email_uid, '(RFC822)')
        raw_email = email_data[0][1]
        
        raw_email_string = raw_email.decode('utf-8')
        email_message = email.message_from_string(raw_email_string)

        subject = decode_header(email_message['Subject'])        
        return subject[0][0]
    
    def delete_all_email (self, label='inbox'):
        #select label
        self.conn.list()
        self.conn.select(label)

        self.conn.recent()
        result, data = self.conn.search(None, "ALL") 
        for email_uid in data[0].split():
            self.conn.store(email_uid, '+FLAGS', '\\Deleted')
##            self.conn.expunge()

    def check_email_content(self, expected_content, compare_type=0, index=-1, label='inbox'):
        res = ''
        #compare type = 0: ralative comparition (check if content contains expected string)
        if(compare_type == 0):
            ## To fix case having 2 or more emails in mailbox ==> cannot get the expected email correctly,
            ## Mr Nguyen assumes subject is correct and do not need to check.
            ## I will base on expected subject to find expected email.
            index = self.get_email_index_by_subject(expected_content['subject'])
            
            actual_subject = self.get_email_subject(index, label)            
            if not expected_content['subject'] in actual_subject: res+='\n+ Subject does NOT match! Actual subject: ' + actual_subject + '.' 

            actual_body = self.get_body_content(index, label)
            #print actual_body
            for item in expected_content['body']:
                if not item in actual_body: res+='\n+ Body does NOT contain "' + item + '".'

##            if (res != ''):
##                raise AssertionError(res)
            return res

        #compare_type = 1: absolute comparition (exactly the same)
        elif(compare_type == 1):
            print 'to be implemented'    
            return 'Function is being implemented, please choose compare_type = 0'
            
        else:
            return 'Invalid value for 2nd argument (compare_type)'

    def get_a_link_in_email(self, expected_link, index=-1, label='inbox'):
        tmpList = self.get_all_links(index, label)
        
        #Because ride always passes unicode to fuction, so i have to cast:
        try:
            expected_link = int(expected_link)
        except ValueError:
            expected_link = str(expected_link)

        if(type(expected_link) == int):
            try:
                return tmpList[expected_link]
            except IndexError:
                print 'Invalid value for 1st argument "expected_link"!'
                return None
        elif(type(expected_link) == str or type(expected_link) == unicode):
            try:
                for item in tmpList:
                    if expected_link in item: return item
            except:
                return None
        else:
            print 'Unexpected argument type: ' + type(expected_link)
            return None


    def get_unseen_emails(self, label = 'inbox'):
        #select label
        self.conn.list()
        self.conn.select(label)

        result, data = self.conn.uid('search', None, "UNSEEN")
        return data[0].split()

    def wait_for_email(self, timeout=120, time_step=30):
        """@Edited by Minh.nguyen
        By default, if user inputs incorrect timeout, time_step, this keyword will assigned 120 to timeout, 30 to time_step

        """
        try:
            timeout = int(timeout)
        except:
            timeout = 120
        
        try:
            time_step = int(time_step)
        except:
            time_step = 30

        while(timeout >= time_step):            
            self.conn.recent()
            if len(self.get_unseen_emails()) > 0:
                return -1
            time.sleep(time_step)
            timeout -= time_step

        if(timeout >= 0):
            time.sleep(timeout)
            self.conn.recent()
            if len(self.get_unseen_emails()) > 0:
                return -1
            
        raise AssertionError('No email arrives!')
        
    def get_email_index_by_subject(self, subject, label = 'inbox'):
        self.conn.list()
        self.conn.select(label)

        #Matched email
        result, data = self.conn.uid('search', None, '(HEADER Subject "' + subject + '")')
        ##All email
        result, data2 = self.conn.uid('search', None, "ALL")
        
        return data2[0].split().index(data[0].split()[0])
        
            
            

##ex = {'body': ['capital.TXT', 'View This File'], 'subject': 've shared a file with you'}     
##
##a= Email()
##a.connect_to_email('fsauto003@gmail.com', '1qazxsw2@')
##b = a.get_a_link_in_email('verification')
##a.delete_all_email()
##a.close_connection()

##b = a.get_email_subject()
##b = a.get_email_index_by_subject('ve shared a file with you')
##b = a.check_email_content(ex)
##
##print b


##
##a= Email()
##a.connect_to_email('autotest.filestring@gmail.com', 'FS@123456')
##b = a.wait_for_email()
##print b        
##raw_input('End...')

