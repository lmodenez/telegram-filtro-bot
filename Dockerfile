FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV SESSION_PATH=/app/user_session.session
RUN bash -c 'if [ ! -z "$SESSION_B64" ]; then echo "$SESSION_B64" | base64 -d > $SESSION_PATH; fi'

CMD ["python", "main.py"]