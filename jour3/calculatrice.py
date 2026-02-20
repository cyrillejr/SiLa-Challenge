import tkinter as tk
from tkinter import messagebox
import ast
import operator
import math

class CalculatriceSecurisee:
    def __init__(self, root):
        self.root = root
        self.root.title("Cyrille - SecCalc Jour 3")
        self.root.geometry("400x600")
        self.root.configure(bg="#1e1e1e")
        
        self.equation = ""
        
        self.operators = {
            ast.Add: operator.add, ast.Sub: operator.sub, 
            ast.Mult: operator.mul, ast.Div: operator.truediv, 
            ast.Pow: operator.pow, ast.BitXor: operator.xor,
            ast.USub: operator.neg
        }
        
        self.functions = {
            'sin': math.sin, 'cos': math.cos, 'tan': math.tan,
            'log': math.log10, 'sqrt': math.sqrt, 'pi': math.pi
        }

        self.setup_ui()

    def setup_ui(self):
        self.display = tk.Entry(self.root, font=("Courier", 22), bd=0, bg="#2d2d2d", fg="#61afef", justify='right')
        self.display.pack(fill="both", padx=10, pady=20)

        self.history = tk.Listbox(self.root, height=5, bg="#1e1e1e", fg="#98c379", borderwidth=0)
        self.history.pack(fill="both", padx=10)
        
        btn_frame = tk.Frame(self.root, bg="#1e1e1e")
        btn_frame.pack(fill="both", expand=True, padx=5, pady=5)

        btns = [
            'sin', 'cos', 'tan', '/',
            'log', '(', ')', '*',
            '7', '8', '9', '-',
            '4', '5', '6', '+',
            '1', '2', '3', '=',
            '0', '.', 'C', 'sqrt'
        ]

        r, c = 0, 0
        for b in btns:
            cmd = lambda x=b: self.on_click(x)
            tk.Button(btn_frame, text=b, font=("Arial", 12, "bold"), bg="#3e4451", fg="white",
                      command=cmd, height=2).grid(row=r, column=c, sticky="nsew", padx=2, pady=2)
            c += 1
            if c > 3: c = 0; r += 1

        for i in range(4): btn_frame.columnconfigure(i, weight=1)
        for i in range(6): btn_frame.rowconfigure(i, weight=1)

    def on_click(self, char):
        if char == "=": self.calculer()
        elif char == "C": self.display.delete(0, tk.END)
        else: self.display.insert(tk.END, char)

    def safe_eval(self, node):
        if isinstance(node, ast.Num):  # <number>
            return node.n
        elif isinstance(node, ast.BinOp):  # <left> <operator> <right>
            return self.operators[type(node.op)](self.safe_eval(node.left), self.safe_eval(node.right))
        elif isinstance(node, ast.UnaryOp):  # -<number>
            return self.operators[type(node.op)](self.safe_eval(node.operand))
        elif isinstance(node, ast.Call):  # function()
            func_name = node.func.id
            if func_name in self.functions:
                args = [self.safe_eval(arg) for arg in node.args]
                return self.functions[func_name](*args)
        elif isinstance(node, ast.Name): # Constantes comme pi
            if node.id in self.functions: return self.functions[node.id]
        
        raise TypeError(f"Action non autorisée : {node}")

    def calculer(self):
        expr = self.display.get()
        try:
            tree = ast.parse(expr, mode='eval')
            resultat = self.safe_eval(tree.body)
            
            self.history.insert(tk.END, f"{expr} = {resultat}")
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(resultat))
        except Exception as e:
            messagebox.showerror("Sécurité", f"Entrée invalide ou bloquée")

if __name__ == "__main__":
    root = tk.Tk()
    CalculatriceSecurisee(root)
    root.mainloop()
