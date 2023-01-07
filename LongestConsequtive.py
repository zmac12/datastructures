class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ### Optimal solution requires some intuition around the first number in the sequence. We don't have to check numbers that are already part of a longer sequence if we first check that the number immediately preceding the sequence is not a part of a streak already. We just pass by numbers that have a preceding number as they will be counted during their preceding number's streak build. The while loop is only reached when building sequences.
        longest_streak = 0
        num_set = set(nums)
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak +=1
                
                longest_streak = max(longest_streak, current_streak)
                
        return longest_streak