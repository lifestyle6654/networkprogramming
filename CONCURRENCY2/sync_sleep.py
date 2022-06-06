# 1초 후에 'hello', 2초 후에 'world'를 출력하는 프로그램
# 동기방식

import time

def say_after(delay, what):
    time.sleep(delay)
    print(what)

def main():
    print(f"started at {time.strftime('%X')}")

    say_after(1, 'hello')
    say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")

main()