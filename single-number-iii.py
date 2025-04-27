# Time O(2n)
# Space O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        bitmask = 0
        for num in nums:
            bitmask ^= num
        
        leastSignificantBit = bitmask & (-bitmask)

        bitmask2 = 0
        for num in nums:
            if (num & leastSignificantBit) != 0:
                bitmask2 ^= num
        return [bitmask2, bitmask ^ bitmask2]

# Time O(n)
# Time O(n)
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        nmap = set()
        for num in nums:
            if num in nmap:
                nmap.remove(num)
            else:
                nmap.add(num)
        return list(nmap)
