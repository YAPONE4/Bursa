import xml.dom.minidom

def convert_button(from_conv, to_conv, count):
    file = open('data.xml', 'rb')
    dom = xml.dom.minidom.parse(file)
    dom.normalize()
    nodeArray = dom.getElementsByTagName('Valute')
    for node in nodeArray:
        childs = node.childNodes
        if childs[3].childNodes[0].nodeValue == from_conv:
            value = childs[4].childNodes
            from_conv_res = float(value[0].nodeValue.replace(',', '.'))
        if childs[3].childNodes[0].nodeValue == to_conv:
            value = childs[4].childNodes
            to_conv_res = float(value[0].nodeValue.replace(',', '.'))
    result.config(text = str("%.4f" % (count * (from_conv_res / to_conv_res))))

if __name__ == "__main__":
    with open('data.xml', 'rb') as file:
        print(convert_button(file, 'Австралийский доллар', 'Азербайджанский манат', 100))
    