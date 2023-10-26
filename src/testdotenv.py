from dotenv import dotenv_values

secrets=dotenv_values('h.env')
email=secrets['EMAIL']
passwd=secrets['PASSWD']

print(email)