import xml.etree.ElementTree as ET

xml_file = 'working_files/test_namespace.xml'

tree = ET.parse(xml_file)
ET.dump(tree)

root = tree.getroot()
# print(root.tag)

print("*****************************************************************")
print("No Namespace Registered")

for x in root.findall('.//name'):
    print(x.tag, " ", x.text)

print("*****************************************************************")

for actor in root.findall('{http://people.example.com}actor/{http://people.example.com}name'):
    print(actor.text)

print("*****************************************************************")
print("Namespace Registered")

ET.register_namespace("persona", 'http://people.example.com')
ET.register_namespace("ruolo", 'http://characters.example.com')
ET.dump(tree)

for actor in root.findall('.//'):
    print(actor.tag, "", actor.text)

for actor in root.findall('.//{http://people.example.com}name'):
    print(actor.text)

print("*****************************************************************")

ns = {'real_person': 'http://people.example.com',
      'role': 'http://characters.example.com'}

for actor in root.findall('real_person:actor', ns):
    name = actor.find('real_person:name', ns)
    print(name.text)
    for char in actor.findall('role:character', ns):
        print(' |-->', char.text)

print("*****************************************************************")

# esso = root.iterfind("./real_person:actor/{*}name/")
# for illo in esso:
#     print(illo.text)


