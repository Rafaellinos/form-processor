# Simple Form Processor

### Before you start

<p>
Fill the env file on /src/config/.env.example.
Rename the file to .env
</p>

E.g.:

```shell
cp src/config/.env.example src/config/.env
```

<p>
This application uses AWS DynamoDB therefore you need to create a table with the name <b>my-simple-forms</b> and a primary key <b>id</b>.
Also, make sure to fill the AWS credentials on the .env file and also use the environment variables necessary to use the AWS SDK.
</p>


### Run on local machine
<p>Installing dependencies</p>

```shell
poetry install
```

<p>How to run:</p>

```shell
uvicorn app.main:app
```

### Run on Docker

```shell
docker compose up -d
```

#### Running docker manually

```shell
docker build -t form-processor:latest . && docker run -p 8080:8080 form-processor:latest
```

### Health check

```shell
curl -f http://localhost:8080/api/health
```

