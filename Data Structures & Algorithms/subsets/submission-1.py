class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sols = []
        n = len(nums)
        def dfs(idx: int, candidate: list[int]):
            if idx >= n:
                sols.append(candidate.copy())
                return

            candidate.append(nums[idx])
            dfs(idx + 1, candidate)
            candidate.pop()
            dfs(idx + 1, candidate)
        dfs(0, [])
        return sols