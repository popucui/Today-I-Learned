## Aim
merge every 2 lines into 1

## solution

```
awk 'NR%2{printf "%s ",$0;next;}1' youfile
```

refer to [post at stackoverflow](https://stackoverflow.com/questions/9605232/how-to-merge-every-two-lines-into-one-from-the-command-line) for more.