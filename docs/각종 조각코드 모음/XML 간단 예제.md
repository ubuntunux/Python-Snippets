> [Python Snippets](../README.md) / [각종 조각코드 모음](README.md) / XML 간단 예제.md
## XML 간단 예제
https://docs.python.org/2/library/xml.etree.elementtree.html
    
    from xml.etree.ElementTree import Element, dump, parse, SubElement, ElementTree, tostring
    from xml.dom import minidom
    
Unicode

I encountered the same problem as you in Python 2.6.

It seems that "utf-8" encoding for cElementTree.parse in Python 2.x and 3.x version are different. In Python 2.x, we can use XMLParser to encode the unicode. For example:

```
import xml.etree.cElementTree as etree

parser = etree.XMLParser(encoding="utf-8")
targetTree = etree.parse( "./targetPageID.xml", parser=parser )
pageIds = targetTree.find("categorymembers")
print "pageIds:",etree.tostring(pageIds)
```

You can refer to this page for the XMLParser method (Section "XMLParser"):

http://effbot.org/zone/elementtree-13-intro.htm

While the following method works for Python 3.x version:

```
import xml.etree.cElementTree as etree
import codecs

target_file = codecs.open("./targetPageID.xml",mode='r',encoding='utf-8')

targetTree = etree.parse( target_file )
pageIds = targetTree.find("categorymembers")
print "pageIds:",etree.tostring(pageIds)
```


xmlns : xml namespace 무시하기

- 이거 엄청 걸리적 거리는데 걍 string으로 xml load후 정규식으로 없애고 string을 xml로 파싱하면 된다.


Find tag from all children
```
country= tree.findall('.//country')
```