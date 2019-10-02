import os
import operator
import nltk
import mytokenizer

nltk.download('punkt')
nltk.download('stopwords')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_DIR = os.path.join(BASE_DIR, "dataset2")
TRAIN_DIR = os.path.join(DATASET_DIR, "train")
TEST_DIR = os.path.join(DATASET_DIR, "test")
COMP_TRAIN_DIR = os.path.join(TRAIN_DIR, "comp.sys.ibm.pc.hardware")
COMP_TEST_DIR = os.path.join(TEST_DIR, "comp.sys.ibm.pc.hardware")
ELEC_TRAIN_DIR = os.path.join(TRAIN_DIR, "sci.electronics")
ELEC_TEST_DIR = os.path.join(TEST_DIR, "sci.electronics")


comp_train_flines = mytokenizer.get_files_lines(COMP_TRAIN_DIR)
elec_train_flines = mytokenizer.get_files_lines(ELEC_TRAIN_DIR)
comp_test_flines = mytokenizer.get_files_lines(COMP_TEST_DIR)
elec_test_flines = mytokenizer.get_files_lines(ELEC_TEST_DIR)

comp_train_tokens = mytokenizer.tokenize(comp_train_flines)
elec_train_tokens = mytokenizer.tokenize(elec_train_flines)
comp_test_tokens = mytokenizer.tokenize(comp_test_flines)
elec_test_tokens = mytokenizer.tokenize(elec_test_flines)

comp_train_token_dic = {}
elec_train_token_dic = {}
comp_test_token_dic = {}
elec_test_token_dic = {}

for token in comp_train_tokens:
    if token not in comp_train_token_dic:
        comp_train_token_dic[token] = 0
    else:
        comp_train_token_dic[token] += 1

for token in elec_train_tokens:
    if token not in elec_train_token_dic:
        elec_train_token_dic[token] = 0
    else:
        elec_train_token_dic[token] += 1

for token in comp_test_tokens:
    if token not in comp_test_token_dic:
        comp_test_token_dic[token] = 0
    else:
        comp_test_token_dic[token] += 1

for token in elec_test_tokens:
    if token not in elec_test_token_dic:
        elec_test_token_dic[token] = 0
    else:
        elec_test_token_dic[token] += 1


comp_train_token_dic = sorted(comp_train_token_dic.items(), key=operator.itemgetter(1), reverse=True)
elec_train_token_dic = sorted(elec_train_token_dic.items(), key=operator.itemgetter(1), reverse=True)
comp_test_token_dic = sorted(comp_test_token_dic.items(), key=operator.itemgetter(1), reverse=True)
elec_test_token_dic = sorted(elec_test_token_dic.items(), key=operator.itemgetter(1), reverse=True)

print(comp_train_token_dic)
print(elec_train_token_dic)
print(comp_test_token_dic)
print(elec_test_token_dic)
