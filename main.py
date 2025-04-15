import tkinter as tk
from tkinter import messagebox
import sqlite3

# Função que sempre cria a tabela caso não exista
def conectar():
    conn = sqlite3.connect('estoque.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS produtos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        codigo TEXT NOT NULL UNIQUE,
                        quantidade INTEGER NOT NULL,
                        valor REAL NOT NULL)''')
    conn.commit()
    return conn, cursor

class StockWiseApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("StockWise - Gestão de Estoque")
        self.geometry("450x550")
        self.configure(bg="#F0F0F0")
        self.create_main_menu()

    def create_main_menu(self):
        tk.Label(self, text="Bem-vindo ao StockWise!", font=("Arial", 18, "bold"), bg="#F0F0F0").pack(pady=20)

        botoes = [
            ("Cadastrar Produto", self.cadastro_produto),
            ("Visualizar Estoque", self.view_estoque),
            ("Sair", self.quit)
        ]

        for texto, comando in botoes:
            tk.Button(self, text=texto, width=35, height=2, bg="#4CAF50", fg="white", command=comando).pack(pady=7)

    def cadastro_produto(self):
        win = tk.Toplevel(self)
        win.title("Cadastro de Produto")
        win.geometry("300x400")
        win.configure(bg="#E8E8E8")

        labels = ["Nome", "Código", "Quantidade", "Valor"]
        entries = []

        for l in labels:
            tk.Label(win, text=l, bg="#E8E8E8").pack(pady=3)
            e = tk.Entry(win)
            e.pack()
            entries.append(e)

        def salvar():
            nome, codigo, quantidade, valor = [e.get() for e in entries]
            if not nome or not codigo or not quantidade or not valor:
                messagebox.showwarning("Atenção", "Preencha todos os campos!")
                return

            try:
                valor_float = float(valor)
            except ValueError:
                messagebox.showwarning("Erro", "Valor precisa ser numérico!")
                return

            conn, cursor = conectar()
            try:
                cursor.execute("INSERT INTO produtos (nome, codigo, quantidade, valor) VALUES (?, ?, ?, ?)",
                               (nome, codigo, int(quantidade), valor_float))
                conn.commit()
                messagebox.showinfo("Sucesso", "Produto cadastrado!")
                win.destroy()
            except sqlite3.IntegrityError:
                messagebox.showerror("Erro", "Código de produto já existe!")
            conn.close()

        tk.Button(win, text="Salvar", bg="#4CAF50", fg="white", command=salvar).pack(pady=15)

    def view_estoque(self):
        win = tk.Toplevel(self)
        win.title("Estoque Atual")
        win.geometry("400x500")
        win.configure(bg="#E8E8E8")

        conn, cursor = conectar()
        cursor.execute("SELECT nome, codigo, quantidade, valor FROM produtos")
        dados = cursor.fetchall()
        conn.close()

        if dados:
            for d in dados:
                frame = tk.Frame(win, bg="white", pady=5, padx=5, relief=tk.RIDGE, bd=2)
                frame.pack(pady=5, fill="x", padx=10)
                tk.Label(frame, text=f"Produto: {d[0]}", bg="white", anchor="w").pack(fill="x")
                tk.Label(frame, text=f"Código: {d[1]}", bg="white", anchor="w").pack(fill="x")
                tk.Label(frame, text=f"Quantidade: {d[2]}", bg="white", anchor="w").pack(fill="x")
                tk.Label(frame, text=f"Preço: R$ {d[3]:.2f}", bg="white", anchor="w").pack(fill="x")
        else:
            tk.Label(win, text="Nenhum produto cadastrado ainda.", bg="#E8E8E8").pack(pady=20)


if __name__ == "__main__":
    app = StockWiseApp()
    app.mainloop()