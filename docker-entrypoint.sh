#!/bin/bash

set -ex

/h-client/bake.py

exec nginx -g "daemon off;"
