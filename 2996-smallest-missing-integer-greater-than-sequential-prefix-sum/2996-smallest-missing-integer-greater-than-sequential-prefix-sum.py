class Solution(object):
    def missingInteger(self, nums):
        # Step 1: Sequential prefix ka sum
        total = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
            else:
                break

        # Step 2: Array ke elements ko set me store
        nums_set = set(nums)

        # Step 3: Missing number find karo
        while total in nums_set:
            total += 1

        return total