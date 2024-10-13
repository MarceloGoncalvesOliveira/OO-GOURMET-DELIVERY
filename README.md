# 🍽️ Sistema de Gerenciamento de Restaurantes

Este projeto é um sistema de gerenciamento de restaurantes desenvolvido em Python, que utiliza conceitos de **Orientação a Objetos (OO)**, como classes, herança e encapsulamento. O objetivo do aplicativo é permitir o cadastro de restaurantes, a adição de itens ao cardápio, o recebimento de avaliações e a listagem das informações relevantes sobre cada restaurante.

## 🛠 Tecnologias Utilizadas
- **Python**: Linguagem de programação utilizada para a implementação do sistema, fazendo uso dos princípios de OO.

## 📋 Funcionalidades
- ✅ **Cadastro de Restaurantes**: Permite cadastrar novos restaurantes, definindo nome e categoria.
- ✅ **Adição de Itens ao Cardápio**: Os usuários podem adicionar bebidas e pratos ao cardápio do restaurante, aplicando descontos.
- ✅ **Receber Avaliações**: Permite que os clientes avaliem os restaurantes com notas numéricas, encapsulando a lógica de avaliação na classe `Avaliacao`.
- ✅ **Listagem de Restaurantes**: Exibe todos os restaurantes cadastrados com suas informações, como média de avaliações e status, utilizando o conceito de **encapsulamento** para proteger os dados.

## 📂 Estrutura do Projeto
- **`avaliacao.py`**: Contém a classe `Avaliacao`, que encapsula a lógica de avaliação dos restaurantes.
- **`item_cardapio.py`**: Contém a classe abstrata `ItemCardapio`, que define a estrutura de itens do cardápio, como pratos e bebidas.
- **`bebida.py`**: Contém a classe `Bebida`, que representa as bebidas do cardápio e aplica descontos.
- **`prato.py`**: Contém a classe `Prato`, que representa os pratos do cardápio e aplica descontos.
- **`restaurante.py`**: Contém a classe `Restaurante`, responsável pela lógica de cadastro e gerenciamento dos restaurantes.
- **`main.py`**: Arquivo principal que inicializa o programa, cria instâncias e interage com as classes.

