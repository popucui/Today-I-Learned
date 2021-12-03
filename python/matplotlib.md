## refresh previous plot

```
import sys
import pandas as pd
import matplotlib.pyplot as plt

g1 = y.plot.bar(rot=0, color="g", figsize=(6,4))
g1.set_title("TCRb barcodes depth dist")
plt.savefig(sys.argv[2], dpi=300)

## use plt.clf() after savefig() to forget previous plot
plt.clf()
```