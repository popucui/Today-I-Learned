## summary for a dataframe

```python
import pandas as pd
from matplotlib import pyplot as plt

df = pd.DataFrame({'lab':['A', 'B', 'C'], 'val':[10, 30, 20]})

## for the df
df.describe()

## for one column
df['val'].describe()
```

## hide tick label

```python
g1 = df.plot.barh( y='val')
g1.set(yticklabels=[])
plt.show()

## save fig to a file
g2 = df.plot.barh( y='val')
g2.set(yticklabels=[])
## set dpi higher
plt.savefig('./abc.png', dpi=300)
```

## subset df using groupby

```python
## select the 1st from each Barcode group
tcrb_ct_abundant = tcrb_ct.groupby('Barcode').first()
tcrb_ct_abundant_sorted = tcrb_ct_abundant.sort_values(by=['UMIs'], ascending=True)

## select the 2nd from each Barcode group
tcrb_ct_second_abundant = tcrb_ct.groupby('Barcode').nth(1)
```

## filter

keep those records which contains specific string in one column
```python
clonotype_uniq_jurkat = clonotype_uniq[ clonotype_uniq['CDR3_aa'].str.contains('ASSFSTCSANYGYT') ]
```