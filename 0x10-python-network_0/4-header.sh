#!/bin/bash
# script that sends a GET request with a specific header
curl -sH "X-School-User-Id: 98" "$1"
