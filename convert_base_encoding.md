## Aim
Convert base quality phred+64 => phred+33

```bash
## -Q INT    quality shift: ASCII-INT gives base quality [33]
## -V        shift quality by '(-Q) - 33'

seqtk seq -Q64 -V ample_name_R1.fastq.gz > sample_name_phred33_R1.fastq
```
