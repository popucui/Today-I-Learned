## Aim
Disable user account or lock it when an account is no longer needed

## Solution
```bash
## -e means expiredate, below command set the account expired at 1970/1/2
## which literally means disabled
sudo usermod -e 1 <username>

## Note this lock the passwd, the user still may login by other way, 
## like using ssh key
sudo passwd -l <username>
```