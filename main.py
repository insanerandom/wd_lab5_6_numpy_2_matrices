import numpy as np

#skummulowana suma dla rzędu
#print(a.cumsum(axis=1))

#Zadanie 1
#Utwórz dwie macierze 1x3 różnych wartości a następnie wykonaj operację mnożenia.
print('Zadanie 1')
a1 = np.array([15, 30, 45])
b1 = np.array([2, 3, 4])
print(a1)
print(b1)
c = a1 * b1
print(c)
print('########################')

#Zadanie 2
#Utwórz macierz 3x3 oraz 4x4 i znajdź najniższe wartości dla każdej kolumny i każdego rzędu.
print('Zadanie 2')
b = np.arange(9)
print(b)
mat1 = b.reshape((3, 3))
print(mat1)
b = np.arange(16)
mat2 = b.reshape((4, 4))
print(mat2)
print('Dla macierzy 3x3:')
print('Najnizsza wartosc dla kazdej kolumny:', mat1.min(axis=0))
print('Najnizsza wartosc dla kazdego rzedu:', mat1.min(axis=1))
print('Najwyzsza wartosc dla kazdej kolumny:', mat1.max(axis=0))
print('Najwyzsza wartosc dla kazdego rzedu:', mat1.max(axis=1))
print('Dla macierzy 4x4:')
print('Najnizsza wartosc dla kazdej kolumny:', mat2.min(axis=0))
print('Najnizsza wartosc dla kazdego rzedu:', mat2.min(axis=1))
print('Najwyzsza wartosc dla kazdej kolumny:', mat2.max(axis=0))
print('Najwyzsza wartosc dla kazdego rzedu:', mat2.max(axis=1))
print('########################')

#Zadanie 3
#Wykorzystaj macierze z zadania pierwszego i wykonaj iloczyn macierzy.
print('Zadanie 3')
c = np.dot(a1, b1)
print(c)
print('########################')

#Zadanie 4
#Utwórz dwie macierze 1x3 gdzie pierwsza z nich będzie zawierała liczby całkowite, a druga
#liczby rzeczywiste. Następnie wykonaj na nich operację mnożenia.
print('Zadanie 4')
a4 = np.array([20, 30, 40])
print(a4)
b4 = np.array([9.54, 7.98, 1.6180339887])
print(b4)
c4 = np.dot(a4, b4)
d4 = a4 * b4
print(c4)
print(d4)
print('########################')

#Zadanie 5
#Utwórz macierz 2x3 różnych wartości a następnie wylicz sinus dla każdej z jej wartości i
#zapisz do zmiennej “a”
print('Zadanie 5')
a5 = np.random.randint(0, 17, 6)
print(a5)
a5 = a5.reshape((2, 3))
print('Macierz a5:')
print(a5)
a = np.sin(a5)
print('Sinus dla kazdej wartosci macierzy a5:')
print(a)
print('########################')

#Zadanie 6
#Utwórz nową macierz 2x3 różnych wartości a następnie wylicz cosinus dla każdej z jej
#wartości i zapisz do zmiennej “b”.
print('Zadanie 6')
a6 = np.random.randint(16, 26, 6)
print(a6)
a6 = a6.reshape((2, 3))
print('Macierz a6:')
print(a6)
b = np.cos(a6)
print('Cosinus dla kazdej wartosci macierzy a6:')
print(b)
print('########################')

#Zadanie 7
#Wykonaj funkcję dodawania obu macierzy zapisanych wcześniej do zmiennych a i b.
print('Zadanie 7')
print('Wynik dodawania macierzy a i b:')
print(np.add(a, b))
print('########################')

#Zadanie 8
#Wygeneruj macierz 3x3 i wyświetl w pętli każdy z rzędów
print('Zadanie 8')
a = np.arange(9).reshape((3, 3))
print(a)
i = 0
for b in a:
    print('Rzad', i, ':', b)
    i = i + 1
print('########################')

#Zadanie 9
#Wygeneruj macierz 3x3 i wyświetl w pętli każdy element korzystając z opcji “spłaszczenia”
#macierzy. (użyj funkcji flat())
print('Zadanie 9')
a = np.arange(9).reshape((3, 3))
print(a)
for b in a.flat:
    print(b)
print('########################')

#Zadanie 10
#Wygeneruj macierz 9x9 a następnie zmień jej kształt. Jakie mamy możliwości i dlaczego?
print('Zadanie 10')
a = np.arange(81).reshape((9, 9))
print(a)
b = a.reshape(3, 27)
print(b)
c = b.reshape(27, 3)
print(c)
d = c.ravel()
print(d)
print(d.shape)
print('########################')

#Zadanie 11
#Wygeneruj macierz płaską (wektor) i przekształć ją na macierz 3x4. Wygeneruj w ten sposób
#jeszcze kombinacje 4x3 i 2x6. Spłaszcz każdą z nich i wyświetl wyniki. Czy są identyczne?
print('Zadanie 11')
a = np.random.randint(0, 13, 12)
print(a)
mat1 = a.reshape((3, 4))
print('mat1:')
print(mat1)
mat2 = a.reshape((4, 3))
print('mat2:')
print(mat2)
mat3 = a.reshape((2, 6))
print('mat3:')
print(mat3)
print('mat1 splaszczona:')
print(mat1.flatten())
print('mat2 splaszczona:')
print(mat2.flatten())
print('mat3 splaszczona:')
print(mat3.flatten())
print('########################')
print('THE END')