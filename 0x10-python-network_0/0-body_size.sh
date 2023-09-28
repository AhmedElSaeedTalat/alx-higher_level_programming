#!/usr/bin/env bash
#script to display response size
url=$1
curl -s -o /dev/null -w '%{size_download}\n' "$url"
