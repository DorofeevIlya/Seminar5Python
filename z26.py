# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А
#  в целую степень B с помощью рекурсии.

def stepen (A,B):
    if (B == 1):
        return A
    if (B != 1):
        return (A*stepen(A,B-1))

A = int(input("Введите число A: "))
B = int(input("Введите степень числа: "))
print (f"Число {A} в степени {B} равно {stepen (A,B)}")