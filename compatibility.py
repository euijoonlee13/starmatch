# compatibility.py

# zodiac.py의 ZODIAC_EN과 동일하게 유지 (import해서 써도 됨)
ZODIACS = [
    "zodiac_aries","zodiac_taurus","zodiac_gemini","zodiac_cancer","zodiac_leo","zodiac_virgo",
    "zodiac_libra","zodiac_scorpio","zodiac_sagittarius","zodiac_capricorn","zodiac_aquarius","zodiac_pisces"
]

# 기본값: 같은 별자리 70, 나머지 50
_default = {a: {b: (70 if a == b else 50) for b in ZODIACS} for a in ZODIACS}

# 이미지 표 기반(내 별자리 기준) - 영어 키로 작성
GOOD_3 = {
    "zodiac_capricorn":  ["zodiac_virgo", "zodiac_taurus", "zodiac_capricorn"],
    "zodiac_aquarius":   ["zodiac_gemini", "zodiac_aquarius", "zodiac_libra"],
    "zodiac_pisces":     ["zodiac_cancer", "zodiac_scorpio", "zodiac_pisces"],
    "zodiac_aries":      ["zodiac_leo", "zodiac_sagittarius"], 
    "zodiac_taurus":     ["zodiac_capricorn", "zodiac_virgo", "zodiac_taurus"],
    "zodiac_gemini":     ["zodiac_aquarius", "zodiac_libra", "zodiac_gemini"],
    "zodiac_cancer":     ["zodiac_pisces", "zodiac_scorpio", "zodiac_cancer"],
    "zodiac_leo":        ["zodiac_aries", "zodiac_sagittarius", "zodiac_leo"],
    "zodiac_virgo":      ["zodiac_taurus", "zodiac_capricorn", "zodiac_virgo"],
    "zodiac_libra":      ["zodiac_aquarius", "zodiac_gemini", "zodiac_libra"],
    "zodiac_scorpio":    ["zodiac_pisces", "zodiac_cancer", "zodiac_scorpio"],
    "zodiac_sagittarius":["zodiac_leo", "zodiac_aries", "zodiac_sagittarius"],
}

BAD_3 = {
    "zodiac_capricorn":  ["zodiac_aries", "zodiac_cancer", "zodiac_libra"],
    "zodiac_aquarius":   ["zodiac_taurus", "zodiac_leo", "zodiac_scorpio"],
    "zodiac_pisces":     ["zodiac_gemini", "zodiac_virgo", "zodiac_sagittarius"],
    "zodiac_aries":      ["zodiac_cancer", "zodiac_libra", "zodiac_capricorn"],
    "zodiac_taurus":     ["zodiac_leo", "zodiac_scorpio", "zodiac_aquarius"],
    "zodiac_gemini":     ["zodiac_virgo", "zodiac_sagittarius", "zodiac_pisces"],
    "zodiac_cancer":     ["zodiac_libra", "zodiac_capricorn", "zodiac_aries"],
    "zodiac_leo":        ["zodiac_scorpio", "zodiac_aquarius", "zodiac_taurus"],
    "zodiac_virgo":      ["zodiac_sagittarius", "zodiac_gemini", "zodiac_pisces"],
    "zodiac_libra":      ["zodiac_capricorn", "zodiac_aries", "zodiac_cancer"],
    "zodiac_scorpio":    ["zodiac_aquarius", "zodiac_taurus", "zodiac_leo"],
    "zodiac_sagittarius":["zodiac_pisces", "zodiac_gemini", "zodiac_virgo"],
}

GOOD_SCORE = 85
BAD_SCORE = 35

_override = {}

def _put(a: str, b: str, v: int, bidirectional: bool = True):
    """(a,b) 점수 덮어쓰기. bidirectional=True면 (b,a)도 같이 맞춤."""
    _override[(a, b)] = v
    if bidirectional:
        _override[(b, a)] = v

# 표 기반 점수 반영
for my_zodiac, good_list in GOOD_3.items():
    for other in good_list:
        if other != my_zodiac:  # 같은 별자리는 기본 70 유지하고 싶으면 제외
            _put(my_zodiac, other, GOOD_SCORE, bidirectional=True)

for my_zodiac, bad_list in BAD_3.items():
    for other in bad_list:
        _put(my_zodiac, other, BAD_SCORE, bidirectional=True)

# (선택) 개인 커스텀 덮어쓰기 예시
# _put("zodiac_capricorn", "zodiac_scorpio", 60, bidirectional=True)
# _put("zodiac_aries", "zodiac_leo", 85, bidirectional=True)

# override 적용
for (a, b), v in _override.items():
    _default[a][b] = v

COMPAT = _default

def score(a: str, b: str) -> int:
    return int(COMPAT.get(a, {}).get(b, 50))

def top_matches_for(z: str, n: int = 3):
    """z와 잘 맞는 별자리 Top n (점수 높은 순)"""
    pairs = [(other, score(z, other)) for other in ZODIACS if other != z]
    pairs.sort(key=lambda x: x[1], reverse=True)
    return pairs[:n]

def worst_matches_for(z: str, n: int = 3):
    """z와 안 맞는 별자리 Worst n (점수 낮은 순)"""
    pairs = [(other, score(z, other)) for other in ZODIACS if other != z]
    pairs.sort(key=lambda x: x[1])
    return pairs[:n]

def good_bad_for(z: str):
    """
    표에 있는 '확정 good/bad 리스트'를 그대로 쓰고 싶을 때.
    (top_matches_for는 점수 기반이라 커스텀 점수 섞이면 바뀔 수 있음)
    """
    return {
        "good": GOOD_3.get(z, [])[:3],
        "bad": BAD_3.get(z, [])[:3],
    }