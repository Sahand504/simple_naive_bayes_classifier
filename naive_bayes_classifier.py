import os
import operator
import nltk
import mytokenizer
import math

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

comp_train_fnames, comp_train_flines = mytokenizer.get_files_lines(COMP_TRAIN_DIR)
elec_train_fnames, elec_train_flines = mytokenizer.get_files_lines(ELEC_TRAIN_DIR)
comp_test_fnames, comp_test_flines = mytokenizer.get_files_lines(COMP_TEST_DIR)
elec_test_fnames, elec_test_flines = mytokenizer.get_files_lines(ELEC_TEST_DIR)

comp_train_tokens = mytokenizer.tokenize(comp_train_flines)
elec_train_tokens = mytokenizer.tokenize(elec_train_flines)
comp_test_files_tokens = mytokenizer.test_tokenize(comp_test_flines)
elec_test_files_tokens = mytokenizer.test_tokenize(elec_test_flines)

comp_train_token_dic = {}
elec_train_token_dic = {}
comp_test_token_dic = {}
elec_test_token_dic = {}

for token in comp_train_tokens:
    if token not in comp_train_token_dic:
        comp_train_token_dic[token] = 1
    else:
        comp_train_token_dic[token] += 1

for token in elec_train_tokens:
    if token not in elec_train_token_dic:
        elec_train_token_dic[token] = 1
    else:
        elec_train_token_dic[token] += 1

# print(type(comp_train_token_dic))
# comp_train_token_dic = sorted(comp_train_token_dic.items(), key=operator.itemgetter(1), reverse=True)
# elec_train_token_dic = sorted(elec_train_token_dic.items(), key=operator.itemgetter(1), reverse=True)
# print(type(comp_train_token_dic))

print(comp_train_token_dic)
print(elec_train_token_dic)
print(comp_test_files_tokens)
print(elec_test_files_tokens)

p_comp = len(comp_train_token_dic) / (len(comp_train_token_dic) + len(elec_train_token_dic))
p_elec = 1 - p_comp

c_comp = math.log2(p_comp)
c_elec = math.log2(p_elec)

print(math.log2(p_comp))
print(math.log2(p_elec))

missclass_counter = 0
for file_idx, comp_test_file_tokens in enumerate(comp_test_files_tokens):
    c_comp = math.log2(p_comp)
    c_elec = math.log2(p_elec)
    for comp_test_file_token in comp_test_file_tokens:
        if comp_test_file_token in comp_train_token_dic:
            c_comp += math.log2(comp_train_token_dic[comp_test_file_token])
        if comp_test_file_token in elec_train_token_dic:
            c_elec += math.log2(elec_train_token_dic[comp_test_file_token])
    if c_elec > c_comp:
        print("Miss Classified! Test Filename --> " + comp_test_fnames[file_idx])
        print("c_comp: " + str(c_comp))
        print("c_elec: " + str(c_elec))
        missclass_counter += 1

for file_idx, elec_test_file_tokens in enumerate(elec_test_files_tokens):
    c_comp = math.log2(p_comp)
    c_elec = math.log2(p_elec)
    for elec_test_file_token in elec_test_file_tokens:
        if elec_test_file_token in comp_train_token_dic:
            c_comp += math.log2(comp_train_token_dic[elec_test_file_token])
        if elec_test_file_token in elec_train_token_dic:
            c_elec += math.log2(elec_train_token_dic[elec_test_file_token])
    if c_elec < c_comp:
        print("Miss Classified! Test Filename --> " + elec_test_fnames[file_idx])
        print("c_comp: " + str(c_comp))
        print("c_elec: " + str(c_elec))
        print("-------------------------------------------------------------------")
        missclass_counter += 1

test_num = (len(comp_test_fnames) + len(elec_test_fnames))

correctclass_counter = test_num - missclass_counter
print("Missclassified Counter = " + str(missclass_counter))
print("Precision = " + str((correctclass_counter / test_num) * 100))
