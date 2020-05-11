## Aim
raw BAM/SAM file from IonTorrent sequencers may need aligning before downstreaming analysis

## solution

```bash
/path/to/tmap mapall -n 16 -f /path/to/genome.fa  -r /path/to/Ion_pt2_B1700.bam  -v -Y -u --prefix-exclude 5 -o 2  -s B1700.bam  stage1 map4
```