#!/usr/bin/env bash

# docker run --rm -v "$(pwd):/app" -w /app -ti python:2.7 ./setup.sh

set -ex

cd "$( dirname "${BASH_SOURCE[0]}" )"

[ -f .env ] || cp -vf .env.example .env

pip install -r requirements.txt
