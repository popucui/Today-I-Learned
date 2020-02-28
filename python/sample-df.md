## Aim
To get a fraction or fix num of records from a dataframe or array

```python
import numpy as np
import pandas as pd
## 90% as train set, 10% as validation set
df_train, df_validate = np.split(df, [ int(.9 * len(df)) ])

## to just get a sample set from dataframe
df_subset = df.sample(frac=0.9, random_state=1)
```

Refer to numpy's doc for more info