tel={
    "marka":"samsung",
    "model":"a9",
    "yil":2018
}
print(tel)
print(tel["marka"])
print(tel["model"])
print(tel["yil"])
tel["renk"] = "siyah"
print(tel)
print(tel["renk"])
tel["renk"] = "mavi"
print(tel)
print(tel.keys())
print(tel.values())
for i in tel.keys():
    print(i, ":", tel[i])