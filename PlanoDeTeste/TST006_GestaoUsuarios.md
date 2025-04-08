# Plano de Teste - Caso de Uso: Gestão de Usuários

## 1. Identificação
- **Caso de Uso**: Gestão de Usuários
- **Ator(es)**: Administrador
- **Descrição**: Permite cadastrar e gerenciar usuários do sistema, definindo permissões de acesso.

---

## 2. Funcionalidades Testadas
- Acesso à funcionalidade "Gestão de Usuários"
- Cadastro de novos usuários
- Edição de dados de usuários existentes
- Remoção de usuários
- Definição e alteração de permissões de acesso
- Validação de campos obrigatórios (ex: nome, e-mail, senha)

---

## 3. Casos de Teste

### CT01 - Acessar funcionalidade "Gestão de Usuários"
| Item                | Descrição                                      |
|---------------------|-----------------------------------------------|
| Pré-condição        | Administrador autenticado                     |
| Ação                | Acessar o menu "Gestão de Usuários"           |
| Resultado Esperado  | Tela de gerenciamento de usuários é exibida com sucesso |

---

### CT02 - Cadastrar novo usuário com dados válidos
| Item                | Descrição                                      |
|---------------------|-----------------------------------------------|
| Pré-condição        | Tela de gestão aberta                          |
| Ação                | Preencher os dados do usuário e definir permissões |
| Dados de entrada    | Nome: João Silva, E-mail: joao@exemplo.com, Permissão: Usuário |
| Resultado Esperado  | Usuário cadastrado com sucesso e listado na interface |

---

### CT03 - Tentar cadastrar usuário com e-mail duplicado
| Item                | Descrição                                      |
|---------------------|-----------------------------------------------|
| Pré-condição        | Já existe um usuário com o mesmo e-mail       |
| Ação                | Tentar cadastrar outro usuário com mesmo e-mail |
| Resultado Esperado  | Sistema exibe mensagem de erro e impede o cadastro |

---

### CT04 - Editar dados de um usuário
| Item                | Descrição                                      |
|---------------------|-----------------------------------------------|
| Pré-condição        | Usuário existente na base                     |
| Ação                | Alterar nome ou permissão e salvar            |
| Resultado Esperado  | Alterações salvas com sucesso e refletidas na listagem |

---

### CT05 - Remover usuário do sistema
| Item                | Descrição                                      |
|---------------------|-----------------------------------------------|
| Pré-condição        | Usuário existente                             |
| Ação                | Selecionar usuário e clicar em "Remover"      |
| Resultado Esperado  | Usuário excluído do sistema e removido da listagem |

---

### CT06 - Definir permissões de acesso corretamente
| Item                | Descrição                                      |
|---------------------|-----------------------------------------------|
| Pré-condição        | Cadastro ou edição de usuário em andamento    |
| Ação                | Selecionar perfil de acesso (ex: Administrador, Usuário) |
| Resultado Esperado  | Permissão atribuída corretamente ao perfil e refletida no uso do sistema |

---

### CT07 - Validar campos obrigatórios ao cadastrar
| Item                | Descrição                                      |
|---------------------|-----------------------------------------------|
| Pré-condição        | Cadastro em andamento                          |
| Ação                | Tentar salvar sem preencher e-mail ou nome     |
| Resultado Esperado  | Sistema bloqueia cadastro e exibe mensagens de erro |

---

## 4. Critérios de Aceitação
- Apenas administradores devem acessar esta funcionalidade
- O sistema deve impedir cadastro com e-mail já existente
- As permissões devem ser respeitadas em todas as áreas do sistema
- As alterações devem ser refletidas imediatamente no sistema
- Os dados dos usuários devem ser armazenados com segurança

---

## 5. Ambiente de Testes
- **Sistema Operacional**: Windows 10 / Linux
- **Plataforma**: Web / Desktop
- **Banco de Dados**: PostgreSQL / MySQL
- **Versão do Sistema**: v1.0.0

---

## 6. Observações
- Verificar integração com autenticação (login)
- Confirmar que usuários com permissões diferentes têm acesso limitado conforme esperado
