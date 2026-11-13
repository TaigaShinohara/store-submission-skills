# パック構成（固定）

置き場所の既定：`~/workspace/store-packs/<app-slug>/<version>/`
提出先ごとにフォルダを増やさない。ストア別の差分は中の `by-store/` で持つ。

```
<app-slug>/<version>/
  README.md                     パックの目次、対象ストア、完成状態の要約
  00_manifest.yaml              正本情報（下記）
  01_copy/
    master-copy.md              マスター原稿（名前、短文、長文、キーワード、更新内容）
    by-store/
      apple.md / google-play.md / chrome-web-store.md / microsoft-store.md ...
  02_images/
    icon/                       正本アイコンと各サイズ書き出し
    screenshots/<store>/<device>/   実画面スクリーンショット
    promo/                      フィーチャーグラフィック、プロモーションタイル等
  03_legal/
    privacy-policy.md           公開文面の正本（公開URLを manifest に書く）
    support.md                  サポート連絡先と窓口の文面
    licenses.md                 使用素材、フォント、OSS の権利メモ
  04_declarations/
    data-map.yaml               データ棚卸し（種類、目的、共有、削除）
    privacy-answers.md          各ストアのプライバシー申告への回答
    permission-justifications.md 権限ごとの理由文
    age-rating-answers.md       年齢レーティング質問への回答
    pricing-and-iap.md          価格、課金、広告、アフィリエイトの申告材料
  05_build/
    build-pointer.md            ビルドの置き場所、版、番号、チェックサムへの参照のみ
  06_review/
    review-notes.md             審査用メモ（ログイン手順、主要導線、特殊条件）
    demo-account.ref.md         デモアカウントの保管場所への参照（値は書かない）
  07_submission/
    pack-status.md              検証結果（揃ったもの、不足、未確認、禁止素材）
    store-checklist.md          ストア別の提出チェック（提出実行スキルが更新）
```

## 00_manifest.yaml の項目

- app_name、app_slug、version、build_number
- developer_display_name、category、price_model（free / paid / iap / subscription / ads）
- support_email、support_url、privacy_policy_url、website_url
- target_stores（ストア名、登録IDやアプリIDへの参照、状態）
- default_language と対応言語
- updated_at、pack_owner

値は秘密情報にしない。ID は提出に必要な公開・管理IDのみとし、鍵やトークンは書かない。
