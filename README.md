# 🤖 Telegram Filtro Bot

Um bot que monitora canais do Telegram e envia mensagens filtradas (com base em palavras-chave) para outro chat ou bot.

## ✨ Funcionalidades

* Monitora mensagens de múltiplos canais do Telegram
* Filtra mensagens com base em palavras-chave configuradas
* Reenvia mensagens filtradas para um chat ou bot específico
* Fácil configuração via `.env`
* Containerizado com Docker

---

## 🚀 Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/telegram-filtro-bot.git
cd telegram-filtro-bot
```

### 2. Crie o arquivo `.env`

Baseie-se no exemplo:

```bash
cp .env.example .env
```

Edite o `.env` com suas credenciais do Telegram e bot.

---

## 🥪 Variáveis de ambiente

| Variável    | Descrição                                                        |
| ----------- | ---------------------------------------------------------------- |
| `API_ID`    | Seu ID da API do Telegram                                        |
| `API_HASH`  | Hash da API obtido no [my.telegram.org](https://my.telegram.org) |
| `BOT_TOKEN` | Token do seu bot Telegram                                        |
| `CHAT_ID`   | Chat ID ou grupo que receberá as mensagens                       |
| `KEYWORDS`  | Palavras-chave para filtro (separadas por vírgula)               |
| `CHANNELS`  | Canais a monitorar (sem `@`, separados por vírgula)              |

---

## 🐳 Usando com Docker

### Build da imagem

```bash
docker build -t telegram-filtro-bot .
```

### Executar

```bash
docker run --env-file .env telegram-filtro-bot
```

---

## 📦 Usando com Docker Compose (opcional)

Crie um `docker-compose.yml`:

```yaml
version: '3.8'
services:
  bot:
    build: .
    env_file: .env
    restart: unless-stopped
```

Execute com:

```bash
docker-compose up -d
```

---

## 📜 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

## 🤛 Contribuindo

Contribuições são bem-vindas!
Sinta-se livre para abrir uma issue ou enviar um PR.

---

## 🧠 Créditos

Desenvolvido com ❤️ por [Luiz Pedro Modenez](https://github.com/lmodenez)
