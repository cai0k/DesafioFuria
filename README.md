# 📢 Bot de Telegram - Fãs da FURIA

Este projeto foi desenvolvido como parte do processo seletivo para a FURIA Esports.  
O objetivo é criar um bot no Telegram para engajar e informar os fãs sobre jogos, campeonatos e novidades da organização.

---

## 🚀 Funcionalidades

- ✅ Teclado interativo com opções rápidas
- ✅ Responde perguntas digitadas de forma inteligente
- ✅ Atualiza automaticamente o tempo para os próximos campeonatos
- ✅ Mensagens personalizadas e organizadas

---

## ⚙️ Tecnologias usadas

- Python 3.10+
- Biblioteca `python-telegram-bot`
- Hospedagem em nuvem (Render ou Railway)

---

## 📄 Como rodar o projeto localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/cai0k/DesafioFuria.git
   cd DesafioFuria

2. Instale as dependências:
    pip install python-telegram-bot


3. Configure o token do bot:
    Crie um arquivo token.py contendo:
        BOT_TOKEN = "seu-token-aqui"


4. Rode o projeto:
    python main.py

---

## 🖥️ Hospedagem e Deploy

Para manter o bot sempre online, recomenda-se usar:
    - Render
    - Railway

Comando de inicialização:
    python main.py

---

## 📸 Layout do Bot

Teclado de opções exibido no início:
    [ Proximo Jogo ] [ Ultimos Resultados ]
    [ Lineup ] [ Proximos Campeonatos ]
    [ Redes Sociais ]

---

## ✨ Melhorias Futuras

Implementar notificações automáticas 30 minutos antes dos jogos:
   • Permitir que o usuário personalize alertas de campeonatos
   • Integração com API oficial da ESL para dados em tempo real
   • Uso de inteligência artificial para resumos pós-jogo
