'''
Created on 2013. 10. 8.

@author: azzrael'''


        
import smtplib  
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText  



class MailManager(object):      
   
    MAIL_ACCOUNT = "hancue-build-machine@npluto.com"
    MAIL_PASSWORD = "1111111"   
    MAIL_TO = ["cho415@npluto.com","shwlstjr@npluto.com", "inthebox2@npluto.com", "burninghuny@npluto.com", "azzrael@npluto.com"]    
    #MAIL_TO = ["azzrael@npluto.com"]     
     
    
    def __init__(self):
        pass
    
    @classmethod
    def send_via_gmail_all(thisClass, title, description):   
        for mailTo in thisClass.MAIL_TO :
            thisClass.send_via_gmail(mailTo, title, description)
            
    
    @classmethod  
    def get_message_formatted(thisClass, from_address, to, title, description):  
        msg = MIMEMultipart('localhost')  
        msg['Subject'] = title  
        msg['From'] = from_address  
        msg['To'] = ', '.join(to)  
      
        content = MIMEText(description, 'plain', _charset="utf-8")  
        msg.attach(content)  
        return msg  
    
    @classmethod  
    def send_via_gmail(thisClass, to, title, description):  
        """ 
        send e-mail via a gmail server 
        param to: list of e-mail addresses 
        param title: subject of a mail 
        param description: content of a mail 
        """  
        from_address = thisClass.MAIL_ACCOUNT  
        msg = thisClass.get_message_formatted(from_address, to, title, description)  
      
        try:  
            #s = smtplib.SMTP('smtp.gmail.com:587') # port 465 or 587
            s = smtplib.SMTP('i.npluto.com:25') # port 25
            s.starttls()  
            #s.login(thisClass.MAIL_ACCOUNT, thisClass.MAIL_PASSWORD)  
            s.sendmail(from_address, to, msg.as_string())  
            s.quit()  
        except:  
            print( "error: failed to send a mail" ) 
    
    

        