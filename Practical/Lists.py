from math import sqrt

squares = [4, 9, 16, 25]
iteration = 0

squares.append(49)
squares.append(64)
squares.append(81)
squares.extend([121, 144, 169])

for i in range(11):
    print(squares[iteration])
    print("Square root -", sqrt(squares[iteration]))
    iteration = iteration + 1
