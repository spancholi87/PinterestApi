#Testing the functionalities with the hostname of a cluster
hostname=192.168.0.78

#Attach Pin
echo $'\nTesting Attach Pin****************'
curl -i -H "Accept: application/json" -X PUT --data "pin_id=3" http://${hostname}:8080/v1/user/swap1/board/1

