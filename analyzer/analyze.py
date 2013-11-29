# -*- coding: utf-8 -*-
# copyright (c) Reto Aebersold.
# see license for details.
import glob
import json
import os

analyzer_root = os.path.dirname(os.path.abspath(__file__))


def main():
    grand_total = 0
    for json_file in glob.glob(analyzer_root + "/store/*.json"):
        json_data = open(json_file)
        data = json.load(json_data)
        grand_total += len(data)
        print data[0]['source'], len(data)
        json_data.close()

    print "Total", grand_total


if __name__ == "__main__":
    main()