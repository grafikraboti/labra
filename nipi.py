def func1(arg1, arg2):
    var27 = func2(arg1, arg2)
    var34 = var30(var27, arg2)
    var35 = ((1472725142 & arg2) + -696759913) | arg1
    var36 = 258 ^ arg1 ^ var35 & (var34 - 281) + var34
    var37 = ((var27 - -801 | 1901431447) | arg2) & var27
    result = ((arg1 | 775693309) - ((var36 ^ -1979293316 - arg2) & ((arg1 - (arg2 & arg2)) ^ 1945732874 + var34) ^ var35)) - var36
    return result
def func8(arg31, arg32):
    var33 = -963 - arg31 + arg32
    result = -301 ^ var33 ^ -1829176668
    return result
def func7():
    closure = [-5]
    def func6(arg28, arg29):
        closure[0] += func8(arg28, arg29)
        return closure[0]
    func = func6
    return func
var30 = func7()
def func2(arg3, arg4):
    var5 = 0
    for var26 in ((i | var5) ^ var5 for i in func3(var5, 3)):
        var5 += var5 | 3
    return var5
def func4(arg8, arg9):
    var14 = func5(arg9, arg8)
    result = (656803619 + -784530956 + (arg8 - -1104694504 + var14 + 1468020351 ^ 992 - -925) + var14 - 1915655614 + arg8) & var14
    return result
def func5(arg10, arg11):
    var12 = 0
    for var13 in xrange(34):
        var12 += arg10 | arg10 ^ arg11
    return var12
def func3(arg6, arg7):
    var15 = func4(-1049128581, -603)
    yield var15
    var16 = 247 - 1057882766 + arg7
    yield var16
    var17 = -165 - var16
    yield var17
    var18 = var17 - var16 + 424651166 | 479958206
    yield var18
    var19 = var16 | ((arg6 - arg6) - -2)
    yield var19
    var20 = var18 ^ var19
    yield var20
    var21 = -847885191 - arg6 ^ (arg7 - arg6)
    yield var21
    var22 = var21 | var20 - var16
    yield var22
    var23 = (var17 - arg7) & var20 | var17
    yield var23
    var24 = var22 | (var23 & arg7) - var18
    yield var24
    var25 = ((var23 ^ var19) - var20) - var24
    yield var25
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 9'
    print 'arg_number: 38'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
