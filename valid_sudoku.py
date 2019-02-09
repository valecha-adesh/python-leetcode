#Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

#Each row must contain the digits 1-9 without repetition.
#Each column must contain the digits 1-9 without repetition.
#Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

class Solution:

#    def c_list(self,l):
#        for x in range(9):
#            if l.count(str(x)) > 1:
#                return False
#            else:
#                return True

                
    
    def isValidSudoku(self, board: 'List[List[str]]') -> 'bool':
        
        for i in range(9):
            for x in range(1,10):
                if board[i].count(str(x)) > 1:
                    return False
        
        for i in range(9):
            temp = []
            for j in range(9):
                temp.append(board[j][i])  
            for x in range(1,10):
                if temp.count(str(x)) > 1:
                    return False
        
        
        temp_00 = []
        for i in range(3):
            for j in range(3):
                    temp_00.append(board[i][j])
        
        for x in range(1,10):
            if temp_00.count(str(x)) > 1:
                return False
            
                    
        
        temp_10 = []
        for i in range(3,6):
            for j in range(3):
                    temp_10.append(board[i][j])
        
        for x in range(1,10):
            if temp_10.count(str(x)) > 1:
                return False
            
            
        temp_20 = []
        for i in range(6,9):
            for j in range(3):
                    temp_20.append(board[i][j])
        
        for x in range(1,10):
            if temp_20.count(str(x)) > 1:
                return False
            
            
            
        temp_01 = []
        for i in range(3):
            for j in range(3,6):
                    temp_01.append(board[i][j])
        
        for x in range(1,10):
            if temp_01.count(str(x)) > 1:
                return False
            
            
        temp_11 = []
        for i in range(3,6):
            for j in range(3,6):
                    temp_11.append(board[i][j])
        
        for x in range(1,10):
            if temp_11.count(str(x)) > 1:
                return False
            
            
        temp_21 = []
        for i in range(6,9):
            for j in range(3,6):
                    temp_21.append(board[i][j])
        
        for x in range(1,10):
            if temp_21.count(str(x)) > 1:
                return False
            
            
        temp_02 = []
        for i in range(3):
            for j in range(6,9):
                    temp_02.append(board[i][j])
        
        for x in range(1,10):
            if temp_02.count(str(x)) > 1:
                return False
            
            
        temp_12 = []
        for i in range(3,6):
            for j in range(6,9):
                    temp_12.append(board[i][j])
        
        for x in range(1,10):
            if temp_12.count(str(x)) > 1:
                return False
            
            
        temp_22 = []
        for i in range(6,9):
            for j in range(6,9):
                    temp_22.append(board[i][j])
        
        for x in range(1,10):
            if temp_22.count(str(x)) > 1:
                return False
            
        return True
