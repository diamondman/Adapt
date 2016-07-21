from __future__ import print_function
import requests
from bs4 import BeautifulSoup
import re
import time

id_lookup_url = "http://bsdl.info/list.htm?search="
details_url = "http://bsdl.info/details.htm?sid="
bsdl_url = "http://bsdl.info/download.htm?sid="

test_jtag_product_id = "XXXX0110110101001XXX000010010011"
test_sid = "40317e60555feba388ca59b002289d77"

register_csspath = "/html/body/table/tbody/tr/td[1]/table/tbody/tr[2]/td/div/table/tbody/tr[5]/td"
instructions_csspath = "/html/body/table/tbody/tr/td[1]/table/tbody/tr[2]/td/div/table/tbody/tr[6]/td"


def get_sid(jtag_product_id):
    r = requests.get(id_lookup_url + jtag_product_id)
    soup = BeautifulSoup(r.content, 'html.parser')
    cell = soup.find_all('table')[2].find_all('tr')[1].find_all('td')[0]
    url = cell.find_all('a')[0]['href']
    sid = url.split('?')[1].replace("sid=", "")
    return sid

def get_details(sid):
    r = requests.get(details_url + sid)
    soup = BeautifulSoup(r.content, 'html.parser')
    table0 = soup.findAll('table', {'class':'details'})[0]
    table1 = soup.findAll('table', {'class':'details'})[1]
    name = table0.findAll('tr')[1].findAll('td')[0].text
    vendor = table0.findAll('tr')[2].findAll('td')[0].text
    family = table0.findAll('tr')[3].findAll('td')[0].text
    register = table1.findAll('tr')[4].findAll('td')[0].text
    instructions = table1.findAll('tr')[5].findAll('td')[0].text.replace('\n', '').replace('\t', '').upper()
    return {
        'name': name.replace(u'\xa0', u' ').strip(' '),
        'vendor': vendor.replace('\n', '').replace('\t', '').replace(u'\xa0', u' '),
        'family': family.replace('\n', '').replace('\t', '').replace(u'\xa0', u' '),
        'ir_size': int(register.replace('\n', '').replace('\t', '').replace(u'\xa0', u' ').replace('bit','')),
        'instructions': instructions.split(', ')
    }

def strip_inner_whitespace(l):
    #print(l)
    ranges = [(m.start(0), m.end(0)) for m in re.finditer('[^\w] +[^\w]|[\w] +[^\w]|[^\w] +[\w]',l)][::-1]
    #print(ranges, "=>")
    
    #import ipdb
    #ipdb.set_trace()
    
    for s, e in ranges:
        l = l[:s+1] + (" " if (l[s].isalnum() and l[e-1].isalnum()) else "") + l[e-1:]
    #print(l)
    #print(ranges, "=>")    
    ranges = [(m.start(0), m.end(0)) for m in re.finditer('[^\w] ',l)][::-1]
    #print(ranges)
    for s, e in ranges:
        l = l[:s+1] + l[e:]
    #l = l.replace(": ",":")
        
    return l

def _filter_attributes(lines):
    lines_out = []
    for l in lines:
        if l.lower().startswith("attribute"):
            lines_out.append(l)
    return lines_out

def extract_attributes(lines):
    attribs = dict()
    for l in lines:
        #print(l)
        first_space = l.index(" ", 10)
        attrib_name = l[10:first_space].upper()
        type_index = l.index(":")
        value_index = l.index(" is", type_index)
        v = l[value_index+3:].strip(" ")[:-1]
        if attrib_name == "INSTRUCTION_OPCODE":
            v = v[1:-1]
            v = v.split(',')
            regs = dict()
            for reg in v:
                kv = reg.split('(')
                regs[kv[0].upper()] = kv[1][:-1]
            v = regs
        elif attrib_name == "BOUNDARY_REGISTER":
            v = v[2:-2].split('),')
            v = [elem.split('(') for elem in v]
            v = {elem[0]:elem[1].split(',') for elem in v}
        elif v.startswith('('):
            pass
        elif v.startswith('"'):
            v = v[1:-1]
        elif v.isnumeric():
            v = int(v)
        attribs[attrib_name] = v
    return attribs
        
def _get_bsdl_and_strip_white_and_comments(sid):
    r = requests.get(bsdl_url + sid)
    lines = []
    for i, l in enumerate(r.iter_lines()):
        try:
            l = l[:l.index(b"--")]
        except ValueError:
            pass
        #print(i, l)
        l = l.decode('utf-8')
        l = l.replace("\t", " ").strip(' ')
        if l is "": continue

        l = strip_inner_whitespace(l)

        #print(l)
        #print()
        lines.append(l)
    return lines

def _combine_lines(lines_in):
    lines_out = []
    linetmp = ""
    for i,l in enumerate(lines_in):
        if linetmp and linetmp[-1].isalnum() and l[0].isalnum():
            linetmp += " "
        linetmp += l
        if l.endswith(';') or l.endswith("("):
            linetmp = linetmp.replace('"&"', '')
            lines_out.append(linetmp)
            linetmp = ""
    return lines_out

def decode_bsdl(sid):
    lines = _get_bsdl_and_strip_white_and_comments(sid)
    lines = _combine_lines(lines)
    lines = _filter_attributes(lines)
    return extract_attributes(lines)
