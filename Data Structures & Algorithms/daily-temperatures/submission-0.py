class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result= [0]* len(temperatures)
        stack= []  #pair of temp and index
        for i, t in enumerate(temperatures):
            while stack and t>stack[-1][0]:  #stack[-1] is top of the stack and stack[0] is first value in teh pair 
                stackT, stackInd= stack.pop()
                result[stackInd]= (i- stackInd)
            stack.append([t, i])
        return result