# 📢 Bot de Telegram - Fãs da FURIA

Este projeto foi desenvolvido como parte do processo seletivo para a FURIA Esports.  
O objetivo é criar um bot no Telegram para engajar e informar os fãs sobre jogos, campeonatos e novidades da organização.

---

## 🐍 Funcionalidades

- 🎮 Informa o próximo jogo da FURIA
- 📊 Mostra os resultados mais recentes
- 🧠 Exibe o lineup atual
- 🏆 Lista os próximos campeonatos (com contagem regressiva automática)
- 📲 Compartilha as redes sociais oficiais da FURIA

---

## ⚙️ Tecnologias usadas

- Python 3.10+
- Biblioteca `python-telegram-bot`

---

## 📄 Como rodar o projeto localmente

### 1. Clone o repositório:
   ```bash
   git clone https://github.com/cai0k/DesafioFuria.git
   cd DesafioFuria
   ``` 

### 2. Instale as dependências

```bash
pip install python-telegram-bot
```


### 3. Crie seu bot no Telegram

1. Acesse o [@BotFather](https://t.me/BotFather) no Telegram.
2. Envie `/newbot` e siga os passos.
3. Copie o **token do bot** gerado.


### 4. Crie o arquivo `furia_keys.py`

Na raiz do projeto, crie o arquivo `furia_keys.py` com o conteúdo:

```python
BOT_TOKEN = "seu_token_aqui"
```

> Substitua `"seu_token_aqui"` pelo token do seu bot.

---

### 5. Rode o bot

```bash
python FuriaBot.py
```

Você verá a mensagem:

```
Bot rodando...
```

Agora seu bot está ativo e pode ser usado no Telegram!

---

## 📸 Layout do Bot

### Teclado de opções exibido no início:

    [ Proximo Jogo ] [ Ultimos Resultados ]
    [ Lineup ] [ Proximos Campeonatos ]
    [ Redes Sociais ]

---

## ✨ Melhorias Futuras

### Implementar notificações automáticas 30 minutos antes dos jogos:

   • Permitir que o usuário personalize alertas de campeonatos
   • Integração com API oficial da ESL para dados em tempo real
   • Uso de inteligência artificial para resumos pós-jogo

## 📄 Licença

Este projeto é apenas para fins educacionais e não possui vínculo oficial com a FURIA Esports.
