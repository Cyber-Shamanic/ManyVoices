# 🔌 API נתונים מקומי
אין בשלב זה API רשת או שרת. מבנה הנתונים הקנוני נמצא ב־`prayers/index.json`.

## שדות
`id` מזהה יציב באנגלית; `title` כותרת בעברית; `kind` אחד מ־`traditional`, `original`; `file` נתיב יחסי; `section` שער; `summary` תיאור; `status` ערך `draft` או `reviewed`.

`prayers-data.js` נוצר על ידי `tools/build_catalog.py` ומכיל `window.KOL_PRAYERS` עם `content` המועתק מקובץ ה־Markdown. הוא מיועד לטעינה סטטית; אל תכניסו אליו מפתחות או מידע פרטי.

### דוגמה
```json
{"id":"modeh-ani","title":"מודה אני","kind":"traditional","file":"prayers/traditional/modeh-ani.md","section":"השכמת הבוקר","summary":"הודיה עם היקיצה","status":"draft"}
```
