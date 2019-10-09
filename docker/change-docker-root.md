## Change the default Root dir for image
Refer to [this post](https://github.com/IronicBadger/til/blob/master/docker/change-docker-root.md) for detail

`vi /etc/systemd/system/docker.service.d/docker.root.conf` and fill in the commands below.

*Actually the conf file may be any name as long as the suffix is .conf*

```
[Service]
ExecStart=
ExecStart=/usr/bin/dockerd -g /new/docker/root -H fd://
```
Then do this:

```bash
sudo systemctl daemon-reload
sudo systemctl restart docker
## To verify the above setting take effect, if it works as expected, you'll see Docker Root Dir: /new/docker/root
docker info
```
