## Aim and solution
Sort vcf file, natural ordering (1,2,10,MT,X)

```
head -1000 $1 | grep "^#"; cat $@ | grep -v "^#" | sort -k1,1V -k2,2n
```

Sort vcf file, use the default ordering (1,10,2,MT,X)

```
head -1000 $1 | grep "^#"; cat $@ | grep -v "^#" | sort -k1,1d -k2,2n
```

Refer to [script from vcflib](https://github.com/vcflib/vcflib/blob/5e3ce04f758c6df16bc4d242b18a24d725d2e6e5/scripts/vcfsort) and [vcftools](https://github.com/vcftools/vcftools) for detail.
