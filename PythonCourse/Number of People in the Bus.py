# https://www.codewars.com/kata/5648b12ce68d9daa6b000099/train/python

def number(bus_stops):
    result = 0
    for i in range(len(bus_stops)):
        result+=bus_stops[i][0]
        result-=bus_stops[i][1]
    return result





print(number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]))