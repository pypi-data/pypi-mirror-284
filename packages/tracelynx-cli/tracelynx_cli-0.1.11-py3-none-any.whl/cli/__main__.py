import sys

from cli import tlcli


def main():
    tlcli.process_xml(username=sys.argv[1], password=sys.argv[2], xml_input=sys.argv[3], xml_output=sys.argv[4],
                      data=sys.argv[5] if len(sys.argv) > 5 else None)


if __name__ == '__main__':
    main()
