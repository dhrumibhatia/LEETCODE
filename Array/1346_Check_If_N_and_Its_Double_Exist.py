class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i != j and arr[i] == 2 * arr[j]:
                    return True
        return False

# Time Complexity: O(n^2) - We have a nested loop iterating over the array.
# Space Complexity: O(1) - No extra space is used except for a few variables.

class Solution:
    def checkIfExist(self, arr):
        seen = set()
        for num in arr:
            if num * 2 in seen or num / 2 in seen:
                return True
            seen.add(num)
        return False

# Time Complexity: O(n) - We iterate over the array once.
# Space Complexity: O(n) - We use a set to store the elements we have seen.