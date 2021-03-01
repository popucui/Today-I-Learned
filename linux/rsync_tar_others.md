## rsync a list of files

```bash
rsync -a --files-from=/tmp/foo /usr remote:/backup

rsync -avz  -h --progress --files-from ./file_to_transfer.txt ./ root@51.158.78.204:/data/RCC.FR2/
```
Refer to [transfer list of files using rsync](https://stackoverflow.com/questions/16647476/how-to-rsync-only-a-specific-list-of-files) for details

## exclude directory when tar

```
tar -zcf ~/AbSolution_live.tar.gz --exclude="AbSolution_live/Resources" ./AbSolution_live/
```