import json
import xml.etree.ElementTree as Elem


class SerializeJson:
    def serialize_json(self) -> str:
        return json.dumps({
            "title": self.title,
            "content": self.content,
        })


class SerializeXml:
    def serialize_xml(self) -> str:
        root = Elem.Element("book")
        Elem.SubElement(root, "title").text = self.title
        Elem.SubElement(root, "content").text = self.content
        return Elem.tostring(root, encoding="unicode")
