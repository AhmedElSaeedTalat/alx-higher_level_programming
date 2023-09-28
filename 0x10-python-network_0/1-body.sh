#!/bin/bash
#script to sends a GET request to the URL, and displays the body of the response
if [ "$(curl -s -w '%{http_code}' -o /dev/null "$1")"  -eq 200 ]
then
        curl -s "$1";
fi
