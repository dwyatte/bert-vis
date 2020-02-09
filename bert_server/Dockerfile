# FROM nvidia/cuda:10.0-base
FROM ubuntu:18.04

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

RUN pip3 install pip --upgrade

COPY requirements.txt .
RUN pip install -r requirements.txt && rm requirements.txt

CMD bert-serving-start -model_dir $MODEL_DIR -ckpt_name $CKPT_NAME -num_worker $NUM_WORKER