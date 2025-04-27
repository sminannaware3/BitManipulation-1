# Time O(n)
# Space O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = nums[0]
        for num in nums[1:]:
            result ^= num # XOR
        return result 

# Time O(n)
# Space O(n/2)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nmap = set()
        for num in nums:
            if num not in nmap:
                nmap.add(num)
            else: nmap.remove(num)
        return list(nmap)[0]