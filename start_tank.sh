#!/usr/bin/env bash
python3 ammo_generator.py
docker run \
    -v $(pwd):/var/loadtest \
    --net host \
    -it direvius/yandex-tank
