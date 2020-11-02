FROM python:3.7-slim
WORKDIR /app/
RUN pip install flask
ENV FLASK_ENV=production

COPY . .

CMD python -m my_app.main