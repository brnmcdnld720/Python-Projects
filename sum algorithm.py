import random

def load_array():
    target = input("What is the target number: ")
    length_arr = int(input("How long should the arrays be: "))

    arrA = [None] * length_arr
    arrB = [None] * length_arr

    for i in range(len(arrA)):
        arrA[i] = random.randint(1, 20)
    for i in range(len(arrB)):
        arrB[i] = random.randint(1, 20)
    return arrA, arrB, target

#arrA, arrB = load_array()
# load_array() will be for real use, debugging purposes we will
# select the appropriate numbers.
target = 12
arrA = [0, 2, 5, 1, 10]
arrB = [5, 2, 6, 4, 12]
print(arrA, arrB, 12)

