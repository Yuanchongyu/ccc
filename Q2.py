import sys

def donut_shop():
    D = int(input()) 
    E = int(input())  

    for _ in range(E):
        operation = input()
        Q = int(input())  

        if operation == "+":
            D += Q  
        elif operation == "-":
            D -= Q  

    print(D)


if __name__ == "__main__":
    donut_shop()
