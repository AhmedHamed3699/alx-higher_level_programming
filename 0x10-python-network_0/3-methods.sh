#!/bin/bash
# script that gets available http methods
curl -siX OPTIONS "$1" | grep Allow | sed 's/Allow: //'
