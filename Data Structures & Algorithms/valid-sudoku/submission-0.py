class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squareOne = set()
        squareTwo = set()
        squareThree = set()
        squareFour = set()
        squareFive = set()
        squareSix = set()
        squareSeven = set()
        squareEight = set()
        squareNine = set()

        # Test Rows
        for i in range(len(board)):
            row_nums = set()
            for j in range(len(board[0])):
                num = board[i][j]
                if num in row_nums:
                    print('Row Invalid')
                    print(row_nums)
                    return False
                if num != '.':
                    row_nums.add(num)
                if i < 3 and j < 3:
                    if num in squareOne:
                        print('squareOne invalid')
                        print(squareOne)
                        return False
                    if num != '.':
                        squareOne.add(num)
                if i < 3 and 3 <= j and j < 6:
                    if num in squareTwo:
                        print('squareTwo invalid')
                        print(squareTwo)
                        return False
                    if num != '.':
                        squareTwo.add(num)
                if i < 3 and 6 <= j:
                    if num in squareThree:
                        print('squareThree invalid')
                        print(squareThree)
                        return False
                    if num != '.':
                        squareThree.add(num)
                if 3 <= i and i < 6 and j < 3:
                    if num in squareFour:
                        print('squareFour invalid')
                        print(squareFour)
                        return False
                    if num != '.':
                        squareFour.add(num)
                if 3 <= i and i < 6 and 3 <= j and j < 6:
                    if num in squareFive:
                        print('squareFive invalid')
                        print(squareFive)
                        return False
                    if num != '.':
                        squareFive.add(num)
                if 3 <= i and i < 6 and 6 <= j:
                    if num in squareSix:
                        print('squareSix invalid')
                        print(squareOne)
                        return False
                    if num != '.':
                        squareSix.add(num)
                if 6 <= i and j < 3:
                    if num in squareSeven:
                        print('squareSeven invalid')
                        print(squareSeven)
                        return False
                    if num != '.':
                        squareSeven.add(num)
                if 6 <= i and 3 <= j and j < 6:
                    if num in squareEight:
                        print('squareEight invalid')
                        print(squareEight)
                        return False
                    if num != '.':
                        squareEight.add(num)
                if 6 <= i and 6 <= j:
                    if num in squareNine:
                        print('squareNine invalid')
                        print(squareNine)
                        return False
                    if num != '.':
                        squareNine.add(num)
            
            # Check Columns
            for j in range(len(board[0])):
                col_nums = set()
                for i in range(len(board)):
                    num = board[i][j]
                    if num in col_nums:
                        return False
                    if num != '.':
                        col_nums.add(num)
                
        return True
        