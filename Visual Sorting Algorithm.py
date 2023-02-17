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
# Input Values
# Menu
# Displaying Sort Graph