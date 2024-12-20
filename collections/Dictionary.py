actions = {'r':1,'l':-1}

print(actions.get("l"))
actions['u'] = 1
print(actions)

print(actions.values())
print(actions.keys())
print(actions.items())
del(actions['u'])
print(actions)