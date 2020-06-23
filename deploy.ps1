docker rm wake_on_lan_server -f
docker rmi 117503445/wake_on_lan_server
docker run --name wake_on_lan_server --network host -d --restart always  117503445/wake_on_lan_server
