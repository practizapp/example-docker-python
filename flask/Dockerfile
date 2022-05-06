ARG PYTHON_VERSION
FROM python:${PYTHON_VERSION}
RUN useradd --create-home --shell /bin/nologin \
    --system --home-dir /app app
WORKDIR /app
COPY --chown=app:app ./src/requirements.txt /app/
RUN pip install -r /app/requirements.txt
COPY --chown=app:app ./src/ /app/
ENV FLASK_ENV=development
USER app
EXPOSE 5000
CMD ["python", "./main.py"]