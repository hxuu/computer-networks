# Routers configuration

## R1

### interface ip addr

```bash
R1#show ip int brief
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/1            12.12.12.1      YES manual up                    up
Serial1/0                  172.16.28.2     YES manual up                    up
Serial1/1                  192.168.5.1     YES manual up                    up
```

## R2

### interface ip addr

```bash
R2(config-if)#do show ip int brief
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            13.13.13.1      YES manual up                    up
Serial1/0                  192.168.5.2     YES manual up                    up
Serial1/1                  10.10.10.1      YES manual up                    up
```

## R3

### interface ip addr

```bash
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            11.11.11.1      YES manual up                    up
Serial1/0                  10.10.10.2      YES manual up                    up
Serial1/1                  172.16.28.1     YES manual up                    up
```
