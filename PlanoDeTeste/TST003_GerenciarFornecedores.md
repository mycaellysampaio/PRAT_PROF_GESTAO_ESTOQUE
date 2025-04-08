# Plano de Teste - Caso de Uso: Gerenciar Fornecedores

## 1. Identificação
- **Caso de Uso**: Gerenciar Fornecedores
- **Ator(es)**: Usuário, Administrador
- **Descrição**: Permite cadastrar e manter informações sobre fornecedores, incluindo nome, contato, CNPJ, produtos fornecidos e prazos de entrega.

---

## 2. Funcionalidades Testadas
- Acesso à funcionalidade "Gerenciar Fornecedores"
- Cadastro de novos fornecedores
- Edição de informações de fornecedores existentes
- Exclusão de fornecedores
- Validação de campos obrigatórios e formatos (ex: CNPJ)
- Atualização do banco de dados

---

## 3. Casos de Teste

### CT01 - Acessar funcionalidade "Gerenciar Fornecedores"
| Item                | Descrição                                      |
|---------------------|-----------------------------------------------|
| Pré-condição        | Usuário autenticado com permissão              |
| Ação                | Acessar o menu "Gerenciar Fornecedores"       |
| Resultado Esperado  | Tela de gerenciamento de fornecedores é exibida |

---

### CT02 - Cadastrar fornecedor com dados válidos
| Item                | Descrição                                      |
|---------------------|-----------------------------------------------|
| Pré-condição        | Tela de gerenciamento aberta                   |
| Ação                | Preencher os campos obrigatórios e salvar     |
| Dados de entrada    | Nome: Fornecedora XYZ, Contato: (11)99999-9999, CNPJ: 12.345.678/0001-90, Produtos: Papel, Prazos: 3 dias |
| Resultado Esperado  | Fornecedor cadastrado com sucesso             |

---

### CT03 - Tentar cadastrar fornecedor com CNPJ inválido
| Item                | Descrição                                      |
|---------------------|-----------------------------------------------|
| Pré-condição        | Tela de gerenciamento aberta                   |
| Ação                | Preencher campos com CNPJ inválido e salvar   |
| Dados de entrada    | CNPJ: 12345678900000                          |
| Resultado Esperado  | Sistema exibe mensagem de erro e impede cadastro |

---

### CT04 - Editar dados de fornecedor existente
| Item                | Descrição                                      |
|---------------------|-----------------------------------------------|
| Pré-condição        | Fornecedor já cadastrado                      |
| Ação                | Alterar informações (ex: prazo de entrega) e salvar |
| Resultado Esperado  | Dados atualizados com sucesso no sistema      |

---

### CT05 - Remover fornecedor do sistema
| Item                | Descrição                                      |
|---------------------|-----------------------------------------------|
| Pré-condição        | Fornecedor listado na interface               |
| Ação                | Selecionar fornecedor e acionar "Remover"     |
| Resultado Esperado  | Fornecedor removido e não aparece mais na listagem |

---

### CT06 - Cadastrar fornecedor com campos obrigatórios em branco
| Item                | Descrição                                      |
|---------------------|-----------------------------------------------|
| Pré-condição        | Tela de gerenciamento aberta                   |
| Ação                | Tentar salvar fornecedor sem preencher todos os campos obrigatórios |
| Resultado Esperado  | Sistema exibe mensagens de erro e bloqueia o cadastro |

---

### CT07 - Listar fornecedores cadastrados
| Item                | Descrição                                      |
|---------------------|-----------------------------------------------|
| Pré-condição        | Sistema possui fornecedores cadastrados       |
| Ação                | Acessar tela de "Gerenciar Fornecedores"      |
| Resultado Esperado  | Lista completa de fornecedores é exibida corretamente |

---

## 4. Critérios de Aceitação
- O sistema deve permitir apenas usuários autorizados acessarem a funcionalidade
- CNPJ deve ser validado conforme o formato brasileiro
- Campos obrigatórios devem ser preenchidos corretamente
- Ações de adicionar, editar e excluir devem refletir no banco de dados
- A interface deve fornecer feedback claro ao usuário sobre o sucesso ou falha da operação

---

## 5. Ambiente de Testes
- **Sistema Operacional**: Windows 10 / Linux
- **Plataforma**: Web / Desktop
- **Banco de Dados**: PostgreSQL / MySQL
- **Versão do Sistema**: v1.0.0

---

## 6. Observações
- Garantir que fornecedores removidos não fiquem vinculados a pedidos ou produtos (validação de integridade referencial)
- Avaliar consistência dos dados após edição

