#!/bin/bash
now=$(date +"%Y%m%d_%H%M%S")
job='1464_semi'
ROOT=../../../..

mkdir -p log

# use torch.distributed.launch
python -m torch.distributed.launch \
    --nproc_per_node=$1 \
    --nnodes=1 \
    --node_rank=0 \
    --master_addr=localhost \
    --master_port=$2 \
    $ROOT/train_semi.py --config=config.yaml --seed 2 --port $2 2>&1 | tee log/seg_$now.txt


# python -m torch.distributed.launch --nproc_per_node=1 --nnodes=1 --node_rank=0 --master_addr=localhost --master_port=6007 ../../../../train_semi.py --config=config.yaml --seed 2 --port 6007
# python ../../../../eval.py --config=config.yaml --base_size 2048 --scales 1.0 --model_path=checkpoints/ckpt_best.pth --save_folder=checkpoints/results 
