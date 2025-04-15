#!/bin/bash
CONTAINER="nvcr.io/nvidia/clara/bionemo-framework:2.5"
DATA_PATH="/home/neoho/M2Lab/workspace/data"
RESULT_PATH="/home/neoho/M2Lab/workspace/results"
WANDB_API_KEY="cd96b4a25d19e39cfeeee4dd3f7c456c5bfe2783"
WANDB_OFFLINE="TRUE" # Set to FALSE to upload to WandB during training

sudo docker run -t \
-p 8888:8888 \
--rm \
--network host \
--gpus all \
--shm-size=1g \
--ulimit memlock=-1 \
--ulimit stack=67108864 \
--volume ${DATA_PATH}:/data \
--volume ${RESULT_PATH}:/result \
--env HOME=/opt/nvidia/nemo_chem \
-w /opt/nvidia/nemo_chem \
--env WANDB_API_KEY=$WANDB_API_KEY \
--name bionemo_container \
${CONTAINER}