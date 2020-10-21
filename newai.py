import aiml
import webbrowser as w
import pygame as pg
a = aiml.Kernel()
a.learn('ai.aiml')
a.learn('alice.aiml')
a.learn('astrology.aiml')
a.learn('atomic.aiml')
a.learn('badanswer.aiml')
a.learn('biography.aiml')
a.learn('bot.aiml')
a.learn('bot_profile.aiml')
a.learn('client.aiml')
a.learn('client_profile.aiml')
a.learn('computers.aiml')
a.learn('continuation.aiml')
a.learn('date.aiml')
a.learn('default.aiml')
a.learn('drugs.aiml')
a.learn('emotion.aiml')
a.learn('food.aiml')
a.learn('geography.aiml')
a.learn('gossip.aiml')
a.learn('history.aiml')
a.learn('humor.aiml')
a.learn('imponderables.aiml')
a.learn('inquiry.aiml')
a.learn('interjection.aiml')
a.learn('iu.aiml')
a.learn('junktest.aiml')
a.learn('knowledge.aiml')
a.learn('literature.aiml')
a.learn('loebner10.aiml')
a.learn('money.aiml')
a.learn('movies.aiml')
a.learn('mp0.aiml')
a.learn('mp1.aiml')
a.learn('mp2.aiml')
a.learn('mp3.aiml')
a.learn('mp4.aiml')
a.learn('mp5.aiml')
a.learn('mp6.aiml')
a.learn('music.aiml')
a.learn('numbers.aiml')
a.learn('personality.aiml')
a.learn('phone.aiml')
a.learn('pickup.aiml')
a.learn('politics.aiml')
a.learn('primeminister.aiml')
a.learn('primitive-math.aiml')
a.learn('psychology.aiml')
a.learn('pyschology.aiml')
a.learn('reduction.names.aiml')
a.learn('reduction0.safe.aiml')
a.learn('reduction1.safe.aiml')
a.learn('reduction2.safe.aiml')
a.learn('reduction3.safe.aiml')
a.learn('reduction4.safe.aiml')
a.learn('reductions-update.aiml')
a.learn('religion.aiml')
a.learn('salutations.aiml')
a.learn('science.aiml')
a.learn('sex.aiml')
a.learn('sports.aiml')
a.learn('stack.aiml')
a.learn('stories.aiml')
a.learn('that.aiml')
a.learn('update_mccormick.aiml')
a.learn('update1.aiml')
a.learn('wallace.aiml')
a.learn('xfind.aiml')
while True:
	n = input('enter:')
	if n == 'activate vcmd':
		while True:
			q = input('(vcmd)enter:')
			if q.split()[0] == 'info>':
				print('''#information regarding the app:
			===============================

			navigation: navigate through different folders using the nav bar in the extreme left.
			chatroom  : the chatroom is easy to use and helps you to talk to all active users
			notes     : the notes is still in progress
			goals     : the goals is still in progress
			about us  : know more about or contact us through the links provided.

			#information on special commands:
			==============================

			help> : to search anything online
			web>  : to open a website of your choice
			cf>   : to create different files''')
			elif q.split()[0] == 'help>':
				try: 
				    from googlesearch import search 
				except ImportError:  
				    print("No module named 'google' found") 
				# to search 
				query = q[5:] 
				for j in search(query, tld="co.in", num=10, stop=1, pause=2): 
				    w.open(j)
			elif q.split()[0] == 'web>':
				w.open('http://www.'+q[5:]+'.com')
			elif q.split()[0] == '#emoji':
				pass
			elif q == 'deactivate':
				break
	else:
		print(a.respond(n))