#!/bin/bash -e
# Copyright (c) Facebook, Inc. and its affiliates.

# Download some files needed for running tests.

cd "${0%/*}"

BASE=https://dl.fbaipublicfiles.com/detectron2
mkdir -p coco/annotations

for anno in instances_val2017_100 
    dest=coco/annotations/$anno.json
    [[ -s $dest ]] && {
      echo "$dest exists. Skipping ..."
    } || {
      wget $BASE/annotations/coco/$anno.json -O $dest}
