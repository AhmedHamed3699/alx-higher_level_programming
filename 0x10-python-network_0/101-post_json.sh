#!/bin/bash
# script that sends a request using a json file
curl -sH "Content-Type: application/json" -d "@$2" "$1"
