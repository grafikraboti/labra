def func1(arg1, arg2):
    var18 = var5(arg1, arg2)
    var21 = class5()
    for var22 in range(9):
        var21.func6(var22, var22)
    var27 = func7(arg2, var18)
    var32 = func8(var18, var27)
    def func9(arg33, arg34):
        var35 = var32 + arg2
        if var35 < var27:
            var36 = 830 | arg34 - (var32 ^ var32)
        else:
            var36 = (var32 - arg2) - arg34 - var18
        if arg33 < arg1:
            var37 = arg34 | (-64 + arg33) - var35
        else:
            var37 = (arg2 | arg1) + var32 | arg2
        var38 = (arg1 | var18) - var18 ^ arg2
        var39 = var27 + var32 ^ arg33 ^ var38
        if var39 < var38:
            var40 = (var39 ^ arg2) - var39 - -308
        else:
            var40 = (arg33 | (var18 & arg34)) & arg2
        var41 = ((var27 + var18) ^ -1737806305) | var32
        var42 = var32 - arg2 + arg34
        var43 = arg1 | (var42 ^ var38)
        var44 = var41 & var32 + -161 ^ arg2
        var45 = ((arg1 ^ var18) ^ arg33) & var41
        var46 = var27 ^ var27 ^ var32 + var35
        var47 = (var32 & var32 ^ arg34) + var45
        if var32 < var41:
            var48 = var41 - var38
        else:
            var48 = var43 + (arg2 + var41)
        var49 = var27 & var35
        var50 = arg2 & arg1
        var51 = var32 - var32 ^ var32 ^ var27
        var52 = (var38 | var35) ^ var27 ^ var39
        var53 = (var47 + var41 & var52) ^ var51
        result = var52 + var43
        return result
    var54 = func9(arg2, var32)
    var55 = (arg2 & var32) & arg2 & var54
    var56 = var54 | (var27 ^ 556584872 - var27)
    var57 = (var54 ^ arg1 - var55) | var54
    if var18 < var57:
        var58 = var18 + (var32 - -177731515) + arg1
    else:
        var58 = (var18 & var18) | var57 - var55
    var59 = (var18 - (var55 - -441)) ^ arg2
    var60 = var57 + var18
    var61 = var32 & (var55 | var60) ^ var57
    var62 = (-836060717 & var27 + 1999159306) - var57
    var63 = (var62 + (var61 - var59)) + var55
    var64 = var56 ^ (var63 | var57) ^ var63
    var65 = -954451872 - arg1
    var66 = var27 & var63 ^ 16 ^ -1728662221
    var67 = (var54 - var64 & var56) | var57
    if var18 < var62:
        var68 = (var56 ^ var32) - arg1 & var66
    else:
        var68 = var56 | var18
    var69 = var56 + var63
    result = arg1 ^ -1249158256 - var57
    return result
def func8(arg28, arg29):
    var30 = 0
    for var31 in range(42):
        var30 += var31 ^ (var31 | var30)
    return var30
def func7(arg23, arg24):
    var25 = 0
    for var26 in range(4):
        var25 += arg23 ^ var25 + arg23
    return var25
class class5(object):
    def func6(self, arg19, arg20):
        result = 2035275036 - ((((arg20 ^ -1245333915) | 47903645) ^ -554512381 & arg19) ^ arg19)
        return result
def func4(arg6, arg7):
    var8 = (917 ^ (arg6 + -476880981)) - 561
    var9 = var8 & arg7
    var10 = arg7 & var8 - var8 + var9
    var11 = (var10 + arg6 + var9) ^ 833
    if arg7 < arg7:
        var12 = ((arg6 - var11) | var8) + arg7
    else:
        var12 = 852835246 ^ (var9 + var8 & var10)
    var13 = arg7 - -760
    var14 = var13 + arg6 | var9 + arg7
    if arg6 < var13:
        var15 = (-1071354454 + var11 - arg6) & var14
    else:
        var15 = 106 + 843372849
    var16 = var10 & (var8 & var9) & 961
    var17 = arg6 & ((var8 ^ var13) + var8)
    result = var17 + ((var13 + var13 ^ var8 + arg6 ^ var9 | var8 + (arg6 ^ var8 - 387 + 126152564)) | var10)
    return result
def func3():
    closure = [-10]
    def func2(arg3, arg4):
        closure[0] += func4(arg3, arg4)
        return closure[0]
    func = func2
    return func
var5 = func3()
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 10'
    print 'arg_number: 70'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
