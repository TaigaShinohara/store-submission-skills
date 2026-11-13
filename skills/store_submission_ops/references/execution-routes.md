# 実行経路の振り分け

使い方：案件の開始時に、対象ストアの経路をこの表で確定させる。自動化の可否は変わるため、案件ごとに公式ドキュメントで再確認する。表は 2026-11-13 時点の実務整理。

## 経路の3分類

- A 自動化可：公式APIやCLIで下書き作成、素材投入、提出準備まで進められる。本人の承認が要る確定操作は止まる。
- B ブラウザ操作：管理画面を Chrome（クラウドブラウザ）で操作する。下書きと入力は進められ、確定操作は止まる。
- C 手作業のみ：開発者本人の環境や端末でしかできない。手順書で渡す。

## ストア別

### Apple App Store（App Store Connect）

- 経路：A と B の併用。App Store Connect API と fastlane 等でメタデータ、スクリーンショット、ビルド紐付け、提出準備が自動化できる。管理画面のブラウザ操作でも同じことができる。
- C に切り分けるもの：Developer Program 登録と本人確認、規約と税・銀行、証明書とプロビジョニングの新規作成、Xcode での署名ビルドとアップロード（Transporter 等の実行環境が開発者側にある場合）、2要素認証の承認操作。
- 注意：APIキーや .p8 鍵はパックに入れない。保管場所への参照だけを持つ。

### Google Play（Play Console）

- 経路：A と B の併用。Google Play Developer API（Edits）と fastlane supply 等で AAB 投入、ストア掲載情報、リリース作成が自動化できる。初回のアプリ作成と申告フォームの一部は管理画面が確実。
- C に切り分けるもの：開発者登録と本人確認、サービスアカウントの作成と権限付与（初回）、署名鍵の生成と Play App Signing の登録、クローズドテストのテスター集めと期間の消化。
- 注意：本番トラックへの公開確定は止まる場所に含める。テストトラックへの投入と本番公開を分けて扱う。

### Chrome Web Store

- 経路：主に B。Developer Dashboard で ZIP 投入、掲載情報、Privacy practices、配布設定を入力する。公開APIは限定的なため、原則ブラウザ操作で進め、自動化できる部分が確認できた場合だけ A に寄せる。
- C に切り分けるもの：開発者登録料の支払い、2段階認証の設定、拡張機能のビルドと ZIP 化（開発者側）。
- 注意：権限の正当化は Privacy practices の入力が審査の中心になる。パックの permission-justifications.md をそのまま使える形にしておく。

### Microsoft Store（Partner Center）

- 経路：主に B。Partner Center で名前予約、パッケージ投入、各申告、ストア掲載を入力する。提出APIは条件付きで存在するため、使える場合だけ A として扱う。
- C に切り分けるもの：開発者登録と本人確認、MSIX のパッケージングと署名設定（ストア提出用 identity の反映）、WACK 等のローカル検証。
- 注意：初回提出は Partner Center で行う前提の案内がある。ツールの自動化だけで初回を済ませようとしない。

### その他のストア

- Firefox Add-ons、Edge Add-ons：開発者ハブのブラウザ操作が中心（B）。Chrome版パックの流用可否を確認してから入力する。
- Samsung Galaxy Store、Amazon Appstore：各コンソールのブラウザ操作が中心（B）。独自申告はパックの差分として追加する。
- Steam：Steamworks のブラウザ操作と SteamPipe でのビルド投入（A と B の併用）。パートナー登録と費用は止まる場所に含める。
- 直接配布（自サイト、GitHub Releases 等）：ストア審査はないが、署名と公証（macOS）、署名（Windows）など OS 側の要件を store_review_readiness で別途判定する。
