## Aim
Calculate the time consumed running a script or simple command.
Besides using `time` or `date`, we can use a special variable in bash named `SECONDS`.

## Solution

```bash
SECONDS=0

## Command to run here

duration=$SECONDS
echo "$(($duration / 60)) minutes and $(($duration % 60)) seconds elapsed."
```