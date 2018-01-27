import re

_matches = lambda url, regexs: any(r.search(url) for r in regexs)

url = 'https://www.zhihu.com/collection/38887091'
patten = re.compile(r'collection\/\d+')
allow_res = []
allow_res.append(patten)


def match(url, allow_res):
    if allow_res and not _matches(url, allow_res):
        return False
    else:
        return True


print(match(url, allow_res))
