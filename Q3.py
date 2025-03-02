
import sys

def update_product_codes():
    N = int(input())

    for _ in range(N):
        code = input()
        letters = []
        num = ""
        total = 0

        for char in code:
            if char.isupper():
                letters.append(char)
            if char.isdigit() or char == "-":
                num += char
            else:
                if num:
                    total += int(num)
                    num = ""

        if num:
            total += int(num)

        print("".join(letters) + str(total))


if __name__ == "__main__":
    update_product_codes()