import smtplib
import sys
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def notify():
   fromaddr = "tylerhhorton@gmail.com"
   toaddr = input_var
   msg = MIMEMultipart()
   msg['From'] = fromaddr
   msg['To'] = toaddr
   msg['Subject'] = "Motion deteted at the front door"

   body = "Frog.txt"
   msg.attach(MIMEText(body, 'plain'))

   server = smtplib.SMTP('smtp.gmail.com', 587)
   server.ehlo()
   server.starttls()
   server.login(fromaddr, "ugoxiuvrhjopmptd")
   text = msg.as_string()
   server.sendmail(fromaddr, toaddr, text)
   server.quit()

global input_var

input_var = raw_input("Please enter a phone number or an email address: ")

print "We will notify", str(input_var), "thank you."

notify()
