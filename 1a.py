def corrected_max_arr(arr):
    if not arr:
        return 0  # or float('-inf') depending on design

    max_sum = float('-inf')  # Supports negative values
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            total = 0
            for k in range(i, j + 1):  # ✅ FIXED: Include j
                total += arr[k]
            max_sum = max(max_sum, total)
    return max_sum

# Test Cases
print("Corrected Output (All Negatives):", corrected_max_arr([-2, -1, -3]))  # ✅ Expected: -1
print("Corrected Output (Mixed):", corrected_max_arr([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # ✅ Expected: 6
