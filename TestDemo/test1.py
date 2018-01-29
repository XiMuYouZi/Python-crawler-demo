import re

_matches = lambda url, regexs: any(r.search(url) for r in regexs)

url = 'https://book.douban.com/tag/BL?start=500&type=R>'
patten = re.compile(r'start=\d+\&type=')
allow_res = []
allow_res.append(patten)


def match(url, allow_res):
    if allow_res and not _matches(url, allow_res):
        return False
    else:
        return True


print(match(url, allow_res))
