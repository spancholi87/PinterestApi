#!/bin/bash
#
# test client access to our service

echo -e "\n"
curl -i http://192.168.0.78:8080/moo/ping
echo -e "\n"
