#!/usr/bin/env bash
python3 ammo_generator_old.py
sudo docker run \
    -v $(pwd):/var/loadtest \
    --net host \
    --rm \
    -it direvius/yandex-tank
