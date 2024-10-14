# Api.alphavantag

- Uso a API Alpha Vantage, a função obtém dados intradiários de uma ação e bolsas.
- Este código pode ser usado para coletar dados históricos de ações, armazenar essas informações em um banco de dados local (SQLite), e posteriormente realizar análises ou consultas.

#### Criando o BD;

Escolhi aqui o SQLite que é um banco de dados leve, que pode ser útil para protótipos ou pequenos Data Warehouses.

- Baixe o arquivo executavel do SQLite do site https://www.sqlite.org/download.html
- Extraia o arquivo zip > Adicione o SQLite ao seu caminho do sistema > Vá até Configurações Avançadas do Sistema > Variáveis de Ambiente. Em Variáveis do Sistema, selecione Path e clique em Editar, adicione o caminho do arquivo SQLite e clique em ok.
- Abra o Prompt de Comando e digite > caminhe até a pasta do arquivo e digite o nome do executavel: sqlite3
- Baixe o DB Browser for SQLite : https://sqlitebrowser.org/dl/
- Faça a instalação.
![image](https://github.com/user-attachments/assets/4afa9ba7-5e56-4044-8157-7dcb04fec098)

#### SQLite para Power BI
Consumo os dados criados, tratados e exportados para o banco de dados, para o Power Bi, criando dashboards.

Primeiro baixe o DevartODBCSQLite.exe > https://marketplace.visualstudio.com/items?itemName=DevartSoftware.SQLiteODBCDriver3264bit
Faça a instalação do arquivo acima.
Vá em fontes de dados ODBC na pesquisa do windowns.
Adicionar > procure, na pasta do seu projeto, o banco de dados > vá em configuração > database e coloque o caminho correto, caso não tenha ido automaticamente.

![image](https://github.com/user-attachments/assets/ba89cd52-012d-4a23-8f3a-7dc8d7bdb858)
![image](https://github.com/user-attachments/assets/27a51849-3d64-4cfd-ab10-97a64c4b77d3)

