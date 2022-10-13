#-------------------------------------------------
x=[1,2,3]
y=[True,313422133,None,[3,0.5,"la"]]
print(x)
print(y)
print(y[0])
print(y[3][1])
ben="yusuf"
print(ben[1:4])
y[3][1] = [12, 33, 4.5, "saas"]
print(y[3][1])
print(y[3][1][3])
print("------------------------------------------")
#-------------------------------------------------
z=[4,3]
# (.append())sona ekleme yamak için
z.append(5)
print(z)
# (.pop()) sondaki değeri siler
z.pop()
print(z)
# (.insert(yerine,konulan))
# (.remove())istenilen sayıyı listeden atar
z.insert(1, 100)
z.remove(4)
print(z)
#
print(z.pop())
print(z)
# (.clear())
z.clear()
print(z)
print("------------------------------------------")
#-------------------------------------------------
uzay=["ay","gunes","yildiz"]
uzay.sort()
print(uzay)
#
uzay.reverse()
print(uzay)
#
def fonksiyon(n):
    return abs(n-50)
#??
sira_no=[5,300,45,32,64]
sira_no.sort(key=fonksiyon)
print(sira_no)
print("------------------------------------------")
#-------------------------------------------------
kat_no=[3,4,5,10,-8,13]
a=kat_no
print(a)
kat_no.sort()
print(a)
print("------------------------------------------")
#-------------------------------------------------
kat_no=[3,4,5,10,-8,13]
a=kat_no.copy()
print(a)
kat_no.sort()
print(a)
print("------------------------------------------")
#-------------------------------------------------