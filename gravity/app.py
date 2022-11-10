import database 
from database import Database 
import sys 
from sys import * 
import colorama 
from colorama import Fore 
print(' -------  Gravity meter--------: ')
print('=====welcome , to Gravity meter _=============: ')
print(' in this app we will measure the gravitational force of yours  in diffrent planet-----')
print( ' what you want for , 1. what is Gravity ? \n 2. Measure Earth Gravitational Force \n 3.Measure Moon  Gravitational Force  \n 4.Measure mercary Gravitational Force \n 5.Measure Jupiter  Gravitational Force \n  6.  Measure stran  Gravitational Force \n 7.exit')

a=  int(input('enter your response : '))
if a== 1 : 
    b=  Database.gravity()
    print(b)
elif a== 2: 
    c= Database.earth()
elif a== 3 : 
    ca= Database.moon()
elif a== 4 : 
    cq=  Database.marcay()
elif a==  5 : 
    ce= Database.Jupiter()
elif a==  6: 
    cs=  Database.stran()
elif a==  7 : 
     sys.exit()
else: 
    print(Fore.RED , ' Invalid Input : ')
    