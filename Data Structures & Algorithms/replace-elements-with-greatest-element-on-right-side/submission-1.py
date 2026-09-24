class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        last= arr[-1]
        for i in range(len(arr)-2, -1, -1):
            current= arr[i] if arr[i]> last else last
            arr[i]= last
            last= current
        arr[-1]= -1
        return arr