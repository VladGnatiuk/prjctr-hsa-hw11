#!/bin/bash
set -e

siege -c 10 -r 10 -H "Content-Type: application/json" -f ./urls_cached.txt -b