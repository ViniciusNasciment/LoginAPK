# Flet with Firebase

Este é um projeto que integra o framework Flet com o serviço de autenticação Firebase da Google. Ele fornece uma interface de usuário para registro e login, utilizando Firebase como backend para autenticação de usuários.

## Configuração

Antes de executar o código, você precisa configurar suas credenciais do Firebase. Certifique-se de ter uma conta no Firebase e obtenha as credenciais necessárias. As credenciais devem ser inseridas no arquivo `config` no código-fonte, na seção de configuração do Firebase.

## Requisitos

- Python 3.x
- Bibliotecas Python: `pyrebase`, `flet`

## Execução

Execute o arquivo Python `main.py` para iniciar o aplicativo. Isso iniciará um servidor local onde você pode acessar o aplicativo através de um navegador da web.

## Funcionalidades

- Registro de usuário: Os usuários podem se cadastrar fornecendo um e-mail e senha.
- Login de usuário: Os usuários registrados podem fazer login no aplicativo.
- Suporte ao login via Google e Facebook.

## Estrutura do Código

O código está estruturado em torno de duas principais classes: `UserWidget` e `main`. 
- `UserWidget`: Esta classe representa um widget de interface do usuário que é usado para criar campos de entrada e botões para registro e login.
- `main`: Esta função configura a página principal do aplicativo, definindo o título, cores, layout e adicionando os widgets de registro e login.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar uma solicitação de pull request.


