'''
Q: Given an array, rotate the array to the right by k steps, where k is non-negative.
'''

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        #Do not return anything, modify nums in-place instead.
        
        ''' 
        popping it from the beginning(pop also removes the element from the list) and appending each popped element to the end
        '''
        nums.reverse()
        for i in range(k):
            nums.append(nums.pop(0)) 
        nums.reverse()