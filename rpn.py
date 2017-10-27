#!/usr/bin/env python3

def calculate(arg):

    arr = arg.split()
    print(arr)



def main():
    while True:
        calculate(input('rpn calc> '))



        
if __name__ == '__main__':
    print('running rpn')
    main()
