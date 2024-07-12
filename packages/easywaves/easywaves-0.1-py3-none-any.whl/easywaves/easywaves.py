from .curves import *
import numpy as np

def ease(currentTime, beginValue, changeValue, duration, easingFunction):

    if currentTime <= 0:
        return beginValue
    elif currentTime >= duration:
        return beginValue + changeValue
    
    progress = currentTime / duration
    
    eased_progress = easingFunction(progress)
    
    currentValue = beginValue + eased_progress * changeValue
    
    return currentValue


def ease_map(currentVal, startVal, endVal, startValue, endValue, easingFunction):
    
    if currentVal <= startVal:
        return startValue
    elif currentVal >= endVal:
        return endValue
    
    c = endValue - startValue
    d = endVal - startVal
    
    return ease(currentVal, startValue, c, d, easingFunction)

def wave(x, easingFunction):
    # ensure that 0 to 1 = a full wave
    x *= 2
    # ensure that the wave starts on zero
    x -= 0.5
    # modulus to repeat wave
    x = x % 2.0
    if x > 1:
        x = 2 - x
    return 2 * easingFunction(x) - 1
