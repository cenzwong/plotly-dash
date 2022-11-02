# https://github.com/w4/bin

```
$ curl -X PUT --data 'hello world' https://bin.gy
https://bin.gy/cateettary
$ curl https://bin.gy/cateettary
hello world
```

```
import requests

r = requests.put('https://bin.gy', data ={'key':'value'})
r.text


rr = requests.get(r.text, headers = {"User-Agent": "curl"})
rr.content
```