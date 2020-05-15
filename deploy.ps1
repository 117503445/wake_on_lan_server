docker build -t 117503445/wake_on_lan_server .
docker rm wake_on_lan_server -f
docker run --name wake_on_lan_server -p 8004:80 -d --restart always  117503445/wake_on_lan_server

docker push 117503445/wake_on_lan_server