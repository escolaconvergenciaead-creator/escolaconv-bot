from telegram import Update
from telegram.ext import ApplicationBuilder, ChatMemberHandler, CommandHandler, ContextTypes

TOKEN = "8624222620:AAE0xXfY-xphM9DNADWzQStFCckh1M_1bXg"
BOT_USERNAME = "EscolaConvBot"

async def boas_vindas_grupo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = update.chat_member
    if result.new_chat_member.status == "member":
        user = result.new_chat_member.user
        nome = user.first_name
        try:
            await context.bot.send_message(
                chat_id=result.chat.id,
                text=f"Seja bem-vindo(a), {nome}! 🎉 Clique aqui 👉 @{BOT_USERNAME} para receber seu material no privado!"
            )
        except Exception as e:
            print(f"Erro: {e}")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    nome = update.effective_user.first_name
    await update.message.reply_text(
        f"Olá, {nome}! Seja bem-vindo(a)! 🎉 Aqui está seu e-book:\nhttps://drive.google.com/file/d/1dCPFnSsDYsykzQF0hKj9GlluQM8BshMV/view?usp=sharing"
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(ChatMemberHandler(boas_vindas_grupo, ChatMemberHandler.CHAT_MEMBER))
app.add_handler(CommandHandler("start", start))
app.run_polling()
