import docx, re, sys, json
from docx.oxml.ns import qn
def inv(path):
    d = docx.Document(path); body = d.element.body
    sec = 'front'; c = {}
    for el in body.iterchildren():
        if el.tag == qn('w:p'):
            t = ''.join(n.text or '' for n in el.iter(qn('w:t'))).strip()
            if t == 'References': sec = 'references'
            elif t == 'Figure captions': sec = 'captions'
            elif t == 'Abstract': sec = 'abstract'
            elif re.match(r'^1\. Introduction', t): sec = 'body'
            c[sec] = c.get(sec, 0) + len(t.split())
        elif el.tag == qn('w:tbl'):
            t = ' '.join(n.text or '' for n in el.iter(qn('w:t')))
            c['eq_tables'] = c.get('eq_tables', 0) + len(t.split())
    return c
for p in sys.argv[1:]:
    c = inv(p); tot = sum(c.values()); print(p, c, 'text', tot, 'effective(6x280)', tot + 6*280)
