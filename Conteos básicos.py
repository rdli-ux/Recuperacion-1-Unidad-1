import sys

def main():
    entrada = sys.stdin.read().split()
    if len(entrada) >= 2:
        a = int(entrada[0])
        b = int(entrada[1])
        for i in range(a, b + 1):
            print(i)

if __name__ == '__main__':
    main()
    