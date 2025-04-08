# Plano de Teste - Caso de Uso: Controle de Estoque

## 1. Identificação
- **Caso de Uso**: Controle de Estoque
- **Ator(es)**: Usuário, Administrador
- **Descrição**: Registra entradas e saídas de estoque, permitindo acompanhar o saldo atual e gerar alertas para níveis baixos.

---

## 2. Funcionalidades Testadas
- Acesso à funcionalidade "Controle de Estoque"
- Registro de entrada de produtos
- Registro de saída de produtos
- Atualização correta do saldo
- Geração de alertas quando o nível mínimo for atingido ou ultrapassado
- Validação dos dados de movimentação

---

## 3. Casos de Teste

### CT01 - Acessar funcionalidade "Controle de Estoque"
| Item                | Descrição                                      |
|---------------------|-----------------------------------------------|
| Pré-condição        | Usuário autenticado                           |
| Ação                | Acessar o menu "Controle de Estoque"          |
| Resultado Esperado  | Tela de controle de estoque é exibida         |

---

### CT02 - Registrar entrada de produto com dados válidos
| Item                | Descrição                                      |
|---------------------|-----------------------------------------------|
| Pré-condição        | Produto já cadastrado                         |
| Ação                | Selecionar "Entrada", informar produto, quantidade e motivo |
| Dados de entrada    | Produto: Caneta Azul, Qtd: 100, Motivo: Reposição |
| Resultado Esperado  | Saldo do produto atualizado corretamente (+100) |

---

### CT03 - Registrar saída de produto com dados válidos
| Item                | Descrição                                      |
|---------------------|-----------------------------------------------|
| Pré-condição        | Produto com saldo suficiente                  |
| Ação                | Selecionar "Saída", informar produto, quantidade e motivo |
| Dados de entrada    | Produto: Caneta Azul, Qtd: 30, Motivo: Venda  |
| Resultado Esperado  | Saldo do produto reduzido corretamente (-30)  |

---

### CT04 - Registrar movimentação com dados incompletos
| Item                | Descrição                                      |
|---------------------|-----------------------------------------------|
| Pré-condição        | Tela de controle de estoque aberta            |
| Ação                | Tentar registrar entrada/saída sem preencher todos os campos obrigatórios |
| Dados de entrada    | Produto: (vazio), Qtd: (vazio), Motivo: (vazio) |
| Resultado Esperado  | Sistema bloqueia operação e exibe mensagens de erro |

---

### CT05 - Geração de alerta para nível de estoque baixo
| Item                | Descrição                                      |
|---------------------|-----------------------------------------------|
| Pré-condição        | Produto com quantidade mínima definida        |
| Ação                | Registrar saída que reduz o saldo abaixo da quantidade mínima |
| Resultado Esperado  | Sistema atualiza saldo e exibe alerta de estoque baixo |

---

### CT06 - Registrar saída maior que o saldo atual
| Item                | Descrição                                      |
|---------------------|-----------------------------------------------|
| Pré-condição        | Produto com saldo inferior à quantidade solicitada |
| Ação                | Informar quantidade de saída superior ao saldo atual |
| Resultado Esperado  | Sistema bloqueia a operação e exibe mensagem de erro |

---

## 4. Critérios de Aceitação
- A funcionalidade deve ser acessível somente a usuários autorizados
- O sistema deve atualizar corretamente o saldo dos produtos
- Alertas devem ser gerados sempre que o nível mínimo for atingido
- Nenhuma saída deve ser registrada se exceder o saldo atual
- Todos os campos devem ser obrigatoriamente preenchidos
- Motivo da movimentação deve ser registrado para rastreabilidade

---

## 5. Ambiente de Testes
- **Sistema Operacional**: Windows 10
- **Plataforma**: Sistema Web / Desktop
- **Banco de Dados**: PostgreSQL / MySQL
- **Versão do Sistema**: v1.0.0

---

## 6. Observações
- Avaliar impacto dos registros no histórico de movimentações.
