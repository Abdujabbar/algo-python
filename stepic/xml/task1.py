__author__ = 'abdujabbor'

from xml.etree import ElementTree
_dict = {'red': 0, 'green': 0, 'blue': 0}


def sub(node, tag):
    return node.findall(tag) or []

def find_pages(node, depth=1):
  global _dict
  for r in sub(node, "cube"):
    find_pages(r, depth=depth+1)
    _dict[r.attrib['color']] += depth


xmlcontent = input()


root = ElementTree.fromstring('<xml>' + xmlcontent + '</xml>')
find_pages(root)
print(_dict['red'], _dict['green'], _dict['blue'])
