#!/bin/bash
#
# test registration process

echo -e "\n"
curl -i -H "Accept: application/json" --data "username='foo'&password='bar'" http://192.168.0.78:8080/v1/reg
echo -e "\n"
