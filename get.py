import tkinter as tk
from tkinter import ttk
import math

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("เครื่องคิดเลขวิทยาศาสตร์")
        self.window.geometry("400x600")
        self.window.configure(bg='#f0f0f0')
        
        # สร้างตัวแปรเก็บค่า
        self.current = ''
        self.expression = ''
        
        # สร้างสไตล์สำหรับปุ่ม
        style = ttk.Style()
        style.configure('Calculator.TButton', 
                       padding=10, 
                       font=('Arial', 12),
                       width=8)
        
        # สร้างเฟรมหลัก
        main_frame = ttk.Frame(self.window, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # สร้างช่องแสดงผล
        self.expression_display = tk.Entry(main_frame, 
                                         width=30,
                                         font=('Arial', 12),
                                         justify='right',
                                         bg='#e8e8e8')
        self.expression_display.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky='ew')
        
        self.display = tk.Entry(main_frame,
                              width=30,
                              font=('Arial', 20, 'bold'),
                              justify='right',
                              bg='white')
        self.display.grid(row=1, column=0, columnspan=4, padx=5, pady=5, sticky='ew')
        
        # ปุ่มฟังก์ชันพิเศษ
        special_buttons = [
            'sin', 'cos', 'tan', '√',
            'x²', 'x³', 'π', 'e',
            '(', ')', 'mod', '^'
        ]
        
        # สร้างปุ่มฟังก์ชันพิเศษ
        row = 2
        col = 0
        for button in special_buttons:
            cmd = lambda x=button: self.click_special(x)
            ttk.Button(main_frame, 
                      text=button,
                      command=cmd,
                      style='Calculator.TButton'
                      ).grid(row=row, column=col, padx=2, pady=2)
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        # ปุ่มตัวเลขและเครื่องหมายพื้นฐาน
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        # สร้างปุ่มตัวเลขและเครื่องหมาย
        for button in buttons:
            cmd = lambda x=button: self.click(x)
            ttk.Button(main_frame,
                      text=button,
                      command=cmd,
                      style='Calculator.TButton'
                      ).grid(row=row, column=col, padx=2, pady=2)
            col += 1
            if col > 3:
                col = 0
                row += 1
                
        # ปุ่มล้างข้อมูล
        ttk.Button(main_frame,
                  text='C',
                  command=self.clear,
                  style='Calculator.TButton'
                  ).grid(row=row, column=0, columnspan=2, padx=2, pady=2, sticky='ew')
        
        # ปุ่มลบตัวเลขทีละหลัก
        ttk.Button(main_frame,
                  text='⌫',
                  command=self.backspace,
                  style='Calculator.TButton'
                  ).grid(row=row, column=2, columnspan=2, padx=2, pady=2, sticky='ew')

    def click_special(self, key):
        if key == 'sin':
            self.expression += 'math.sin(math.radians('
        elif key == 'cos':
            self.expression += 'math.cos(math.radians('
        elif key == 'tan':
            self.expression += 'math.tan(math.radians('
        elif key == '√':
            self.expression += 'math.sqrt('
        elif key == 'x²':
            self.expression += '**2'
        elif key == 'x³':
            self.expression += '**3'
        elif key == 'π':
            self.expression += 'math.pi'
        elif key == 'e':
            self.expression += 'math.e'
        elif key == 'mod':
            self.expression += '%'
        elif key == '^':
            self.expression += '**'
        else:
            self.expression += key
            
        self.current += key
        self.update_display()

    def click(self, key):
        if key == '=':
            try:
                # เพิ่มวงเล็บปิดสำหรับฟังก์ชันตรีโกณมิติ
                expr = self.expression
                while expr.count('(') > expr.count(')'):
                    expr += ')'
                    
                result = eval(expr)
                self.expression = str(result)
                self.current = str(result)
                self.update_display()
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
                self.expression = ''
                self.current = ''
        else:
            self.expression += key
            self.current += key
            self.update_display()

    def clear(self):
        self.display.delete(0, tk.END)
        self.expression_display.delete(0, tk.END)
        self.expression = ''
        self.current = ''

    def backspace(self):
        if self.current:
            # ลบตัวอักษรสุดท้ายของ expression และ current
            self.expression = self.expression[:-1]
            self.current = self.current[:-1]
            self.update_display()

    def update_display(self):
        # อัพเดตการแสดงผลทั้งสองช่อง
        self.expression_display.delete(0, tk.END)
        self.expression_display.insert(tk.END, self.expression)
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.current)

    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    calc = Calculator()
    calc.run()