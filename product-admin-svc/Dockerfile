FROM python:3.9-slim

WORKDIR /root/app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "product-admin-app.py"]