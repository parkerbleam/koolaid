import smtplib

username = 'email'
password = 'password'
fromaddr = 'email'
toaddrs = 'phone-num@txt.att.net'

msg = '\nHELLO'

server = smtplib.SMTP("smtp.gmail.com:587")
server.starttls()
server.login(username, password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
