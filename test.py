import sys
import getopt
import xml.etree
import xml.etree.ElementTree as ET
import xml.dom.minidom


def main(argv):
    inputfile = ''
    query_to_find = ''
    replace_value = ''
    query_to_delete = ''
    outputfile = ''
    tree = ''
    root = ''
    tree_out = ET.Element
    encoding = 'UTF-8'
    count = 0
    i = q = r = d = o = False
    xml_string = ''
    help_answer = 'Usage: xmlcat.py -i <file> -q <XPath> -r <value> -d <XPath> -o <outputfile> -e <encoding>'

    try:
        opts, args = getopt.getopt(
            argv, "hi:q:o:r:d:e:", ["input=", "query=", "help=", "output=", "replace=", "delete=", "encoding="]
        )

    except getopt.GetoptError:
        print(help_answer)
        exit()

    for opt, arg in opts:

        if opt in ("-i", "--input"):
            i = True
            inputfile = arg

        if opt in ("-q", "--query"):
            q = True
            query_to_find = arg

        if opt in ("-o", "--output"):
            outputfile = arg
            o = True

    if i:
        tree = ET.parse(inputfile)
        root = tree.getroot()
        founded = root.findall('.')
        print(founded)
        tree_out = ET.ElementTree(founded)
        print("Найдено", len(founded), "узлов")
        
        #print(tree_out)
        tree_out.write('out.xml', encoding, True)    
    else:
        print(help_answer)
        exit()


if __name__ == "__main__":
    main(sys.argv[1:])
