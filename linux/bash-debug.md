There are 2 options useful when debugging a bash script:

```bash
set -x
set -e
## Note that these 2 lines should be put at the begining of a bash script

#set -x
## for error trace, which means printing out each line of command that's beeing executed

#set -e
## Roughly means Exit when encounter error Exit if a pipeline, a list or compound command exit with non-zero status

```
