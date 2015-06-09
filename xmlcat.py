import sys
import time
import getopt
import xml.etree
import xml.etree.ElementTree as ET


class Profiler(object):
    def __enter__(self):
        self._startTime = time.time()
         
    def __exit__(self, type, value, traceback):
        print("Время затраченное на выполнение: {:.20f} sec".format(time.time() - self._startTime))

def main(argv):
    with Profiler() as p:
        inputfile = ''
        query_to_find = ''
        replace_value = ''
        query_to_delete = ''
        outputfile = ''
        tree = ''
        root = ''
        tree_out = ET
        element_string = ''
        encoding = 'UTF-8'
        count = 0

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
                founded = root.findall(query_to_find)
                if r:
                    for element in founded:
                        element.text = replace_value
                        count += 1
                    print("Изменено", count, "узлов.")
                else:
                    #tree_out.Element.append()
                    #print(ET.ElementTree(founded))
                    print("Найдено", len(founded), "узлов")       

            elif d:
                if q:
                    root = tree_out.getroot()
                    for element in root.findall(query_to_find):
                        root.remove(element)
                else:
                    for element in root.findall(query_to_delete):
                        root.remove(element)
                        count += 1
                    print("Удалено", count, "узлов.")    

            else:
                print(help_answer)
                exit()

            if o:
                if q and not r:
                    tree_out.write(outputfile, encoding, True)
                else:
                    tree.write(outputfile, encoding, True)
            else:
                outputfile = inputfile.split('.', 1)[0] + '_edited.xml'
                #print(outputfile)
                if q and not r:
                    tree_out.write(outputfile, encoding, True)
                else:
                    tree.write(outputfile, encoding, True)
            print("Отредактированный файл сохранен в ", outputfile,".")
        else:
            print(help_answer)
            exit()


if __name__ == "__main__":
    main(sys.argv[1:])
