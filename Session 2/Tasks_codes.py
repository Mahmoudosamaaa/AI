# Task(1)
n = int(input("Enter number"))
print(abs(n))
#____________________________________________________
# Task(2)
year = int(input("Enter year:"))

if year % 4 == 0 :
    print(year, "is leap year")
else:
    print(year, "is not a leap year")
# ___________________________________________________
# Task(3)
age1 = int(input('Enter age1:'))
age2 = int(input('Enter age2:'))
age3 = int(input('Enter age3:'))

oldest = age1
youngest = age1

if age2 > oldest:
    oldest = age2
if age3 > oldest:
    oldest = age3

if age2 < youngest:
    youngest = age2
if age3 < youngest:
    youngest = age3

print("oldest:", oldest)
print("youngest:", youngest)
# ___________________________________________________
# Task (4)
import msvcrt

def getpass(prompt="Enter your password: "):
    password = ""
    print(prompt, end="", flush=True)

    while True:
        char = msvcrt.getch().decode("utf-8")

        if char == "\r" or char == "\n":
            break
        elif char == "\b":
            if password:
                password = password[:-1]
                print("\b \b", end="", flush=True)
        else:
            password += char
            print("*", end="", flush=True)

    print()
    return password

password = getpass()
print("Your password is:", password)    
