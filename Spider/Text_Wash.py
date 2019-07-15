import re


def Wash(text):

    # 匹配除a-z,A-Z,',",-之外所有
    pattern_letter = re.compile(r'[^a-zA-Z  \'  a-zA-Z+\-+a-zA-Z]+')
    new_text = pattern_letter.sub(' ', text).strip().lower()

    # to find the 's following the pronouns. re.I is refers to ignore case, he is
    pattern_is = re.compile("(it|he|she|that|this|there|here)(\'s)", re.I)
    # to find the 's following the letters, jack's
    pattern_s = re.compile("(?<=[a-zA-Z])\'s")
    # to find the ' following the words ending by s, students'
    pattern_s2 = re.compile("(?<=s)\'s?")
    # to find the abbreviation of not,isn't
    pattern_not = re.compile("(?<=[a-zA-Z])n\'t")
    # to find the abbreviation of would, I'd
    pattern_would = re.compile("(?<=[a-zA-Z])\'d")
    # to find the abbreviation of will
    pattern_will = re.compile("(?<=[a-zA-Z])\'ll")
    # to find the abbreviation of am
    pattern_am = re.compile("(?<=[I|i])\'m")
    # to find the abbreviation of are
    pattern_are = re.compile("(?<=[a-zA-Z])\'re")
    # to find the abbreviation of have
    pattern_ve = re.compile("(?<=[a-zA-Z])\'ve")

    new_text = pattern_is.sub(r"\1 is", new_text)
    new_text = pattern_s.sub("", new_text)
    new_text = pattern_s2.sub("", new_text)
    new_text = pattern_not.sub(" not", new_text)
    new_text = pattern_would.sub(" would", new_text)
    new_text = pattern_will.sub(" will", new_text)
    new_text = pattern_am.sub(" am", new_text)
    new_text = pattern_are.sub(" are", new_text)
    new_text = pattern_ve.sub(" have", new_text)
    new_text = new_text.replace('\'', ' ')

    return new_text
