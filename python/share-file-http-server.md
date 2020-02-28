## Aim

- Share large file in the same subnet
- Debug some issues with web server or issues related to port

## Solution
Use `http.server` module to set up a basic web server with one command, simple and very useful:

```bash
## We use python3 unless specifid other wise, you may consider SimpleHTTPServer for python2
## default bind IP is 0.0.0.0, default port is 8000
python -m http.server --directory /path/to/workdir --bind 192.168.xx.xx  8000

## python2
python -m SimpleHTTPServer 8000
```

Refer to [http.server](https://docs.python.org/3/library/http.server.html) for detail.