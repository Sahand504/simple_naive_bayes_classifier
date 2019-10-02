
import os
import nltk

def remove_headers(lines):
    for line_idx, line in enumerate(lines):
        if line == "":
            lines = lines[line_idx + 1:]
            break
    return lines


def remove_digits(str):
    return ''.join([i for i in str if not i.isdigit()])


def get_files_lines(dir_name):
    files_lines = []
    for root, dirs, files in os.walk(dir_name):
        for filename in files:
            path = os.path.join(root, filename)
            with open(path) as file:
                file_str = file.read().splitlines()
                files_lines.append(remove_headers(file_str))
    return files_lines


stop_words = set(nltk.corpus.stopwords.words('english'))
def tokenize(files_lines):
    filtered_tokens = []
    for lines in files_lines:
        for line in lines:

            # Convert every string to lowercase
            line = line.lower()
            # Remove digits
            line = remove_digits(line)

            # Filter Punctuation
            tokenizer = nltk.RegexpTokenizer(r'\w+')
            word_tokens = tokenizer.tokenize(line)

            # Filter Stopwords and digits
            for w in word_tokens:
                if w not in stop_words:
                    filtered_tokens.append(w)
    return filtered_tokens

