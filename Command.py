import webbrowser
import os
import json

print('''   __  __                      _     _                       
 |  \/  |       /\           (_)   | |                      
 | \  / |_ __  /  \   ___ ___ _ ___| |_ __ _ _ __   ___ ___ 
 | |\/| | '__|/ /\ \ / __/ __| / __| __/ _` | '_ \ / __/ _ \
 | |  | | |_ / ____ \\__ \__ \ \__ \ || (_| | | | | (_|  __/
 |_|  |_|_(_)_/    \_\___/___/_|___/\__\__,_|_| |_|\___\___|
                                                            
 \n''')

lists = ['Search','Help','Updates','Calculator','IPTrack']
print(lists)
command = input("\nCommand: ")

if command == 'Search':
        print("What would you like to search?")
        search = input("Search: ")
        webbrowser.open('https://google.com/?#q=' + search)
elif command == 'Help':
        print("Don't know what to do? Just type what you want from the list! Also you can speak with me just say hello or how are you an I will respond! Enjoy!")
elif command == 'Updates':
    print("You may be wondering why there is a short amount of commands well don't worry! More updates to come!")
    print('''
Updates!
Generating exploits or along with hacking!
Opening files and applications!
Games to play
And much! much! more! ''')

elif command == 'Calculator':
    num1 = float(input("Enter a number: "))
    math = input("Enter a operator: ")
    num2 = float(input("Enter a number: "))

    if math == "+":
        print(num1+num2)
    elif math == "-":
        print(num1-num2)
    elif math == "*":
        print(num1*num2)
    elif math == "/":
        print(num1/num2)
        
if command == 'IPTrack':
    ip = input("IP of target or yourself: ")
    url = ("http:ip-api.com/")
    response = webbrowser.open(url + ip)


if command == 'Hello':
        print("Mr.Assistant: Hello! how are you?")
        answer = input("Good or bad?: ")
elif answer == 'Good':
        print("Mr.Assistant: Awesome me too!")
elif answer == 'Bad':
        print("Mr.Assistant: Sorry to hear! Feel better.")
else:
    print("Not the answer I was looking for!")

        
        

