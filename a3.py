# a3.py
# Nicolas Barone and Jeffrey Zhang (njb227 and jz674)
# 10/6/2016
""" Functions for Assignment A3"""

import colormodel
import math

def complement_rgb(rgb):
    """Returns: the complement of color rgb.
    
    Parameter rgb: the color to complement
    Precondition: rgb is an RGB object"""
    # THIS IS WRONG.  FIX IT
    return colormodel.RGB(255 - rgb.red, 255 - rgb.green, 255 - rgb.blue)


def round(number, places):
    """Returns: the number rounded to the given number of decimal places.
    
    The value returned is a float.
    
    This function is more stable than the built-in round.  The built-in round
    has weird behavior where round(100.55,1) is 100.5 while round(100.45,1) is
    also 100.5.  We want to ensure that anything ending in a 5 is rounded UP.
    
    It is possible to write this function without the second precondition on
    places. If you want to do that, we leave that as an optional challenge.
    
    Parameter number: the number to round to the given decimal place
    Precondition: number is an int or float
    
    Parameter places: the decimal place to round to
    Precondition: places is an int; 0 <= places <= 3"""
    
    
    dec_pos1 = number * (10**places)
    result = int(dec_pos1 + 0.5) / (10.0**places)
    return result


def str5(value):
    """ Returns: value as a string, but expand or round to be exactly
    5 characters.
    
    The decimal point counts as one of the five characters.
   
    Examples:
        str5(1.3546)  is  '1.355'.
        str5(21.9954) is  '22.00'.
        str5(21.994)  is  '21.99'.
        str5(130.59)  is  '130.6'.
        str5(130.54)  is  '130.5'.
        str5(1)       is  '1.000'.
        .0004
    0.00
    Parameter value: the number to conver to a 5 character string.
    Precondition: value is a number (int or float), 0 <= value <= 360."""
    # Note:Obviously, you want to use the function round() that you
    # just defined. 
    # However, remember that the rounding takes place at a different
    # place depending 
    # on how big value is. Look at the examples in the specification.
    
    
    a = str(value) #locate the decimal by converting the thing into a str
    pos1 = 4 - a.find('.') 
    first = str(round(value,pos1))
    if len(first) < 5:
        a = first + '0000000000'
        return a[ :5]
    else:
        result = first[:5] 
        return result   


def str5_cmyk(cmyk):
    """Returns: String representation of cmyk in the form "(C, M, Y, K)".
    
    In the output, each of C, M, Y, and K should be exactly 5 characters long.
    Hence the output of this function is not the same as str(cmyk)
    
    Example: if str(cmyk) is 
    
          '(0.0,31.3725490196,31.3725490196,0.0)'
    
    then str5_cmyk(cmyk) is '(0.000, 31.37, 31.37, 0.000)'. Note the spaces after the
    commas. These must be there.
    
    Parameter cmtk: the color to convert to a string
    Precondition: cmyk is an CMYK object."""
    c = cmyk
    C = str5(c.cyan)
    M = str5(c.magenta)
    Y = str5(c.yellow)
    K = str5(c.black)
    return ('(' + C + ', ' + M + ', ' + Y +', ' + K + ')')


def str5_hsv(hsv):
    """Returns: String representation of hsv in the form "(H, S, V)".
    
    In the output, each of H, S, and V should be exactly 5 characters long.
    Hence the output of this function is not the same as str(hsv)
    
    Example: if str(hsv) is 
    
          '(0.0,0.313725490196,1.0)'
    
    then str5_hsv(hsv) is '(0.000, 0.314, 1.000)'. Note the spaces after the
    commas. These must be there.
    
    Parameter hsv: the color to convert to a string
    Precondition: hsv is an HSV object."""
    
    h = hsv
    H = str5(h.hue)
    S = str5(h.saturation)
    V = str5(h.value)
    return ('('+ H + ', ' + S + ', ' + V + ')')


def rgb_to_cmyk(rgb):
    """Returns: color rgb in space CMYK, with the most black possible.
    
    Formulae from en.wikipedia.org/wiki/CMYK_color_model.
    
    Parameter rgb: the color to convert to a CMYK object
    Precondition: rgb is an RGB object"""
    R = rgb.red/255.0       # The RGB numbers are in the range 0..255.
    G = rgb.green/255.0   # Change the RGB numbers to the range 0..1 by
                            #dividing them by 255.0.
    B = rgb.blue/255.0

    C1 = 1 - R
    M1 = 1 - G
    Y1 = 1 - B

    if C1 == 1 and M1 == 1 and  Y1 == 1:
        return colormodel.CMYK(0, 0, 0, 100.0)
    else:
        K2 = min([C1, M1, Y1])
        C2 = (C1 - K2)/(1 - K2) 
        M2 = (M1 - K2)/(1 - K2) 
        Y2 = (Y1 - K2)/(1 - K2)
        
        C = C2 * 100.0
        M = M2 * 100.0
        Y = Y2 * 100.0
        K = K2 * 100.0
        
        cmyk = colormodel.CMYK(C, M, Y, K)
      
        return cmyk


def cmyk_to_rgb(cmyk):
    """Returns : color CMYK in space RGB.

    Formulae from en.wikipedia.org/wiki/CMYK_color_model.
   
    Parameter cmyk: the color to convert to a RGB object
    Precondition: cmyk is an CMYK object."""
    # The CMYK numbers are in the range 0.0..100.0.  Deal with them in the 
    # same way as the RGB numbers in rgb_to_cmyk()
    
    C = cmyk.cyan/100.0     
    M = cmyk.magenta/100.0
    Y = cmyk.yellow/100.0
    K = cmyk.black/100.0
    n = (1-C)*(1-K)*255.0
    R = int(round(n, 0))
    a = (1-M)*(1-K)*255.0
    G = int(round(a, 0))
    l = (1-Y)*(1-K)*255.0
    B = int(round(l, 0))
   
    rgb = colormodel.RGB(R, G, B)
      
    return rgb
    


def rgb_to_hsv(rgb):
    """Return: color rgb in HSV color space.

    Formulae from wikipedia.org/wiki/HSV_color_space.
   
    Parameter rgb: the color to convert to a HSV object
    Precondition: rgb is an RGB object"""
    # The RGB numbers are in the range 0..255.
    # Change them to range 0..1 by dividing them by 255.0.
    
    #first convert to new range
    R = rgb.red/255.0       
    G = rgb.green/255.0
    B = rgb.blue/255.0
    
    MAX = max([R, G, B])
    MIN = min([R, G, B])
    
    if (MAX == MIN):
        H = 0
    elif ((MAX == R) & (G >= B)):
        H = 60.0 * (G - B) / (MAX - MIN)
    elif((MAX == R) & (G<B)):
        H = 60.0 * (G - B) / (MAX - MIN) + 360.0
    elif(MAX == G):
        H = 60.0 * (B - R) / (MAX - MIN) + 120.0
    elif(MAX == B):
        H = 60.0 * (R - G) / (MAX - MIN) + 240.0
        
    if(MAX == 0):
        S = 0
    else:
        S = 1 - MIN/MAX
        
    V = MAX
    
    hsv = colormodel.HSV(H, S, V)
    return hsv  



def hsv_to_rgb(hsv):
    """Returns: color in RGB color space.
    
    Formulae from http://en.wikipedia.org/wiki/HSV_color_space.
    
    Parameter hsv: the color to convert to a RGB object
    Precondition: hsv is an HSV object."""
    H = hsv.hue
    S = hsv.saturation
    V = hsv.value
    
    Hi = math.floor(H/60)
    f = H/60 - Hi
    p = V*(1-S)
    q = V*(1-f*S)
    t = V*(1-(1-f)*S)
    
    if(Hi == 0):
        R = V
        G = t
        B = p
    elif(Hi == 1):
        R = q
        G = V
        B = p
    elif(Hi == 2):
        R = p
        G = V
        B = t
    elif(Hi == 3):
        R = p
        G = q
        B = V
    elif(Hi == 4):
        R = t
        G = p
        B = V
    elif(Hi == 5):
        R = V
        G = p
        B = q
        
    R2 = int(round(R*255.0, 0)) 
    G2 = int(round(G*255.0, 0))
    B2 = int(round(B*255.0, 0))
    
    rgb = colormodel.RGB(R2, G2, B2)
    return rgb

