# Plano de Teste - Caso de Uso: Gerenciar Produtos

## 1. Identificação
- **Caso de Uso**: Gerenciar Produtos
- **Ator(es)**: Usuário, Administrador
- **Descrição**: Permite adicionar, editar e excluir produtos do estoque. Inclui campos como nome, código, categoria, fornecedor, quantidade mínima e preço.

---

## 2. Funcionalidades Testadas
- Acesso à funcionalidade de gerenciamento de produtos
- Adição de novos produtos
- Edição de produtos existentes
- Exclusão de produtos
- Validação de campos obrigatórios
- Armazenamento persistente das alterações

---

## 3. Casos de Teste

### CT01 - Acessar funcionalidade "Gerenciar Produtos"
| Item                | Descrição                                      |
|---------------------|-----------------------------------------------|
| Pré-condição        | Usuário autenticado com permissão de acesso   |
| Ação                | Acessar o menu "Gerenciar Produtos"           |
| Resultado Esperado  | Tela de gerenciamento de produtos é exibida   |

---

### CT02 - Adicionar um novo produto com dados válidos
| Item                | Descrição                                      |
|---------------------|-----------------------------------------------|
| Pré-condição        | Tela de "Gerenciar Produtos" aberta           |
| Ação                | Preencher todos os campos obrigatórios e salvar |
| Dados de entrada    | Nome: Caneta Azul, Código: 00123, Categoria: Papelaria, Fornecedor: ABC Ltda, Qtd. mínima: 10, Preço: R$2,50 |
| Resultado Esperado  | Produto adicionado com sucesso ao estoque     |

---

### CT03 - Adicionar produto com campos obrigatórios em branco
| Item                | Descrição                                      |
|---------------------|-----------------------------------------------|
| Pré-condição        | Tela de "Gerenciar Produtos" aberta           |
| Ação                | Tentar salvar produto sem preencher campos obrigatórios |
| Dados de entrada    | Nome: (vazio), Código: (vazio), etc.          |
| Resultado Esperado  | Mensagem de erro exibida e produto não salvo  |

---

### CT04 - Editar produto existente
| Item                | Descrição                                      |
|---------------------|-----------------------------------------------|
| Pré-condição        | Produto já existente no sistema               |
| Ação                | Modificar dados e salvar                      |
| Dados de entrada    | Alterar preço de R$2,50 para R$3,00           |
| Resultado Esperado  | Produto atualizado corretamente               |

---

### CT05 - Excluir produto existente
| Item                | Descrição                                      |
|---------------------|-----------------------------------------------|
| Pré-condição        | Produto existente listado                     |
| Ação                | Selecionar produto e acionar "Excluir"        |
| Resultado Esperado  | Produto removido do estoque                   |

---

### CT06 - Inserir código de produto duplicado
| Item                | Descrição                                      |
|---------------------|-----------------------------------------------|
| Pré-condição        | Produto com mesmo código já cadastrado        |
| Ação                | Tentar cadastrar novo produto com mesmo código |
| Resultado Esperado  | Sistema bloqueia cadastro e exibe erro        |

---

## 4. Critérios de Aceitação
- A funcionalidade deve ser acessível somente a usuários autorizados
- Todos os campos obrigatórios devem ser validados corretamente
- Os dados devem ser armazenados, atualizados ou excluídos de forma persistente
- Mensagens de erro devem ser claras e informativas
- A interface deve permanecer responsiva e sem falhas após as operações

---

## 5. Ambiente de Testes
- **Sistema Operacional**: Windows 10
- **Navegador / Plataforma**: Google Chrome / Sistema Desktop (caso aplicável)
- **Banco de Dados**: SQL Server / MySQL
- **Versão do Sistema**: v1.0.0

---

## 6. Observações
- Garantir que não haja produtos órfãos após exclusões (ex: referência em pedidos).
- Testar com diferentes perfis de usuário (Administrador vs Usuário).
- Verificar persistência após reiniciar o sistema.

