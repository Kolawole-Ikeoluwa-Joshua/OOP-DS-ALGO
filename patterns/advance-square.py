def printSquare(N):
    if N > 20:
        return "Please input a valid integer between 1 to 20"
    
    # logic here
    for i in range(0, 2*N-1):
        for j in range(0, 2*N-1):
                
            # get elemental distances
            top = i
            left = j
            right = (2*N-2) - j
            down = (2*N-2) - i
                
            # get value on displayed matrix
                
            value = N - min(top, down, left, right)
            print(value, end=" ")
        print()



    return "Pattern Printed Successfully"



result = printSquare(4)
print(result)