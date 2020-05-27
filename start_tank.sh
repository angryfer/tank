#!/usr/bin/env bash
python3 ammo_generator.py
docker run \
    -v $(pwd):/var/loadtest \
    --net host \
    --rm
    -it direvius/yandex-tank
