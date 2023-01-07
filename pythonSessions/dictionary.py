creds={"UserName":"Jothi","Password":"XXXX"}
print(creds['UserName'])

print(creds.get('UserName'))

print(creds.values())

print(type(creds.values()))

print(creds.keys())

print(creds.items())

creds['Connection']='ADW'

creds.update({'Connection':'ADW UAT'})

for i in creds.items():
    print(i)

creds1=creds.copy()
print(creds1)

creds.pop('Connection')
print(creds)

creds1.popitem()
print(creds1)
