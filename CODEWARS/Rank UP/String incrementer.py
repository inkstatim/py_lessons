# https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python

def increment_string(strng):
    if strng[-1].isdigit():
        x = len(strng)-1
        while x >= 0 and strng[x].isdigit():
            x-=1
        x+=1
        num = str(int(strng[x:]) + 1).zfill(len(strng) - x)
        return strng[:x] + num
    else:
        return strng+'1'