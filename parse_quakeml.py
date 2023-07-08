import xml.etree.ElementTree as ET

xml_file = 'working_files/response_1688110777216.xml'

tree = ET.parse(xml_file)
root = tree.getroot()

# ET.dump(tree)

# for elem in root.findall('.'):
#     print(elem.attrib)
#
# for elem in root.findall("./{http://quakeml.org/xmlns/bed/1.2}eventParameters"):
#     print(elem.attrib)
#
# for elem in root.findall("./{http://quakeml.org/xmlns/bed/1.2}eventParameters/{http://quakeml.org/xmlns/bed/1.2}event"):
#     print(elem.attrib)
#
# for elem in root.findall("./{http://quakeml.org/xmlns/bed/1.2}eventParameters/{http://quakeml.org/xmlns/bed/1.2}event/"
#                          "{http://quakeml.org/xmlns/bed/1.2}type"):
#     print(elem.text)

ns = {'g': "http://quakeml.org/xmlns/quakeml/1.2",
      'g': "http://quakeml.org/xmlns/bed/1.2",
      'i': "http://webservices.ingv.it/fdsnws/event/1"
      }

print("*****************************************************************")

for elem in root.findall("g:eventParameters", ns):
    print(elem.tag)

print("*****************************************************************")

for elem in root.findall("g:eventParameters/g:event", ns):
    print(elem.attrib['publicID'].split("=")[-1])

print("*****************************************************************")

for elem in root.findall("g:eventParameters/g:event/g:type", ns):
    print(elem.text)

print("*****************************************************************")

# for elem in root.findall("general:eventParameters/general:event/general:creationInfo/general:creationTime", ns):
#     print(elem.text)
#
# for elem in root.findall("general:eventParameters/general:event/general:latitude", ns):
#     print(elem.text)
#
# for elem in root.findall("general:eventParameters/general:event/general:longitude", ns):
#     print(elem.text)

all_elements = []
for elem in root.findall("g:eventParameters/g:event/g:creationInfo/", ns):
    all_elements.append(elem.text)

chunks = [all_elements[x:x+4] for x in range(0, len(all_elements), 4)]
print(chunks)

print("*****************************************************************")

for elem in root.findall("g:eventParameters/g:event/g:description/g:text", ns):
    print(elem.text)

print("*****************************************************************")