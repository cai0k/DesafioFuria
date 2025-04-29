from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters
import unicodedata
from furia_keys import BOT_TOKEN
from datetime import datetime


app = ApplicationBuilder().token(BOT_TOKEN).build()


def remover_acentos(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    ).lower()


def calcular_dias_para_campeonato(data_inicio):
    """Calcula quantos dias faltam para o início do campeonato."""
    hoje = datetime.now()
    dias_restantes = (data_inicio - hoje).days
    return dias_restantes


def analisar_mensagem(texto):
    """Analisa a mensagem para responder de forma inteligente."""
    if ("proximo jogo" in texto or "quando" in texto or "jogo" in texto or "partida" in texto):
        return ("🎮 Próximo jogo:\n"
                "**FURIA x G2** — 25/04 às 16h (horário de Brasília)")

    if ("resultado" in texto or "ultimos jogos" in texto or "ultimas partidas" in texto or "jogos" in texto):
        return ("📊 Últimos resultados:\n"
                "• FURIA 0x2 The MongolZ\n"
                "• FURIA 0x2 Virtus.pro\n"
                "• FURIA 1x2 Complexity\n"
                "• FURIA 2x0 Betclic")

    if ("lineup" in texto or "jogadores" in texto or "time atual" in texto or "line" in texto):
        return ("🧠 Lineup atual:\n"
                "- Molodoy\n"
                "- KSCERATO\n"
                "- yuurih\n"
                "- Yekindar\n"
                "- FalleN (IGL)\n"
                "- Sidde (COACH)")

    if ("campeonato" in texto or "torneio" in texto or "proximos jogos" in texto):
        # Lista dos campeonatos
        campeonatos = [
            {"nome": "PGL Astana 2025", "inicio": datetime(2025, 5, 10), "fim": datetime(2025, 5, 18)},
            {"nome": "IEM Dallas 2025", "inicio": datetime(2025, 5, 19), "fim": datetime(2025, 5, 25)},
            {"nome": "BLAST.tv Austin Major 2025", "inicio": datetime(2025, 6, 3), "fim": datetime(2025, 6, 22)},
        ]
        
        resposta_campeonatos = "🏆 **Próximos Campeonatos:**\n\n"
        hoje = datetime.now()

        # Encontra qual é o próximo campeonato (menor dias_restantes)
        proximos_validos = [(camp, calcular_dias_para_campeonato(camp["inicio"])) for camp in campeonatos if calcular_dias_para_campeonato(camp["inicio"]) >= 0]
        proximos_validos.sort(key=lambda x: x[1])  # Ordena pelos dias restantes

        for i, (camp, dias_restantes) in enumerate(proximos_validos):
            destaque = "🔥" if i == 0 else "•"
            resposta_campeonatos += (
            f"{destaque} {camp['nome']} — começa em {dias_restantes} dias\n"
            f"   📅 {camp['inicio'].strftime('%d/%m')} até {camp['fim'].strftime('%d/%m')}\n\n"
        )

        return resposta_campeonatos.strip()

    if ("redes sociais" in texto or "instagram" in texto or "twitter" in texto or "youtube" in texto or "site" in texto or "x" in texto):
        return ("📲 Redes da FURIA:\n"
                "• Instagram: https://instagram.com/furiagg\n"
                "• X: https://x.com/FURIA\n"
                "• YouTube: https://www.youtube.com/@FURIAgg\n"
                "• Site oficial: https://furia.gg/")

    return None


# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    teclado = [["Proximo Jogo", "Ultimos Resultados"],
               ["Lineup", "Proximos Campeonatos"],
               ["Redes Sociais"]]
    reply_markup = ReplyKeyboardMarkup(teclado, resize_keyboard=True)

    await update.message.reply_text(
        "Fala, FURIOSO! 🐍\n\n"
        "Escolha uma opção ou digite o que está procurando 👇",
        reply_markup=reply_markup
    )


# Responder mensagens
async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = remover_acentos(update.message.text)

    resposta_inteligente = analisar_mensagem(texto)

    if resposta_inteligente:
        await update.message.reply_text(resposta_inteligente)
    else:
        await update.message.reply_text("Não entendi! Escolha uma opção no teclado. 👇")


if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, responder))

    print("Bot rodando...")
    app.run_polling()
