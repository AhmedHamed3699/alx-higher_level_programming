#!/bin/bash
# script that takes in a URL, sends a request to that URL
curl -sw '%{size_download}' -o /dev/null "$1"
