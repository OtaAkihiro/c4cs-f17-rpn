#!/usr/bin/env python3

import sys

def calculate(arg):

    arr = arg.split()
    st = []

    debug = False
    if len(sys.argv) > 1:
        if sys.argv[1] == 'debug':
            print('Debug is on')
            debug = True
	
    for elt in arr:

        if debug == True:
            print(st)
	
        result = 0
        
        if elt == '+':
            for i in range(len(st)):
                result += st.pop()
            st.append(result)
            
        elif elt == '-':
            for i in range(len(st)-1):
                result += st.pop()
            first = st.pop()
            st.append(first - result)
	
        elif elt == '^':
            power = st.pop()
            base = st.pop()
            st.append(base**power)
            
        else:
            st.append(int(elt))

    if debug == True:
        print(st)
            
    return st.pop()
            
def main():
    while True:
        calculate(input('rpn calc> '))



        
if __name__ == '__main__':
    print('running rpn')
    main()
