import math
import numpy as np

############
# These functions output a value from 0 to 1
############

def linear(x):
    return x

def sineIn(x):
    return 1 - math.cos((x * math.pi) / 2)

def sineOut(x):
    return math.sin((x * math.pi) / 2)

def sineInOut(x):
    return -(math.cos(math.pi * x) - 1) / 2

# polynomial easing
# exp: 2 = quad, 3 = cubic, 4 = quart, 5 = quint etc
def polyIn(x, exp=2):
    return pow(x, exp)

def polyOut(x, exp=2):
    return 1 - math.pow(1 - x, exp)

def polyInOut(x, exp=2):
    return pow(2, exp-1) * math.pow(x, exp) if x < 0.5 else 1 - math.pow(-2 * x + 2, exp) / 2

def quadIn(x):
    return x * x

def quadOut(x):
    return 1 - (1 - x) * (1 - x)

def quadInOut(x):
    return 2 * x * x if x < 0.5 else 1 - math.pow(-2 * x + 2, 2) / 2

def cubicIn(x):
    return x * x * x

def cubicOut(x):
    return 1 - math.pow(1 - x, 3)

def cubicInOut(x):
    return 4 * x * x * x if x < 0.5 else 1 - math.pow(-2 * x + 2, 3) / 2

def quartIn(x):
    return x * x * x * x

def quartOut(x):
    return 1 - math.pow(1 - x, 4)

def quartInOut(x):
    return 8 * x * x * x * x if x < 0.5 else 1 - math.pow(-2 * x + 2, 4) / 2

def quintIn(x):
    return x * x * x * x * x

def quintOut(x):
    return 1 - math.pow(1 - x, 5)

def quintInOut(x):
    return 16 * x * x * x * x * x if x < 0.5 else 1 - math.pow(-2 * x + 2, 5) / 2

def expoIn(x):
    return 0 if x == 0 else math.pow(2, 10 * x - 10)

def expoOut(x):
    return 1 if x == 1 else 1 - math.pow(2, -10 * x)

def expoInOut(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    return math.pow(2, 20 * x - 10) / 2 if x < 0.5 else (2 - math.pow(2, -20 * x + 10)) / 2

def circIn(x):
    return 1 - math.sqrt(1 - math.pow(x, 2))

def circOut(x):
    return math.sqrt(1 - math.pow(x - 1, 2))

def circInOut(x):
    return (1 - math.sqrt(1 - math.pow(2 * x, 2))) / 2 if x < 0.5 else (math.sqrt(1 - math.pow(-2 * x + 2, 2)) + 1) / 2

def backIn(x):
    c1 = 1.70158
    c3 = c1 + 1
    return c3 * x * x * x - c1 * x * x

def backOut(x):
    c1 = 1.70158
    c3 = c1 + 1
    return 1 + c3 * math.pow(x - 1, 3) + c1 * math.pow(x - 1, 2)

def backInOut(x):
    c1 = 1.70158
    c2 = c1 * 1.525
    return (math.pow(2 * x, 2) * ((c2 + 1) * 2 * x - c2)) / 2 if x < 0.5 else (math.pow(2 * x - 2, 2) * ((c2 + 1) * (x * 2 - 2) + c2) + 2) / 2

def elasticIn(x):
    c4 = (2 * math.pi) / 3
    return 0 if x == 0 else 1 if x == 1 else -math.pow(2, 10 * x - 10) * math.sin((x * 10 - 10.75) * c4)

def elasticOut(x):
    c4 = (2 * math.pi) / 3
    return 0 if x == 0 else 1 if x == 1 else math.pow(2, -10 * x) * math.sin((x * 10 - 0.75) * c4) + 1

def elasticInOut(x):
    c5 = (2 * math.pi) / 4.5
    if x == 0:
        return 0
    if x == 1:
        return 1
    return -(math.pow(2, 20 * x - 10) * math.sin((20 * x - 11.125) * c5)) / 2 if x < 0.5 else (math.pow(2, -20 * x + 10) * math.sin((20 * x - 11.125) * c5)) / 2 + 1

def bounceIn(x):
    return 1 - bounceOut(1 - x)

def bounceOut(x):
    n1 = 7.5625
    d1 = 2.75
    if x < 1 / d1:
        return n1 * x * x
    elif x < 2 / d1:
        return n1 * (x - 1.5 / d1) * x + 0.75
    elif x < 2.5 / d1:
        return n1 * (x - 2.25 / d1) * x + 0.9375
    else:
        return n1 * (x - 2.625 / d1) * x + 0.984375

def bounceOut(x):
    return (1 - bounceIn(1 - 2 * x)) / 2 if x < 0.5 else (1 + bounceOut(2 * x - 1)) / 2


############
# These functions are for "realtime" decay - they have no end time
############

def decay(dt, startValue, endValue, decay):
	return endValue + (startValue - endValue) * math.exp(-decay * dt)

def decayDamped(dt, startValue, endValue, decay=0.5, omega=1):

    if decay < 1:
        # Underdamped
        omega_d = omega * np.sqrt(1 - decay**2)
        A = startValue - endValue
        B = (0 + decay * omega * A) / omega_d  # Initial velocity is 0 in this context
        y = endValue + np.exp(-decay * omega * dt) * (A * np.cos(omega_d * dt) + B * np.sin(omega_d * dt))
    elif decay == 1:
        # Critically damped
        A = startValue - endValue
        B = 0 + omega * A  # Initial velocity is 0 in this context
        y = endValue + (A + B * dt) * np.exp(-omega * dt)
    else:
        # Overdamped
        r1 = -decay * omega + omega * np.sqrt(decay**2 - 1)
        r2 = -decay * omega - omega * np.sqrt(decay**2 - 1)
        A = (0 - r2 * (a - endValue)) / (r1 - r2)
        B = (r1 * (startValue - endValue) - 0) / (r1 - r2)
        y = endValue + A * np.exp(r1 * dt) + B * np.exp(r2 * dt)
    
    return y
