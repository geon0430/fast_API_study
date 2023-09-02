FROM nvcr.io/nvidia/pytorch:23.01-py3

RUN mkdir -p /workspace
WORKDIR /workspace

RUN apt-get update && apt-get -y upgrade
RUN pip install fastapi uvicorn

RUN git clone https://github.com/geon0430/fast_API_study.git

