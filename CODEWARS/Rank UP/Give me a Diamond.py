# https://www.codewars.com/kata/5503013e34137eeeaa001648/train/python

def diamond(n):
    if n < 0 or n % 2 == 0:
        return None

    result = "*" * n + "\n";
    spaces = 1;
    n = n - 2
    while n > 0:
        current = " " * spaces + "*" * n + "\n"
        spaces = spaces + 1
        n = n - 2
        result = current + result + current

    return result