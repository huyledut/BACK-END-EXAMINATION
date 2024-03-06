FROM python:3.9.6
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]