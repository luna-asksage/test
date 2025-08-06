def bubble_sort(arr):
    """
    Bubble Sort Algorithm Implementation
    
    This function sorts an array using the bubble sort algorithm.
    Time Complexity: O(n²) in worst and average case, O(n) in best case
    Space Complexity: O(1)
    
    Args:
        arr (list): List of comparable elements to be sorted
        
    Returns:
        list: Sorted list in ascending order
    """
    # Make a copy of the array to avoid modifying the original
    arr_copy = arr.copy()
    n = len(arr_copy)
    
    # Traverse through all array elements
    for i in range(n):
        # Flag to optimize - if no swapping occurs, array is sorted
        swapped = False
        
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                swapped = True
        
        # If no two elements were swapped by inner loop, array is sorted
        if not swapped:
            break
    
    return arr_copy


def bubble_sort_descending(arr):
    """
    Bubble Sort Algorithm Implementation for Descending Order
    
    Args:
        arr (list): List of comparable elements to be sorted
        
    Returns:
        list: Sorted list in descending order
    """
    arr_copy = arr.copy()
    n = len(arr_copy)
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):
            # Change comparison for descending order
            if arr_copy[j] < arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                swapped = True
        
        if not swapped:
            break
    
    return arr_copy


# Example usage and testing
if __name__ == "__main__":
    # Test cases
    test_arrays = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 4, 6, 1, 3],
        [1],  # Single element
        [],   # Empty array
        [1, 1, 1, 1],  # All same elements
        [5, 4, 3, 2, 1]  # Reverse sorted
    ]
    
    print("Bubble Sort Algorithm Testing")
    print("=" * 40)
    
    for i, arr in enumerate(test_arrays, 1):
        print(f"Test {i}:")
        print(f"Original:  {arr}")
        print(f"Ascending: {bubble_sort(arr)}")
        print(f"Descending: {bubble_sort_descending(arr)}")
        print("-" * 30)