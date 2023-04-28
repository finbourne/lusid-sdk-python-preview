FROM python:3.11.3

WORKDIR /usr/src/

RUN apt-get update && apt-get -y install jq

COPY requirements.txt requirements.dev.txt /usr/src/

RUN pip install --no-cache-dir -r requirements.txt -r requirements.dev.txt

#CMD /bin/bash
ENTRYPOINT PYTHONPATH=/usr/src/:/usr/src/tests python -m unittest discover -v
