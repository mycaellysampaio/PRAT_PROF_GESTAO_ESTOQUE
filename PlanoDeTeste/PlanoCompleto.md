# Plano de Testes do Sistema de Gestão de Estoque

## Índice
1. [Gerenciar Produtos](#1-gerenciar-produtos)  
2. [Controle de Estoque](#2-controle-de-estoque)  
3. [Gerenciar Fornecedores](#3-gerenciar-fornecedores)  
4. [Gerenciar Pedidos](#4-gerenciar-pedidos)  
5. [Geração de Relatórios](#5-gera%C3%A7%C3%A3o-de-relat%C3%B3rios)  
6. [Gestão de Usuários](#6-gest%C3%A3o-de-usu%C3%A1rios)  

---

## 1. Gerenciar Produtos
**Ator(es):** Usuário, Administrador  
**Descrição:** Permite adicionar, editar e excluir produtos do estoque. Inclui campos como nome, código, categoria, fornecedor, quantidade mínima e preço.

### Casos de Teste
- **CT01:** Acessar funcionalidade de gerenciamento de produtos  
- **CT02:** Adicionar novo produto com dados válidos  
- **CT03:** Adicionar produto com campos obrigatórios em branco  
- **CT04:** Editar produto existente  
- **CT05:** Excluir produto existente  
- **CT06:** Validar formato e valores (ex: preço não negativo)  

---

## 2. Controle de Estoque
**Ator(es):** Usuário, Administrador  
**Descrição:** Registra entradas e saídas de estoque, permitindo acompanhar o saldo atual e gerar alertas para níveis baixos.

### Casos de Teste
- **CT01:** Acessar "Controle de Estoque"  
- **CT02:** Registrar entrada de produto  
- **CT03:** Registrar saída de produto  
- **CT04:** Inserir movimentação com quantidade inválida  
- **CT05:** Validar saldo atualizado após movimentação  
- **CT06:** Gerar alerta para produto abaixo da quantidade mínima  

---

## 3. Gerenciar Fornecedores
**Ator(es):** Usuário, Administrador  
**Descrição:** Permite cadastrar e manter informações sobre fornecedores, incluindo nome, contato, CNPJ, produtos fornecidos e prazos de entrega.

### Casos de Teste
- **CT01:** Acessar funcionalidade de fornecedores  
- **CT02:** Cadastrar fornecedor com dados válidos  
- **CT03:** Editar dados de fornecedor existente  
- **CT04:** Remover fornecedor  
- **CT05:** Cadastrar fornecedor com CNPJ inválido ou duplicado  

---

## 4. Gerenciar Pedidos
**Ator(es):** Usuário, Administrador  
**Descrição:** Facilita a criação e acompanhamento de pedidos de compra para reposição de estoque.

### Casos de Teste
- **CT01:** Acessar funcionalidade "Gerenciar Pedidos"  
- **CT02:** Criar novo pedido com dados válidos  
- **CT03:** Criar pedido com campos obrigatórios vazios  
- **CT04:** Atualizar status do pedido  
- **CT05:** Verificar número único de pedido  
- **CT06:** Listar pedidos com seus status  

---

## 5. Geração de Relatórios
**Ator(es):** Usuário, Administrador  
**Descrição:** Gera relatórios sobre movimentações, estoque atual, produtos críticos e previsão de reposição.

### Casos de Teste
- **CT01:** Acessar funcionalidade "Geração de Relatórios"  
- **CT02:** Gerar relatório de movimentações  
- **CT03:** Gerar relatório de estoque atual  
- **CT04:** Gerar relatório de produtos críticos  
- **CT05:** Gerar previsão de reposição  
- **CT06:** Tentar gerar relatório sem dados  
- **CT07:** Verificar exibição de gráficos e tabelas  

---

## 6. Gestão de Usuários
**Ator(es):** Administrador  
**Descrição:** Permite cadastrar e gerenciar usuários do sistema, definindo permissões de acesso.

### Casos de Teste
- **CT01:** Acessar funcionalidade "Gestão de Usuários"  
- **CT02:** Cadastrar novo usuário com dados válidos  
- **CT03:** Tentar cadastrar usuário com e-mail duplicado  
- **CT04:** Editar dados de um usuário  
- **CT05:** Remover usuário  
- **CT06:** Definir permissões corretamente  
- **CT07:** Validar campos obrigatórios ao cadastrar  

---

**Observações Gerais:**  
- Todos os testes devem ser executados em ambiente de homologação.  
- Registros devem ser auditáveis sempre que possível.  
- Validar também aspectos de usabilidade, performance e segurança quando aplicável.
