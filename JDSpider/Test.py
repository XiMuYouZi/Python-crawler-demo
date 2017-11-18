from JDSpider.Spider import *
from haixinSpider.parseHtml import *

def main():
    spider = JDSpider()
    spider.getComputerInfo()


def test():
    parser = parseHtml()
    text = parser.getStaticHtmlConten('http://huaban.com/boards/16312689/')
    print(text)

if __name__ == '__main__':
    test()