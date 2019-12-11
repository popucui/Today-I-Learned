## Aim
Shift DataFrame index from the default 0 to 1 based
```python
import numpy as np
dataframe.index = np.arange(1, len(dataframe) + 1)
```