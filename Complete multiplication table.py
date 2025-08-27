from pystyle import *
print(Box.Lines('[+] Complete multiplication table'))
Write.Print('[-] Complete multiplication table \n ',Colors.purple_to_red, interval=0.1)
print(Box.Lines("<Program>1"))

while True :
    number = int (Write.Input('[+] write your number :',Colors.blue_to_purple , interval=0.1))
    for i in range (1 , 11):
                      print(number, '*',i,'=',number *i)