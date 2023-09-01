#!bin/bash
# Send a GET request to a given URL and display the body of the response
curl -s -o /dev/null -w "%{http_code}" "$1"
