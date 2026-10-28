# zodiac.py
from datetime import date

ZODIAC_EN = [
    "zodiac_aries","zodiac_taurus","zodiac_gemini","zodiac_cancer","zodiac_leo","zodiac_virgo",
    "zodiac_libra","zodiac_scorpio","zodiac_sagittarius","zodiac_capricorn","zodiac_aquarius","zodiac_pisces"
]

def zodiac_from_date(d: date) -> str:
    """서양 별자리(12궁) 이름(en)) 반환"""
    m, day = d.month, d.day

    # 경계일 기준
    if (m == 3 and day >= 21) or (m == 4 and day <= 19):
        return "zodiac_aries"
    if (m == 4 and day >= 20) or (m == 5 and day <= 20):
        return "zodiac_taurus"
    if (m == 5 and day >= 21) or (m == 6 and day <= 20):
        return "zodiac_gemini"
    if (m == 6 and day >= 21) or (m == 7 and day <= 22):
        return "zodiac_cancer"
    if (m == 7 and day >= 23) or (m == 8 and day <= 22):
        return "zodiac_leo"
    if (m == 8 and day >= 23) or (m == 9 and day <= 22):
        return "zodiac_virgo"
    if (m == 9 and day >= 23) or (m == 10 and day <= 22):
        return "zodiac_libra"
    if (m == 10 and day >= 23) or (m == 11 and day <= 21):
        return "zodiac_scorpio"
    if (m == 11 and day >= 22) or (m == 12 and day <= 21):
        return "zodiac_sagittarius"
    if (m == 12 and day >= 22) or (m == 1 and day <= 19):
        return "zodiac_capricorn"
    if (m == 1 and day >= 20) or (m == 2 and day <= 18):
        return "zodiac_aquarius"
    return "zodiac_pisces"