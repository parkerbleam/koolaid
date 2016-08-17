import smtplib

username = 'bleam.parker@gmail.com'
password = '***REMOVED***'
fromaddr = 'bleam.parker@gmail.com'
toaddrs = '***REMOVED***@txt.att.net'

msg = '\nHELLO'

server = smtplib.SMTP("smtp.gmail.com:587")
server.starttls()
server.login(username, password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
