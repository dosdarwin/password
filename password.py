password = input('please type in password:')
x = 2
while True:	
	if password == ('a123456'):
		print('log in succeed!!!!!!!!!!')
		break
	elif x > 0:
		print("log in fail!!!!!!!!!!" , "you have ", x , "chance left")
		password = input('please type in password:')
		x = x - 1
	else:
		print('you have no more chance!!!!!!!!!!!')
		break