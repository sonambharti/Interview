'''
Implement a single excel sheet of data

Features:
Print entire excel sheet
Update value of a cell
Get value of a cell
Add Basic formulae such as add, subtract, multiply
Add range operations such as sum() over range.
Formatting of each cells - Bold, Italics, Underline, Strikethrough
Conditional functions based on other cells ()
Conditional formatting of cells
'''

import re 
import math

class Cell:
    def __init__(self, value = None):
        self.value = value
        self.format = {"bold": False, "italic": False, "Underline": False, "strike": False}
        
class Sheet:
    def __init__(self, rows, cols):
        self.grid = [[Cell(0) for _ in range(cols)] for _ in range(rows)]
        
    def print_sheet(self):
        for row in self.grid:
            print([cell.value for cell in row])
            # print([{"value":c.value, "format": c.format} for c in row])
            
    def update_cell(self, row, col, value):
        self.grid[row][col].value = value
        
    def get_cell(self, row, col):
        return self.grid[row][col].value
        
    def add(self, r1, c1, r2, c2, tr, tc):
        # return self.get_cell(r1,c1) + self.get_cell(r2, c2)
        num = self.get_cell(r1,c1)
        deno = self.get_cell(r2, c2)
        
        if not isinstance(num, (int, float)) or not isinstance(deno, (int, float)):
            print("Error: Non-numerc value(s) in cells")
            return
        add =  num + deno
        self.update_cell(tr,tc, add)
       
    def subtract(self, r1, c1, r2, c2, tr, tc):
        # return self.get_cell(r1,c1) - self.get_cell(r2, c2)
        num = self.get_cell(r1,c1)
        deno = self.get_cell(r2, c2)
        
        if not isinstance(num, (int, float)) or not isinstance(deno, (int, float)):
            print("Error: Non-numerc value(s) in cells")
            return
        subtract =  num - deno
        self.update_cell(tr,tc, subtract)
        
    def multiply(self, r1, c1, r2, c2, tr, tc):
        # return self.get_cell(r1,c1) * self.get_cell(r2, c2)
        num = self.get_cell(r1,c1)
        deno = self.get_cell(r2, c2)
        
        if not isinstance(num, (int, float)) or not isinstance(deno, (int, float)):
            print("Error: Non-numerc value(s) in cells")
            return
        multiply =  num * deno
        self.update_cell(tr,tc, multiply)
        
    def division(self, r1, c1, r2, c2, tr, tc):
        # return self.get_cell(r1,c1) / self.get_cell(r2, c2)
        num = self.get_cell(r1,c1)
        deno = self.get_cell(r2, c2)
        
        if not isinstance(num, (int, float)) or not isinstance(deno, (int, float)):
            print("Error: Non-numerc value(s) in cells")
            return
        
        if deno == 0:
            print("Error: Division can't be possible by zero.")
            return
        
        division =  num / deno
        division = round(division, 2)
        self.update_cell(tr,tc, division)
        
    def sum_range(self, r1, c1, r2, c2, tr, tc):
        # return sum(self.grid[r][c].value for r in range(r1, r2+1) for c in range(c1, c2+1))
        
        # summ = sum(self.grid[r][c].value for r in range(r1, r2+1) for c in range(c1, c2+1))
        summ = 0
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                val = self.grid[r][c].value
                if not isinstance(val, (int, float)):
                    print("Error: Non-numeric value(s) in cells")
                    return
                else:
                    summ += val
        self.update_cell(tr,tc, summ)
        
    def set_format(self, row, col, **kwargs):
        for key, value in kwargs.items():
            if key in self.grid[row][col].format:
                self.grid[row][col].format[key] = value
                
    
    # def conditional_func(self, source_cell, dest_cell, rules):
    #     for 
    
        

if __name__ == "__main__":
    sheet_obj = Sheet(5,5)
    # sheet_obj.print_sheet()
    sheet_obj.update_cell(0,0,2)
    sheet_obj.update_cell(1,0,2)
    sheet_obj.update_cell(2,0,0)
    sheet_obj.update_cell(3,0,1)
    sheet_obj.update_cell(0,1,1)
    sheet_obj.print_sheet()
    print()
    # sheet_obj.add(0,0,2,0,2,2)
    # sheet_obj.print_sheet()
    # sheet_obj.subtract(0,0,2,0,2,2)
    # sheet_obj.print_sheet()
    # sheet_obj.multiply(0,0,2,0,2,2)
    # sheet_obj.print_sheet()
    # sheet_obj.division(0,0,2,0,2,2)
    # sheet_obj.print_sheet()
    sheet_obj.sum_range(0,0,2,1,2,2)
    # sheet_obj.set_format(0,0,bold=True)
    sheet_obj.print_sheet()
    
    
        



