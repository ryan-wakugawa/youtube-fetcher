# Trabalho Prático de NoSQL

Permite importar informações dos últimos 10 videos publicados por canal de um canal do YouTube a partir da URL. Essas informações são armazenadas em um banco de dados MongoDB.

<div align="center">
   <img src="https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white"></>
   <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"></>
   <img src="https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white">
</div>

## Funcionalidades

- Comentários
- Live Chats
- Super Chats
- Transcrições

## Demonstração
https://github.com/user-attachments/assets/60acbf44-112b-405b-830c-97834130a84c

## Setup

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/youtube-fetcher.git
   cd python-transcription
   ```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure as variáveis de ambiente necessárias (por exemplo, chaves de API do YouTube e URI do MongoDB).

5. Execute o script principal:
   ```bash
   python main.py
   ```
