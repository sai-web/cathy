from random import randint
import webbrowser as w
person = {
	"name":['what your name may','who is are you Jeff','what call you'],
	"age":['how old you','how long lived','what age you'],
	"bot":['what do are you','what your job','can help me'],
	"creator":['who made you','who you creat','who Sai about is'],
	"app":['what this more about app','how use work app','update on in app'],
	"place":['where you from live born','which country you','what national you']
}
qna = {
	"greet":["hey there",'how are you','hello']
}
lm = ['name','age','bot','creator','app','place']
qm = ['greet']
responses = {
	"name":["Hey there I'm Jefferey","You can call me Jeff","call me Jeff"],
	"age":["I've not lived for long","I'm pretty young if you ask me","I'm 1 day old"],
	"bot":["I'm a bot","I'm basially jobless","I am programmed to help you complete your tasks"],
	"creator":['Sai created me','I was made by Sai','Sai is a student at OOW'],
	"app":['this is an app made for guiding your day-to-day tasks','the app has a lot of features.Type (info>) for more information','New features will be added by September, for more info visit our website'],
	"place":["I'm from India","I was born in India, but live in UAE","I'm considered Indian though I was built in UAE atleast that's what he said."]
}
while True:
	n = input('enter')
	thrust = 0
	iterate = 0
	p = randint(0,1)
	if n.split()[0] == 'help>':
		if n[5] != ' ':
			w.open(n[5:])
			thrust = 2
		else:
			w.open(n[6:])
			thrust = 2
	elif n.split()[0] == 'web>':
		if n[4] == ' ':
			w.open('http://www.'+n[5:]+'.com')
			thrust = 2
		else:
			w.open('http://www.'+n[4:]+'.com')
			thrust = 2
	elif n.split()[0] == 'info>':
		thrust = 2
		print('''#information regarding the app:
	===============================

	navigation: navigate through different folders using the nav bar in the extreme left.
	chatroom  : the chatroom is easy to use and helps you to talk to all active users
	notes     : the notes is still in progress
	goals     : the goals is still in progress
	about us  : know more about or contact us through the links provided.

	#information on special usage:
	==============================

	help> : to search anything online
	web>  : to open a website of your choice''')
	elif n == 'quit':
		break
	else:
		for i in person.values():
			if 'may i know' in n:
				thrust += 1
			for j in i:
				thrust = 0
				if n == j:
					thrust = 2
					if person[lm[iterate]][2].split()[1] in n:
						thrust = 2
						print(responses[lm[iterate]][2])
						#continue
					else:
						print(responses[lm[iterate]][p])
						thrust = 2
						#continue
				else:
					for k in j.split():
						if k in n:
							thrust += 1
						if thrust > 2:
							if person[lm[iterate]][2].split()[1] in n:
								print(responses[lm[iterate]][2])
								thrust = 2
								#continue
							else:
								print(responses[lm[iterate]][p])
								thrust = 2
								#continue
			iterate +=1
		else:
			for i in qna.values():
				for j in i:
					if n == j:
						print('Hello Sai!')
					else:
						for k in j.split():
							if k in n:
								print('Hello Sai!')
								break
		if thrust <= 2:
			print("I'm not sure about that!!")