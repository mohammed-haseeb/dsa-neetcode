class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, len(nums) - 1

            while j < k:
                current_sum = nums[i] + nums[j] + nums[k]

                if current_sum == 0:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j += 1
                    # skip duplicate j values after finding a valid triplet
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                elif current_sum < 0:
                    j += 1
                else:
                    k -= 1

        return triplets