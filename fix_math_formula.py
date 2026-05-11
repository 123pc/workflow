import re
from pathlib import Path

files = [
    Path(r'D:\学习资料\学校课程\机械工程\固体力学\课件\Ch1_拉压与剪切_复习笔记.md'),
    Path(r'D:\学习资料\学校课程\机械工程\固体力学\课件\Ch2_轴向加载构件_复习笔记.md'),
    Path(r'D:\学习资料\学校课程\机械工程\固体力学\课件\Ch3_扭转_复习笔记.md'),
    Path(r'D:\学习资料\学校课程\机械工程\固体力学\课件\Ch7_应力应变分析_复习笔记.md'),
    Path(r'D:\学习资料\学校课程\机械工程\固体力学\课件\Ch8_组合载荷_复习笔记.md'),
    Path(r'D:\学习资料\学校课程\机械工程\固体力学\课件\Ch9_梁的挠度_复习笔记.md'),
    Path(r'D:\学习资料\学校课程\机械工程\固体力学\课件\Final_期末重点回顾_复习笔记.md'),
]

replacements = [
    (re.compile(r'\\boxed\{([^{}]*)\}'), r'\1'),
    (re.compile(r'\\text\{([^{}]*)\}'), r'\1'),
    (re.compile(r'\\mathrm\{([^{}]*)\}'), r'\1'),
    (re.compile(r'\\mathbf\{([^{}]*)\}'), r'\1'),
    (re.compile(r'\\left'), ''),
    (re.compile(r'\\right'), ''),
    (re.compile(r'\\,|\\;|\\:|\\!'), ''),
    (re.compile(r'\\quad'), ' '),
    (re.compile(r'\\propto'), '∝'),
    (re.compile(r'\\approx'), '≈'),
    (re.compile(r'\\times'), '×'),
    (re.compile(r'\\leq'), '≤'),
    (re.compile(r'\\geq'), '≥'),
    (re.compile(r'\\neq'), '≠'),
    (re.compile(r'\\pm'), '±'),
    (re.compile(r'\\cdot'), '·'),
    (re.compile(r'\\rightarrow'), '→'),
    (re.compile(r'\\Rightarrow'), '⇒'),
    (re.compile(r'\\xrightarrow\{([^{}]*)\}'), r'→ \1'),
    (re.compile(r'\\leftarrow'), '←'),
    (re.compile(r'\\sum'), 'Σ'),
    (re.compile(r'\\infty'), '∞'),
    (re.compile(r'\\pi'), 'π'),
    (re.compile(r'\\alpha'), 'α'),
    (re.compile(r'\\beta'), 'β'),
    (re.compile(r'\\gamma'), 'γ'),
    (re.compile(r'\\delta'), 'δ'),
    (re.compile(r'\\Delta'), 'Δ'),
    (re.compile(r'\\epsilon'), 'ε'),
    (re.compile(r'\\varepsilon'), 'ε'),
    (re.compile(r'\\theta'), 'θ'),
    (re.compile(r'\\phi'), 'φ'),
    (re.compile(r'\\rho'), 'ρ'),
    (re.compile(r'\\nu'), 'ν'),
    (re.compile(r'\\sigma'), 'σ'),
    (re.compile(r'\\tau'), 'τ'),
    (re.compile(r'\\mu'), 'µ'),
    (re.compile(r'\\%'), '%'),
    (re.compile(r'\\sim'), '~'),
    (re.compile(r'\\le'), '≤'),
    (re.compile(r'\\ge'), '≥'),
    (re.compile(r'\\cdots'), '...'),
    (re.compile(r'\\ '), ''),
    (re.compile(r'\\boxed'), ''),
    (re.compile(r'\\_'), '_'),
    (re.compile(r'\\\^'), '^'),
]


def replace_frac(text):
    pattern = re.compile(r'\\frac\{([^{}]*)\}\{([^{}]*)\}')
    while True:
        new_text = pattern.sub(lambda m: f'({m.group(1)})/({m.group(2)})', text)
        if new_text == text:
            break
        text = new_text
    return text

for file in files:
    text = file.read_text(encoding='utf-8')
    text = text.replace('$$', '')
    text = text.replace('$', '')
    text = text.replace('\\[', '').replace('\\]', '')
    text = text.replace('\\(', '').replace('\\)', '')
    text = replace_frac(text)
    for pat, repl in replacements:
        text = pat.sub(repl, text)
    text = re.sub(r' {2,}', ' ', text)
    file.write_text(text, encoding='utf-8')
    print(f'Processed {file.name}')
