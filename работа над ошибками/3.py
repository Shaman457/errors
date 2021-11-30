n = int(input())
if n<2:
    print("Младенец")
elif n>=2 and n<13:
    print("Малыш")
elif n>=13 and n<20:
    print("Подросток")
elif n>=20 and n<65:
    print("Взрослый")
else:
    print("Пожилой")