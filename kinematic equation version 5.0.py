#from os import *
from time import *
print("alpha version 5.0")

while True:

    print(" ")
    print(" ")
    print(" ")
    print("please use abreviations instead of whole words: a, t, vf, vi, d")
    solve = str(input("type the variable you would like to solve for: "))
    nouse = str(input("type the variable that will not be used: "))

    """def ivf():
        #ivf = v_f
        v_f = float(input("final velocity value: "))

    def ivi():
        v_i = float(input("initial velocity value: "))

    def it():
        #it = t
        t = float(input("time in seconds: "))"""


    """ivi = float(input("final velocity value: "))
    ivi = float(input("initial velocity value: "))
    it = float(input("time in seconds: "))
    ia = a = float(input("acceleration value: "))
    #id = d = float(input("time value: "))"""


    """var1 = v_i
    var2 = a
    var3 = t
    var4 = int
    var4 = v_f
    var5 = v_f - v_i
    var6 = v_i**2+2*a*d
    var7 = a*2*d-v_f**2
    var8 = v_f**2
    var9 = v_i**2
    var10 = var8 - var9
    var11 = .5*a
    var12 = var11* t**2
    var13 = var12+t*v_i
    var14 = v_f + v_i
    var15 = var14 / 2
    var16 = v_i * t
    var17 = -2+v_i
    var18 = 2*d
    var19 = var17 + var18
    var20 = t
    var21 = d/t-v_i
    var22 = var21*2
    var23 = 2 * d
    var24 = var23/t
    var25 = .5*a
    var26 = d / var25
    var27
    var28
    var29"""
    #sqrt = x**(.5)

    if solve == "a" and nouse == "d":
         v_i = float(input("initial velocity value: "))
         v_f = float(input("final velocity value: "))
         t = float(input("time in seconds: "))
         print((v_f - v_i)/t)

    #first equation: vf = vi + a*t
    if solve == "vf" and nouse == "d":
        a = float(input("acceleration value: "))
        v_i = float(input("initial velocity value: "))
        t = float(input("time in seconds: "))
        print(a*t+v_i)

    if solve == "vi" and nouse == "d":
        v_f = float(input("final velocity value: "))
        a = float(input("acceleration value: "))
        t = float(input("seconds: "))
        print(a*t-v_f)
        
    if solve == "t" and nouse == "d":
        v_f = float(input("final velocity value: "))
        v_i = float(input("initial velocity value: "))
        a = float(input("acceleration value: "))
        var27 = (v_f-v_i)/a
        #str(var27)
        print(str(var27))
        #print("in seconds")

    #second equation: vf^2 = vi^2 + 2*a*d
    if solve == "vf" and nouse == "t":
        d = float(input("distance value: "))
        v_i = float(input("initial velocity value: "))
        a = float(input("acceleration value: "))
        var6 = v_i**2+2*a*d
        print(var6**(.5))

    if solve == "vi" and nouse == "t":
        d = float(input("distance value: "))
        v_f = float(input("final velocity value: "))
        a = float(input("acceleration value: "))
        var7 = a*2*d-v_f**2
        print(-var7**(.5))

    if solve == "a" and nouse == "t":
        d = float(input("distance value: "))
        v_i = float(input("initial velocity value: "))
        v_f = float(input("final velocity value: "))
        var8 = v_f**2
        var9 = v_i**2
        var10 = var8 - var9
        print((var10/d)/2)

    if solve == "d" and nouse == "t":
        v_f = float(input("final velocity value: "))
        v_i = float(input("initial velocity value: "))
        a = float(input("acceleration value: "))
        print(((v_f**2-v_i**2)/a/2))
        
    #third equation: d = vi*t + .5*a* t^2
    if solve == "d" and nouse == "vf":
        t = float(input("time in seconds: "))
        v_i = float(input("initial velocity value: "))
        a = float(input("acceleration value: "))
        print(v_i*t+a*.5*t**2)

    if solve == "vi" and nouse == "vf":
        d = float(input("distance value: "))
        t = float(input("time in seconds: "))
        a = float(input("acceleration value: "))
        var11 = .5*a
        var12 = var11* t**2
        var13 = var12+t*v_i
        print(var13)

    if solve == "a" and nouse == "vf":
        d = float(input("distance value: "))
        v_i = float(input("initial velocity value: "))
        t = float(input("time in seconds: "))
        var21 = d/t-v_i
        var22 = var21*2
        print(var22/t)

    if solve == "t" and nouse == "vf":
        d = float(input("distance: "))
        v_i = float(input("initial velocity value: "))
        a = float(input("acceleration value: "))

        a = .5 * a
        c = -d
        b = v_i
        descr = (b**2 - 4*a*c)**.5
        ans1= (-b+descr)/(2*a)
        ans2= (-b-descr)/(2*a)
        print(descr)
        print("The first root is: ", ans1)
        print("The second root is: ", ans2)

    # fourth equation: d = (vi + vf)/2 * t
    if solve == "d" and nouse == "a":
        t = float(input("time in seconds: "))
        v_i = float(input("initial velocity value: "))
        v_f = float(input("final velocity value: "))
        var14 = v_f + v_i
        var15 = var14 / 2
        print(var15*t)

    if solve == "vi" and nouse == "a":
        t = float(input("time in seconds: "))
        d = float(input("distance value: "))
        v_f = float(input("final velocity value: "))
        var23 = 2 * d
        var24 = var23/t
        print(var24-v_f)

    if solve == "vf" and nouse == "a":
        t = float(input("time in seconds: "))
        v_i = float(input("initial velocity value: "))
        d = float(input("distance value: "))
        var23 = 2 * d
        var24 = var23/t
        print(var24-v_i)

    if solve == "t" and nouse == "a":
        d = float(input("distance: "))
        v_i = float(input("initial velocity value: "))
        v_f = float(input("final velocity value: "))
        var29 = d/((v_i+v_f)/2)
        print(str(var29))

    if nouse == "vi":
        print("Try reversing time. You always have initial velocity somewhere.")
        
    #print("All the left over floppy discs left over will take over the world in the year of 2060")

