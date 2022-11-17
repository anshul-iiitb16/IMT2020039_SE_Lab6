#!/usr/bin/python3

def sum_natnums(n):
    if n == 1:
        return 1
    else:
        return n + sum_natnums(n-1)

# if __name__ == '__main__':
#     print(sum_natnums(10))
