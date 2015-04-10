import sys
import getopt
import xml.etree
import xml.etree.ElementTree as ET
from xml.dom import minidom


def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")


def main(argv):
    inputfile = ''
    query_to_find = ''
    replace_value = ''
    query_to_delete = ''
    outputfile = ''
    tree = ''
    root = ''
    tree_out = ET.Element('nodes')
    encoding = 'UTF-8'

    i = q = r = d = o = False

    help_answer = 'Usage: xmlcat.py -i <file> -q <XPath> -r <value> -d <XPath> -o <outputfile> -e <encoding>'

    try:
        opts, args = getopt.getopt(
            argv, "hi:q:o:r:d:e:", ["input=", "query=", "help=", "output=", "replace=", "delete=", "encoding="])

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

        if opt in ("-r", "--replace"):
            r = True
            replace_value = arg

        if opt in ("-d", "--delete"):
            query_to_delete = arg
            d = True

        if opt in ("-e", "--encoding"):
            encoding = arg

        if opt in ("-o", "--output"):
            outputfile = arg
            o = True

        if opt in ("-h", "--help"):
            print(help_answer)
            exit()

    if i:
        tree = ET.parse(inputfile)
        root = tree.getroot()

        if q:
            for node in root.findall(query_to_find):
                if r:
                    node.text = replace_value
                tree_out.extend(node)

        elif d:
            if q:
                root = tree_out.getroot()
                for node in root.findall(query_to_delete):
                    root.remove(node)
            else:
                for node in root.findall(query_to_delete):
                    root.remove(node)

        else:
            print(help_answer)
            exit()

        if o:
            if q:
                ET(tree_out).write(outputfile, encoding, True)
            else:
                tree.write(outputfile, encoding, True)
        else:
            if q:
                ET(tree_out).write(sys.stdout)
            else:
                tree.write(sys.stdout)
    else:
        print(help_answer)
        exit()


if __name__ == "__main__":
    main(sys.argv[1:])
