import colorama 
from colorama import * 
class Database: 
    def gravity(): 
        print( Fore.CYAN , 'Gravity is  a Kind of force which Invented by the Sir, Isaac Newton : ')
        print(Fore.GREEN, 'he invented this just seeing the apple , was siting under the apple tree : ')
    def earth(): 
        a= float(input('enter your mass in killogram : '))
        print( f'your gravitational froce in Planet Earth is {a* 9.8 } ')
    def  moon():
        a=  float(input('enter your mass in killogram: '))
        print(f'your gravitational froce in moon is {a *  10 } ')
    def marcay(): 
        a=  float(input('enter your  mass in killogram : '))
        print(f' your gravitational froce in marcay is {a* 12 }  ') 
    def Jupiter(): 
        a=  float(input('enter your  mass in killogram : '))
        print(f' your gravitational froce in Jupiter  is {a* 7  }  ') 
    def stran(): 
        a=  float(input('enter your  mass in killogram : '))
        print(f' your gravitational froce in Starn is {a* 6 }  ') 
    