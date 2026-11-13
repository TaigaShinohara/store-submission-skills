#!/usr/bin/env python3
"""Scaffold a store listing pack folder. Never overwrites existing files."""
import argparse, os, sys

DIRS = [
    "01_copy/by-store", "02_images/icon", "02_images/screenshots",
    "02_images/promo", "03_legal", "04_declarations", "05_build",
    "06_review", "07_submission",
]
FILES = {
    "README.md": "# Store pack\n\n対象ストアと完成状態は 07_submission/pack-status.md を見る。\n",
    "00_manifest.yaml": "app_name: \"\"\napp_slug: \"{slug}\"\nversion: \"{version}\"\nbuild_number: \"\"\ndeveloper_display_name: \"\"\ncategory: \"\"\nprice_model: \"\"\nsupport_email: \"\"\nsupport_url: \"\"\nprivacy_policy_url: \"\"\nwebsite_url: \"\"\ntarget_stores: []\ndefault_language: \"ja\"\nupdated_at: \"\"\npack_owner: \"\"\n",
    "01_copy/master-copy.md": "# マスター原稿\n\n## アプリ名\n\n## 短い紹介（1文）\n\n## 機能（実態のみ、3から5点）\n\n## 詳しい説明\n\n## キーワード候補\n\n## 更新内容\n",
    "03_legal/privacy-policy.md": "# プライバシーポリシー（公開文面の正本）\n\n公開URLは 00_manifest.yaml に書く。\n",
    "03_legal/support.md": "# サポート\n\n連絡先と窓口の文面を書く。実際に届くものだけを使う。\n",
    "03_legal/licenses.md": "# 権利メモ\n\n使用素材、フォント、OSS の利用可否を書く。未確認は未確認と書く。\n",
    "04_declarations/data-map.yaml": "# データ棚卸し: 種類 / 目的 / 第三者共有 / 保存期間 / 削除手段。SDK分を含む。\ncollected: []\nshared: []\n",
    "04_declarations/privacy-answers.md": "# プライバシー申告への回答\n\ndata-map.yaml と一致させる。\n",
    "04_declarations/permission-justifications.md": "# 権限ごとの理由文\n\n権限1つにつき、使う機能と場面を1文で書く。\n",
    "04_declarations/age-rating-answers.md": "# 年齢レーティング回答\n\n実態と一致させる。\n",
    "04_declarations/pricing-and-iap.md": "# 価格・課金・広告の申告材料\n",
    "05_build/build-pointer.md": "# ビルド参照\n\n置き場所、バージョン、ビルド番号、チェックサムだけを書く。ビルド本体と鍵は入れない。\n",
    "06_review/review-notes.md": "# 審査用メモ\n\nログイン手順、主要導線、特殊条件を書く。パスワードは書かない。\n",
    "06_review/demo-account.ref.md": "# デモアカウント参照\n\n保管場所（Secure Vault / 1Password 等）だけを書く。値は書かない。\n",
    "07_submission/pack-status.md": "# パック状態\n\n- 揃ったもの:\n- 不足:\n- 未確認:\n- 提出に使ってはいけない素材:\n",
    "07_submission/store-checklist.md": "# ストア別提出チェック\n\nstore_submission_ops が更新する。\n",
}

def main():
    p = argparse.ArgumentParser()
    p.add_argument("slug"); p.add_argument("version")
    p.add_argument("--out", default=os.path.expanduser("~/workspace/store-packs"))
    a = p.parse_args()
    root = os.path.join(a.out, a.slug, a.version)
    created, skipped = [], []
    for d in DIRS:
        os.makedirs(os.path.join(root, d), exist_ok=True)
    for rel, body in FILES.items():
        path = os.path.join(root, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        if os.path.exists(path):
            skipped.append(rel); continue
        with open(path, "w", encoding="utf-8") as f:
            f.write(body.format(slug=a.slug, version=a.version))
        created.append(rel)
    print(f"pack: {root}")
    print(f"created: {len(created)}  skipped(existing): {len(skipped)}")
    for s in skipped: print(f"  skipped {s}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
