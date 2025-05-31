Olá, este é o repositório do grupo 25 de "Praticas Profissionais Em Analise e Desenvolvimento de Sistemas"!
Pretendemos criar ao longo do primeiro semestre de 2025 uma aplicação desktop para a gestão de estoques.
O grupo é composto por: Ana Carolina Gonçalves Bernini, Gustavo Mezei Silva, Matheus Miguel Abreu da Silva e Mycaelly Barboza Sampaio.

# 📦 StockWise - Sistema de Gestão de Estoque

O *StockWise* é um sistema desktop de controle de estoque desenvolvido em Python com interface gráfica via tkinter e banco de dados local SQLite.  
Simples, direto, leve e funcional: feito sob medida para pequenas empresas, com foco na usabilidade e organização de produtos e fornecedores.

---

## ✅ Funcionalidades

### 📌 Gestão de Produtos
- Cadastro de produtos com:
  - Nome, código único, quantidade e valor (suporte a casas decimais).
- Visualização de estoque com separação visual por item.
- Alerta visual automático para produtos com estoque inferior a 5 unidades.
- Registro de *entrada* ou *saída* de produtos com atualização automática de quantidade.

### 🧾 Gestão de Fornecedores
- Cadastro de fornecedores com:
  - Nome, CNPJ, telefone e produtos fornecidos.
- Visualização organizada dos fornecedores cadastrados.

### 🛠️ Experiência e Usabilidade
- Interface intuitiva com botões grandes e legíveis.
- Cores suaves e design amigável para facilitar a navegação.
- Mensagens claras de erro e sucesso (validação de campos, códigos duplicados etc).

---

## 🧠 Tecnologias Utilizadas

- *Linguagem:* Python 3.12
- *GUI:* Tkinter
- *Banco de dados:* SQLite
- *Estilo visual:* Customização leve com tk.Frame, Label, RIDGE e cores personalizadas.

---

## 🚀 Como executar o projeto

1. *Clone o repositório:*
   ```bash
   git clone https://github.com/SEU-USUARIO/stockwise.git
   cd stockwise