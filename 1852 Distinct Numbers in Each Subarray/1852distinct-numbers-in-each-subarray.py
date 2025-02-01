class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        mapping = defaultdict(int)
        ans = []
        left = 0

        for right in range(k):
            mapping[nums[right]] += 1

        ans.append(len(mapping))

        for right in range(k, len(nums)):
            mapping[nums[left]] -= 1
            mapping[nums[right]] += 1

            if mapping[nums[left]] == 0:
                del mapping[nums[left]]
            
            ans.append(len(mapping))
            left += 1
        
        return ans