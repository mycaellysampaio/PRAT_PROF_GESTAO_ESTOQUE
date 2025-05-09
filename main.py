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
    cursor.execute('''CREATE TABLE IF NOT EXISTS fornecedores (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        cnpj TEXT,
                        telefone TEXT,
                        produtos TEXT)''')
    conn.commit()
    return conn, cursor

class StockWiseApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("StockWise - Gestão de Estoque")
        self.geometry("450x600")
        self.configure(bg="#F0F0F0")
        self.create_main_menu()

    def create_main_menu(self):
        tk.Label(self, text="Bem-vindo ao StockWise!", font=("Arial", 18, "bold"), bg="#F0F0F0").pack(pady=20)

        botoes = [
            ("Cadastrar Produto", self.cadastro_produto),
            ("Visualizar Estoque", self.view_estoque),
            ("Registrar Entrada de Produto", self.registrar_entrada),
            ("Registrar Saída de Produto", self.registrar_saida),
            ("Cadastrar Fornecedor", self.cadastro_fornecedor),
            ("Sair", self.quit)
        ]

        for texto, comando in botoes:
            tk.Button(self, text=texto, width=35, height=2, bg="#4CAF50", fg="white", command=comando).pack(pady=5)

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
                quantidade_int = int(quantidade)
            except ValueError:
                messagebox.showwarning("Erro", "Valor e quantidade precisam ser numéricos!")
                return

            conn, cursor = conectar()
            try:
                cursor.execute("INSERT INTO produtos (nome, codigo, quantidade, valor) VALUES (?, ?, ?, ?)",
                               (nome, codigo, quantidade_int, valor_float))
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
                alerta = " ESTOQUE BAIXO" if d[2] < 5 else ""
                tk.Label(frame, text=f"Produto: {d[0]}{alerta}", bg="white", anchor="w", font=("Arial", 10, "bold")).pack(fill="x")
                tk.Label(frame, text=f"Código: {d[1]}", bg="white", anchor="w").pack(fill="x")
                tk.Label(frame, text=f"Quantidade: {d[2]}", bg="white", anchor="w").pack(fill="x")
                tk.Label(frame, text=f"Preço: R$ {d[3]:.2f}", bg="white", anchor="w").pack(fill="x")
        else:
            tk.Label(win, text="Nenhum produto cadastrado ainda.", bg="#E8E8E8").pack(pady=20)

    def registrar_entrada(self):
        self.registrar_movimentacao("entrada")

    def registrar_saida(self):
        self.registrar_movimentacao("saida")

    def registrar_movimentacao(self, tipo):
        win = tk.Toplevel(self)
        win.title(f"Registrar {tipo.capitalize()} de Produto")
        win.geometry("300x250")
        win.configure(bg="#E8E8E8")

        tk.Label(win, text="Código do Produto", bg="#E8E8E8").pack(pady=5)
        codigo_entry = tk.Entry(win)
        codigo_entry.pack()

        tk.Label(win, text="Quantidade", bg="#E8E8E8").pack(pady=5)
        quantidade_entry = tk.Entry(win)
        quantidade_entry.pack()

        def aplicar():
            codigo = codigo_entry.get()
            try:
                qtd = int(quantidade_entry.get())
            except ValueError:
                messagebox.showwarning("Erro", "Quantidade deve ser um número inteiro!")
                return

            conn, cursor = conectar()
            cursor.execute("SELECT quantidade FROM produtos WHERE codigo = ?", (codigo,))
            resultado = cursor.fetchone()
            if not resultado:
                messagebox.showerror("Erro", "Produto não encontrado!")
                conn.close()
                return

            nova_qtd = resultado[0] + qtd if tipo == "entrada" else resultado[0] - qtd
            if nova_qtd < 0:
                messagebox.showerror("Erro", "Estoque insuficiente!")
                conn.close()
                return

            cursor.execute("UPDATE produtos SET quantidade = ? WHERE codigo = ?", (nova_qtd, codigo))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucesso", f"{tipo.capitalize()} registrada com sucesso!")
            win.destroy()

        tk.Button(win, text="Aplicar", bg="#4CAF50", fg="white", command=aplicar).pack(pady=15)

    def cadastro_fornecedor(self):
        win = tk.Toplevel(self)
        win.title("Cadastro de Fornecedor")
        win.geometry("300x400")
        win.configure(bg="#E8E8E8")

        labels = ["Nome", "CNPJ", "Telefone", "Produtos Fornecidos"]
        entries = []

        for l in labels:
            tk.Label(win, text=l, bg="#E8E8E8").pack(pady=3)
            e = tk.Entry(win)
            e.pack()
            entries.append(e)

        def salvar():
            nome, cnpj, telefone, produtos = [e.get() for e in entries]
            if not nome:
                messagebox.showwarning("Atenção", "O campo Nome é obrigatório!")
                return
            conn, cursor = conectar()
            cursor.execute("INSERT INTO fornecedores (nome, cnpj, telefone, produtos) VALUES (?, ?, ?, ?)",
                           (nome, cnpj, telefone, produtos))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucesso", "Fornecedor cadastrado com sucesso!")
            win.destroy()

        tk.Button(win, text="Salvar", bg="#4CAF50", fg="white", command=salvar).pack(pady=15)


if __name__ == "__main__":
    app = StockWiseApp()
    app.mainloop()
