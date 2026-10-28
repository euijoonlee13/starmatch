# app.py
from datetime import datetime, date
import random

from flask import Flask, render_template, request, redirect, url_for, session

from storage import get_storage
from zodiac import zodiac_from_date
from compatibility import score, top_matches_for, worst_matches_for
from i18n import t

app = Flask(__name__)
app.secret_key = "dev-secret-key"  # CS50 프로젝트용: 나중에 환경변수로 바꿔도 됨

store = get_storage()

def get_lang() -> str:
    lang = request.args.get("lang") or session.get("lang") or "en"
    if lang not in ("en", "de", "ko"):
        lang = "en"
    session["lang"] = lang
    return lang

def parse_birth(s: str):
    return datetime.strptime(s, "%Y-%m-%d").date()

@app.route("/lang/<code>")
def set_lang(code):
    if code in ("en", "de", "ko"):
        session["lang"] = code
    return redirect(url_for("index"))

@app.route("/", methods=["GET", "POST"])
def index():
    lang = get_lang()

    if request.method == "POST":
        name = (request.form.get("name") or "").strip()
        birth = (request.form.get("birth") or "").strip()

        if not name or not birth:
            return render_template("index.html", t=t, lang=lang, error=t(lang, "error_required"))

        try:
            b = parse_birth(birth)
        except ValueError:
            return render_template("index.html", t=t, lang=lang, error=t(lang, "error_birth"))

        if b > date.today():
            return render_template("index.html", t=t, lang=lang, error=t(lang, "error_birth"))

        z = zodiac_from_date(b)
        user = store.add_user(name=name, birth=birth, zodiac=z)

        # value which take over to next ,save
        session["user_id"] = user["id"]
        return redirect(url_for("step2"))

    return render_template("index.html", t=t, lang=lang, error=None)

@app.route("/step2", methods=["GET"])
def step2():
    lang = get_lang()
    user_id = session.get("user_id")
    if not user_id:
        return redirect(url_for("index"))

    user = store.get_user(user_id)
    if not user:
        return redirect(url_for("index"))

    best = top_matches_for(user["zodiac"], n=3)
    worst = worst_matches_for(user["zodiac"], n=3)
    
    return render_template(
        "step2.html",
        t=t, lang=lang,
        user=user,
        best=best,
        worst=worst
    )

@app.route("/couple", methods=["POST"])
def couple():
    lang = get_lang()
    user_id = session.get("user_id")
    user = store.get_user(user_id) if user_id else None
    if not user:
        return redirect(url_for("index"))

    partner_name = (request.form.get("partner_name") or "").strip()
    partner_birth = (request.form.get("partner_birth") or "").strip()

    if not partner_name or not partner_birth:
        # show again in step2 phase
        recommendations = top_matches_for(user["zodiac"], n=3)
        return render_template("step2.html", t=t, lang=lang, user=user,
                               recommendations=recommendations, error=t(lang, "error_required"))

    try:
        pb = parse_birth(partner_birth)
    except ValueError:
        recommendations = top_matches_for(user["zodiac"], n=3)
        return render_template("step2.html", t=t, lang=lang, user=user,
                               recommendations=recommendations, error=t(lang, "error_birth"))

    partner_z = zodiac_from_date(pb)
    s = score(user["zodiac"], partner_z)

    a_name = t(lang, user["zodiac"])
    b_name = t(lang, partner_z)  

    msg = t(lang, "couple_msg").format(a=a_name, b=b_name, score=s)
    return render_template("result.html", t=t, lang=lang, message=msg, me=user, partner={"name": partner_name, "birth": partner_birth, "zodiac": partner_z})

@app.route("/recommend", methods=["POST"])
def recommend():
    lang = get_lang()
    user_id = session.get("user_id")
    me = store.get_user(user_id) if user_id else None
    if not me:
        return redirect(url_for("index"))

    users = store.list_users()
    candidates = [u for u in users if u["id"] != me["id"]]

    if not candidates:
        return render_template("recommend.html", t=t, lang=lang, me=me, pick=None, score=None, no_candidates=True)

    # "궁합 높은 사람들 중 random 선택
    scored = [(u, score(me["zodiac"], u["zodiac"])) for u in candidates]
    scored.sort(key=lambda x: x[1], reverse=True)
    top = scored[:5] if len(scored) >= 5 else scored
    pick, sc = random.choice(top)

    return render_template("recommend.html", t=t, lang=lang, me=me, pick=pick, score=sc, no_candidates=False)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)