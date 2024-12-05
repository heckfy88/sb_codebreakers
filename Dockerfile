FROM python:3.10-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY . .

#RUN python3.12 -m venv /app/.venv
#RUN uv sync --frozen
#python3-dev
#RUN apt-get install python3
#RUN python3 -m venv /app/.venv

RUN uv sync --frozen
ENV PATH="/app/.venv/bin:$PATH"

RUN crewai install

# Expose the port your app runs on (optional, if your app serves HTTP)
EXPOSE 8080

CMD ["tail", "-f", "/dev/null"]