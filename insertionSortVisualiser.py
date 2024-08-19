import time
import random
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

nums=[]
n=50
gap=4
colors=['blue']*n

def insertSort(nums,n):
    for i in range(0,n):
        curr=nums[i]
        j=i-1
        while j>=0 and nums[j]>curr:
            nums[j+1]=nums[j]
            nums[j]=curr
            colors[j]='yellow'
            j=j-1
            plt.bar([i for i in range(len(nums))],nums,color=colors,edgecolor='black')
            plt.title("Sorting in progress")
            plt.show(block=False)
            plt.pause(0.001)
            plt.clf()
            colors[j+1]='blue'
         
        
def main():
    for i in range(1,n+1):
        nums.append(i)
    random.seed(time.time())
    random.shuffle(nums)
    print('Initial array:')
    print(nums)
    plt.bar([i for i in range(len(nums))],nums)
    plt.show(block=False)
    plt.pause(0.01)
    plt.clf()

    insertSort(nums,n)

    print("Sorted Array:")
    for i in range(n):
      print(nums[i],end=" ")
    print()
    
    plt.bar([i for i in range(len(nums))], nums,color='green',edgecolor='black')
    plt.title("Sorted array")
    plt.show(block=False)
    plt.pause(5)
    plt.clf()

main()