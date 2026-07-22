"""Generate one QR code PNG per store branch.

Each QR points at the same deployed app, with a different ?store=<slug>
query param so customers land on their own branch's review page.

Usage:
    1. Deploy app.py (e.g. to Streamlit Community Cloud) and get its URL.
    2. Set BASE_URL below to that URL.
    3. Run: python generate_qr.py
    4. Print/display the PNGs from qr_codes/ at each branch's counter.
"""

from pathlib import Path

import qrcode

from config import STORE_CONFIG

BASE_URL = "https://vilvah-review.streamlit.app"

OUT_DIR = Path(__file__).parent / "qr_codes"
OUT_DIR.mkdir(exist_ok=True)

for slug, store in STORE_CONFIG.items():
    url = f"{BASE_URL}/?store={slug}"
    img = qrcode.make(url)
    out_path = OUT_DIR / f"{slug}.png"
    img.save(out_path)
    print(f"{store['name']}: {url} -> {out_path}")
