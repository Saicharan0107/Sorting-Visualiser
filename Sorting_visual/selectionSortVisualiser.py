import time
import random
import matplotlib.pyplot as plt 

nums=[]
n=100
gap=4
colors=['blue']*n
def swap(x,y):
    return y,x

def selectSort(nums):
    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if nums[j]<nums[min_index]:
                min_index=j
        
        colors[min_index]='yellow'
        
        plt.bar([i for i in range(len(nums))],nums,color=colors,edgecolor='black')
        plt.title("Sorting in progress")
        plt.show(block=False)
        plt.pause(0.4)
        plt.clf()
        nums[min_index],nums[i]=nums[i],nums[min_index]
        colors[min_index]='blue'
        #print(nums)

def main():
    for i in range(1,n+1):
        nums.append(i)

    random.seed(time.time())
    random.shuffle(nums)

    print('Initial array:')
    print(nums)
    plt.bar([i for i in range(len(nums))],nums)
    plt.show(block=False)
    plt.pause(0.1)
    plt.clf()

    selectSort(nums)

    print("Sorted Array:")
    for i in range(n):
      print(nums[i],end=" ")
    print()
    plt.bar([i for i in range(len(nums))],nums,color='green',edgecolor='black')
    plt.title("Sorted array")
    plt.show(block=False)
    plt.pause(5)
    plt.clf()

main()
        