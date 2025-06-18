import unittest
from html.parser import HTMLParser

class MetaRefreshParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.url = None

    def handle_starttag(self, tag, attrs):
        if tag.lower() == 'meta':
            attr_dict = dict((k.lower(), v) for k, v in attrs)
            if attr_dict.get('http-equiv', '').lower() == 'refresh':
                content = attr_dict.get('content', '')
                if '=' in content:
                    self.url = content.split('=', 1)[1].strip().strip("'\"")

class TestRedirect(unittest.TestCase):
    def test_meta_refresh_target(self):
        parser = MetaRefreshParser()
        with open('index.html', 'r', encoding='utf-8') as f:
            parser.feed(f.read())
        self.assertEqual(parser.url, 'https://www.wanglasa.com')

if __name__ == '__main__':
    unittest.main()
