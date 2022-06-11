#Código que modifica uma coleção sobre a qual está iterando pode ser inseguro. No lugar disso, usualmente você deve iterar sobre uma cópia da coleção ou criar uma nova coleção

#Strategy: Iterate over a copy 
for user status in users.copy().items():
    if status == 'inactivea':
        del users[user]

#Strategy: Create a new collection 
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status 
