"""Ödev kapağı üreteci — deponun imza dili.

Kullanım:
    python tools/kapak.py <odev-klasörü> [--ad "Ödev adı"] [--hat java] [--no 05]

Çıktı:
    <odev-klasörü>/docs/rozet.svg    (600x600 imza rozeti)
    <odev-klasörü>/docs/kapak.svg    (1280x480 ödev kapağı)
"""

from __future__ import annotations

import argparse
import pathlib
import re

FONT = "'Segoe UI',Inter,system-ui,-apple-system,Arial,sans-serif"
MONO = "'JetBrains Mono','Cascadia Code',Consolas,monospace"

HATS = {
    "java":    ("#FBBF24", "#F59E0B"),
    "node":    ("#22D3EE", "#0EA5E9"),
    "react":   ("#38BDF8", "#0284C7"),
    "rust":    ("#FB923C", "#EA580C"),
    "sql":     ("#60A5FA", "#2563EB"),
    "web":     ("#94A3B8", "#64748B"),
    "game":    ("#F87171", "#DC2626"),
    "default": ("#22D3EE", "#A78BFA"),
}


def parse_name(folder: str) -> tuple[str, str]:
    m = re.match(r"^(\d+)-(.+)$", folder)
    if m:
        no, rest = m.group(1), m.group(2)
    else:
        no, rest = "", folder
    ad = " ".join(w.capitalize() for w in rest.replace("-", " ").replace("_", " ").split())
    return no, ad


def rozet(ad: str, no: str, c1: str, c2: str) -> str:
    body = "M300 92 L480 160 V312 C480 410 398 476 300 508 C202 476 120 410 120 312 V160 Z"
    L: list[str] = []
    a = L.append
    a('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600" width="600" height="600" '
      f'role="img" aria-label="{ad} — Enes Öztürk imzalı rozet">')
    a("<defs>"
      '<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#060B14"/>'
      '<stop offset="55%" stop-color="#0A1220"/><stop offset="100%" stop-color="#121E33"/></linearGradient>'
      f'<linearGradient id="acc" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c1}"/>'
      f'<stop offset="100%" stop-color="{c2}"/></linearGradient>'
      '<linearGradient id="metal" x1="0" y1="0" x2="1" y2="1">'
      '<stop offset="0" stop-color="#FFFFFF" stop-opacity="0.18"/>'
      '<stop offset="60%" stop-color="#FFFFFF" stop-opacity="0.03"/>'
      '<stop offset="100%" stop-color="#FFFFFF" stop-opacity="0.08"/></linearGradient>'
      f'<radialGradient id="glow" cx="50%" cy="40%" r="55%"><stop offset="0" stop-color="{c1}" stop-opacity="0.28"/>'
      f'<stop offset="100%" stop-color="{c1}" stop-opacity="0"/></radialGradient>'
      f'<style>.t{{font-family:{FONT}}}.m{{font-family:{MONO}}}.cap{{font-family:{FONT};font-weight:700;letter-spacing:2.6px}}</style>'
      "</defs>")
    a('<rect width="600" height="600" rx="28" fill="url(#bg)"/>')
    a('<ellipse cx="300" cy="250" rx="250" ry="220" fill="url(#glow)"/>')
    a(f'<path d="{body}" fill="#0A1220" fill-opacity="0.96" stroke="url(#acc)" stroke-width="4"/>')
    a(f'<g transform="translate(300,300) scale(0.84) translate(-300,-300)">'
      f'<path d="{body}" fill="url(#metal)" stroke="#FFFFFF" stroke-opacity="0.10" stroke-width="1.5"/></g>')
    # merkez: ödev numarası
    a(f'<circle cx="300" cy="238" r="72" fill="none" stroke="{c1}" stroke-opacity="0.6" stroke-width="2.5"/>')
    a(f'<text x="300" y="272" text-anchor="middle" class="t" font-size="72" font-weight="700" fill="{c1}">'
      f'{no or "•"}</text>')
    size = 21 if len(ad) <= 22 else (18 if len(ad) <= 30 else 15)
    a(f'<text x="300" y="352" text-anchor="middle" class="t" font-size="{size}" font-weight="700" '
      f'fill="#E9F0FB">{ad}</text>')
    a('<text x="300" y="380" text-anchor="middle" class="m" font-size="11.5" fill="#8FA0BD">'
      'Patika ödevi · Enes Öztürk</text>')
    a('<g transform="rotate(-5 300 428)">'
      f'<rect x="212" y="412" width="176" height="32" rx="16" fill="{c1}" fill-opacity="0.13" '
      f'stroke="{c1}" stroke-opacity="0.6" stroke-width="1.5"/>')
    a(f'<text x="300" y="433" text-anchor="middle" class="cap" font-size="11.5" fill="{c1}">TAMAMLANDI</text></g>')
    a('<text x="300" y="478" text-anchor="middle" class="m" font-size="10" fill="#5A6B88">'
      'github.com/EnesBinMalik</text>')
    a("</svg>")
    return "\n".join(L) + "\n"


def kapak(ad: str, no: str, c1: str, c2: str) -> str:
    W, H = 1280, 480
    L: list[str] = []
    a = L.append
    a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
      f'role="img" aria-label="{ad} — ödev kapağı">')
    a("<defs>"
      '<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#05090F"/>'
      '<stop offset="52%" stop-color="#0A1220"/><stop offset="100%" stop-color="#111D31"/></linearGradient>'
      f'<linearGradient id="acc" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{c1}"/>'
      f'<stop offset="55%" stop-color="{c2}"/><stop offset="100%" stop-color="{c2}" stop-opacity="0.06"/></linearGradient>'
      '<pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">'
      '<path d="M40 0H0V40" fill="none" stroke="#FFFFFF" stroke-opacity="0.035"/></pattern>'
      f'<radialGradient id="g1" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="{c1}" stop-opacity="0.26"/>'
      f'<stop offset="100%" stop-color="{c1}" stop-opacity="0"/></radialGradient>'
      f'<style>.t{{font-family:{FONT}}}.m{{font-family:{MONO}}}'
      f'.ttl{{font-family:{FONT};font-weight:700;letter-spacing:-1.6px}}'
      f'.cap{{font-family:{FONT};font-weight:700;letter-spacing:3px}}</style>'
      "</defs>")
    a(f'<rect width="{W}" height="{H}" fill="url(#bg)"/>')
    a(f'<rect width="{W}" height="{H}" fill="url(#grid)"/>')
    a(f'<ellipse cx="200" cy="70" rx="420" ry="240" fill="url(#g1)"/>')
    a(f'<rect x="0" y="0" width="6" height="{H}" fill="url(#acc)"/>')
    a(f'<text x="56" y="48" class="m" font-size="12" fill="#5A6B88" letter-spacing="1.8">'
      f'PATİKA · ÖDEV {no or "—"}</text>')
    a(f'<text x="1224" y="48" text-anchor="end" class="m" font-size="12" fill="{c1}" '
      'letter-spacing="1.8" fill-opacity="0.9">ENES ÖZTÜRK</text>')
    a('<line x1="56" y1="64" x2="1224" y2="64" stroke="#FFFFFF" stroke-opacity="0.07"/>')
    a(f'<text x="56" y="176" class="ttl" font-size="56" fill="#E9F0FB">{ad}</text>')
    a('<text x="56" y="216" class="t" font-size="19" fill="#8FA0BD">'
      'Künye · kazanımlar · kurulum · kabul kriterleri</text>')
    a(f'<rect x="56" y="244" width="56" height="3" rx="1.5" fill="{c1}"/>')
    a(f'<text x="56" y="316" class="m" font-size="13" fill="#5A6B88">$ npm install &amp;&amp; npm run dev</text>')
    a(f'<text x="56" y="344" class="m" font-size="13" fill="{c1}">$ git commit -m "odev {no or "--"}: hazır"</text>')
    a('<line x1="56" y1="392" x2="1224" y2="392" stroke="#FFFFFF" stroke-opacity="0.07"/>')
    a('<text x="56" y="428" class="t" font-size="24" font-weight="700" fill="#E9F0FB">Enes Öztürk</text>')
    a('<text x="56" y="452" class="m" font-size="12" fill="#5A6B88">github.com/EnesBinMalik</text>')
    a('<text x="1224" y="428" text-anchor="end" class="cap" font-size="12" fill="#475569">İMZALI ÖDEV</text>')
    a("</svg>")
    return "\n".join(L) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    ap.add_argument("--ad", default=None)
    ap.add_argument("--hat", default="default")
    ap.add_argument("--no", default=None)
    ns = ap.parse_args()

    path = pathlib.Path(ns.folder)
    no, ad = parse_name(path.name)
    ad = ns.ad or ad
    no = ns.no or no
    c1, c2 = HATS.get(ns.hat, HATS["default"])
    (path / "docs").mkdir(parents=True, exist_ok=True)
    (path / "docs" / "rozet.svg").write_text(rozet(ad, no, c1, c2), encoding="utf-8")
    (path / "docs" / "kapak.svg").write_text(kapak(ad, no, c1, c2), encoding="utf-8")
    print(f"✓ {path}/docs/rozet.svg · {path}/docs/kapak.svg")


if __name__ == "__main__":
    main()
