# -*- coding: UTF-8 -*-

from fbchat import Client
from fbchat.models import *

mail=input('Saisir votre adresse mail : ')
mdp=input('Saisir votre mot de passe : ')

print('\n') #saut ligne
## debugg 

print('mail = ', mail)
print ('mdp = ', mdp)

print('\n') #saut ligne

client = Client(mail, mdp)

users = client.fetchAllUsers()
print (users)

#print("les id: {}".format(client.uid))

client.logout()
