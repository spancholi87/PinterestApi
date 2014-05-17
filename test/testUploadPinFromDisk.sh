#Testing the functionalities with the hostname of a cluste
hostname=192.168.0.78

#Upload Pin From Disk
echo $'\nTesting Upload Pin****************'
curl "http://${hostname}:8080/v2/user/swap1/pin/uploadfile" -F value=@"/home/swap/1.jpg"
