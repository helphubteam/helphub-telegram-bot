# helphub-telegram-bot
Bot uses pyTelegramBotAPI module from https://github.com/eternnoir/pyTelegramBotAPI. The module can be installed via pip 

# Installation:

1. Clone repository
2. CP env.example to .env and fill the file with propper token
3. docker build -t teleg_bot .
4. docker run --env-file .env teleg_bot
