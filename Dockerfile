FROM python:3.7

COPY \
  requirements.txt /etc/

RUN \
  pip install --upgrade pip && \
  pip install -r /etc/requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/opt/app"

ENTRYPOINT python -m rest
