import xml.etree.ElementTree as ET

xml_file = 'working_files/country_data.xml'

tree = ET.parse(xml_file)
root = tree.getroot()

ET.dump(tree)

# print(root.tag)
# print(root[0].tag)
# print(root[0][0].tag)
# print(root[0][1].tag)

# for child in root:
#     print("Child Root")
#     print(child.tag, child.attrib)
#     print("Child Data")
#     for child_data in child:
#         print(f'\t tag {child_data.tag}, attrib {child_data.attrib}, value {child_data.text}')
#     print("*****************************************************************")

for elem in root.findall("./country[@name='Panama']/neighbor[@direction='W']"):
    print(elem.attrib)

ranks = []
for elem in root.findall("./country/rank"):
    ranks.append(elem.text)
print(ranks)

countries = []
for elem in root.findall("./country"):
    print(elem.attrib)
    countries.append(elem.attrib["name"])
print(countries)

print("================================")

lst_cntry_rnks=[]
countries = root.findall("./country")
ranks = root.findall("./country/rank")

for rank in ranks:
    print(rank.text)

print("================================")

for country, rank in zip(countries, ranks):
    print(country.attrib['name'], rank.text)
    lst_cntry_rnks.append([country.attrib['name'], rank.text])

print(lst_cntry_rnks)
print(lst_cntry_rnks[-1])
