import collections


def compressed_string(string_1):
    d = collections.defaultdict(int)
    d.default_factory
    # for k, v in string_1:
    #     v = 1
    #     d[k].append(v)
    # d.items()
    print(d.items())
    for char in string_1:
        d[char] = +1
    print(d.items())




string_1 = "aAAAAAACCCCAAAARRRRROOOOOOBb"
compressed_string(string_1)

