FROM python:3.12

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY app ./
COPY main.py ./

ENV PYTHONPATH=/app
#RUN flask db upgrade head
CMD ["flask", "db", "upgrade", "head"]
#CMD ["flask", "db","run","-h", "0.0.0.0", "-p", "5000"]