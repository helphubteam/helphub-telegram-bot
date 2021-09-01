FROM python:3.8
RUN pip install pyTelegramBotAPI
WORKDIR /app
COPY . .
ENTRYPOINT ["python", "teleg_bot.py"]
