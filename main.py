from telegram import Update
from telegram.ext import CommandHandler, ApplicationBuilder, ContextTypes, MessageHandler, filters
import requests

# for railway hosting and local
import os
try:
    from config import TOKEN, WEATHER_API, BOT_USERNAME
except ImportError:
     TOKEN = os.environ.get("TOKEN")
     WEATHER_API = os.environ.get("WEATHER_API")
     BOT_USERNAME = os.environ.get("BOT_USERNAME")

###################

async def start_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello there, Welcome to Rain 'n Shine Bot. Use \'/weather <city>\' to know the weather :)")

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(" Rain \'n Shine Bot Commands List:\n \n"
        "/start - Welcome message\n"
        "/help - Show this command list\n"
        "/weather <city> - Shows the weather of the City you entered."
        )

async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE):

    city = " ".join(context.args)

    if not city:
        await update.message.reply_text("usage: /weather <city>")
        return


    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API}&units=metric"

    response = requests.get(url)

    if response.status_code == 404:
            await update.message.reply_text("City not found! Check the spelling.")
            return


    data = response.json()


    city_name = data["name"]
    country = data["sys"]["country"]
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]
    wind = data["wind"]["speed"]

    result = f'''🌥️ {city_name}, {country} ☁️ 

• Temperature: {temp}°C
• Feels like: {feels_like}°C
• Condition: {description}
• Humidity: {humidity}%
• Wind: {wind} KM/H 

Thank You for using {BOT_USERNAME}.'''

    await update.message.reply_text(result)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    print(f"{BOT_USERNAME} is starting...")

    app.add_handler(CommandHandler("weather", weather))
    app.add_handler(CommandHandler("start", start_cmd))
    app.add_handler(CommandHandler("help", help_cmd))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, weather))

    print(f"{BOT_USERNAME} is polling...")
    app.run_polling()
