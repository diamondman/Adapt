import csv
import os

manufacturer_lookup = {}
with open(os.path.join(os.environ['ADAPT_CORE_DIR'],'res','jtagmanufacturers.txt')) as f:
    reader = csv.reader(f,delimiter=';')
    manufacturer_lookup={int(r[0],16):r[1] for r in reader}
