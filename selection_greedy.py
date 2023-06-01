
A = [64, 25, 12, 22, 11]

for i in range(len(A)):
    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j
    A[i], A[min_idx] = A[min_idx], A[i]
    
print ("Sorted array : ")
for i in range(len(A)):
    print("%d" %A[i],end=" ")







# def greedy_selection_sort(arr):
#     sorted_arr = []
#     while len(arr) > 0:
#         min_val = float('inf')  # Initialize minimum value as positive infinity
#         min_index = -1

#         # Find the minimum element in the remaining unsorted array
#         for i in range(len(arr)):
#             if arr[i] < min_val:
#                 min_val = arr[i]
#                 min_index = i

#         # Remove the minimum element from the unsorted array and append it to the sorted array
#         sorted_arr.append(arr.pop(min_index))

#     return sorted_arr

# # Example usage:
# arr = [64, 25, 12, 22, 11]
# sorted_arr = greedy_selection_sort(arr)
# print(sorted_arr)  
# # Output: [11, 12, 22, 25, 64]














# The selection sort algorithm is not typically implemented using a greedy search approach. Instead, 
# it uses an iterative process to find the minimum element in each iteration and places it in its correct position.

# However, if you're specifically interested in exploring a greedy search variation for selection sort, you could adapt the algorithm as follows:

# Start with an unsorted array.
# Initialize an empty sorted array.
# While the unsorted array is not empty:
# a. Find the minimum element in the unsorted array using a greedy approach (e.g., selecting the smallest element).
# b. Remove the minimum element from the unsorted array.
# c. Append the minimum element to the sorted array.
# Return the sorted array.