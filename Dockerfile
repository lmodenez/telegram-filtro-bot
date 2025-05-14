FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /app/session
RUN bash -c 'if [ ! -z "$SESSION_B64" ]; then echo "$SESSION_B64" | base64 -d > /app/session/user_session.session; fi'

CMD ["python", "main.py"]