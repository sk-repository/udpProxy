# udpProxy
Cloning the incoming UDP packets

copy udpProxy.py to /opt/udpProxy.py
copy udpProxy.service to /etc/systemd/system/udpProxy.service

sudo systemctl daemon-reload
sudo systemctl enable udpProxy.service
sudo systemctl start udpProxy.service
