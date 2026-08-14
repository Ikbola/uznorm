from normalize import normalize_apostrophes

# Declared here with explicit escapes, not imported from normalize.py —
# a test that imports the value it's checking can't catch a wrong value.
OQ_GQ = "\u02bb"   # ʻ
TUTUQ = "\u02bc"   # ʼ


def test_o_takes_oq_gq():
    assert normalize_apostrophes("O'zbekiston") == f"O{OQ_GQ}zbekiston"


def test_g_takes_oq_gq():
    assert normalize_apostrophes("g'alaba") == f"g{OQ_GQ}alaba"


def test_standalone_takes_tutuq():
    assert normalize_apostrophes("ma'no") == f"ma{TUTUQ}no"


def test_uppercase_g_is_handled():
    assert normalize_apostrophes("G'ANI") == f"G{OQ_GQ}ANI"


def test_backtick_variant():
    assert normalize_apostrophes("g`alaba") == f"g{OQ_GQ}alaba"


def test_curly_quote_variant():
    assert normalize_apostrophes("ma\u2019no") == f"ma{TUTUQ}no"


def test_multiple_in_one_string():
    result = normalize_apostrophes("O'zbekiston san'ati")
    assert result == f"O{OQ_GQ}zbekiston san{TUTUQ}ati"


def test_text_without_apostrophes_unchanged():
    assert normalize_apostrophes("Toshkent shahri") == "Toshkent shahri"


def test_empty_string():
    assert normalize_apostrophes("") == ""