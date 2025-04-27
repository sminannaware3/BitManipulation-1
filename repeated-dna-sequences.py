# Time O(2n)
# Space O(n)
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        smap = defaultdict(int)
        for i in range(n-9):
            smap[s[i:i+10]] += 1
        
        result = []
        for key, val in smap.items():
            if val > 1:
                result.append(key)
        
        return result

# Time O(n)
# Space O(2n)
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
       # print(n)
        sset = set()
        result = set()
        for i in range(n-9):
            substr = s[i:i+10]
            if substr in sset:
                result.add(substr)
            else:
                sset.add(substr)
        
        return list(result)

# Time O(n)
# Space O(2n)
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n < 10: return []
        # Rolling Hash
        cmap = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
        shashset = set()
        result = set()
        currHash = 0
        for i in range(10):
            ch = s[i]
            currHash = currHash * 10 + cmap[ch]
        shashset.add(currHash)
        for i in range(1, n - 9):
            # outgoing char
            ch = s[i-1]
            currHash = currHash - (cmap[ch] * (10 ** 9))
            # incoming char
            ch = s[i+9]
            currHash = currHash * 10 + cmap[ch]
            
            if currHash in shashset:
                result.add(s[i: i+10])
            else:
                shashset.add(currHash)

        return list(result)
