FROM python:3.12-slim

WORKDIR /code

COPY pyproject.toml ./

RUN pip install uv && \
    uv pip install --system .

COPY . .

ENV PYTHONPATH=/code

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]