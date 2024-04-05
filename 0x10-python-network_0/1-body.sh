#!/bin/bash
# script that request a URL and display response if status code is 200
url="$1"
cmd=$(curl -Ls -w "%http_code" -o /tmp/response "$url")
code=${cmd: -3}
if [ "$code" -eq 200 ]; then
  cat /tmp/response
fi
rm -f /tmp/response
