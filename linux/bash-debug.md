There are 2 options useful when debugging a bash script. ALL options here can be found using `man bash`.

```bash
set -x
set -e
## Note that these 2 lines should be put at the begining of a bash script

#set -x
## for error trace, which means printing out each line of command that's beeing executed

#set -e
## Roughly means Exit when encounter error.
## Exit if a pipeline, a list or compound command exit with non-zero status

set -u
## Treat unset variables and parameters other than the special parameters "@" and "*" as 
## an error when performing parameter expansion

set -o pipefail
## If  set,  the  return value of a pipeline is the value of the last (rightmost) 
## command to exit with a non-zero status, or zero if all commands in the pipeline 
## exit successfully.
```
