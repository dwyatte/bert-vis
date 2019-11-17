FROM ubuntu:18.04

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

COPY requirements.txt .

RUN pip3 install -r requirements.txt && rm requirements.txt

COPY *.py /bert_vis/

CMD bokeh serve /bert_vis/vis.py --args $INPUT_FILES