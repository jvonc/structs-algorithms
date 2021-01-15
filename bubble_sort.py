def bubbleSort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j + 1] < array[j]:
                array[j + 1], array[j] = array[j], array[j + 1]

def main():
    test_array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    bubbleSort(test_array)
    print(test_array)

main()