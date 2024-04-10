FROM python:3.9-alpine
ADD requirements.txt /requirements.txt
RUN pip install -r requirements.txt
COPY . /src
WORKDIR /src
RUN chmod +x ./run_cardknox.sh && chmod 755 ./run_cardknox.sh
EXPOSE 80
CMD ["python", "./run_cardknox.py"]