FROM python:3-slim AS builder
ADD . /app
WORKDIR /app
COPY main.py /app/main.py
# We are installing a dependency here directly into our app source dir
RUN pip install -r requirements.txt
ENV PYTHONPATH /app
ENTRYPOINT [ "python", "/app/main.py" ]
