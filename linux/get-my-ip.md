## Aim
- get the current ip address
- get the current proxy server's ip address if you have a list of servers

## Solution

```bash
## you may want to add below into the .bashrc file
getip () {
  curl https://api.myip.com
}
## need to install and set up proxychains4 
getpip () {
  proxychains4 -q curl https://api.myip.com
}

```

Refer to [myip](https://www.myip.com/api-docs/) for more info.