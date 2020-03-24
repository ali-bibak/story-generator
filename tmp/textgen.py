import random, re

SEP = " " # token separator symbol
words = []
eps = 0.05
delm_prop = 40
sentence_min_length, sentence_max_length = 3, 6
output_file = 'persian_story.txt'
def make_ngrams(tokens, N):
    """ Returns a list of N-long ngrams from a list of tokens """

    ngrams = []
    for M in xrange(1, N + 1):
        for i in range(len(tokens)-M+1):
            ngrams.append(tokens[i:i+M])
    return ngrams


def ngram_freqs(ngrams):
    """ Builds dict of TOKEN_SEQUENCEs and NEXT_TOKEN frequencies """

    ### has form TOKEN_SEQUENCE : DICT OF { NEXT_TOKEN : COUNT }
    ###      e.g        "a b c" : {"d" : 4, "e" : 2, "f" : 6 }
    counts = {}
    story = {}
    # Using example of ngram "a b c e" ...
    for ngram in ngrams:
        token_seq  = SEP.join(ngram[:-1])   # "a b c"
        last_token = ngram[-1]              # "e"
        story[last_token] = 1
        # create empty {NEXT_TOKEN : COUNT} dict if token_seq not seen before
        if token_seq not in counts:
            counts[token_seq] = {};

        # initialize count for newly seen next_tokens
        if last_token in ['.','!', '?', ',']:
            last_token = '.'
        if last_token not in counts[token_seq]:
            counts[token_seq][last_token] = 0;

        counts[token_seq][last_token] += 1;
        # if last_token == '.':
        #     counts[token_seq][last_token] += delm_prop
    words = story.keys()
    return counts;


def next_word(text, N, counts):
    """ Outputs the next word to add by using most recent tokens """

    token_seq = SEP.join(text.split()[-(N-1):]);
    choices = counts[token_seq].items();

    # make a weighted choice for the next_token
    # [see http://stackoverflow.com/a/3679747/2023516]
    for w in words:
        if not w in counts[token_seq]:
            # if not w in ['.','!', '?', ',']:
            choices.append((w, eps))
            # else:
            #     choices.append(('.', eps * delm_prop))
    total = sum(weight for choice, weight in choices)
    r = random.uniform(0, total)
    upto = 0
    for choice, weight in choices:
        upto += weight;
        if upto > r: return choice
    assert False                            # should not reach here


def preprocess_corpus(filename):
    s = open(filename, 'r').read()
    s = re.sub('[()]', r'', s)                              # remove certain punctuation chars
    s = re.sub('([.-])+', r'\1', s)                         # collapse multiples of certain chars
    s = re.sub('([^0-9])([.,!?])([^0-9])', r'\1 \2 \3', s)  # pad sentence punctuation chars with whitespace
    s = ' '.join(s.split()).lower()                         # remove extra whitespace (incl. newlines)
    return s;


def postprocess_output(s):
    s = re.sub('\\s+([.,!?])\\s*', r'\1 ', s)                       # correct whitespace padding around punctuation
    s = s.capitalize();                                             # capitalize first letter
    s = re.sub('([.!?]\\s+[a-z])', lambda c: c.group(1).upper(), s) # capitalize letters following terminated sentences
    return s


def gengram_sentence(corpus, N=4, sentence_count=20, start_seq="#"):
    """ Generate a random sentence based on input text corpus """

    ngrams = make_ngrams(corpus.split(SEP), N)
    counts = ngram_freqs(ngrams)

    if start_seq is None: start_seq = random.choice(counts.keys());
    rand_text = start_seq.lower();
    last_word = rand_text

    sentences = 0;
    i = 1
    while sentences < sentence_count and (last_word != '#' or rand_text == '#') and last_word != '$':
    # while (last_word != '#' or rand_text == '#') and last_word != '$':
        last_word = next_word(rand_text, min(i, N), counts)
        # if last_word.endswith(('.', '!', '?', ',')): # a little bug here :-"
        #     last_word = last_word[:-1] + SEP + '.'
        rand_text += SEP + last_word;
        i += 1
        sentences += 1 if rand_text.endswith(('.','!', '?')) else 0

    return postprocess_output(rand_text);

def normalize_sentence_length(text):
    text = text.split('.')
    new_text = []
    for x in text:
        length = random.randint(sentence_min_length, sentence_max_length)
        new_text.append(' '.join(x.split(' ')[-length:]) + ' . ')
    return ' '.join(new_text)

if __name__ == "__main__":

    corpus = preprocess_corpus("sinohe (2).txt")
    # corpus = preprocess_corpus("Chekhov.txt")
    f = open(output_file, 'w')
    f.write(normalize_sentence_length(gengram_sentence(corpus, start_seq="#")))
    f.close() 
