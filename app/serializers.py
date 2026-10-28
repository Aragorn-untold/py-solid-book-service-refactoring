import json
import xml.etree.ElementTree as ET


class SerializeJson:
    def serialize_json(self) -> str:
        return json.dumps({
            "title": self.title,
            "content": self.content,
        })


class SerializeXml:
    def serialize_xml(self) -> str:
        root = ET.Element("book")
        ET.SubElement(root, "title").text = self.title
        ET.SubElement(root, "content").text = self.content
        return ET.tostring(root, encoding="unicode")
