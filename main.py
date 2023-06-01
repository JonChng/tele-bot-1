import logging
from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, filters, MessageHandler, InlineQueryHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="I am a bot. Please talk to me!"
    )

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = ' '.join(context.args).upper()
    print(context.args)

    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)

async def inline_caps(update: Update, context:ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query

    if not query:
        return

    answers = []
    answers.append(
        InlineQueryResultArticle(
            id = query.upper(),
            title="Caps",
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    await context.bot.answer_inline_query(update.inline_query.id, answers)
if __name__ == "__main__":
    app = ApplicationBuilder().token("test").build()

    #Start Handler
    start_handler = CommandHandler("start", start)
    app.add_handler(start_handler)

    #Echo Handler
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    app.add_handler(echo_handler)

    #Caps Handler
    caps_handler = CommandHandler("caps", caps)
    app.add_handler(caps_handler)

    app.run_polling()