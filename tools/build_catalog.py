#!/usr/bin/env python3
"""Build a local browser-friendly catalog without third-party dependencies."""
from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
items=json.loads((root/'prayers/index.json').read_text(encoding='utf-8'))
seen=set()
for item in items:
 assert item['id'] not in seen, f"Duplicate id: {item['id']}"
 seen.add(item['id'])
 assert item['kind'] in {'original','traditional'}
 file=(root/item['file']).resolve()
 assert file.is_relative_to(root.resolve()), 'Path outside root'
 assert file.is_file(), f'Missing {file}'
 item['content']=file.read_text(encoding='utf-8')
(root/'prayers-data.js').write_text('window.KOL_PRAYERS = '+json.dumps(items,ensure_ascii=False,indent=2)+';\n',encoding='utf-8')
print('Generated prayers-data.js:',len(items),'entries')
