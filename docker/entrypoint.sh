#!/bin/sh
bert-serving-start -http_port 8125 -num_worker=$1 -model_dir /model -max_seq_len None -pooling_strategy NONE
