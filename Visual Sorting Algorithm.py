# Visual Sorting Algorithm
# Brand New Improvements

# Import Packages
import matplotlib.pyplot as plt
import numpy as np
import random

# Bubble Sort
def BubbleSort(amount):
    lst = np.random.randint(0, 100, amount)
    x = np.arange(0, amount, 1)
    n = len(lst)

    for i in range(n):
        for j in range(0, n - i - 1):
            plt.bar(x, lst)
            plt.pause(0.001)
            plt.clf()
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    plt.show()

# Insertion Sort
def InsertionSort(amount):
    lst = np.random.randint(0, 100, amount)
    x = np.arange(0, amount, 1)

    n = len(lst)

    for k in range(1, n):
        key = lst[k]
        l = k - 1
        while l >= 0 and key < lst[l]:
            lst[l + 1] = lst[l]
            l = l - 1
            plt.bar(x, lst)
            plt.pause(0.001)
            plt.clf()
        else:
            lst[l + 1] = key

    plt.show()

# Selection Sort
def SelectionSort(amount):
    lst = np.random.randint(0, 100, amount)
    x = np.arange(0, amount, 1)
    n = len(lst)

    for i in range(0, n - 1):
        smallest = i
        for j in range(i + 1, n):
            plt.bar(x, lst)
            plt.pause(0.001)
            plt.clf()
            if lst[j] < lst[smallest]:
                smallest = j
        lst[i], lst[smallest] = lst[smallest], lst[i]
    plt.show()

# Merge Sort
def MergeSort(amount):
    num = [random.randint(0, 1000) for _ in range(amount)]

    def merge_sort(lst, left, right):

        if left >= right:
            return

        mid = (left + right) // 2

        plt.bar(list(range(amount)), lst)
        plt.pause(0.001)
        plt.clf()

        merge_sort(lst, left, mid)
        merge_sort(lst, mid + 1, right)

        plt.bar(list(range(amount)), lst)
        plt.pause(0.001)
        plt.clf()

        merge(lst, left, right, mid)
        plt.bar(list(range(amount)), lst)
        plt.pause(0.001)
        plt.clf()

    def merge(lst, left, right, mid):

        l_cy = lst[left:mid + 1]
        r_cy = lst[mid + 1:right + 1]

        l_cou = r_cou = 0

        count = left

        while l_cou < (len(l_cy)) and r_cou < (len(r_cy)):
            if l_cy[l_cou] <= r_cy[r_cou]:
                lst[count] = l_cy[l_cou]
                l_cou += 1
            else:
                lst[count] = r_cy[r_cou]
                r_cou += 1

            count += 1

        while l_cou < (len(l_cy)):
            lst[count] = l_cy[l_cou]
            l_cou += 1
            count += 1

        while l_cou < (len(r_cy)):
            lst[count] = r_cy[r_cou]
            r_cou += 1
            count += 1

    merge_sort(num, 0, len(num) - 1)
    plt.bar(list(range(amount)), num)
    plt.show()

# Input Values
amount = int(input('Enter an integer: '))

if amount <= 10:
    amount = 15

# Menu
sort = int(input('''~~~MENU~~~
\t 1.) Bubble Sort
\t 2.) Selection Sort
\t 3.) Insertion Sort
\t 4.) Merge Sort
Enter: '''))

# Displaying Sort Graph