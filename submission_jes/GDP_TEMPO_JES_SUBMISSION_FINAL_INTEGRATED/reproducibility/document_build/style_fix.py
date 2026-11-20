# Normalise Word style definitions: Times New Roman, black text, no character spacing.
import sys, docx
from docx.oxml.ns import qn
def normalise(path):
    d = docx.Document(path); st = d.styles.element
    for rf in st.iter(qn('w:rFonts')):
        for a in list(rf.attrib):
            if a.endswith('Theme'): del rf.attrib[a]
        for a in ('ascii', 'hAnsi', 'cs', 'eastAsia'): rf.set(qn('w:' + a), 'Times New Roman')
    for c in st.iter(qn('w:color')):
        c.set(qn('w:val'), '000000')
        for a in list(c.attrib):
            if 'theme' in a.lower(): del c.attrib[a]
    for rpr in st.iter(qn('w:rPr')):
        for sp in rpr.findall(qn('w:spacing')): rpr.remove(sp)
    dd = st.find(qn('w:docDefaults'))
    rpr = dd.find(qn('w:rPrDefault')).find(qn('w:rPr'))
    if rpr.find(qn('w:rFonts')) is None:
        rf = rpr.makeelement(qn('w:rFonts'), {}); rpr.insert(0, rf)
        for a in ('ascii', 'hAnsi', 'cs', 'eastAsia'): rf.set(qn('w:' + a), 'Times New Roman')
    d.save(path)
if __name__ == '__main__':
    for p in sys.argv[1:]: normalise(p); print('normalised', p)
