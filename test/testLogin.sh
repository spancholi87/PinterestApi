#Testing the functionalities with the hostname of a cluster
hostname=192.168.0.78

#Login
echo $'\nTesting Login****************'
curl -i -H "Accept: application/json" --data "user_id=swap1&password=swap123" http://${hostname}:8080/v1/login

