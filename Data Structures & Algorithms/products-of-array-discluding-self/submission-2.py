class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        solution: List[int] = []
        for num in nums:
            result: int = 1
            buffer: List[int] = nums.copy()
            buffer.remove(num)
            for n in buffer:
                result *= n
            else:
                solution.append(result)
        return solution