# udpProxy
Cloning the incoming UDP packets

```shell
cp udpProxy.py /opt/udpProxy.py
cp udpProxy.service /etc/systemd/system/udpProxy.service

sudo systemctl daemon-reload
sudo systemctl enable udpProxy.service
sudo systemctl start udpProxy.service
```
