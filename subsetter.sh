# $1 list of PubMed IDs - only pubmed ids, nothing else
# $2 output file
while read p; do
  echo "$p"
        grep -m 1 $p all_abstracts.tsv >> $2
done <$1
