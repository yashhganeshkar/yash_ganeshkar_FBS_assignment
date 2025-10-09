
import threading

def print_lowercase():
    for ch in range(ord('a'), ord('z') + 1):
        print(chr(ch), end=' ')
    print()

def print_uppercase():
    for ch in range(ord('A'), ord('Z') + 1):
        print(chr(ch), end=' ')
    print()


t1 = threading.Thread(target=print_lowercase)
t2 = threading.Thread(target=print_uppercase)

t1.start()
t2.start()

t1.join()
t2.join()
