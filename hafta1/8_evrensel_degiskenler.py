x=15
def y():
    x=25
    print(x)

y()
print(x)
#global değişkenin kalıcı olarak değişmesini sağlıyor.
def z():
    global x
    x=35
    print(x)

z()
print(x)