API de Piadas
API REST desenvolvida em Python com Flask e banco de dados SQLite.

Disciplina: Programação no Desenvolvimento de Sistemas Trio: Miguel Pieri Helmann, Ícaro Rybaczik Pedroso e Lucas Avance Mafort


📋 Sobre o projeto
Esta API gerencia uma coleção de piadas organizadas por categorias. É possível cadastrar categorias (como "Programação" ou "Tio do Pavê") e associar piadas a cada uma delas. A API permite listar, criar, atualizar, apagar e buscar registros com suporte a busca textual e exclusão em cascata.


🗂️ Tabelas do banco
O sistema utiliza o banco de dados relacional *SQLite* com duas tabelas associadas por Chave Estrangeira (Foreign Key).

Tabela categorias (Tabela Pai)
Campo
Tipo
Descrição
id
INTEGER
Chave primária (gerada automaticamente)
nome
TEXT
Nome da categorias de piadas (obrigatório)

Tabela piadas (Tabela Filhos)
Campo
Tipo
Descrição
id
INTEGER
Chave primária (gerada automaticamente)
pergunta
TEXT
A pergunta/início da piada (obrigatório)
resposta
INTEGER
 A resposta/punchline da piada (obrigatório)
categoria_id
INTEGER 
Chave estrangeira → aponta para categorias(id) com ON DELETE CASCADE 


Relação:Cada piada pertence obrigatoriamente a uma categoria. Caso a categoria seja deletada, todas as piadas associadas a ela são removidas automaticamente (ON DELETE CASCADE).




🚀 Como rodar o projeto

  1. Instalar o Flask (caso não tenha)
pip install flask

  2. Rodar a API
python app.py

  3. A API estará disponível em:
 [http://127.0.0.1:5000](http://127.0.0.1:5000)



🛣️ Rotas da API
Liste todas as rotas que você criou. Exemplo:
Tabela categorias [pai]
Método
Rota
O que faz
GET
/categorias
Lista todas as categorias
GET
/categorias/<id>
Busca uma categiria pelo id
POST
/categorias
Cria um nova categoria
PUT
/categorias/<id>
Atualiza o nome de um acategoria
DELETE
/categorias/<id>
Apaga uma categoria e suas piadas vinculadas

Tabela piadas [filho]
Método
Rota
O que faz
GET
/piadas
Lista todas as piadas
GET
/piadas/<id>
Busca uma piada pelo ID
POST
/piadas
Cria uma nova piada vinculado a uma categoria
PUT
/piadas/<id>
Atualiza a pergunta, resposta e categoria de uma piada
DELETE
/piadas/<id>
Apaga uma piada

Rotas especiais
Método
Rota
O que faz
GET
/piadas/detalhes
Lista piadas trazendo o nome da categoria vinculada (JOIN)
GET
/categorias/<id>/piadas
Lista todas as piadas de uma categoria específica (Filtro por caminho)
GET
/piadas/busca?q=termo
Busca piadas que contêm o termo na pergunta (Filtro por Query String com LIKE)



🧪 Como testar
Os testes das rotas foram configurados no arquivo testes.http para uso com a extensão REST Client do VS Code.
Exemplo de requisição para criar uma categoria:
HTTP
POST http://127.0.0.1:5000/categorias
Content-Type: application/json

{
  "nome": "Programação"
}

Exemplo de requisição para criar uma piada:
HTTP
POST http://127.0.0.1:5000/piadas
Content-Type: application/json

{
  "pergunta": "Por que o computador foi ao médico?",
  "resposta": "Porque ele estava com um vírus!",
  "categoria_id": 1
}




👥 Integrantes
Integrante: Miguel
Foco Principal: Estrutura Base & Tabela Pai (categorias)
Responsabilidade Prática no Código: Conexão com banco, criação das tabelas e CRUD completo de Categorias.
Integrante: Ícaro
Foco Principal: Tabela Filho (piadas) & Regras de Negócio
Responsabilidade Prática no Código: CRUD completo de Piadas, Foreign Key com Cascade e validações de dados.
Integrante: Lucas
Foco Principal: Consultas Avançadas & Documentação/Testes
Responsabilidade Prática no Código: Rotas de JOIN, filtros (Path e Query String), testes.http e README.md.



