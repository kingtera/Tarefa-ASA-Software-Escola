FROM python
RUN apt-get update && apt-get install python3-pip -y
WORKDIR /aula1408
COPY . /aula1408/
RUN pip install -r requirements.txt
CMD ["uvicorn","main:app", "--host", "0.0.0.0", "--port", "5000"] 