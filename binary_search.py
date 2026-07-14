"""Binary search implementation for sorted lists."""

def binary_search(arr, target):
    """Return index of target in sorted arr, or -1 if not found."""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    numbers = [1, 3, 5, 7, 9, 11, 13]
    target = 7
    index = binary_search(numbers, target)
    print(f"Array: {numbers}")
    print(f"Target {target} found at index: {index}")
