#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    number = len(sys.argv)
    total = 0
    if number <= 1:
        print(total)
    else:
        for i in range(1, number):
            total += int(sys.argv[i])
        print(total)
