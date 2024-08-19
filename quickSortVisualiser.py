import random
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import time

# Recursive QuickSort function
def quickSortRecursive(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quickSortRecursive(arr, low, p - 1)
        quickSortRecursive(arr, p + 1, high)

# Function to partition the array with the first element as pivot
def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1

    for j in range(low + 1, high + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            visualize(arr, 'Sorting in Progress (sorting the sub array with colors(r-b-y))', low, i-1, high)

    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    visualize(arr, 'Sorting in Progress (sorting the sub array with colors(r-b-y))', low, i-1, high)
    return i - 1

# Function to visualize the array
def visualize(arr, title, pivot_index, boundary_index, high):
    colors = ['none'] * len(arr)  # Initialize all elements to have no color
    for i in range(high + 1):
        if i<pivot_index:
            colors[i]='g'    #elements that are sorted
        elif i == pivot_index:
            colors[i] = 'r'  # Pivot in red
        elif i <= boundary_index:
            colors[i] = 'b'  # Smaller elements in blue
        else:
            colors[i] = 'yellow'  # Larger elements in yellow
    
    plt.bar(range(len(arr)), arr, color=colors, edgecolor='black', width=1.0)
    plt.title(title)
    
    # Create custom legend handles
    sorted_patch=mpatches.Patch(color='g', label='Sorted Subarray')
    pivot_patch = mpatches.Patch(color='r', label='Pivot (red)')
    smaller_patch = mpatches.Patch(color='b', label='Smaller elements than pivot(blue)')
    larger_patch = mpatches.Patch(color='yellow', label='Larger elements than pivot and Unclassified elements (yellow)')
    
    plt.legend(handles=[sorted_patch,pivot_patch, smaller_patch, larger_patch], loc='upper left',fontsize='small')
    plt.draw()
    plt.pause(0.25)
    plt.clf()

def main():
    size = 100
    numbers = list(range(1, size + 1))
    random.seed(time.time())
    random.shuffle(numbers)

    # Initial plot of numbers
    plt.bar(range(len(numbers)), numbers, color='none', edgecolor='black', width=1.0)
    plt.title('Initial Array')
    plt.show(block=False)
    plt.pause(1)
    plt.clf()

    # Call recursive quicksort
    quickSortRecursive(numbers, 0, size - 1)

    # Final plot of numbers
    plt.bar(range(len(numbers)), numbers, color='g', edgecolor='black', width=1.0)
    plt.title('Sorted Array')
    plt.show(block=False)
    plt.pause(5)
    plt.clf()

    # Print sorted numbers
    print(numbers)

main()
