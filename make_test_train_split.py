import pandas as pd
from sys import argv
import random

# argv = ['script', 'Tadpole/tadpole_fake_pmid_abstract.tsv', 'Tadpole/tadpole_real_pmid_abstract.tsv', 'Tadpole']

fake = pd.read_csv(argv[1], sep='\t')
real = pd.read_csv(argv[2], sep='\t')
real.index = list(range(len(real)))

fake_test_size = int(fake.shape[0] / 10)
fake_test_ids = random.sample(range(fake.shape[0]), fake_test_size)
fake_train_ids = [i for i in list(range(fake.shape[0])) if i not in fake_test_ids]
fake_train = fake.loc[fake_train_ids]
fake_test = fake.loc[fake_test_ids]

real_test_size = int(real.shape[0] / 10)
real_test_ids = random.sample(range(real.shape[0]), real_test_size)
real_train_ids = [i for i in list(range(real.shape[0])) if i not in real_test_ids]
real_train = real.loc[real_train_ids]
real_test = real.loc[real_test_ids]

train_labels = (['real'] * real_train.shape[0]) + (['fake'] * fake_train.shape[0])
train = pd.DataFrame({'pmid': list(real_train['pmid']) + list(fake_train['pmid']),
                      'abstract': list(real_train['abstract']) + list(fake_train['abstract']),
                      'label': train_labels})

test_labels = (['real'] * real_test.shape[0]) + (['fake'] * fake_test.shape[0])
test = pd.DataFrame({'pmid': list(real_test['pmid']) + list(fake_test['pmid']),
                     'abstract': list(real_test['abstract']) + list(fake_test['abstract']),
                     'label': test_labels})

res_dir = argv[3]
if res_dir[-1] != '/':
    res_dir += '/'
train.to_csv(res_dir + 'train.tsv', sep='\t')
test.to_csv(res_dir + 'test.tsv', sep='\t')
pd.concat([test, train]).to_csv(res_dir + 'dataset.tsv', sep='\t')