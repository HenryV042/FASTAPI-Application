# FASTAPI-Application
Projeto desenvolvido na cadeira de Banco de Dados na UFC de Quixadá.

API para gestão agropecuária: CRUD de animais e consultas às views de
produção de leite e resumo geral da fazenda, usando **PostgreSQL** como
banco de dados.

## Estrutura de pastas

```
FASTAPI-Application-main/
├── requirements.txt
├── .env                       <- criar na raiz com as variáveis de conexão
└── app/
    ├── main.py                <- cria o FastAPI e registra as rotas
    ├── config/
    │   └── config.py          <- lê as variáveis de ambiente (.env)
    ├── database/
    │   └── db.py              <- abre a conexão com o PostgreSQL (psycopg2)
    ├── model/
    │   ├── animal_model.py            <- schemas Pydantic de Animal (Animal / AnimalUpdate)
    │   ├── v_producao_model.py        <- schema da view de produção de leite
    │   └── v_resumo_fazenda_model.py  <- schema da view de resumo da fazenda
    ├── repositories/
    │   ├── animal_crud.py             <- todo o SQL de ANIMAL fica aqui
    │   ├── v_producao_crud.py         <- SQL da view de produção de leite
    │   └── v_resumo_fazenda_crud.py   <- SQL da view de resumo da fazenda
    └── routers/
        ├── animal_router.py       <- endpoints /animais (CRUD)
        ├── v_producao_router.py   <- endpoints /producao
        └── v_resumo_router.py     <- endpoints /resumo
```

**Por que separar assim?**
- `model` = o que a API recebe/devolve (validação com Pydantic)
- `repositories` = o único lugar que sabe SQL / fala com o banco
- `routers` = só recebe a requisição, chama o repositório e devolve a resposta
- `main.py` = só monta tudo

Isso deixa cada arquivo pequeno e com uma responsabilidade só — e fica fácil
de mostrar no relatório/apresentação "aqui está a camada X, que faz Y".

## Como rodar

1. Entrar na pasta do projeto:
   ```
   cd FASTAPI-Application-main
   ```
2. Instalar as dependências:
   ```
   pip install -r requirements.txt
   ```
3. Criar o arquivo `.env` na raiz do projeto com as variáveis de conexão:
   ```
   DB_HOST=localhost
   DB_NAME=bd_gestao_agropecuaria
   DB_USER=fazenda_admin
   DB_PASSWORD=admin123
   ```
4. Rodar a API:
   ```
   uvicorn app.main:app --reload
   ```
5. Abrir no navegador: http://127.0.0.1:8000/docs
   Ali dá pra testar todos os endpoints direto pela interface do Swagger.

## Endpoints disponíveis

| Método | Rota                | O que faz                                          |
|--------|----------------------|-----------------------------------------------------|
| GET    | `/`                    | Status da API                                       |
| GET    | `/animais`             | Lista todos os animais                              |
| GET    | `/animais/animal/{id}` | Busca um animal específico                          |
| POST   | `/animais`              | Cadastra um novo animal                             |
| PATCH  | `/animais/animal/{id}` | Atualiza campos de um animal                        |
| DELETE | `/animais/animal/{id}` | Remove um animal                                    |
| GET    | `/producao`             | Lista a produção de leite agregada por animal       |
| GET    | `/producao/animal/{id}`| Consulta a produção de leite de um animal específico|
| GET    | `/resumo`               | Lista o resumo geral de todas as fazendas           |
| GET    | `/resumo/fazenda/{id}` | Consulta o resumo de uma fazenda específica          |

## Controle de Acesso (DCL)

O banco `bd_gestao_agropecuaria` possui dois níveis de usuário, criados e
configurados via SQL (DCL):

```sql
-- Controle de Acesso (DCL)

-- 1. Criação dos Usuários
CREATE USER fazenda_admin WITH PASSWORD 'admin123';
CREATE USER fazenda_leitura WITH PASSWORD 'leitura123';

-- 2. Garantindo privilégios para o ADMIN (Leitura e Escrita total)
GRANT ALL PRIVILEGES ON DATABASE "bd_gestao_agropecuaria" TO fazenda_admin;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO fazenda_admin;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO fazenda_admin;

-- 3. Garantindo privilégios para o LEITURA (Apenas SELECT)
GRANT CONNECT ON DATABASE "bd_gestao_agropecuaria" TO fazenda_leitura;
GRANT USAGE ON SCHEMA public TO fazenda_leitura;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO fazenda_leitura;
GRANT SELECT ON ALL SEQUENCES IN SCHEMA public TO fazenda_leitura;

-- 4. Revogando permissões de escrita do usuário de leitura por segurança
REVOKE INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public FROM fazenda_leitura;
```

- **`fazenda_admin`** — leitura e escrita total (todas as tabelas e sequências).
- **`fazenda_leitura`** — apenas `SELECT`; qualquer tentativa de `INSERT`,
  `UPDATE` ou `DELETE` é rejeitada pelo PostgreSQL.

### Testando os dois níveis de acesso

Para provar que o controle de acesso funciona também pela aplicação:

1. No `.env`, deixe `DB_USER=fazenda_admin` e `DB_PASSWORD=admin123` →
   todos os endpoints funcionam normalmente (GET, POST, PATCH, DELETE).
2. Troque para `DB_USER=fazenda_leitura` e `DB_PASSWORD=leitura123`,
   reinicie o `uvicorn`, e tente:
   - `GET /animais`, `GET /producao`, `GET /resumo` → devem funcionar
     normalmente.
   - `POST /animais`, `PATCH /animais/animal/{id}` ou
     `DELETE /animais/animal/{id}` → devem retornar erro de permissão
     negada vindo do PostgreSQL (isso é o esperado e vale tirar print para
     o relatório).

## Print para o relatório
Tire print de:
- `/docs` mostrando todas as rotas listadas
- Cada operação do CRUD de animais funcionando (GET, POST, PATCH, DELETE)
- As consultas de `/producao` e `/resumo` funcionando
- O erro de permissão ao tentar POST/PATCH/DELETE usando o `fazenda_leitura`