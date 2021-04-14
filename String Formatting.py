# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/python-string-formatting/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

def print_formatted(number):
    # your code goes here
    width=len(bin(number)[2:])
    for i in range(1,number+1):
        print(str(i).rjust(width),oct(i).replace("0o", "").rjust(width),hex(i).replace("0x", "").upper().rjust(width),bin(i).replace("0b", "").rjust(width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)