# uznorm

Normalization utilities for Uzbek text — apostrophe variants, with transliteration and whitespace cleanup planned.

**Live:** https://uznorm.onrender.com
**Docs:** https://uznorm.onrender.com/docs

## What it does

Uzbek Latin orthography uses two distinct characters that are commonly typed as a plain `'`:

- `ʻ` (U+02BB) — in `oʻ` and `gʻ`, as in `Oʻzbekiston`, `gʻalaba`
- `ʼ` (U+02BC) — tutuq belgisi, standalone, as in `maʼno`, `sanʼat`

Text found in the wild mixes `'`, `'`, `` ` ``, and `´` for both. This normalizes them to the correct character based on context.

## API

`POST /normalize`

```json
{ "text": "O'zbekiston san'ati" }
```

```json
{
  "original": "O'zbekiston san'ati",
  "normalized": "Oʻzbekiston sanʼati",
  "changed": true
}
```

`GET /health` — liveness check
`GET /docs` — interactive API documentation

## Install

```bash
git clone https://github.com/Ikbola/uznorm.git
cd uznorm
uv venv
source .venv/bin/activate    # Windows: .venv\Scripts\Activate.ps1
uv pip install -e .
```

## Run locally

```bash
uvicorn uznorm.api:app --reload
```

## Test

```bash
pytest
```

## Why this exists

Built as a practice project for Python packaging, testing, and deployment. Also serves as a normalization dependency for a retrieval system over Uzbek school textbooks.