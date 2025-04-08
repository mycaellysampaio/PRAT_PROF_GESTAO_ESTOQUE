# Plano de Teste - Caso de Uso: Gerenciar Pedidos

## 1. Identificação
- **Caso de Uso**: Gerenciar Pedidos
- **Ator(es)**: Usuário, Administrador
- **Descrição**: Facilita a criação e acompanhamento de pedidos de compra para reposição de estoque.

---

## 2. Funcionalidades Testadas
- Acesso à funcionalidade "Gerenciar Pedidos"
- Criação de novos pedidos com fornecedor, produtos e quantidades
- Geração automática de número de pedido
- Atualização de status do pedido conforme etapas de entrega
- Validação dos dados inseridos

---

## 3. Casos de Teste

### CT01 - Acessar funcionalidade "Gerenciar Pedidos"
| Item                | Descrição                                      |
|---------------------|-----------------------------------------------|
| Pré-condição        | Usuário autenticado com permissão              |
| Ação                | Acessar o menu "Gerenciar Pedidos"            |
| Resultado Esperado  | Tela de pedidos é exibida com sucesso         |

---

### CT02 - Criar novo pedido com dados válidos
| Item                | Descrição                                      |
|---------------------|-----------------------------------------------|
| Pré-condição        | Tela de pedidos aberta                         |
| Ação                | Informar fornecedor, produtos e quantidades, e salvar |
| Dados de entrada    | Fornecedor: ABC Ltda, Produtos: Caneta (100), Papel A4 (50) |
| Resultado Esperado  | Pedido criado com número gerado automaticamente e status inicial definido (ex: "Pendente") |

---

### CT03 - Criar pedido com campos obrigatórios vazios
| Item                | Descrição                                      |
|---------------------|-----------------------------------------------|
| Pré-condição        | Tela de pedidos aberta                         |
| Ação                | Tentar salvar pedido sem preencher fornecedor ou produtos |
| Resultado Esperado  | Sistema exibe mensagens de erro e bloqueia o envio |

---

### CT04 - Atualizar status do pedido manualmente
| Item                | Descrição                                      |
|---------------------|-----------------------------------------------|
| Pré-condição        | Pedido criado anteriormente                    |
| Ação                | Selecionar pedido e atualizar status (ex: de "Pendente" para "Entregue") |
| Resultado Esperado  | Status atualizado com sucesso e refletido na interface |

---

### CT05 - Verificar número de pedido único
| Item                | Descrição                                      |
|---------------------|-----------------------------------------------|
| Pré-condição        | Dois ou mais pedidos criados                   |
| Ação                | Verificar números dos pedidos criados          |
| Resultado Esperado  | Cada pedido possui um número único e sequencial (ou UUID) |

---

### CT06 - Listar pedidos e seus status
| Item                | Descrição                                      |
|---------------------|-----------------------------------------------|
| Pré-condição        | Sistema com pedidos cadastrados               |
| Ação                | Acessar listagem de pedidos                    |
| Resultado Esperado  | Sistema exibe todos os pedidos com seus status atuais corretamente |

---

## 4. Critérios de Aceitação
- O sistema deve gerar um número único para cada pedido criado
- Campos obrigatórios devem ser validados corretamente
- O status do pedido deve ser atualizado e armazenado com precisão
- A interface deve permitir visualização clara dos pedidos e seus status
- Apenas usuários autorizados podem acessar e gerenciar pedidos

---

## 5. Ambiente de Testes
- **Sistema Operacional**: Windows 10 / Linux
- **Plataforma**: Web / Desktop
- **Banco de Dados**: PostgreSQL / MySQL
- **Versão do Sistema**: v1.0.0

---

## 6. Observações
- Validar impacto da atualização de status no controle de estoque (ex: movimentação após entrega).

