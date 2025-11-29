FROM Python 3.13.7-slim

WORKDIR .
COPY . .

RUN pip install -r requirements.txt

CMD ["Python", "AudioYouTube.py"]