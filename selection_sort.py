# Selection sort is a sorting algorithm that sorts an array by repeatedly finding the minimum element and putting them in ascending order. Selection sort in python does not require any extra space, so the sorting is done in place. The average time complexity of selection sort in python is O ( N 2 ) O(N^2) O(N2).

## Can you  write a program in selection sort algorithm in python and show how to run it ?

## In this implementation, the selection_sort function takes an array arr as input and sorts it in ascending order using the selection sort algorithm. It iterates over the array and for each iteration, finds the minimum element from the unsorted portion of the array and swaps it with the current element.

## In the example usage, we create an array numbers containing some random values. We then call the selection_sort function passing numbers as the argument. Finally, we print the sorted array after the function call.

## When you run this program, you should see the following output:



def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage
numbers = [5, 2, 8, 12, 1]
print("Before sorting:", numbers)
selection_sort(numbers)
print("After sorting:", numbers)
