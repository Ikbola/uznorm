"""Normalize apostrophe variants in Uzbek Latin text."""

# Everything people actually type instead of the correct characters
APOSTROPHE_VARIANTS = "'\u2019\u0060\u00b4\u02bb\u02bc"

OQ_GQ = "\u02bb"      # ʻ  — used in oʻ and gʻ
TUTUQ = "\u02bc"      # ʼ  — standalone glottal marker


def normalize_apostrophes(text: str) -> str:
    """Replace any apostrophe-like character with the correct Uzbek one."""
    result = []
    for char in text:
        if char in APOSTROPHE_VARIANTS:
            previous = result[-1] if result else ""
            if previous.lower() in ("o", "g"):
                result.append(OQ_GQ)
            else:
                result.append(TUTUQ)
        else:
            result.append(char)
    return "".join(result)

