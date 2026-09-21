class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        store= set()
        for i in range(9):
            for j in range(9):
                num=board[i][j]

                if num== ".":
                    continue
                #using tuple for creating key value
                row_key=(num,'row',i)
                col_key=(num,'col',j)
                box_key=(num,'box',i//3,j//3)
                
                if row_key in store or col_key in store or box_key in store:
                    return False

                store.add(row_key)
                store.add(col_key)
                store.add(box_key)
        return True