import argparse
import sys
import time
from contextlib import contextmanager

sys.setrecursionlimit(10**9)


@contextmanager
def timer():
    t0 = time.time()
    msg = "start"
    print(msg)
    yield
    msg = f"done in {time.time() - t0:.2f} s"
    print(msg)


def fib(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def fib_memo(n: int):
    global done
    global memo
    if n == 0: return 0
    if n == 1: return 1

    if done[n]:
        return memo[n]

    done[n] = True
    memo[n] = fib_memo(n - 1) + fib_memo(n - 2)
    return memo[n]


def fib_loop(n: int):
    global memo
    memo[0] = 0
    memo[1] = 1

    for i in range(2, n+1):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("method", help="Select to solve with which fibonacci method")
    parser.add_argument("max_num", help="Set max number")
    args = parser.parse_args()

    n = int(args.max_num)
    done = [False] * (n + 1)
    memo = [0] * (n + 1)
    with timer():
        print(eval(args.method)(n))
