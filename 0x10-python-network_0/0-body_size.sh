#!/bin/bash
# Gets the size of the body of a response from a URL
curl -sI "$1" | grep 'Content-Length:' | cut -f2 -d' '
