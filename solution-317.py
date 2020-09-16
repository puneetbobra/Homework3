#Nested Loops
##pattern a
print('(a)')
for a in range(0,10):
    for b in range(0,a+1):
        print('*', end='')
    print('')
print('')
#End pattern a

##pattern b
print('(b)')
for a in range(0,10):
    for b in range(0,10-a):
        print('*', end='')
    print('')
print('')
#End pattern b

#pattern c
print('(c)')
for a in range(0,10):
    for c in range(0,a):
        print(' ', end='')
    for b in range(0,10-a):
        print('*',end='')
    print ('')
print('')
#End pattern c        

#pattern d
print('(d)')
for a in range(0,10):
    for c in range(10-a-1):
        print(' ', end='')
    for b in range(0,a+1):
        print('*', end='')
    print ('')
print('')
#End pattern c       