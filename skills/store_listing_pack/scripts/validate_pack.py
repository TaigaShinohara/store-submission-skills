#!/usr/bin/env python3
"""Validate a store listing pack: required files, image sizes, secret-like strings.
Usage: validate_pack.py <pack_dir> [--expect store=device:WxH ...]
Example: --expect apple=iphone:1320x2868 --expect chrome=main:1280x800
Without --expect it only checks presence, format and readability of images.
"""
import argparse, os, re, sys
from PIL import Image

REQUIRED = ["00_manifest.yaml", "01_copy/master-copy.md", "03_legal/privacy-policy.md",
            "04_declarations/data-map.yaml", "04_declarations/privacy-answers.md",
            "04_declarations/permission-justifications.md", "04_declarations/age-rating-answers.md",
            "05_build/build-pointer.md", "06_review/review-notes.md", "07_submission/pack-status.md"]
SECRET_RE = re.compile(r"(password\s*[:=]\s*\S+|api[_-]?key\s*[:=]\s*\S+|-----BEGIN (RSA |EC )?PRIVATE KEY-----)", re.I)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("pack")
    p.add_argument("--expect", action="append", default=[],
                   help="store=device:WxH ; checks every image under 02_images/screenshots/<store>/<device>/")
    a = p.parse_args()
    problems, warnings = [], []
    if not os.path.isdir(a.pack):
        print(f"ERROR pack not found: {a.pack}"); return 2
    for rel in REQUIRED:
        if not os.path.isfile(os.path.join(a.pack, rel)):
            problems.append(f"missing required file: {rel}")
    images = []
    for root, _, files in os.walk(os.path.join(a.pack, "02_images")):
        for fn in files:
            if fn.lower().endswith((".png", ".jpg", ".jpeg")):
                path = os.path.join(root, fn)
                try:
                    with Image.open(path) as im:
                        images.append((os.path.relpath(path, a.pack), im.size, im.format))
                except Exception as e:
                    problems.append(f"unreadable image: {path}: {e}")
    for exp in a.expect:
        try:
            store_dev, size = exp.split(":", 1); store, dev = store_dev.split("=", 1)
            w, h = (int(x) for x in size.lower().split("x"))
        except Exception:
            problems.append(f"bad --expect format: {exp} (want store=device:WxH)"); continue
        folder = os.path.join(a.pack, "02_images", "screenshots", store, dev)
        if not os.path.isdir(folder):
            problems.append(f"missing screenshot folder: 02_images/screenshots/{store}/{dev}"); continue
        found = [i for i in images if i[0].startswith(f"02_images/screenshots/{store}/{dev}/")]
        if not found:
            problems.append(f"no screenshots in 02_images/screenshots/{store}/{dev}")
        for rel, (iw, ih), fmt in found:
            if (iw, ih) != (w, h):
                problems.append(f"size mismatch {rel}: {iw}x{ih} != expected {w}x{h}")
    for root, _, files in os.walk(a.pack):
        for fn in files:
            if fn.endswith((".md", ".yaml", ".yml", ".txt")):
                path = os.path.join(root, fn)
                try:
                    text = open(path, encoding="utf-8", errors="ignore").read()
                except Exception:
                    continue
                if SECRET_RE.search(text):
                    warnings.append(f"possible secret-like text in {os.path.relpath(path, a.pack)} (check manually, do not print the value)")
    copy_dir = os.path.join(a.pack, "01_copy")
    if os.path.isdir(copy_dir):
        print("copy character counts (compare against references/copy-specs.md manually):")
        for root, _, files in os.walk(copy_dir):
            for fn in sorted(files):
                if fn.endswith((".md", ".txt")):
                    path = os.path.join(root, fn)
                    try:
                        n = len(open(path, encoding="utf-8", errors="ignore").read())
                    except Exception:
                        continue
                    print(f"  {os.path.relpath(path, a.pack)}  {n} chars")
    print(f"images found: {len(images)}")
    for rel, (w, h), fmt in images: print(f"  {rel}  {w}x{h} {fmt}")
    for wmsg in warnings: print(f"WARNING {wmsg}")
    for prob in problems: print(f"PROBLEM {prob}")
    print("RESULT:", "FAIL" if problems else "OK (presence/format only; content still needs human check)")
    return 1 if problems else 0

if __name__ == "__main__":
    sys.exit(main())
