#Test Case for REST URL'S discussed among the peers

#Testing the functionalities with the hostname of a cluster
hostname=192.168.0.78

echo 'Testing the functionalities'

#Register
echo $'\nTesting Register****************'
curl -i -H "Accept: application/json" --data "name=swap&user_id=swap1&password=swap123" http://${hostname}:8080/v1/reg

#Login
echo $'\nTesting Login****************'
curl -i -H "Accept: application/json" --data "user_id=swap1&password=swap123" http://${hostname}:8080/v1/login

#GetAllPins
echo $'\nTesting Getting all pins****************'
curl -i -H "Accept: application/json" http://${hostname}:8080/v1/pins

#Comment
echo $'\nTesting comment****************'
curl -i -H "Accept: application/json" --data "comment='good work'" http://${hostname}:8080/v1/user/swap1/pin/1

#Attach Pin
echo $'\nTesting Attach Pin****************'
curl -i -H "Accept: application/json" -X PUT --data "pin_id=2" http://${hostname}:8080/v1/user/swap1/board/1

#Delete Pin
echo $'\nTesting Delete Pin****************'
curl -i -H "Accept: application/json" -X DELETE http://${hostname}:8080/v1/user/swap1/board/4

#Get Pin
echo $'\nTesting Get Pin****************'
curl -i -H "Accept: application/json" http://${hostname}:8080/v1/pin/2

#Get Board
echo $'\nTesting Get Board****************'
curl -i -H "Accept: application/json" http://${hostname}:8080/v1/boards/1

#Get Boards
echo $'\nTesting Get Boards****************'
curl -i -H "Accept: application/json" http://${hostname}:8080/v1/boards

#Upload Pin From Url 
echo $'\nTesting Upload Pin****************'
curl -i -H "Accept: application/json" --data "name='client_url'&value=http://hd.wallpaperhunt.com/wp-content/uploads/2014/03/Hd-wallpapers-of-cars-free-download-1.jpg" http://${hostname}:8080/v2/user/swap1/pin/uploadurl 

#Upload Pin From Disk
echo $'\nTesting Upload Pin****************'
curl "http://${hostname}:8080/v2/user/swap1/pin/uploadfile" -F value=@"/home/swap/1.jpg"

#Get User Info
echo $'\nTesting Get User Info****************'
curl -i -H "Accept: application/json" http://${hostname}:8080/v1/user/swap1

#Create Board
echo $'\nTesting Create Board****************'
curl -i -H "Accept: application/json" --data "boardname='hello'" http://${hostname}:8080/v1/user/swap1/board
