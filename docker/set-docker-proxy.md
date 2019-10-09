## set proxy server for docker daemon

For detail, please refer to <https://docs.docker.com/config/daemon/systemd/>. Basically you need to do this:
```bash

sudo mkdir -p /etc/systemd/system/docker.service.d
sudo touch /etc/systemd/system/docker.service.d/http-proxy.conf

## the http-proxy.conf content looks like this:
## need to replace demo server url with the real one
## set NO_PROXY variable if needed
[Service]
Environment="HTTP_PROXY=http://proxy.example.com:80/"

sudo systemctl daemon-reload
sudo systemctl restart docker
## verify proxy setting has been loaded 
systemctl show --property=Environment docker
## Or use this
docker info
```
