'''
Created on Apr 17, 2018

@author: mohd.dzarif
'''
def half(number):
    while True:
        number = round(number//2)
        print(number)
        if(number <= 1):
            break
    return

def main():
    number = int(input("Enter a number : "))
    half(number)

main()