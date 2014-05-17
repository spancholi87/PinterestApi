#Testing the functionalities with the hostname of a cluster
hostname=192.168.0.78

#Create Board
echo $'\nTesting Create Board****************'
curl -i -H "Accept: application/json" --data "boardname='hello'" http://${hostname}:8080/v1/user/swap1/board
