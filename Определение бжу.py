print('___Описание продукта по БЖУ на 100г.___')
b=float(input('Количество белка: '))
j=float(input('Количество жиров: '))
y=float(input('Количество углеводов: '))
klet=float(input('Количество клетчатки: '))
k=float(input('Калорийность продукта: '))
v=float(input('Вес продукта: '))
k1=b*4.1+j*9.3+y*4.1+klet*2
k2=k1/100*v
print('________________________')
if (j/100*v)>7:
	print('продукт жирный - '+str(j/100*v)+'г жира на порцию')
else:
	print(str(j/100*v)+'г жира')
print(str(b/100*v)+'г белка')
print(str(y/100*v)+'г углеводов')

print('Калорийность на 100г - '+str(round(k1))+' ккал,\nна всю порцию - '+str(round(k2))+' ккал')
if j>6 and y>40:
	print('Скорее всего это что-то сладкое')
if k<60 and b<10:
	print('Это может быть овощ или фрукт')
if b>15 and y<10:
	print('Скорее всего это мясо или молочный продукт')
if y>60 and j<6:
	print('Скорее всего это крупа')
