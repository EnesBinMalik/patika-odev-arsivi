"""Yeni Patika ödev deposu — marka varlıkları.

docs/cover.svg   : 1280x640 depo kapağı (README üstü + social preview kaynağı)
docs/ornek-odev.svg : örnek ödev kartı (şablonun nasıl göründüğünü gösterir)

Kullanım: python tools/assets.py
"""

from __future__ import annotations

import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
OUT = ROOT / "docs"
FONT = "'Segoe UI',Inter,system-ui,-apple-system,Arial,sans-serif"
MONO = "'JetBrains Mono','Cascadia Code',Consolas,monospace"

CYAN, VIOLET, AMBER, GREEN, PINK = "#22D3EE", "#A78BFA", "#FBBF24", "#4ADE80", "#F472B6"


def defs(c1: str = CYAN, c2: str = VIOLET) -> str:
    return (
        "<defs>"
        '<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#05090F"/><stop offset="52%" stop-color="#0A1220"/>'
        '<stop offset="100%" stop-color="#111D31"/></linearGradient>'
        f'<linearGradient id="acc" x1="0" y1="0" x2="1" y2="0">'
        f'<stop offset="0" stop-color="{c1}"/><stop offset="55%" stop-color="{c2}"/>'
        f'<stop offset="100%" stop-color="{c2}" stop-opacity="0.06"/></linearGradient>'
        f'<radialGradient id="g1" cx="50%" cy="50%" r="50%">'
        f'<stop offset="0" stop-color="{c1}" stop-opacity="0.26"/>'
        f'<stop offset="100%" stop-color="{c1}" stop-opacity="0"/></radialGradient>'
        f'<radialGradient id="g2" cx="50%" cy="50%" r="50%">'
        f'<stop offset="0" stop-color="{c2}" stop-opacity="0.22"/>'
        f'<stop offset="100%" stop-color="{c2}" stop-opacity="0"/></radialGradient>'
        '<pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">'
        '<path d="M40 0H0V40" fill="none" stroke="#FFFFFF" stroke-opacity="0.035"/></pattern>'
        '<linearGradient id="metal" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#FFFFFF" stop-opacity="0.18"/>'
        '<stop offset="60%" stop-color="#FFFFFF" stop-opacity="0.03"/>'
        '<stop offset="100%" stop-color="#FFFFFF" stop-opacity="0.08"/></linearGradient>'
        f'<style>.t{{font-family:{FONT}}}.m{{font-family:{MONO}}}'
        f'.ttl{{font-family:{FONT};font-weight:700;letter-spacing:-1.8px}}'
        f'.cap{{font-family:{FONT};font-weight:700;letter-spacing:3px}}</style>'
        "</defs>"
    )


def cover() -> str:
    W, H = 1280, 640
    a: list[str] = []
    L = a.append
    L(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
      'role="img" aria-label="Patika Ödev Arşivi — Enes Öztürk">')
    L("<title>Patika Ödev Arşivi · Enes Öztürk</title>")
    L(defs())
    L(f'<rect width="{W}" height="{H}" fill="url(#bg)"/>')
    L(f'<rect width="{W}" height="{H}" fill="url(#grid)"/>')
    L(f'<ellipse cx="210" cy="90" rx="450" ry="270" fill="url(#g1)"/>')
    L(f'<ellipse cx="1140" cy="600" rx="450" ry="290" fill="url(#g2)"/>')
    L(f'<rect x="0" y="0" width="6" height="{H}" fill="url(#acc)"/>')

    L(f'<g class="m" font-size="12" fill="#5A6B88" letter-spacing="1.8">'
      '<text x="56" y="50">PATİKA</text><text x="132" y="50" fill="#1E3050">/</text>'
      '<text x="148" y="50">ÖDEV ARŞİVİ</text>'
      '<text x="1224" y="50" text-anchor="end" fill="#22D3EE" fill-opacity="0.85">ENES ÖZTÜRK</text></g>')
    L('<line x1="56" y1="66" x2="1224" y2="66" stroke="#FFFFFF" stroke-opacity="0.07"/>')

    L('<text x="56" y="176" class="ttl" font-size="62" fill="#E9F0FB">Patika Ödev Arşivi</text>')
    L('<text x="56" y="238" class="t" font-size="21" fill="#8FA0BD">'
      'Her ödev kendi klasöründe: künye, imza kapağı, çalıştırma adımları ve kabul kriterleri.</text>')
    L('<rect x="56" y="266" width="56" height="3" rx="1.5" fill="#22D3EE"/>')

    stats = [("01", "Klasör", "#22D3EE"), ("02", "Künye", "#A78BFA"), ("03", "Kapak", "#FBBF24"), ("04", "Kabul", "#4ADE80")]
    for i, (n, lab, col) in enumerate(stats):
        x = 56 + i * 150
        L(f'<rect x="{x}" y="300" width="136" height="92" rx="14" fill="#0B1420" fill-opacity="0.92" stroke="#1E3050"/>')
        L(f'<rect x="{x}" y="300" width="4" height="92" rx="2" fill="{col}"/>')
        L(f'<text x="{x+20}" y="344" class="m" font-size="26" font-weight="700" fill="{col}">{n}</text>')
        L(f'<text x="{x+20}" y="370" class="m" font-size="11.5" fill="#8FA0BD">{lab}</text>')

    # sağ terminal
    tx, ty, tw, th = 686, 122, 538, 388
    L(f'<rect x="{tx}" y="{ty}" width="{tw}" height="{th}" rx="16" fill="#0B1420" fill-opacity="0.95" stroke="#1E3050"/>')
    L(f'<rect x="{tx}" y="{ty}" width="{tw}" height="38" rx="16" fill="#0E1A2A"/><rect x="{tx}" y="{ty+24}" width="{tw}" height="14" fill="#0E1A2A"/>')
    L(f'<line x1="{tx}" y1="{ty+38}" x2="{tx+tw}" y2="{ty+38}" stroke="#1E3050"/>')
    for i, c in enumerate(["#F87171", "#FBBF24", "#4ADE80"]):
        L(f'<circle cx="{tx+22+i*18}" cy="{ty+19}" r="5" fill="{c}" fill-opacity="0.85"/>')
    L(f'<text x="{tx+92}" y="{ty+24}" class="m" font-size="11.5" fill="#5A6B88">odev-olustur.sh</text>')
    lines = [
        ("$ ./odev-olustur.sh 04-hesap-makinesi", "#E9F0FB"),
        ("✓ klasör açıldı", "#4ADE80"),
        ("✓ README.md üretildi", "#4ADE80"),
        ("✓ docs/rozet.svg eklendi", "#4ADE80"),
        ("", ""),
        ("$ npm run dev", "#E9F0FB"),
        ("  VITE v8  ready in 412 ms", "#8FA0BD"),
        ("  → http://localhost:3000", "#22D3EE"),
        ("", ""),
        ("$ git commit -m \"odev 04: hesap makinesi\"", "#E9F0FB"),
        ("[main 8f3a1c9] odev 04: hesap makinesi", "#4ADE80"),
    ]
    for i, (ln, col) in enumerate(lines):
        if not ln:
            continue
        L(f'<text x="{tx+26}" y="{ty+78+i*28}" class="m" font-size="13" fill="{col}">{ln.replace("&","&amp;").replace("<","&lt;")}</text>')

    L('<line x1="56" y1="470" x2="1224" y2="470" stroke="#FFFFFF" stroke-opacity="0.07"/>')
    L('<text x="56" y="512" class="t" font-size="26" font-weight="700" fill="#E9F0FB">Enes Öztürk</text>')
    L('<text x="56" y="540" class="m" font-size="13" fill="#5A6B88">github.com/EnesBinMalik</text>')
    L('<text x="1224" y="512" class="t" font-size="17" fill="#8FA0BD" text-anchor="end">Node.js · React · Java · Rust · GraphQL</text>')
    L('<text x="1224" y="540" class="m" font-size="12" fill="#22D3EE" text-anchor="end" fill-opacity="0.85">İMZALI ARŞİV</text>')
    L('<text x="56" y="600" class="m" font-size="11.5" fill="#475569">tasarım &amp; geliştirme · Enes Öztürk</text>')
    L("</svg>")
    return "\n".join(a) + "\n"


def ornek_odev() -> str:
    W, H = 1200, 480
    a: list[str] = []
    L = a.append
    L(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
      'role="img" aria-label="Örnek ödev kartı — Enes Öztürk">')
    L(defs(AMBER, PINK))
    L(f'<rect width="{W}" height="{H}" rx="24" fill="url(#bg)"/>')
    L(f'<rect width="{W}" height="{H}" rx="24" fill="url(#grid)"/>')
    L(f'<ellipse cx="180" cy="70" rx="380" ry="220" fill="url(#g1)"/>')
    L(f'<rect x="0" y="0" width="5" height="{H}" fill="url(#acc)"/>')
    L(f'<g class="m" font-size="11.5" fill="#5A6B88" letter-spacing="1.6">'
      '<text x="44" y="46">ÖDEV 04</text>'
      '<text x="1156" y="46" text-anchor="end" fill="#FBBF24" fill-opacity="0.9">TAMAMLANDI</text></g>')
    L(f'<text x="44" y="112" class="ttl" font-size="42" fill="#E9F0FB">Hesap Makinesi</text>')
    L('<text x="44" y="146" class="t" font-size="16" fill="#8FA0BD">Java · nesne yönelimli programlama · dört işlem + geçmiş</text>')
    L('<rect x="44" y="168" width="48" height="3" rx="1.5" fill="#FBBF24"/>')
    for i, (k, v) in enumerate([("Süre", "2 saat"), ("Zorluk", "Orta"), ("Teknoloji", "Java 21"), ("Dosya", "6 sınıf")]):
        x = 44 + i * 150
        L(f'<rect x="{x}" y="196" width="132" height="74" rx="12" fill="#0B1420" fill-opacity="0.9" stroke="#1E3050"/>')
        L(f'<text x="{x+18}" y="226" class="m" font-size="10.5" fill="#5A6B88">{k}</text>')
        L(f'<text x="{x+18}" y="250" class="t" font-size="15" font-weight="600" fill="#E9F0FB">{v}</text>')
    L('<text x="44" y="316" class="t" font-size="14" font-weight="600" fill="#E9F0FB">Kabul kriterleri</text>')
    for i, t in enumerate(["Dört işlem ve sıfıra bölme kontrolü", "Geçmiş listesi ve temizleme", "Klavye desteği"]):
        L(f'<text x="44" y="{342+i*26}" class="m" font-size="12.5" fill="#8FA0BD">✓ {t}</text>')
    L('<line x1="700" y1="96" x2="700" y2="420" stroke="#FFFFFF" stroke-opacity="0.07"/>')
    L('<text x="736" y="126" class="m" font-size="11.5" fill="#5A6B88">src/Calculator.java</text>')
    code = ["public class Calculator {", "  private final History history;", "",
            "  public double apply(Op op, double a, double b) {", "    history.push(op, a, b);",
            "    return op.eval(a, b);", "  }", "}"]
    for i, ln in enumerate(code):
        L(f'<text x="736" y="{158+i*26}" class="m" font-size="13" fill="{"#FBBF24" if i in (0,4) else "#9DB0C8"}">{ln.replace("&","&amp;").replace("<","&lt;")}</text>')
    L('<text x="1156" y="440" text-anchor="end" class="m" font-size="11" fill="#475569">imza · Enes Öztürk</text>')
    L("</svg>")
    return "\n".join(a) + "\n"


def rozet() -> str:
    """Depo rozeti: kalkan formunda, arşiv simgesi."""
    c1, c2 = CYAN, VIOLET
    a: list[str] = []
    L = a.append
    L('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600" width="600" height="600" '
      'role="img" aria-label="Patika Ödev Arşivi — Enes Öztürk imzalı rozet">')
    L("<title>Patika Ödev Arşivi · Enes Öztürk</title>")
    L(defs())
    L('<rect width="600" height="600" rx="28" fill="url(#bg)"/>')
    L('<rect width="600" height="600" rx="28" fill="url(#grid)"/>')
    L('<ellipse cx="300" cy="240" rx="250" ry="210" fill="url(#g1)"/>')
    body = "M300 92 L480 160 V312 C480 410 398 476 300 508 C202 476 120 410 120 312 V160 Z"
    L(f'<path d="{body}" fill="#0A1220" fill-opacity="0.96" stroke="url(#acc)" stroke-width="4"/>')
    L(f'<g transform="translate(300,300) scale(0.84) translate(-300,-300)">'
      f'<path d="{body}" fill="url(#metal)" stroke="#FFFFFF" stroke-opacity="0.10" stroke-width="1.5"/></g>')
    L(f'<g transform="translate(300,300) scale(0.71) translate(-300,-300)">')
    # arşiv/kutu simgesi
    L(f'<path d="M214 172 h172 v70 h-172 Z" fill="none" stroke="{c1}" stroke-width="11" stroke-linejoin="round"/>')
    L(f'<path d="M232 242 h136 v106 c0 12 -10 22 -22 22 h-92 c-12 0 -22 -10 -22 -22 Z" fill="none" stroke="{c1}" stroke-width="11" stroke-linejoin="round"/>')
    L(f'<path d="M300 262 v56 M274 292 h52" stroke="{c1}" stroke-width="10" stroke-linecap="round"/>')
    L(f'<text x="300" y="392" text-anchor="middle" class="t" font-size="22" font-weight="700" fill="#E9F0FB">Patika Ödevleri</text>')
    L(f'<text x="300" y="418" text-anchor="middle" class="m" font-size="12.5" fill="#8FA0BD">künye · kapak · kabul kriteri</text>')
    L(f'<text x="300" y="446" text-anchor="middle" class="m" font-size="10.5" fill="#5A6B88">ENES ÖZTÜRK · github.com/EnesBinMalik</text>')
    L(f'<g transform="rotate(-5 300 476)"><rect x="212" y="460" width="176" height="32" rx="16" fill="{c1}" fill-opacity="0.13" stroke="{c1}" stroke-opacity="0.6" stroke-width="1.5"/>')
    L(f'<text x="300" y="481" text-anchor="middle" class="cap" font-size="11.5" fill="{c1}">AÇIK ARŞİV</text></g>')
    L("</g>")
    L("</svg>")
    return "\n".join(a) + "\n"


def main() -> None:
    OUT.mkdir(exist_ok=True)
    (OUT / "cover.svg").write_text(cover(), encoding="utf-8")
    (OUT / "ornek-odev.svg").write_text(ornek_odev(), encoding="utf-8")
    (OUT / "rozet.svg").write_text(rozet(), encoding="utf-8")
    print("✓ docs/cover.svg · docs/ornek-odev.svg · docs/rozet.svg")


if __name__ == "__main__":
    main()
