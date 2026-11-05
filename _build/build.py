import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import p_top, p_business, p_recruit, p_env, p_people, p_company
from common import PAGES
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
mods = {"top": p_top, "business": p_business, "recruit": p_recruit, "environment": p_env, "people": p_people, "company": p_company}
for key, _, path in PAGES:
    html = mods[key].build()
    assert "@R@" not in html, key
    fp = os.path.join(OUT, path); os.makedirs(os.path.dirname(fp), exist_ok=True)
    open(fp, "w").write(html); print(path, len(html))
