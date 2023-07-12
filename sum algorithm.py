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

#hash the arrays keying in what the difference should be for 
#sum to reach target
def hash_up_array_solution(arrA, arrB, target):
    hash_map_arr = {}
    closest_numA = 0
    closest_numB = 0
    ans_list = []
    for num in arrA:
        diff_to_tar = target - num
        hash_map_arr.update({diff_to_tar: num})
    for num in arrB:
        if num in hash_map_arr:
            closest_numA = hash_map_arr.get(num)
            closest_numB = num
            ans_list.append([closest_numA, closest_numB])

    return ans_list

#arrA, arrB = load_array()
# load_array() will be for real use, debugging purposes we will
# select the appropriate numbers.
target = 12
arrA = [0, 2, 5, 1, 10, 8]
arrB = [5, 2, 6, 4, 12, 11]

print(hash_up_array_solution(arrA, arrB, target))

# print(arrA, arrB, 12)
correct_pair = [0, 12]

#sort the arrays built in .sort() is O(n log n)
# arrA.sort()
# arrB.sort()
# print(arrA, arrB)



