import random

random.seed()


def is_prime(n):
    prime = True

    for i in range (2, int(n**0.5)+1):
        if n % i == 0:
            prime = False
            break

    return prime


number = random.randint(1,50)
# print(number)

help1 = True
help2 = True
help3 = True
count_guess = 1

print("number in range 1 to 50")
try:
    while True:
        guess = int(input("Enter guess number : "))
        if guess == number:
            print("SUCH WoooW!")
            break
        elif help1 and count_guess == 2:
            print("HELP : ",end='')
            print("that number is EVEN" if number%2 == 0 else "that number is ODD")
            help1 = False
        elif help2 and count_guess == 4:
            print("HELP : ",end='')
            print("that number is PRIME" if is_prime(number) else "that number is NOT PRIME")
            help2 = False
        elif help3 and count_guess == 6:
            print("HELP : ",end='')
            print(f"that number between {random.randint(1,number)}, {random.randint(number,50)}")
            help3 = False
            
        count_guess += 1

            
    print(f"You guess number {number} with {count_guess} guess")
except:
    print("You should enter a <integer number>!")