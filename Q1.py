import sys

def roller_coaster_ride():
    N = int(sys.stdin.readline().strip())  
    C = int(sys.stdin.readline().strip())
    P = int(sys.stdin.readline().strip())
    max_capacity = C * P  

    if N <= max_capacity:
        print("yes")
    else:
        print("no")


if __name__ == "__main__":
    roller_coaster_ride()
