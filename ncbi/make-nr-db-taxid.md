## making nr blastdb for specific taxid

### problem
NCBI NR database is huge if you need to do blast for a large set of seqs

### solution
Extract NR protein seq by taxid and blast using this subset seqs.
Here we build subset db for microbiome org, including bacteria, Archaea, Viruses, Fungi using [taxonkit](https://bioinf.shenwei.me/taxonkit/)
```
#step1 get taxid tree for each parent taxid
~/software/taxonkit/taxonkit list --ids 2 --indent "" > bacteria_taxids.txt
~/software/taxonkit/taxonkit list --ids 2157  --indent "" > Archaea_taxids.txt
~/software/taxonkit/taxonkit list --ids 10239  --indent "" > Viruses_taxids.txt
~/software/taxonkit/taxonkit list --ids 4751  --indent "" > Fungi_taxids.txt

#step2 get all accession id list for taxid trees
for orgn in Archaea_taxids Fungi_taxids Viruses_taxids; do

pigz -dc /mnt/database/public/NR/prot/prot.accession2taxid.gz \
    | /home/cuijie/software/csvtk/csvtk grep -t -f taxid -P ${orgn}.txt \
    | /home/cuijie/software/csvtk/csvtk cut -t -f accession.version \    
    | sed 1d \
    > ${orgn}.acc.txt

done

#step3 get seq for each accession id
for orgn in bacteria_taxids Archaea_taxids Fungi_taxids Viruses_taxids; do

/softwares/miniconda3/bin/seqkit grep -f ${orgn}.acc.txt /mnt/database/public/NR/nr_all_V1/nr > nr.${orgn}.fa

done
```

refer to [taxonkit tutorial](https://bioinf.shenwei.me/taxonkit/tutorial/) for more.
