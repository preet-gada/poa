def twosCompSign(str):
    n = len(str)
    i = n - 1
    while i >= 0:
        if str[i] == '1':
            break
        i -= 1

    k = i - 1
    while k >= 0:
        if str[k] == '1':
            str = list(str)
            str[k] = "0"
            str = "".join(str)
        else:
            str = list(str)
            str[k] = "1"
            str = "".join(str)
        k -= 1

    str = "1" + str[1:]
    return str

def twosCompUnsign(str):
    n = len(str)
    i = n - 1
    while i >= 0:
        if str[i] == '1':
            break
        i -= 1

    k = i - 1
    while k >= 0:
        if str[k] == '1':
            str = list(str)
            str[k] = "0"
            str = "".join(str)
        else:
            str = list(str)
            str[k] = "1"
            str = "".join(str)
        k -= 1

    return str

def binaryAddition(a,b):
    carry = 0
    result = ""
    for i in range(len(a)-1,-1,-1):
        r = carry
        r += 1 if a[i] == '1' else 0
        r += 1 if b[i] == '1' else 0
        result = ("1" if r % 2 == 1 else "0") + result
        carry = 0 if r < 2 else 1
    return result


def booths(num1,num2):
    if num1 > -1:
        M = format(num1,'05b')
        MinusM = twosCompUnsign(M)
    else:
        M = format(num1,'05b')
        MinusM = M
        M = twosCompSign(M)

    if num2 > -1:
        Q = format(num2,'05b')
    else:
        Q = format(num2,'05b')
        Q = twosCompSign(Q)
    
    Qm1 = 0
    count = len(M)
    A = "0"*count
    print("A \t Q \t Q-1 \t Action \t count")


    while count > 0:
        if Q[-1] == "1" and Qm1 == 0:
            A = binaryAddition(A , MinusM)
            print(A ,"\t",Q,"\t",Qm1 , "\t" , "A = A - M" , "\t" , count)

        elif Q[-1] == "0" and Qm1 == 1:
            A = binaryAddition(A , M)
            print(A ,"\t",Q,"\t",Qm1 , "\t" , "A = A + M" , "\t" , count)


        # right Shift
        Qm1 = int(Q[-1])
        temp = A[-1]
        first = A[0]
        tempA = int(A,2)
        tempA = tempA >> 1
        A = format(tempA , "05b")
        A = first + A[1:]

        tempQ = int(Q , 2)
        tempQ = tempQ >> 1
        Q = format(tempQ , '05b')
        Q = temp + Q[1:]


        print(A ,"\t",Q,"\t",Qm1 , "\t" , "Right Shift" , "\t" , count)
        print()

        count -= 1

    if A[0] == 1:
        result = A + Q
        result = twosCompSign(result)
        print(num1 ,"*",num2 , "=" ,  -abs(int(result,2)))
    else:
        result = A + Q
        print(num1 ,"*",num2 , "=" ,  int(result,2))


if __name__ == "__main__":
    num1 = int(input("Enter number one : "))
    num2 = int(input("Enter number two : "))
    booths(num1,num2)





        
        


