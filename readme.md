# Conversor de Moedas 🪙

Um projeto simples e elegante de conversor de moedas que utiliza uma **API em Python (Flask)** para o backend e uma interface moderna em **HTML, CSS (Tailwind)** e **JavaScript** para o frontend.  
A aplicação busca taxas de câmbio em tempo real e realiza a conversão de forma instantânea.

---

## ✨ Funcionalidades

- **Conversão em Tempo Real**: As taxas de câmbio são obtidas de uma API externa para garantir valores atualizados.  
- **Backend Separado**: A lógica de negócio é desacoplada do frontend, rodando em um servidor Flask.  
- **Interface Intuitiva**: Design limpo e moderno, focado na experiência do usuário.  
- **Inversão Rápida**: Botão para inverter facilmente a moeda de origem e destino.  
- **Responsivo**: Funciona bem em desktops e dispositivos móveis.  

---

## 🛠️ Tecnologias Utilizadas

### Backend (API)
- **Python 3**: Linguagem de programação principal.  
- **Flask**: Microframework web para criar a API.  
- **Requests**: Biblioteca para fazer requisições HTTP à API de câmbio.  
- **Flask-Cors**: Para lidar com CORS e permitir comunicação entre frontend e backend.  

### Frontend
- **HTML5**: Estrutura da página.  
- **Tailwind CSS**: Estilização rápida e moderna.  
- **JavaScript (Vanilla)**: Manipulação do DOM e requisições `fetch` para a API.  
- **Phosphor Icons**: Ícones vetoriais.  

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
- **Python 3.8+** instalado  
- Um navegador web moderno (Chrome, Firefox, etc.)  

---

### 1. Clone o Repositório
```bash
git clone https://github.com/gabrielhcastro/Conversor-De-Moedas.git
cd Conversor-De-Moedas
```
### 2. Configure o Backend
#### a. Crie um Ambiente Virtual (Recomendado)
```bash
# Para Windows
python -m venv venv
venv\Scripts\activate

# Para macOS/Linux
python3 -m venv venv
source venv/bin/activate
```
#### b. Instale as Dependências Python
Crie um arquivo chamado `requirements.txt` na raiz do projeto com o seguinte conteúdo:
```bash
Flask
Flask-Cors
requests
```
Em seguida, instale as dependências:
```bash
pip install -r requirements.txt
```
#### c. Obtenha sua Chave de API
1. Vá para [ExchangeRate-API](https://www.exchangerate-api.com) e crie uma conta gratuita para obter sua chave.
2. Abra o arquivo `app.py` e insira sua chave na variável `API_KEY`:
```bash
# Em app.py
API_KEY = "SUA_CHAVE_AQUI"
```
### 3. Inicie a Aplicação
#### a. Inicie o Servidor Backend
No seu terminal, na pasta do projeto, execute:
```bash
python app.py
```
O servidor começará a rodar em `http://127.0.0.1:5000`. Deixe este terminal aberto.
#### b. Abra o Frontend
Simplesmente abra o arquivo `index.html` no seu navegador.
