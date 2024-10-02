# Desafio 06

Desafio referente ao módulo: Arquitetura de Software e Padrão MVC

## Introdução

Faaala Dev,

Nesse desafio você reforçará de forma prática os **conceitos** que aprendemos nesse módulo.

Como se trata de um desafio, ele necessita de alguns conhecimentos além dos abordados nesse módulo, então é importante ter autonomia para conseguir pesquisar essas coisas caso não saiba como resolver. Por isso, lembre-se, t**enha calma** e **acredite no seu processo.**

O aprendizado daqui é muito importante e com certeza você conseguirá sair com muito conhecimento bacana 💜

## Sobre o desafio

<aside>
💡 Como tivemos um módulo completo, **não** vamos descrever detalhadamente rotas e propriedades dos registros a serem criadas, mas sim, as regras e requisitos que a API deve ter.

O motivo disso é para vocês **também** exercitarem ****o desenvolvimento e a estruturação dessa parte.

</aside>

A ideia desse desafio é criar uma API para um banco contendo operações para as tabelas de Pessoa Jurídica e Pessoa Física

Criação de um sistema bancário com clientes:

- Pessoas Físicas
- Pessoas Jurídicas

### Regras da aplicação

- A aplicação deve estar conectada a um banco SQLite;
- O projeto deve conter uma interface Cliente, com os métodos: Sacar dinheiro e Realizar extrato.
- As controllers devem possuir testes unitários para garantir que estão funcionando conforme devem funcionar.
- Deverá ser possível: Criar e listar usuários.

### Regras de negócio

- O método “sacar dinheiro” deve possuir um limite máximo menor em Pessoa física do que para pessoa jurídica

### Conceitos que pode praticar

- MVC
- Testes unitários (e quem sabe de integração 👀)
- Criação e integração com banco de dados SQLite

### Aviso!

Regras para aplicação e regras de negócio são obrigatórias, porém a forma como vão ser implementadas ficam a cargo do desenvolvedor.

### Material complementar

Script para a criação do banco de dados:

```sql
CREATE TABLE IF NOT EXISTS pessoa_fisica (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    renda_mensal REAL,
    idade INTEGER,
    nome_completo TEXT,
    celular TEXT,
    email TEXT,
    categoria TEXT,
    saldo REAL
);

CREATE TABLE IF NOT EXISTS pessoa_juridica (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    faturamento REAL,
    idade INTEGER,
    nome_fantasia TEXT,
    celular TEXT,
    email_corporativo TEXT,
    categoria TEXT,
    saldo REAL
);

INSERT INTO pessoa_fisica (renda_mensal, idade, nome_completo, celular, email, categoria, saldo)
VALUES
(5000.00, 35, 'João da Silva', '9999-8888', 'joao@example.com', 'Categoria A', 10000.00),
(4000.00, 45, 'Maria Oliveira', '7777-6666', 'maria@example.com', 'Categoria B', 15000.00),
(6000.00, 28, 'Pedro Santos', '5555-4444', 'pedro@example.com', 'Categoria C', 8000.00);

INSERT INTO pessoa_juridica (faturamento, idade, nome_fantasia, celular, email_corporativo, categoria, saldo)
VALUES
(100000.00, 10, 'Empresa XYZ', '1111-2222', 'contato@empresa.com', 'Categoria A', 50000.00),
(80000.00, 5, 'Empresa ABC', '3333-4444', 'contato@abc.com', 'Categoria B', 70000.00),
(120000.00, 8, 'Empresa 123', '5555-6666', 'contato@123.com', 'Categoria C', 90000.00);
```

## Entrega

Após concluir o desafio, você deve enviar a URL do seu código no GitHub para a plataforma. 

Além disso, que tal fazer um post no LinkedIn compartilhando o seu aprendizado e contando como foi a experiência?

É uma excelente forma de demonstrar seus conhecimentos e atrair novas oportunidades!

Feito com 💜 por Rocketseat 👋