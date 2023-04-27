
import re

def RLE(nabor): 
    cod = '' 
    last_char = '' 
    count = 1 
    if not nabor: return 'Пустая строка'
    if not re.match(r'[A-Z]+$', nabor): return 'Невалидная строка'
    # if nabor.isalpha() == False: 
    for ch in nabor:
        if ch != last_char:
            if last_char != '': 
                if count < 2:
                    cod += last_char
                else:
                    cod += last_char + str(count) 
            count = 1 
            last_char = ch 
        else:
            count += 1 
    else:
        if count <2:
            cod += last_char
            return cod
        else:
            cod += last_char + str(count)
            return cod
nabor = input("Введите строку из символов от A до Z: ")
print(RLE(nabor))
