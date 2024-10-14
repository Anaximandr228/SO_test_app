FROM python:3.9


WORKDIR /SO_teat_app

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:${PATH}"

COPY poetry.lock pyproject.toml ./

RUN poetry install

COPY . .