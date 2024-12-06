FROM python:3.10-slim

ADD . /app/crewai

WORKDIR /app/crewai

RUN pip3.10 install crewai

RUN crewai install && uv sync --offline

CMD ["tail", "-f", "/dev/null"]