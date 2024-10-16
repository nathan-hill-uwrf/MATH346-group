import math

data1 = [[-1, 0.861], [-.5, 0.958], [0, 1.09], [.5, 1.29]]

def newtons_fd(data,at):
    s = newtons_s(data,at)
    d1,d2,d3 = newtons_deltas(data)
    y0 = data[0][1]
    return print("The interpolated value at", at,
                 "is", newtons_calc(y0,d1,d2,d3,s))
    
    
def newtons_calc(y0, d1, d2, d3, s):
    return (y0 + nCr(s,1)*d1 + nCr(s,2)*d2
            + nCr(s,3)*d3)

def newtons_deltas(data):
    delta1 = {}
    delta2 = {}
    delta3 = {}
    for pair in range(len(data)-1):
        delta1[pair] = data[pair + 1][1] - data[pair][1]
    for value in range(len(delta1)-1):
        delta2[value] = delta1[value + 1] - delta1[value]
    for value in range(len(delta2)-1):
        delta3[value] = delta2[value + 1] - delta2[value]
    return delta1[0], delta2[0], delta3[0]

def newtons_s(data, point):
    return (point - data[0][0])/(data[1][0] - data[0][0])

def nCr(s,k):
    numerator = s
    for term in range(1,k):
        numerator = numerator * (s-term)
    return numerator/math.factorial(k)

newtons_fd(data1, 0.25)
