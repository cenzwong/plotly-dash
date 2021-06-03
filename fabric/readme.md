# Fabric

- Allow you to ssh to a machine to execute code

```
# 可使用任意的文件名
from fabric import Connection

host_ip = '172.16.10.250'  # 服务器地址
user_name = 'gl20-iot-gateway' # 服务器用户名
password = 'password'  # 服务器密码
cmd = 'ls'  # shell 命令，查询服务器上的时间

con = Connection(host_ip, user_name, connect_kwargs={'password': password})
result = con.run(cmd, hide=True)

print(result)
```
