"""
Bubble Sort Implementation
A simple sorting algorithm that repeatedly steps through the list,
compares adjacent elements and swaps them if they are in the wrong order.
"""

def bubble_sort(arr):
    """
    Sort an array using bubble sort algorithm
    
    Args:
        arr: List of comparable elements
    
    Returns:
        None (sorts in-place)
    
    Time Complexity: O(n²)
    Space Complexity: O(1)
    """
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Flag to optimize - if no swapping occurs, array is sorted
        swapped = False
        
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no two elements were swapped, then array is sorted
        if not swapped:
            break

def bubble_sort_with_steps(arr):
    """
    Bubble sort with step-by-step visualization for learning
    """
    n = len(arr)
    print(f"Initial array: {arr}")
    
    for i in range(n):
        print(f"\nPass {i + 1}:")
        swapped = False
        
        for j in range(0, n - i - 1):
            print(f"  Comparing {arr[j]} and {arr[j + 1]}")
            
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                print(f"  Swapped! Array: {arr}")
            else:
                print(f"  No swap needed")
        
        if not swapped:
            print(f"  No swaps in this pass - array is sorted!")
            break
        
        print(f"  End of pass {i + 1}: {arr}")
    
    print(f"\nFinal sorted array: {arr}")

# Example usage
if __name__ == "__main__":
    # Test with sample data
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print("Bubble Sort Example")
    print("=" * 20)
    
    # Make a copy for demonstration
    demo_array = test_array.copy()
    bubble_sort_with_steps(demo_array)
    
    # Test with different cases
    print("\n" + "=" * 40)
    print("Testing different cases:")
    
    # Already sorted array
    sorted_arr = [1, 2, 3, 4, 5]
    print(f"\nAlready sorted: {sorted_arr}")
    bubble_sort(sorted_arr)
    print(f"After bubble sort: {sorted_arr}")
    
    # Reverse sorted array
    reverse_arr = [5, 4, 3, 2, 1]
    print(f"\nReverse sorted: {reverse_arr}")
    bubble_sort(reverse_arr)
    print(f"After bubble sort: {reverse_arr}")
    
    # Array with duplicates
    dup_arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print(f"\nWith duplicates: {dup_arr}")
    bubble_sort(dup_arr)
    print(f"After bubble sort: {dup_arr}")