## problem

> fatal: unable to access 'https://github.com/<user>/<project>.git': server certificate verification failed. CAfile: /home/<user>/.ssl/trusted.pem CRLfile: none

## possible reasons
1. make sure you have `certificates` installed
2. the server CA file maybe expired or not valid

## solution

```bash
# make sure ca-certificates installed
sudo apt-get install --reinstall ca-certificates

# temporary and dirty, add extra params
git -c http.sslverify=false  push origin master

```