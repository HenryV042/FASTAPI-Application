# FASTAPI-Application
Projeto desenvolvido na cadeira de Banco de Dados na UFC de Quixadá.

## Estrutura de pastas

```
codigo_app/
├── requirements.txt
├── .env.example          <- copiar para .env e preencher
└── app/
    ├── main.py            <- só cria o FastAPI e registra as rotas
    ├── config.py          <- lê as variáveis de ambiente (.env)
    ├── database.py        <- abre a conexão com o MySQL
    ├── schemas/
    │   └── animal.py      <- formato dos dados (Pydantic)
    ├── repositories/
    │   ├── animal_repository.py     <- todo o SQL de ANIMAL fica aqui
    │   └── producao_repository.py   <- SQL da view de produção de leite
    └── routers/
        ├── animais.py            <- endpoints /animais (CRUD)
        └── producao_leite.py     <- endpoint /producao-leite
```

**Por que separar assim?**
- `schemas` = o que a API recebe/devolve
- `repositories` = o único lugar que sabe SQL / fala com o banco
- `routers` = só recebe a requisição, chama o repositório e devolve a resposta
- `main.py` = só monta tudo

Isso deixa cada arquivo pequeno e com uma responsabilidade só — e fica fácil
de mostrar no relatório/apresentação "aqui está a camada X, que faz Y".

## Como rodar

1. Entrar na pasta `codigo_app/`:
   ```
   cd codigo_app
   ```
2. Instalar as dependências:
   ```
   pip install -r requirements.txt
   ```
3. Copiar o arquivo de ambiente e ajustar se precisar:
   ```
   cp .env.example .env
   ```
4. Rodar a API (repare que agora é `app.main:app`, não `main:app`):
   ```
   uvicorn app.main:app --reload
   ```
5. Abrir no navegador: http://127.0.0.1:8000/docs
   Ali dá pra testar todos os endpoints direto pela interface do Swagger.

## Endpoints disponíveis

| Método | Rota                 | O que faz                                   |
|--------|-----------------------|----------------------------------------------|
| GET    | `/animais`             | Lista todos os animais (view vw_ficha_animal) |
| GET    | `/animais/{id}`        | Busca um animal específico                    |
| POST   | `/animais`              | Cadastra um novo animal                       |
| PUT    | `/animais/{id}`        | Atualiza campos de um animal                  |
| DELETE | `/animais/{id}`        | Remove um animal                              |
| GET    | `/producao-leite`      | Lista produção de leite agregada por fazenda  |

## Testando os dois níveis de acesso (Parte 2 da entrega)

Para provar que o controle de acesso funciona também pela aplicação:
1. No `.env`, deixe `DB_USER=admin_agro` → todos os endpoints funcionam.
2. Troque para `DB_USER=leitor_agro` e `DB_PASSWORD=LeitorAgro#2026`, reinicie
   o `uvicorn`, e tente:
   - `GET /animais` → deve funcionar normalmente.
   - `POST /animais` → deve retornar erro 500 com mensagem de permissão
     negada vinda do MySQL (isso é o esperado e vale tirar print para o
     relatório).

## Print para o relatório
Tire print de:
- `/docs` mostrando todas as rotas listadas
- Cada operação do CRUD funcionando (GET, POST, PUT, DELETE)
- O erro de permissão ao tentar POST usando o `leitor_agro`
