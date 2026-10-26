# Nexus 用テキスト(Path of the Companions 日本語化 1.0.0-1)

アップロードはユーザーが行う。**権限(Permissions and credits)と版は、アップロード直前に原ページで再確認する。**
新規の翻訳ページ(原 MOD は Nexus 196635)に、1 つのファイルを置く(翻訳と日本語フォントを同じ zip にまとめる。2 ファイルに分けると、MO2 で「一つにまとめる/置き換える」のダイアログが出て混乱するため)。

| ファイル | 版 | 種別 |
|---|---|---|
| `Path of the Companions - Japanese Translations Patch 1.0.0-1.zip` | 1.0.0-1 | Main |

## File credits 欄(各ファイル。空にしない)
- hashhbbrown(Path of the Companions / Fight With Me の作者)。GitHub: fatalCMD
- Noto Sans JP(Adobe)も入れる(フォントを同梱しているため)。

## ファイル説明(Main、短く)
`Path of the Companions 1.0.0 の日本語訳です。原作が外部のテキストファイルに分けているメッセージの日本語版(FightWithMePaths_JAPANESE.txt)を置くだけで、DLLは変更しません。日本語フォントを同梱しています(原作のテーマ用フォントを置き換えます)。日本語表示にはSKSE Menu Framework の日本語設定も必要です。詳細は同梱のREADME。`

## 更新履歴(アップロード時の「Changelog」欄)
1.0.0-1: 初版(Path of the Companions 1.0.0 用)。

## ページの説明(要点。bbcode に整形して使う)
1. 原作へのリンクとクレジット(hashhbbrown / fatalCMD)。非公式の翻訳で、原作者に問い合わせないこと。
2. **導入に必要なもの**: Paths 本体と POTC Effects 1.0.21 以上、SKSE Menu Framework 3 の日本語設定、SKSE Menu Framework の日本語設定。Fight With Me は任意の連携先と書き、必須にしない(併用するなら FWM 用の日本語化パッチも入れる)。
3. **日本語にならないとき**: `sLanguage = JAPANESE`(英語版ゲームの場合は `FightWithMePaths_user.ini`。FWM 併用なら `FightWithMe_user.ini` にも)。ログの `[Text] JAPANESE: N lines`。
4. **日本語にならないもの**: パーティ設定ページの役割・注目対象・位置取りのドロップダウン(原作側の漏れ)、テーマ名(原文のまま)、ゲーム由来の文字列。
5. スクリーンショット(Paths のツリー、詳細パネル、設定)。AI 利用の開示。他サイトへの転載はご遠慮ください。
6. 対応版: Paths 1.0.0。原作の更新時はパッチを外さなくてよいが、新しい文言は英語のまま。
7. GitHub(ソースのみ): https://github.com/dolphag/Skyrim-POTC-JP-Patch
