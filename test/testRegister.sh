#Testing the functionalities with the hostname of a cluster
hostname=192.168.0.78

#Register
echo $'\nTesting Register****************'
curl -i -H "Accept: application/json" --data "name=swap&user_id=swap1&password=swap123" http://${hostname}:8080/v1/reg
