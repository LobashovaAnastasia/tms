#!/bin/bash


# Copy the PATH to your ROOT folder (where all this code is placed) and set this PATH
# instead of my path!
YOUR_ROOT_PATH=/home/anastasiya/tms


export PYTHONPATH=${YOUR_ROOT_PATH}

python ${YOUR_ROOT_PATH}/lesson21_client_server_database/client_and_server/server.py
