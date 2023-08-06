FROM python:3.8-slim-buster

WORKDIR /home/project/

COPY . .

RUN apt-get clean && apt-get update &&  apt-get install -y curl \ 
    && pip install --no-cache-dir --upgrade pip \
    && pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-root 

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "api_mlops_project.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]#ENTRYPOINT ["poetry", "run", "run-main"]