import math

R = 6371     # радиус в нашем случае земли
Shir = float(input("Введите широту: "))                 #
Dolg = float(input("Введите долготу: "))                #
ShirObj = float(input("Введите широту объекта: "))      #
DolgObj = float(input("Введите долготу объекта: "))     # Ну это вводные

ShirRad= math.radians(Shir)                 #
DolgRad= math.radians(Dolg)                 #
ShirRadObj = math.radians(ShirObj)          #
DolgRadObj = math.radians(DolgObj)          # Вычисление растояние между Наблюдателем и местом

delD = DolgRadObj - DolgRad                                                                #
delS = ShirRadObj - ShirRad                                                                #
a = math.sin(delS/2)**2 + math.cos(ShirRad) * math.cos(ShirRadObj) * math.sin(delS/2)**2   #
d = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))                                           #
Rasstoyanie = R * d                                                                        # Вычясляю расстояние по формулам из Интернета

y = math.sin(math.radians(DolgRadObj-DolgRad)) * math.cos(math.radians(ShirRadObj))                                #
x = math.cos(math.radians(ShirRad))*math.sin(math.radians(ShirRadObj)) - \
    math.sin(math.radians(ShirRad))*math.cos(math.radians(ShirRadObj))*math.cos(math.radians(DolgRadObj-DolgRad))  #(тут я кстати перенёс)
azimuth = math.atan2(y, x)                                                                                         #Вычеслил азимут от Наблюдателя до места

print("Расстояние между точками: {:.2f} км".format(Rasstoyanie))                                    #
print("Азимут от первой точки до второй: {:.1f} радиан".format(azimuth))                            #
print("Азимут от первой точки до второй: {:.1f} градусов".format(math.degrees(azimuth)))            #Ну тут выводы
