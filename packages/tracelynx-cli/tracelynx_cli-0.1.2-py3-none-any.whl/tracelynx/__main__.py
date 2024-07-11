import sys

from tracelynx import tlcli


def main():
    tlcli.process_xml(username=sys.argv[1], password=sys.argv[2], xml_input=sys.argv[3], xml_output=sys.argv[4])


if __name__ == '__main__':
    main()
