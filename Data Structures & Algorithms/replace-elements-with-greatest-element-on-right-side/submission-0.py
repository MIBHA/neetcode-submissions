class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_elem=-1
        for i in range(len(arr)-1, -1,-1):
            current= arr[i]
            arr[i]= max_elem
            max_elem= max(max_elem, current)
        return arr
           
