#!/bin/bash
# script that sends a request and display status code
curl -sw "%{http_code}" -o /dev/null "$1"
