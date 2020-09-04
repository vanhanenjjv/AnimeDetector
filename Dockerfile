FROM python:3.8.5-buster

RUN apt-get update && apt-get install libgl1-mesa-glx -y

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

ENV HOST="0.0.0.0" \
    PORT="80"

ENTRYPOINT ["python3", "main.py"]
