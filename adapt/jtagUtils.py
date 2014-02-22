import csv
import os

adapt_base_dir = os.path.abspath(os.path.split(os.path.split(__file__)[0])[0])

manufacturer_lookup = {}
with open(os.path.join(adapt_base_dir, 'res', 'jtagmanufacturers.txt')) as f:
    reader = csv.reader(f,delimiter=';')
    manufacturer_lookup={int(r[0],16):r[1] for r in reader}
