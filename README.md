# Clube Membros do YouTube

Este projeto permite gerenciar membros pagos de um canal do YouTube e realizar sorteios entre os membros atuais. O programa é executado no terminal e utiliza o arquivo CSV exportado do próprio YouTube Studio para acessar informações sobre os membros do canal.

## Requisitos

- Python 3.7+

## Instalação

1. Clone o repositório:

```
git clone https://github.com/gabrielfroes/python-random-youtube-members.git
cd python-random-youtube-members
```

2. Crie um ambiente virtual e ative-o:

```
python -m venv venv
source venv/bin/activate # Para usuários Linux/macOS
venv\Scripts\activate # Para usuários Windows
```

3. Instale as dependências:

```
pip install -r requirements.txt
```

4. Baixe o arquivo CSV com os membros do Clube de Membros do YouTube a partir do painel do YouTube Studio e salve-o na pasta `data` do projeto com o nome `members.csv`. Deixamos um arquivos chamado `members.csv.example` com um modelo de dados de exemplo. Se quiser renomeie-o para testar.

5. Copie o arquivo `.env.example` para `.env` e preencha as informações necessárias:

```
cp .env.example .env
```

6. Edite o arquivo `.env` e substitua `[YOUR_CHANNEL_ID_HERE]` e `[YOUR_YOUTUBE_API_KEY_HERE]` pelos valores reais das suas credenciais.

## Uso

7. Execute o script `main.py` para iniciar o programa:

```
python main.py
```

Siga as instruções exibidas no terminal para gerenciar membros e realizar sorteios.

## Testes

8. Para executar os testes de unidade, execute o seguinte comando:

```
python -m unittest discover tests
```

## Contribuições

Contribuições são bem-vindas! Por favor, sinta-se à vontade para abrir uma issue ou enviar um pull request.
