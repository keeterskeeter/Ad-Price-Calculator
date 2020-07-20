from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r'\w+')


def sep_numswords(str):
    nums = []
    words = []
    for x in str:
        try:
            nums.append(int(x))
        except ValueError:
            words.append(x)
    return [nums, words]


def price_ad_bw(str):
    final_price = 7.50
    all_words = tokenizer.tokenize(str)
    numsNwords = []
    for x in all_words:
        if len(x) >= 2:
            numsNwords.append(x)
        elif x.lower() == "i" or x.lower() == "a":
            numsNwords.append(x)
    numsNwords = sep_numswords(numsNwords)
    word_count = round(len(numsNwords[1]) + len(numsNwords[0]) / 3)

    pbw = word_count - 19
    if pbw >= 1:
        for _ in range(int(pbw)):
            final_price += .30
    return [round(final_price, 2), word_count]
