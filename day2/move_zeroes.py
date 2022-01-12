from collections import deque
class MoveZeroesWithQueue:
    def move_zeroes(self, nums: List[int]) -> None:
        queue = deque()
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                queue.append(i)
            else:
                if len(queue) > 0:
                    zero_index = queue.popleft()
                    nums[zero_index], nums[i] = nums[i], nums[zero_index]
                    queue.append(i)
            i += 1

class MoveZeroes:
    def move_zeroes(self, nums: List[int]) -> None:
        zero_pointer, iterative_pointer = 0, 0 
        while iterative_pointer < len(nums):
            if nums[iterative_pointer] != 0:
                nums[zero_pointer], nums[iterative_pointer] = nums[iterative_pointer], nums[zero_pointer]
                zero_pointer += 1
            iterative_pointer += 1