# Rain 'n Shine Telegram Bot 🌤

A Telegram bot that gives you real-time weather information for any city in the world.

[Check it out](https://t.me/RainNShine_bot)

## Features
- `/weather <city>` — Get current weather for any city
- `/start` — Welcome message
- `/help` — Show available commands
- Real-time data from OpenWeatherMap API
- 404 handling for invalid cities

## Demo
```
/weather London

🌤 London, GB 🌤

• Temperature: 6.16°C
• Feels like: 3.84°C
• Condition: Scattered clouds
• Humidity: 74%
• Wind: 3.09 KM/H

Thank You for using @RainNShine_bot.
```

## Setup

1. Clone the repo
```bash
git clone https://github.com/aditya4w/Rain-n-Shine-Telegram-Bot
cd RainNShine_TGBot
```

2. Install dependencies
```bash
pip install python-telegram-bot requests
```

3. Configure
```bash
cp config.example.py config.py
```

4. Add your credentials in `config.py`
```python
TOKEN = 'your-bot-token'
WEATHER_API = 'your-openweathermap-api-key'
BOT_USERNAME = '@your-bot-username'
```

5. Run
```bash
python main.py
```

## Deployment
This bot is deployed on Railway for 24/7 uptime.
To deploy your own instance, set these environment variables in Railway:
```
TOKEN
WEATHER_API
BOT_USERNAME
```

## Built With
- Python
- python-telegram-bot v22
- OpenWeatherMap API
- Deployed on Railway
