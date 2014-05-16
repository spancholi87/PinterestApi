#Testing the functionalities with the hostname of a cluster
hostname=192.168.0.78

#Get Pin
echo $'\nTesting Get Pin****************'
curl -i -H "Accept: application/json" http://${hostname}:8080/v1/pin/2

