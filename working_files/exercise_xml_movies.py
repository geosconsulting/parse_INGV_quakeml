import xml.etree.ElementTree as ET

# import os
# print(os.getcwd())

xml_file = 'movies.xml'

tree = ET.parse(xml_file)
root = tree.getroot()

print(f"TAG {root.tag}")

print("================================")

for rating in root.findall('./genre/decade/movie/rating'):
    print(rating.text)

print("================================")

for favourite in root.findall("./genre/decade/movie[@favorite='True']"):
    print(favourite.attrib['title'])

print("================================")

for descriptions in root.findall("./genre/decade[@years='1990s']/movie[@favorite='False']/description"):
    print(descriptions.text)



print(root.find('./genre/decade').attrib['years'])
print(root.find('./genre/decade').tag)
print(root.find('./genre/decade/movie').attrib['title'])

print("================================")

for decades in root.iter('years'):
    print(decades.attrib)

print("================================")

for year in root.findall('.//genre/decade/movie/year'):
    print(year.text)

print("================================")


