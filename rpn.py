#!/usr/bin/env python3

def calculate(arg):

    arr = arg.split()
    st = []
    for elt in arr:
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
             
        else:
            st.append(int(elt))
            
    return st.pop()
            
def main():
    while True:
        calculate(input('rpn calc> '))



        
if __name__ == '__main__':
    print('running rpn')
    main()
