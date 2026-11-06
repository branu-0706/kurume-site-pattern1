# 配色の正本 config/themes.json から、全16画面が読む色変数（assets/theme.css）と
# デモ用の配色パネルが使うプリセット（assets/theme/presets.js）を生成する。
# 恒久的な既定色を変えるときは config/themes.json を編集して再ビルド・再デプロイする（ブラウザ内の試し変更は反映されない）。
import json
import os
import re


def css_name(key):
    return "--kk-" + re.sub(r"[A-Z]", lambda m: "-" + m.group(0).lower(), key)


DERIVED = """  /* 派生色：正本の色から計算（個別のHEXを持たない） */
  --kk-navy-08:color-mix(in srgb,var(--kk-brand-navy) 8%,transparent);
  --kk-navy-16:color-mix(in srgb,var(--kk-brand-navy) 16%,transparent);
  --kk-navy-shadow:color-mix(in srgb,var(--kk-brand-navy) 22%,transparent);
  --kk-primary-soft:color-mix(in srgb,var(--kk-primary) 45%,var(--kk-surface));
  --kk-photo-shade:color-mix(in srgb,var(--kk-text) 55%,transparent);"""


def build(out):
    cfg = json.load(open(os.path.join(out, "config", "themes.json"), encoding="utf-8"))
    default = cfg["defaultPreset"]
    tokens = cfg["presets"][default]["tokens"]
    body = "\n".join(f"  {css_name(k)}:{v};" for k, v in tokens.items())
    css = ("/* 自動生成ファイル：直接編集しないでください。正本は config/themes.json（既定：%s）。\n"
           "   全16画面の色は、この --kk-* 変数だけを参照します（ロゴ画像の色は変更しません）。 */\n:root{\n%s\n%s\n}\n") % (default, body, DERIVED)
    open(os.path.join(out, "assets", "theme.css"), "w").write(css)
    os.makedirs(os.path.join(out, "assets", "theme"), exist_ok=True)
    data = {"defaultPreset": default,
            "presets": {k: {"label": v["label"], "tokens": v["tokens"]} for k, v in cfg["presets"].items()},
            "notes": cfg.get("notes", {})}
    open(os.path.join(out, "assets", "theme", "presets.js"), "w").write(
        "/* 自動生成ファイル：正本は config/themes.json */\nwindow.KK_THEMES=" + json.dumps(data, ensure_ascii=False) + ";\n")
    print("theme:", default, len(tokens), "tokens")
