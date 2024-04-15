#CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]

FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN python -m venv /app
ENV PATH = "/app:$PATH"

COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade -r requirements.txt
#COPY poetry.lock pyproject.toml ./
#RUN poetry install

COPY main.py ./

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]



#ARG APP_DIR=/homework_03
#ENV PATH /homework_03:$PATH
#WORKDIR /homework_03
#COPY . ./
#RUN python -m venv ${APP_DIR}
#RUN pip install --no-cache-dir --upgrade -r ${APP_DIR}/requirements.txt


