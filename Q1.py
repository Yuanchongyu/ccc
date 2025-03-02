import sys

def roller_coaster_ride():
    N = int(input())  
    C = int(input())
    P = int(input())
    max_capacity = C * P  

    if N <= max_capacity:
        print("yes")
    else:
        print("no")


if __name__ == "__main__":
    roller_coaster_ride()
