# a3test.py
# Nicolas Barone and Jeffrey Zhang (njb227 and jz674)
# 10/6/2016
""" Unit Test for Assignment A3"""

""" Unit Test for Assignment A3"""

import colormodel
import cornelltest
import a3

def test_complement():
    """Test function complement"""
    cornelltest.assert_equals(colormodel.RGB(255-250, 255-0, 255-71),
                              a3.complement_rgb(colormodel.RGB(250, 0, 71)))


def test_round():
    """Test function round (a3 version)"""
    cornelltest.assert_equals(130.6,   a3.round(130.59,1))
    cornelltest.assert_equals(130.5,   a3.round(130.54,1))
    cornelltest.assert_equals(100.0,   a3.round(100,1))
    cornelltest.assert_equals(100.6,   a3.round(100.55,1))
    cornelltest.assert_equals(99.57,   a3.round(99.566,2))
    cornelltest.assert_equals(99.99,   a3.round(99.99,2))
    cornelltest.assert_equals(100.0,   a3.round(99.995,2))
    cornelltest.assert_equals(22.00,   a3.round(21.99575,2))
    cornelltest.assert_equals(21.99,   a3.round(21.994,2))
    cornelltest.assert_equals(10.01,   a3.round(10.013567,2))
    cornelltest.assert_equals(10.0,    a3.round(10.000000005,2))
    cornelltest.assert_equals(10.0,    a3.round(9.9999,3))
    cornelltest.assert_equals(9.999,   a3.round(9.9993,3))
    cornelltest.assert_equals(1.355,   a3.round(1.3546,3))
    cornelltest.assert_equals(1.354,   a3.round(1.3544,3))
    cornelltest.assert_equals(0.046,   a3.round(.0456,3))
    cornelltest.assert_equals(0.045,   a3.round(.0453,3))
    cornelltest.assert_equals(0.006,   a3.round(.0056,3))
    cornelltest.assert_equals(0.001,   a3.round(.0013,3))
    cornelltest.assert_equals(0.0,     a3.round(.0004,3))
    cornelltest.assert_equals(0.001,   a3.round(.0009999,3))
    
    cornelltest.assert_equals(33.0,    a3.round(33.1,0))
    cornelltest.assert_equals(float,   type(a3.round(33.1,0)))
    
def test_str5():
    """Test function str5"""
    cornelltest.assert_equals('130.6',  a3.str5(130.59))
    cornelltest.assert_equals('130.5',  a3.str5(130.54))
    cornelltest.assert_equals('100.0',  a3.str5(100))
    cornelltest.assert_equals('100.6',  a3.str5(100.55))
    cornelltest.assert_equals('99.57',  a3.str5(99.566))
    cornelltest.assert_equals('99.99',  a3.str5(99.99))
    cornelltest.assert_equals('100.0',  a3.str5(99.995))
    cornelltest.assert_equals('22.00',  a3.str5(21.99575))
    cornelltest.assert_equals('21.99',  a3.str5(21.994))
    cornelltest.assert_equals('10.01',  a3.str5(10.013567))
    cornelltest.assert_equals('10.00',  a3.str5(10.000000005))
    cornelltest.assert_equals('10.00',  a3.str5(9.9999))
    cornelltest.assert_equals('9.999',  a3.str5(9.9993))
    cornelltest.assert_equals('1.355',  a3.str5(1.3546))
    cornelltest.assert_equals('1.354',  a3.str5(1.3544))
    cornelltest.assert_equals('0.046',  a3.str5(.0456))
    cornelltest.assert_equals('0.045',  a3.str5(.0453))
    cornelltest.assert_equals('0.006',  a3.str5(.0056))
    cornelltest.assert_equals('0.001',  a3.str5(.0013))
    cornelltest.assert_equals('0.000',  a3.str5(.0004))
    cornelltest.assert_equals('0.001',  a3.str5(.0009999))
    cornelltest.assert_equals('10.00', a3.str5(10.00000))
    cornelltest.assert_equals(str,   type(a3.str5(33.1)))


def test_str5_color():
    """Test the str5 functions for cmyk and hsv."""
    cornelltest.assert_equals('(98.45, 25.36, 72.80, 1.000)',
    a3.str5_cmyk(colormodel.CMYK(98.448, 25.362, 72.8, 1.0)));
    
    cornelltest.assert_equals('(0.000, 0.000, 0.000, 0.000)',
    a3.str5_cmyk(colormodel.CMYK(0.0000, 0, .00, 000.000)));
    
    cornelltest.assert_equals('(100.0, 50.44, 0.000, 0.997)',
    a3.str5_cmyk(colormodel.CMYK(99.99990, 50.444440, 0.0000099999, 0.99699)));

    
    
    # Tests for round5_hsv (add two)
    cornelltest.assert_equals('(360.0, 0.500, 0.590)',
    a3.str5_hsv(colormodel.HSV(359.95, .50, 0.5899)));
    cornelltest.assert_equals('(244.9, 0.356, 0.799)',
    a3.str5_hsv(colormodel.HSV(244.889999, .35554, 0.79898)));
    cornelltest.assert_equals('(1.000, 0.474, 0.000)',
    a3.str5_hsv(colormodel.HSV(.99999, .474, 0.0000044)));
    cornelltest.assert_equals('(0.000, 0.000, 0.000)',
    a3.str5_hsv(colormodel.HSV(0, 0, 0)));
    
    
def test_rgb_to_cmyk():
    """Test rgb_to_cmyk"""
    rgb = colormodel.RGB(255, 255, 255);
    cmyk = a3.rgb_to_cmyk(rgb);
    cornelltest.assert_equals('0.000', a3.str5(cmyk.cyan))
    cornelltest.assert_equals('0.000', a3.str5(cmyk.magenta))
    cornelltest.assert_equals('0.000', a3.str5(cmyk.yellow))
    cornelltest.assert_equals('0.000', a3.str5(cmyk.black))
    
    rgb = colormodel.RGB(0, 0, 0);
    cmyk = a3.rgb_to_cmyk(rgb);
    cornelltest.assert_equals('0.000', a3.str5(cmyk.cyan))
    cornelltest.assert_equals('0.000', a3.str5(cmyk.magenta))
    cornelltest.assert_equals('0.000', a3.str5(cmyk.yellow))
    cornelltest.assert_equals('100.0', a3.str5(cmyk.black))
        
    rgb = colormodel.RGB(217, 43, 164);
    cmyk = a3.rgb_to_cmyk(rgb);
    cornelltest.assert_equals('0.000', a3.str5(cmyk.cyan))
    cornelltest.assert_equals('80.18', a3.str5(cmyk.magenta))
    cornelltest.assert_equals('24.42', a3.str5(cmyk.yellow))
    cornelltest.assert_equals('14.90', a3.str5(cmyk.black))
    
    rgb = colormodel.RGB(255, 0, 0);
    cmyk = a3.rgb_to_cmyk(rgb);
    cornelltest.assert_equals('0.000', a3.str5(cmyk.cyan))
    cornelltest.assert_equals('100.0', a3.str5(cmyk.magenta))
    cornelltest.assert_equals('100.0', a3.str5(cmyk.yellow))
    cornelltest.assert_equals('0.000', a3.str5(cmyk.black))
    
    rgb = colormodel.RGB(0, 255, 0);
    cmyk = a3.rgb_to_cmyk(rgb);
    cornelltest.assert_equals('100.0', a3.str5(cmyk.cyan))
    cornelltest.assert_equals('0.000', a3.str5(cmyk.magenta))
    cornelltest.assert_equals('100.0', a3.str5(cmyk.yellow))
    cornelltest.assert_equals('0.000', a3.str5(cmyk.black))
    
    rgb = colormodel.RGB(0, 0, 255);
    cmyk = a3.rgb_to_cmyk(rgb);
    cornelltest.assert_equals('100.0', a3.str5(cmyk.cyan))
    cornelltest.assert_equals('100.0', a3.str5(cmyk.magenta))
    cornelltest.assert_equals('0.000', a3.str5(cmyk.yellow))
    cornelltest.assert_equals('0.000', a3.str5(cmyk.black))


def test_cmyk_to_rgb():
    """Test translation function cmyk_to_rgb"""
    cmyk = colormodel.CMYK(0, 0, 0, 0);
    rgb = a3.cmyk_to_rgb(cmyk);
    cornelltest.assert_equals('255.0', a3.str5(rgb.red))
    cornelltest.assert_equals('255.0', a3.str5(rgb.green))
    cornelltest.assert_equals('255.0', a3.str5(rgb.blue))
    
    cmyk = colormodel.CMYK(100, 100, 100, 100);
    rgb = a3.cmyk_to_rgb(cmyk);
    cornelltest.assert_equals('0.000', a3.str5(rgb.red))
    cornelltest.assert_equals('0.000', a3.str5(rgb.green))
    cornelltest.assert_equals('0.000', a3.str5(rgb.blue))
    
    cmyk = colormodel.CMYK(21.10, 40.00, 88.90, 7.320);
    rgb = a3.cmyk_to_rgb(cmyk);
    cornelltest.assert_equals('186.0', a3.str5(rgb.red))
    cornelltest.assert_equals('142.0', a3.str5(rgb.green))
    cornelltest.assert_equals('26.00', a3.str5(rgb.blue))
    
    
#   pass # ADD TESTS TO ME


def test_rgb_to_hsv():
    """Test translation function rgb_to_hsv"""
#Did a test for all 5 conditions plus a (0,0,0) test    
    rgb = colormodel.RGB(255, 255, 255);
    hsv = a3.rgb_to_hsv(rgb);
    cornelltest.assert_equals('0.000', a3.str5(hsv.hue))
    cornelltest.assert_equals('0.000', a3.str5(hsv.saturation))
    cornelltest.assert_equals('1.000', a3.str5(hsv.value))
    
    rgb = colormodel.RGB(255, 180, 90);
    hsv = a3.rgb_to_hsv(rgb);
    cornelltest.assert_equals('32.73', a3.str5(hsv.hue))
    cornelltest.assert_equals('0.647', a3.str5(hsv.saturation))
    cornelltest.assert_equals('1.000', a3.str5(hsv.value))
    
    rgb = colormodel.RGB(255, 180, 180);
    hsv = a3.rgb_to_hsv(rgb);
    cornelltest.assert_equals('0.000', a3.str5(hsv.hue))
    cornelltest.assert_equals('0.294', a3.str5(hsv.saturation))
    cornelltest.assert_equals('1.000', a3.str5(hsv.value))
    
    rgb = colormodel.RGB(255, 90, 180);
    hsv = a3.rgb_to_hsv(rgb);
    cornelltest.assert_equals('327.3', a3.str5(hsv.hue))
    cornelltest.assert_equals('0.647', a3.str5(hsv.saturation))
    cornelltest.assert_equals('1.000', a3.str5(hsv.value))
    
    rgb = colormodel.RGB(150, 255, 50);
    hsv = a3.rgb_to_hsv(rgb);
    cornelltest.assert_equals('90.73', a3.str5(hsv.hue))
    cornelltest.assert_equals('0.804', a3.str5(hsv.saturation))
    cornelltest.assert_equals('1.000', a3.str5(hsv.value))
    
    rgb = colormodel.RGB(150, 50, 255);
    hsv = a3.rgb_to_hsv(rgb);
    cornelltest.assert_equals('269.3', a3.str5(hsv.hue))
    cornelltest.assert_equals('0.804', a3.str5(hsv.saturation))
    cornelltest.assert_equals('1.000', a3.str5(hsv.value))
    
    rgb = colormodel.RGB(0, 0, 0);
    hsv = a3.rgb_to_hsv(rgb);
    cornelltest.assert_equals('0.000', a3.str5(hsv.hue))
    cornelltest.assert_equals('0.000', a3.str5(hsv.saturation))
    cornelltest.assert_equals('0.000', a3.str5(hsv.value))
    
    rgb = colormodel.RGB(150, 50, 50);
    hsv = a3.rgb_to_hsv(rgb);
    cornelltest.assert_equals('0.000', a3.str5(hsv.hue))
    cornelltest.assert_equals('0.667', a3.str5(hsv.saturation))
    cornelltest.assert_equals('0.588', a3.str5(hsv.value))


def test_hsv_to_rgb():
    """Test translation function hsv_to_rgb"""
    pass # ADD TESTS TO ME
    hsv = colormodel.HSV(0, 0, 0);
    rgb = a3.hsv_to_rgb(hsv);
    cornelltest.assert_equals(0.000, (rgb.red))
    cornelltest.assert_equals(0.000, (rgb.green))
    cornelltest.assert_equals(0.000, (rgb.blue))
    
    hsv = colormodel.HSV(0, .25, .75);
    rgb = a3.hsv_to_rgb(hsv);
    cornelltest.assert_equals(191, (rgb.red))
    cornelltest.assert_equals(143, (rgb.green))
    cornelltest.assert_equals(143, (rgb.blue))
    
    hsv = colormodel.HSV(10, .25, .75);
    rgb = a3.hsv_to_rgb(hsv);
    cornelltest.assert_equals(191, (rgb.red))
    cornelltest.assert_equals(151, (rgb.green))
    cornelltest.assert_equals(143, (rgb.blue))
    
    hsv = colormodel.HSV(70, .25, .75);
    rgb = a3.hsv_to_rgb(hsv);
    cornelltest.assert_equals(183, (rgb.red))
    cornelltest.assert_equals(191, (rgb.green))
    cornelltest.assert_equals(143, (rgb.blue))
    
    hsv = colormodel.HSV(121, .25, .75);
    rgb = a3.hsv_to_rgb(hsv);
    cornelltest.assert_equals(143, (rgb.red))
    cornelltest.assert_equals(191, (rgb.green))
    cornelltest.assert_equals(144, (rgb.blue))
    
    hsv = colormodel.HSV(181, .25, .75);
    rgb = a3.hsv_to_rgb(hsv);
    cornelltest.assert_equals(143, (rgb.red))
    cornelltest.assert_equals(190, (rgb.green))
    cornelltest.assert_equals(191, (rgb.blue))
    
    hsv = colormodel.HSV(241, .25, .75);
    rgb = a3.hsv_to_rgb(hsv);
    cornelltest.assert_equals(144, (rgb.red))
    cornelltest.assert_equals(143, (rgb.green))
    cornelltest.assert_equals(191, (rgb.blue))
    
    hsv = colormodel.HSV(301, .25, .75);
    rgb = a3.hsv_to_rgb(hsv);
    cornelltest.assert_equals(191, (rgb.red))
    cornelltest.assert_equals(143, (rgb.green))
    cornelltest.assert_equals(190, (rgb.blue))
    
    hsv = colormodel.HSV(0, 0, .75);
    rgb = a3.hsv_to_rgb(hsv);
    cornelltest.assert_equals(191, (rgb.red))
    cornelltest.assert_equals(191, (rgb.green))
    cornelltest.assert_equals(191, (rgb.blue))
    
    hsv = colormodel.HSV(0, 0.25, 0);
    rgb = a3.hsv_to_rgb(hsv);
    cornelltest.assert_equals(0, (rgb.red))
    cornelltest.assert_equals(0, (rgb.green))
    cornelltest.assert_equals(0, (rgb.blue))
# Script Code
# THIS PREVENTS THE TESTS RUNNING ON IMPORT
if __name__ == "__main__":
    test_complement()
    test_round()
    test_str5()
    test_str5_color()
    test_rgb_to_cmyk()
    test_cmyk_to_rgb()
    test_rgb_to_hsv()
    test_hsv_to_rgb()
    print "Module a3 is working correctly"