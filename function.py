c = {'m': 0, 'i':0, 'p':0, 's':0}
word = 'mississippi'
for i in word:
    if i == 'm':
        c['m'] = c['m']+1
    elif i == 'i':
        c['i'] = c['i']+1
    elif i == 'p':
        c['p'] = c['p']+1
    else:
        c['s'] = c['s']+1
print (c)
