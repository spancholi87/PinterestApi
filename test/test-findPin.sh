#!/bin/bash
#
# test client access to our service

echo -e "\n"
curl -i -H "Accept: application/json" http://192.168.0.78:8080/v1/pins/0001
echo -e "\n"
