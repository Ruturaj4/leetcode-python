# decompress-run-length-encoded-list

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        out = []
        for i in range(0, len(nums),2):
            out.extend([nums[i+1]]*nums[i])
        return out

# solution 2:
# Idea is taken from someone in the comment section
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        return sum([[nums[i+1]]*nums[i] for i in range(0, len(nums),2)],[])
