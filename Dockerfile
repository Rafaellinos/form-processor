FROM python:3.11-buster AS poetry


RUN curl -sSL https://install.python-poetry.org | python3 -

COPY pyproject.toml poetry.lock ./

ENV POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_VIRTUALENVS_IN_PROJECT=false \
    POETRY_NO_INTERACTION=1

RUN pip install poetry

RUN poetry install --no-root --only main

FROM poetry AS app

COPY src/ /app/src/

COPY app.py /app/

CMD ["python", "/app/app.py"]