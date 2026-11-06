# 写真の重複チェック：assets/photos 内で「見た目がほぼ同じ写真」（同じ元写真・トリミング違い）を探す。
# 新しい写真を追加したら実行し、出てきた組は同じサイトで両方使わない（qa.js の ALIAS に追加する）。
import glob, os, itertools, sys
from PIL import Image
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "photos")
if len(sys.argv) > 1: ROOT = sys.argv[1]
def dh(p, n=16):
    im = Image.open(p).convert("L").resize((n + 1, n)); px = list(im.getdata()); b = 0
    for y in range(n):
        for x in range(n): b = b << 1 | (px[y * (n + 1) + x] > px[y * (n + 1) + x + 1])
    return b
H = {os.path.basename(p): dh(p) for p in sorted(glob.glob(os.path.join(ROOT, "*.jpg")))}
hits = [(bin(H[a] ^ H[b]).count("1"), a, b) for a, b in itertools.combinations(H, 2)]
hits = sorted(h for h in hits if h[0] <= 80)
for d, a, b in hits: print(f"{d:3d}  {a}  ≈  {b}")
print("候補なし" if not hits else f"{len(hits)}組（数値が小さいほど似ている。20以下はほぼ同じ写真）")
