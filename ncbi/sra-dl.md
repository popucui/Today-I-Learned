## Problem

NCBI's sra-tools and API's have switched to https since 2016, if you encounter [Obsolete software error](https://github.com/ncbi/sra-tools/wiki/Obsolete-software), you may need to update sra-tools. BTW, version 2.9.6-1 works well right out of the box, while the latest 2.10.0 compiled binary version not.

## Solution

```bash
## -O output dir
## -p show progress
## use 6 thread by default, run several rounds of test before choose the increase this
## as more thread not guarantee more bandwidth.
fasterq-dump SRR5627625 -O ./rawdata -p
```

Refer to [sra-tools howto](https://github.com/ncbi/sra-tools/wiki/HowTo:-fasterq-dump) for detail