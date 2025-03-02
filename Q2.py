import sys

def donut_shop():
    D = int(sys.stdin.readline().strip()) 
    E = int(sys.stdin.readline().strip())  

    for _ in range(E):
        operation = sys.stdin.readline().strip() 
        Q = int(sys.stdin.readline().strip())  

        if operation == "+":
            D += Q  
        elif operation == "-":
            D -= Q  

    print(D)


if __name__ == "__main__":
    donut_shop()
