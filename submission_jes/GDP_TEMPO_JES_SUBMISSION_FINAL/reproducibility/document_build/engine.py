"""Surgical rebuild engine: edits the OBES DOCX paragraph-by-paragraph, preserving untouched OMML."""
import copy, re
import docx
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.shared import Pt, RGBColor

M = 'http://schemas.openxmlformats.org/officeDocument/2006/math'
W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'

def _mel(tag):
    return OxmlElement('m:' + tag)

def _mrun(text):
    r = _mel('r')
    rpr = OxmlElement('w:rPr'); f = OxmlElement('w:rFonts')
    f.set(qn('w:ascii'), 'Cambria Math'); f.set(qn('w:hAnsi'), 'Cambria Math'); rpr.append(f)
    r.append(rpr)
    t = _mel('t'); t.text = text
    t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve'); r.append(t)
    return r

def _parse(expr):
    """Tiny linear-math parser: supports X_{..} and X^{..} (single base char or {..})."""
    out = []; i = 0
    while i < len(expr):
        ch = expr[i]
        if ch == '{':
            j = _match(expr, i); out.append(('grp', expr[i+1:j])); i = j + 1; continue
        if ch in '_^' and out:
            base = out.pop()
            if expr[i+1] == '{':
                j = _match(expr, i+1); arg = expr[i+2:j]; i = j + 1
            else:
                arg = expr[i+1]; i += 2
            kind = 'sub' if ch == '_' else 'sup'
            out.append((kind, base, arg)); continue
        out.append(('chr', ch)); i += 1
    return out

def _match(s, i):
    d = 0
    for j in range(i, len(s)):
        if s[j] == '{': d += 1
        elif s[j] == '}':
            d -= 1
            if d == 0: return j
    raise ValueError(s)

def _emit(parent, items):
    buf = ''
    def flush():
        nonlocal buf
        if buf: parent.append(_mrun(buf)); buf = ''
    for it in items:
        if it[0] == 'chr': buf += it[1]; continue
        flush()
        if it[0] == 'grp': _emit(parent, _parse(it[1])); continue
        kind, base, arg = it
        node = _mel('sSub' if kind == 'sub' else 'sSup')
        e = _mel('e'); _emit(e, [base]); node.append(e)
        s = _mel('sub' if kind == 'sub' else 'sup'); _emit(s, _parse(arg)); node.append(s)
        parent.append(node)
    flush()

def omml(expr):
    om = _mel('oMath'); _emit(om, _parse(expr)); return om

def _text_run(text, bold=False, italic=False, size=12):
    r = OxmlElement('w:r'); rpr = OxmlElement('w:rPr')
    f = OxmlElement('w:rFonts')
    for a in ('ascii', 'hAnsi', 'cs', 'eastAsia'): f.set(qn('w:' + a), 'Times New Roman')
    rpr.append(f)
    if bold: rpr.append(OxmlElement('w:b'))
    if italic: rpr.append(OxmlElement('w:i'))
    c = OxmlElement('w:color'); c.set(qn('w:val'), '000000'); rpr.append(c)
    sz = OxmlElement('w:sz'); sz.set(qn('w:val'), str(size * 2)); rpr.append(sz)
    r.append(rpr)
    t = OxmlElement('w:t'); t.text = text
    t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve'); r.append(t)
    return r

TOKEN = re.compile(r'⟦(.+?)⟧|\*\*(.+?)\*\*|__(.+?)__')

def fill(p_el, text, bold=False, italic=False, size=12):
    """Replace content of paragraph element with text; ⟦expr⟧ -> OMML, **x** bold, __x__ italic."""
    for ch in list(p_el):
        if ch.tag != qn('w:pPr'): p_el.remove(ch)
    pos = 0
    for m in TOKEN.finditer(text):
        if m.start() > pos: p_el.append(_text_run(text[pos:m.start()], bold, italic, size))
        if m.group(1): p_el.append(omml(m.group(1)))
        elif m.group(2): p_el.append(_text_run(m.group(2), True, italic, size))
        else: p_el.append(_text_run(m.group(3), bold, True, size))
        pos = m.end()
    if pos < len(text): p_el.append(_text_run(text[pos:], bold, italic, size))
    return p_el

def new_par(text='', **kw):
    p = OxmlElement('w:p'); fill(p, text, **kw); return p

def words(el):
    return len(re.findall(r'\S+', ''.join(n.text or '' for n in el.iter() if n.tag in (qn('w:t'), qn('m:t')))))
