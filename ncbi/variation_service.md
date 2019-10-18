## Requirement
Get the rsid for a given variant with chrom, pos, ref and alt allelei using NCBI Variation Services API.
"variant_demo_simplify.tsv" hold basic info of variant, looks like:

```
chr1    69511   .       A       G
chr1    865694  .       C       T
```

Below command perform 2 steps:
1. split input tsv file, cause if records are too many, a server error will be returned, although offical site stat that up to 50000 VCF rows may be posted one time
2. use NCBI variation services API to post all rows which are stored in a file


## Solution

```bash
split -l 10000 /path/to/variant_demo_simplify.tsv
for s in $(echo "xa?"); do
curl  -X POST \
  --header "Content-Type: text/plain; charset=utf-8" --header "Accept: text/plain; charset=utf-8" \
  --data-binary "@${s}" \
  "https://api.ncbi.nlm.nih.gov/variation/v0/vcf/file/set_rsids?assembly=GCF_000001405.25" \
  > variant_demo_${s}_recalibrated.tsv
done
```

Here I'm using hg19, if you are using hg38, you should use another assembly version in the API url.
If "-i" was used, a header will appear in the returned result.
For more info, please refer to [offical website](https://api.ncbi.nlm.nih.gov/variation/v0/a)

