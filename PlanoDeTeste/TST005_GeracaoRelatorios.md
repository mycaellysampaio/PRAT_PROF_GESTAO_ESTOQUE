# Plano de Teste - Caso de Uso: Geração de Relatórios

## 1. Identificação
- **Caso de Uso**: Geração de Relatórios
- **Ator(es)**: Usuário, Administrador
- **Descrição**: Gera relatórios sobre movimentações, estoque atual, produtos críticos e previsão de reposição.

---

## 2. Funcionalidades Testadas
- Acesso à funcionalidade "Geração de Relatórios"
- Seleção do tipo de relatório desejado
- Geração de relatórios com dados reais do sistema
- Apresentação de gráficos e tabelas
- Exportação e/ou impressão de relatórios (caso aplicável)

---

## 3. Casos de Teste

### CT01 - Acessar funcionalidade "Geração de Relatórios"
| Item                | Descrição                                      |
|---------------------|-----------------------------------------------|
| Pré-condição        | Usuário autenticado                            |
| Ação                | Acessar o menu "Geração de Relatórios"        |
| Resultado Esperado  | Tela de seleção de tipo de relatório é exibida com sucesso |

---

### CT02 - Gerar relatório de movimentações
| Item                | Descrição                                      |
|---------------------|-----------------------------------------------|
| Pré-condição        | Sistema com movimentações registradas         |
| Ação                | Selecionar "Relatório de Movimentações"       |
| Resultado Esperado  | Relatório exibido com lista de entradas e saídas, datas e responsáveis |

---

### CT03 - Gerar relatório de estoque atual
| Item                | Descrição                                      |
|---------------------|-----------------------------------------------|
| Pré-condição        | Sistema com produtos no estoque               |
| Ação                | Selecionar "Relatório de Estoque Atual"       |
| Resultado Esperado  | Relatório exibido com quantidades disponíveis por produto, categorizados |

---

### CT04 - Gerar relatório de produtos críticos
| Item                | Descrição                                      |
|---------------------|-----------------------------------------------|
| Pré-condição        | Existência de produtos abaixo do nível mínimo |
| Ação                | Selecionar "Produtos Críticos"                |
| Resultado Esperado  | Lista de produtos em estado crítico é exibida com destaque visual (ex: cor vermelha) |

---

### CT05 - Gerar previsão de reposição
| Item                | Descrição                                      |
|---------------------|-----------------------------------------------|
| Pré-condição        | Sistema com histórico de consumo e entradas   |
| Ação                | Selecionar "Previsão de Reposição"            |
| Resultado Esperado  | Sistema apresenta recomendação de pedidos com base em tendências de consumo |

---

### CT06 - Tentar gerar relatório sem dados disponíveis
| Item                | Descrição                                      |
|---------------------|-----------------------------------------------|
| Pré-condição        | Sistema sem dados para o tipo de relatório escolhido |
| Ação                | Selecionar qualquer tipo de relatório         |
| Resultado Esperado  | Sistema informa que não há dados suficientes para gerar o relatório |

---

### CT07 - Visualização com gráficos e tabelas
| Item                | Descrição                                      |
|---------------------|-----------------------------------------------|
| Pré-condição        | Relatório gerado com sucesso                   |
| Ação                | Verificar a presença de gráficos e tabelas    |
| Resultado Esperado  | Dados são apresentados com clareza visual e boa organização |

---

## 4. Critérios de Aceitação
- O sistema deve exibir todos os relatórios com informações corretas
- Cada tipo de relatório deve ter seu layout e estrutura adequados
- Os dados devem ser atualizados e refletir o estado atual do sistema
- Relatórios devem ser exportáveis (se aplicável) e imprimíveis com boa formatação
- O sistema deve lidar com ausência de dados de forma amigável

---

## 5. Ambiente de Testes
- **Sistema Operacional**: Windows 10 / Linux
- **Plataforma**: Web / Desktop
- **Banco de Dados**: PostgreSQL / MySQL
- **Versão do Sistema**: v1.0.0
