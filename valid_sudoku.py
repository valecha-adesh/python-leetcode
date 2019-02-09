#Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

#Each row must contain the digits 1-9 without repetition.
#Each column must contain the digits 1-9 without repetition.
#Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

class Solution:
    def isValidSudoku(self, board: 'List[List[str]]') -> 'bool':
        
        def c_list(self,l:'List[str]'):
            for x in range(1,10):
                if l.count(str(x)) > 1:
                    return False
            return True
        
        for i in range(9):
            res = c_list(self,board[i])
            if res == False:
                return False
        
        for i in range(9):
            temp = []
            for j in range(9):
                temp.append(board[j][i])  
            
            res = c_list(self,temp)
            if res == False:
                return False
            
        
        
        temp_00 = []
        for i in range(3):
            for j in range(3):
                    temp_00.append(board[i][j])
                    
        res = c_list(self,temp_00)
        if res == False:
            return False
          
                    
        
        temp_10 = []
        for i in range(3,6):
            for j in range(3):
                    temp_10.append(board[i][j])
        
                    
        res = c_list(self,temp_10)
        if res == False:
            return False
                    
        temp_20 = []
        for i in range(6,9):
            for j in range(3):
                    temp_20.append(board[i][j])
                  
        res = c_list(self,temp_20)
        if res == False:
            return False
            
            
        temp_01 = []
        for i in range(3):
            for j in range(3,6):
                    temp_01.append(board[i][j])
            
        res = c_list(self,temp_01)
        if res == False:
            return False
            
        temp_11 = []
        for i in range(3,6):
            for j in range(3,6):
                    temp_11.append(board[i][j])
            
        res = c_list(self,temp_11)
        if res == False:
            return False
            
        temp_21 = []
        for i in range(6,9):
            for j in range(3,6):
                    temp_21.append(board[i][j])

        res = c_list(self,temp_21)
        if res == False:
            return False
            
        temp_02 = []
        for i in range(3):
            for j in range(6,9):
                    temp_02.append(board[i][j])
            
        res = c_list(self,temp_02)
        if res == False:
            return False
            
        temp_12 = []
        for i in range(3,6):
            for j in range(6,9):
                    temp_12.append(board[i][j])
            
        res = c_list(self,temp_12)
        if res == False:
            return False
            
        temp_22 = []
        for i in range(6,9):
            for j in range(6,9):
                    temp_22.append(board[i][j])
            
        res = c_list(self,temp_22)
        if res == False:
            return False
        
            
        return True
