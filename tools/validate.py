#!/usr/bin/env python3
from pathlib import Path
import json
r=Path(__file__).resolve().parents[1]
items=json.loads((r/'prayers/index.json').read_text(encoding='utf-8'))
assert len({i['id'] for i in items})==len(items)
for i in items:
 c=(r/i['file']).read_text(encoding='utf-8')
 for phrase in ('## נוסח מנוקד','## פירוש פשוט','## כוונת הלב'):
  assert phrase in c, (i['file'],phrase)
 assert ('**סוג:**' in c)
for fn in ('README.md','LICENSE','CHANGELOG.md','ROADMAP.md','index.html','styles.css','scripts.js','prayers-data.js'):
 assert (r/fn).is_file(),fn
print('PASS:',len(items),'prayer entries, basic file and format checks')
