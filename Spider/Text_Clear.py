# 整理文本，去除多余字符


def clear(parameter):
    parameter = parameter.strip()
    parameter = parameter.replace("'", "")
    parameter = parameter.replace("\n", "")
    parameter = parameter.replace("\t", "")
    return parameter
