"""Build the single-file index.html from src/ (inlines option data and the Vazirmatn font)."""
import base64, pathlib
root = pathlib.Path(__file__).parent
s = (root / 'src/src.html').read_text(encoding='utf-8')
d = (root / 'src/data.js').read_text(encoding='utf-8')
f = base64.b64encode((root / 'fonts/Vazirmatn-wght.woff2').read_bytes()).decode()
s = s.replace('__DATA__', d).replace('__VAZIR__', f)
(root / 'index.html').write_text(s, encoding='utf-8')
print('index.html', len(s), 'bytes')
