import yaml
import xml.etree.ElementTree as xml_tree

with open("feed.yaml", "r") as file:
    yaml_data = yaml.safe_load(file)

rss_element = xml_tree.Element('rss', {
    'version': '2.0',
    'xmlns:itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd',
    'xmlns:podcast': 'https://podcastindex.org/namespace/1.0'
})

channel_element = xml_tree.SubElement(rss_element, 'channel')

for key in yaml_data:
    if key == 'author':
        xml_tree.SubElement(channel_element, f'itunes:{key}').text = yaml_data[key]
    elif key == 'image':
        xml_tree.SubElement(channel_element, f'itunes:{key}', {
            'href': yaml_data['link'] + yaml_data[key]
        })
    elif key == 'category':
        xml_tree.SubElement(channel_element, key, {
            'text': yaml_data[key]
        })
    elif key != 'item':
        xml_tree.SubElement(channel_element, key).text = yaml_data[key]

for item in yaml_data['item']:
    item_element = xml_tree.SubElement(channel_element, 'item')

    for key in item:
        if key == 'duration':
            xml_tree.SubElement(item_element, f'itunes:{key}').text = item[key]
        elif key == 'published':
            xml_tree.SubElement(item_element, 'pubDate').text = item[key]
        elif key == 'length':
            xml_tree.SubElement(item_element, 'enclosure', {
                'length': item[key],
                'url': yaml_data['link'] + item['file'],
                'type': 'audio/mpeg'
            })
        else:
            xml_tree.SubElement(item_element, key).text = item[key]
        
    xml_tree.SubElement(item_element, 'itunes:author').text = yaml_data['author']

output_tree = xml_tree.ElementTree(rss_element)
output_tree.write('podcast.xml', encoding='UTF-8', xml_declaration=True)
