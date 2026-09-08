import getpass

username = 'maezerus'
password = 'taekabata'

un = input('Input Username ---> ')
p = getpass.getpass('Input Username ---> ') 

if username == un and p == password :
        print("ACESS GRANTED")
else :
        print("ACESS DENIED")