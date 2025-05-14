import requests

from telethon import TelegramClient, events
from config.settings import settings

class TelegramFiltered:
    def __init__(self):
        self.client = TelegramClient('bot_session', settings.API_ID, settings.API_HASH)

    def run(self):
        @self.client.on(events.NewMessage())
        async def handle_event(event):
            if not (event.chat and event.chat.username):
                return

            channel = event.chat.username
            message = event.message.message
            self.handle_new_message(channel, message)

        print("⚡️ Monitoramento de canais iniciado!")
        print("Pressione Ctrl+C para sair.\n")
        self.client.start()
        self.client.run_until_disconnected()

    def handle_new_message(self, channel: str, message: str):
        if not message:
            return

        if channel.lower() not in set(settings.CHANNELS):
            return
        
        if any(keyword in message.lower() for keyword in settings.KEYWORDS):
            print(f"📥 [{channel}] Mensagem filtrada:")
            print(message)
            self.send_message(message)

    def send_message(self, message: str):
        url = f"https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": settings.CHAT_ID,
            "text": message
        }
        try:
            response = requests.post(url, data=payload)
            if response.status_code != 200:
                print("❌ Erro ao enviar para bot:", response.text)
        except Exception as e:
            print("Erro ao enviar mensagem:", e)

init = TelegramFiltered()
init.run()