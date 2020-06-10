import pandas as pd
import re

fake = pd.read_csv('Tadpole/fake_abstracts.tsv',sep='\t', header=None)
real = pd.read_csv('Tadpole/rand_abstracts.tsv',sep='\t', header=None)

# get just pmid and abstract
fake_pmid = [ re.match('PMID:\\d*',x).group() for x in fake[0]]
fake_abstracts = list(fake[5])

real_pmid = [ re.match('PMID:\\d*',x).group() for x in real[0]]
real_abstracts = list(real[5])

pd.DataFrame({'pmid':fake_pmid,'abstract':fake_abstracts}).to_csv('Tadpole/tadpole_fake_pmid_abstract.tsv',sep='\t')
pd.DataFrame({'pmid':real_pmid,'abstract':real_abstracts}).to_csv('Tadpole/tadpole_real_pmid_abstract.tsv',sep='\t')






