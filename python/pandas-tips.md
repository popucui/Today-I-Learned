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

## Return multiple columns from pandas apply

```python
from abnumber import Chain
from pandarallel import pandarallel
## https://github.com/nalepae/pandarallel
pandarallel.initialize(progress_bar=True)

def get_vjgene(aaseq):
    chain = Chain(aaseq, scheme='imgt', assign_germline=True)
    vgene = chain.v_gene.split('*')[0]
    jgene = chain.j_gene.split('*')[0]
    return vgene, jgene, chain.cdr3_seq


ab_vs['VH_gene'], ab_vs['JH_gene'], ab_vs['CDRH3AA'] = zip(*ab_vs['VH_Full_length_AA'].apply(get_vjgene))
ab_vs['VL_gene'], ab_vs['JL_gene'], ab_vs['CDRL3AA'] = zip(*ab_vs['VL_Full_length_AA'].apply(get_vjgene))
```

## Return one column based on multiple other columns pandas apply

```python
def check_valiate(origin_seq, corrected_seq):
    return origin_seq == corrected_seq

test_df['validate_status'] = test_df.apply(lambda x: check_valiate(x['aa_sequence'], ['corrected_seq']), axis=1)
```

## Return multiple column based on one colum pandas

```python
def get_antigen(soup):
    lb_style = soup.find_all('a', class_ = 'label-style')

    if len(lb_style) < 1:
        print(f'Skip {soup.title.string}')
        return None
    antigen = lb_style[0].string
    antigen_url = 'https://tabs.craic.com' + lb_style[0]['href']
    # print(antigen_url)
    antigen_seq = extract_seq_antigen_url(antigen_url)
    
    return antigen, antigen_url, antigen_seq

def get_antigen_req(url):
    response = requests.get(url, cookies=cookies, headers=headers)
    assert response.status_code == 200
    soup = BeautifulSoup(response.text, 'html.parser')
    # time.sleep(5)
    # print(soup)
    return get_antigen(soup)

ab_info_df_dedup[ ['antigen', 'antigen_url', 'antigen_seqaa'] ] = ab_info_df_dedup['url_ab'].apply(get_antigen_req).apply(pd.Series)
```
