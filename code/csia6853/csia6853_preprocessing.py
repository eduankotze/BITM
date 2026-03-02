from bs4 import BeautifulSoup
import re
import string

##### HTML
def strip_html_tags(input_text: str) -> str:
    return re.sub(r"<[^>]+>", " ", input_text)


##### Emoticons and Emojis
EMOTICON_RE = re.compile(r"^[:;=8][\-o\*']?[\)\]\(\[dDpP/\\:\}\{@\|]+$")

def is_emoticon(token: str) -> bool:
    return bool(EMOTICON_RE.match(token))

def is_emoji(token: str) -> bool:
    # simple heuristic: non-ascii single char often catches emojis 🙂 😂 etc.
    return any(ord(ch) > 127 for ch in token)
    
def remove_punctuation_keep_emoticons(input_text: str) -> str:
    """
    Remove punctuation BUT keep emoticons like :) :( by extracting them first.
    Also keep apostrophes (don't -> don't) so contractions survive.
    Optionally keep # and @ if you want hashtags/mentions.
    """
    # Tokenize on whitespace just to detect emoticons before punctuation removal
    rough_tokens = input_text.split()
    emoticons = [t for t in rough_tokens if is_emoticon(t)]

    # Remove emoticons from the text temporarily so punctuation removal doesn't destroy them
    text_wo_emoticons = " ".join([t for t in rough_tokens if not is_emoticon(t)])

    # Remove punctuation (but keep apostrophes, #, @)
    punct_to_remove = string.punctuation
    for keep in ["'", "#", "@"]:
        punct_to_remove = punct_to_remove.replace(keep, "")

    trantab = str.maketrans({p: " " for p in punct_to_remove})
    cleaned = text_wo_emoticons.translate(trantab)

    # Add emoticons back as tokens at the end (simple + clear for students)
    if emoticons:
        cleaned = cleaned + " " + " ".join(emoticons)

    return cleaned


##### Lowercase
def to_lower(input_text: str) -> str:
    return input_text.lower()


##### Digits
def remove_digits(input_text: str) -> str:
    return re.sub(r"\d+", "", input_text)


##### Whitespaces
def remove_whitespaces(input_text: str) -> str:
    return " ".join(input_text.split())


##### Stopwords
import nltk
from nltk.corpus import stopwords, wordnet

STOP_WORDS = set(stopwords.words("english"))

def remove_stopwords(input_text: str) -> str:
    whitelist = {"n't", "not", "no"}  # keep sentiment flips
    tokens = input_text.split()

    kept = []
    for tok in tokens:
        # keep emoticons/emojis always
        if is_emoticon(tok) or is_emoji(tok):
            kept.append(tok)
            continue

        # stopword logic
        if tok in whitelist:
            kept.append(tok)
            continue
        if tok in STOP_WORDS:
            continue

        # optional: drop 1-letter noise BUT keep 'i' if you want
        if len(tok) <= 1 and tok not in {"i"}:
            continue

        kept.append(tok)

    return " ".join(kept)

##### Lemmatize
from nltk import word_tokenize, pos_tag
from nltk.stem import WordNetLemmatizer

LEMMATIZER = WordNetLemmatizer()

def to_wordnet_pos(treebank_tag: str):
    if treebank_tag.startswith("J"):
        return wordnet.ADJ
    if treebank_tag.startswith("V"):
        return wordnet.VERB
    if treebank_tag.startswith("N"):
        return wordnet.NOUN
    if treebank_tag.startswith("R"):
        return wordnet.ADV
    return wordnet.NOUN  # default fallback
    
def lemmatize(input_text: str) -> str:
    tokens = word_tokenize(input_text)
    tagged = pos_tag(tokens)

    lemmas = []
    for w, tb_tag in tagged:
        # keep emoticons/emojis as-is
        if is_emoticon(w) or is_emoji(w):
            lemmas.append(w)
            continue

        wn_pos = to_wordnet_pos(tb_tag)
        lemmas.append(LEMMATIZER.lemmatize(w, pos=wn_pos))

    return " ".join(lemmas)


#### Putting it all together
def preprocessing(input_text, do_stopwords=True, do_lemmatize=True):
    stripped_html = strip_html_tags(input_text)
    emotions_text = remove_punctuation_keep_emoticons(stripped_html)
    lower_text = to_lower(emotions_text)
    nodigits_text = remove_digits(lower_text)
    nowhitespaces_text = remove_whitespaces(nodigits_text)
    if do_stopwords:
        filtered_text = remove_stopwords(nowhitespaces_text)
    else:
        filtered_text = nowhitespaces_text

    if do_lemmatize:
        stem_text = lemmatize(filtered_text)
    else:
        stem_text = filtered_text

    return stem_text

