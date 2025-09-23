Celsius = float(input('qual a temperatura em celsius?'))
Kelvin = float(input('qual a temperatura em Kelvins?'))
Fahrenheit = float(input('qual a temperatura em Fahrenheit?'))

c_k = Celsius+273.15
k_c = Kelvin-273.15
c_f = ((Celsius*9)/5)+32
f_c = ((Fahrenheit - 32) * 5) / 9
f_k = (((Fahrenheit - 32) * 5) / 9) + 273.15
k_f = ((Kelvin - 273.15) * 9) / 5 + 32


print('de celsius para kelvin é:', c_k)
print('de celsius para fahrenheit é:', c_f)
print('de kelvin para celsius é:', k_c)
print('de kelvin para fahrenheit é:', k_f)
print('de fahrenheit para celsius é:', f_c)
print('de fahrenheit para kelvin é:', f_k)
