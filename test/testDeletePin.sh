#Testing the functionalities with the hostname of a cluster
hostname=192.168.0.78

#Delete Pin
echo $'\nTesting Delete Pin****************'
curl -i -H "Accept: application/json" -X DELETE http://${hostname}:8080/v1/user/swap1/board/4
