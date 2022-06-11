# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 14:17:44 2022

@author: User
"""

#if Statement
x = 0
y = 5

if x < y:                            # Truthy
    print('yes')

if y < x:                            # Falsy
    print('yes')

if x:                                # Falsy
    print('yes')

if y:                                # Truthy
    print('yes')

if 'aul' in 'grault':                # Truthy
    print('yes')

if 'quux' in ['foo', 'bar', 'baz']:  # Falsy
    print('yes')

##Grouping Statements: Indentation and Blocks
###

if 'foo' in ['bar', 'baz', 'qux']:
    print('Expression was true')
    print('Executing statement in suite')
    print('...')
    print('Done.')
    
print('After conditional')


###
if 'foo' in ['bar', 'baz', 'qux', 'foot']:
    print('Expression was true')
    print('Executing statement in suite')
    print('...')
    print('Done.')
    
print('After conditional')

###

# Does line execute?                        Yes    No
#                                           ---    --
if 'foo' in ['foo', 'bar', 'baz']:        #  x
    print('Outer condition is true')      #  x

    if 10 > 20:                           #  x
        print('Inner condition 1')        #        x

    print('Between inner conditions')     #  x

    if 10 < 20:                           #  x
        print('Inner condition 2')        #  x

    print('End of outer condition')       #  x
print('After outer condition')            #  x


##The else and elif Clauses
###

x = 20

if x < 50:
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')

###
x = 120

if x < 50:
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')
    
###

hargaBuku = 20000
hargaMajalah = 5000
uang = 2000

if uang > hargaBuku:
    print("beli buku")
else:
    print("uang tidak cukup")
    
###
hargaBuku = 20000
hargaMajalah = 5000
uang = 2000

if uang > hargaBuku:
    print("beli buku")
elif uang > hargaMajalah:
    print("beli majalah")
else:
    print("uang tidak cukup")

###
name = 'Hacktiv8'
if name == 'Fred':
    print('Hello Fred')
elif name == 'Xander':
    print('Hello Xander')
elif name == 'Hacktiv8':
    print('Hello Hacktiv8')
elif name == 'Arnold':
    print('Hello Arnold')
else:
    print("I don't know who you are!")
    
###
if 'a' in 'bar':
    print('foo')
elif 1/0:
    print("This won't happen")
elif var:
    print("This won't either")
    
###
if 'f' in 'foo': print('1'); print('2'); print('3')


