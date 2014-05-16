#Testing the functionalities with the hostname of a cluster
hostname=192.168.0.78

#Get Boards
echo $'\nTesting Get Boards****************'
curl -i -H "Accept: application/json" http://${hostname}:8080/v1/boards
