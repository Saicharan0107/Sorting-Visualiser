import time
import random
import matplotlib.pyplot as plt

n = 100
nums = []
gap=4

def mergeSort(nums, startIndex, endIndex):
    if endIndex > startIndex:
        mid = (startIndex + endIndex) // 2
        mergeSort(nums, startIndex, mid)
        mergeSort(nums, mid + 1, endIndex)
        merge(nums, startIndex, endIndex, mid)
        plt.bar([i for i in range(len(nums))], nums,edgecolor='black')
        plt.title("Sorting in progress")
        plt.show(block=False)
        plt.pause(0.1) 
        plt.clf()
    return nums

def merge(nums, startIndex, endIndex, mid):
    left = nums[startIndex:mid + 1]
    right = nums[mid + 1:endIndex + 1]
    i, j, k = 0, 0, startIndex
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        nums[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        nums[k] = right[j]
        j += 1
        k += 1
    return nums

def main():
    global nums
    for i in range(1, n + 1):
        nums.append(i)
    random.seed(time.time())
    random.shuffle(nums)

    print('Initial array:')
    print(nums)
    plt.bar([i for i in range(len(nums))], nums,edgecolor='black')
    plt.show(block=False)
    plt.pause(0.1)
    plt.clf()

    mergeSort(nums, 0, n - 1)

    print("Sorted Array:")
    for i in range(n):
        print(nums[i], end=" ")
    print()

    plt.bar([i for i in range(len(nums))], nums,color='green',edgecolor='black')
    plt.title("Sorted array")
    plt.show(block=False)
    plt.pause(5)
    plt.clf()

main()
