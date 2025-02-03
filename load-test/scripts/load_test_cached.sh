#!/bin/bash
set -e

siege -c 100 -r 3 -H "Content-Type: application/json" -f ./urls_cached.txt -b