import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import p_top, p_business, p_recruit, p_env, p_people, p_company
import p2_top, p2_about, p2_recruit, p2_people, p2_future, p2_company
import cmp_p1_d2, cmp_p1_d3, cmp_p2_d2, cmp_p2_d3
from common import PAGES
from p2common import P2_PAGES
import theme_build
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
theme_build.build(OUT)  # config/themes.json → assets/theme.css・assets/theme/presets.js


def write(path, html, key):
    assert "@R@" not in html and "@P2@" not in html, key
    fp = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    open(fp, "w").write(html)
    print(path, len(html))


# パターン① × デザイン①（既存・URLは変更しない）
mods = {"top": p_top, "business": p_business, "recruit": p_recruit, "environment": p_env, "people": p_people, "company": p_company}
for key, _, path in PAGES:
    write(path, mods[key].build(), key)

# パターン② × デザイン①（/pattern2/ 以下）
p2mods = {"top": p2_top, "about": p2_about, "recruit": p2_recruit, "people": p2_people, "future": p2_future, "company": p2_company}
for key, _, path in P2_PAGES:
    write("pattern2/" + path, p2mods[key].build(), "p2-" + key)

# 比較用TOP（デザイン②・③）
write("compare/pattern1/design-a/index.html", cmp_p1_d2.build(), "p1-d2")
for _path, _mod, _key in [("compare/pattern1/design-b/index.html", cmp_p1_d3, "p1-d3"), ("compare/pattern2/design-a/index.html", cmp_p2_d2, "p2-d2"), ("compare/pattern2/design-b/index.html", cmp_p2_d3, "p2-d3")]:
    write(_path, _mod.build(), _key)

# 1画面で切り替える比較ページ（16画面への入口）
write("compare/index.html", open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "hub.html")).read(), "hub")

import p3_build
p3_build.build(OUT)
