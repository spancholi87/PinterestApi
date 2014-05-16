#Testing the functionalities with the hostname of a cluster
hostname=192.168.0.78

#Comment
echo $'\nTesting comment****************'
curl -i -H "Accept: application/json" --data "comment='good work'" http://${hostname}:8080/v1/user/swap1/pin/1
