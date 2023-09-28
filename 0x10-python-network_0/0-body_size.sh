#!/bin/bash
#script to display response size
curl -s -o /dev/null -w '%{size_download}\n' "$1"
