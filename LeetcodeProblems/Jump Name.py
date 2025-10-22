class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i in range(len(nums)):
            # If the current index is beyond the farthest reachable index, we cannot proceed
            if i > max_reach:
                return False
            # Update the farthest index reachable from the current position
            max_reach = max(max_reach, i + nums[i])
            # If max_reach is greater than or equal to the last index, we can reach the end
            if max_reach >= len(nums) - 1:
                return True
        # This part is technically not needed if the loop condition `i > max_reach` is handled correctly,
        # but is included for completeness as some implementations return based on this line.
        # The loop will break early if the end is reached, so if it completes, it means the end was reached.
        return True
