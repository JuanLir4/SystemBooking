# Sistema de Reserva de Local

## Descrição
Este programa permite aos usuários realizar reservas de um local específico. Utiliza um banco de dados SQLite para armazenar informações sobre as reservas.

## Funcionalidades

### 1. Cadastrar Reserva
Os usuários podem cadastrar uma reserva para um local específico. O cadastro inclui informações como nome, CPF, data, hora inicial e hora final.

Para cadastrar uma reserva, execute o programa e escolha a opção 1 no menu. Siga as instruções no console, inserindo seu nome, CPF, data, hora inicial e hora final. O programa verificará se o horário está disponível e, se estiver, registrará a reserva com sucesso.

### 2. Visualizar Reservas Cadastradas
Os usuários podem visualizar as reservas cadastradas, filtrando por nome, data ou CPF. O sistema exibe informações detalhadas sobre cada reserva.

Para visualizar as reservas, execute o programa e escolha a opção 2 no menu. Você será solicitado a escolher uma opção de filtro (por nome, data ou CPF) e, em seguida, insira as informações correspondentes. O sistema exibirá a lista de reservas que correspondem aos critérios especificados.

## Exemplo do App Rodando

Para demonstrar o funcionamento do aplicativo, vamos considerar o seguinte cenário:

1. **Cadastrando uma Reserva:**
   - Escolha a opção 1 no menu.
   - Insira seu nome, CPF, data, hora inicial e hora final conforme solicitado pelo programa.
   - O programa verificará a disponibilidade e registrará a reserva.

2. **Visualizando Reservas Cadastradas:**
   - Escolha a opção 2 no menu.
   - Selecione um filtro (por exemplo, por nome).
   - Insira as informações correspondentes para o filtro escolhido.
   - O sistema exibirá uma lista de reservas que atendem aos critérios especificados.

Lembre-se de que este aplicativo não possui interface gráfica, mas a interação ocorre através do console. A falta de uma interface gráfica é uma escolha de design para manter a simplicidade do aplicativo, mas é uma parte fácil de melhorar para requisitos mais avançados.

## Executando o Programa

1. Certifique-se de ter o Python instalado no seu sistema.
2. Instale a biblioteca pyodbc usando o comando `pip install pyodbc`.
3. Execute o programa e siga as instruções no console para cadastrar ou visualizar reservas.

