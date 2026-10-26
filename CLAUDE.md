# Path of the Companions 日本語化パッチ(このリポジトリ)

Path of the Companions(Paths。Nexus 196635)の日本語化パッチ。配布は Nexus のパッチ用ページ 196104(https://www.nexusmods.com/skyrimspecialedition/mods/196104)。原作者は hashhbbrown(GitHub: fatalCMD)。Fight With Me(FWM、Nexus 194766)は任意の連携先で、Paths の前提ではない。
FWM の日本語化パッチは別リポジトリ(dolphag/Skyrim-Fight-With-Me-Japanese-translations-patch)。Paths 旧版(0.1.0)の DLL パッチは、そちらの `legacy/0.3.0/` と履歴にある(この MOD の旧版とは別物)。
**方式**: DLL は触らない。原作が外部ファイルに分けたメッセージ(`Translations` フォルダ)の日本語版 `FightWithMePaths_JAPANESE.txt` を置く。経緯と仕様は `docs/FWM-0.5.0_Paths-1.0-findings.md`。
- 正式名は **Paths of the Companions**(原作者の返信。`docs/NAMES.md`)。この文書などに残る `Path of the Companions` は誤りで、次の版で直す。新しく書く文章では正しい名称を使う。
常時読み込まれるので短く保つ。手順は `.claude/skills/`、用語は `docs/GLOSSARY.md`、版ごとの調査は `docs/` に置く。

## 確認済みの環境の事実
- テスト版の受け渡し: SendUserFile で zip を渡せる。
- **タグの push は、このクラウド環境から 403 で拒否される**。GitHub MCP にもタグ作成は無い。タグ(GitHub Release)はユーザーが main の HEAD の commit に付ける。迂回しない。
- 原 MOD の zip は毎回ユーザーが添付する。**翻訳のもとになる一覧は配布 zip を正とする**(原作 git `fatalCMD/potc` は配布版より古いことがある)。

## 応答のしかた
- 日本語。率直・技術的に正確に。褒めない・慰めない。誤りは、どの前提が誤りだったかを示して認める。
- 事実が不確かなら推測せず確認する(Nexus の権限・版・更新時刻、上流の状態など)。確認できなかったことは「未確認」と書く。
- 作業の最後に、やったこと/やっていないこと/ユーザーが判断すること、を分けて報告する。

## 権利・配布(絶対に守る)
- **GitHub はソースのみ。DLL・zip・フォントはコミットしない**(`.gitignore` で除外)。配布物は Nexus のみ。生成した `FightWithMePaths_JAPANESE.txt` も `out/`(git 管理外)。
- 英日対応表(`translations_en_ja.csv`)の英語列は原作者のもの。原作 git は GPL-3.0 を宣言しているが、Nexus ページの権限は別に確認する。README に英語列の扱いを明記し続ける。
- リリースごとに、原 MOD の Nexus ページの権限(Permissions and credits)をその時点で確認し、確認日を README に書く。変わっていたら止めてユーザーに報告。
- 原作者クレジット(hashhbbrown / GitHub fatalCMD)を、README・Nexus 説明・Nexus の **File credits 欄**の 3 か所に入れる(フォントのファイルには Noto Sans JP / Adobe も)。
- **ユーザーの許可なしにしない**: main への push、タグ、Nexus 投稿、原作者への連絡、削除。作業ブランチへの push は可。
- ユーザーが添付した元ファイルは編集しない。コピーで作業する。

## 版番号
- Paths に連動する(Paths 1.0.0 → パッチ 1.0.0-N)。パッチだけの修正は枝番。タグは `v1.0.0-1` の形。
- **Nexus の版と、zip 内 README の版を必ず一致させる**。
- 版ごとに新しいセッションで始める。前の版から持ち越す知識は `docs/` に書いてあるものだけ。

## 翻訳・表示のルール
- 用語は `docs/GLOSSARY.md`。skill→**アビリティ**、「スキルツリー」は使わずツリー。
- 使える漢字は `tools/jp_kanji.txt` の範囲内(範囲外は `lang_build.py` が失敗)。ゲーム由来の文字列は変えられない → README で EnableChinese を推奨している。
- 折り返しは ASCII スペースでしか起きない。長文は文節区切りにスペースを入れる(`lang_build.py` が janome で自動)。
- 表示倍率・位置の補正はできない(DLL を触らない)。窮屈な場所は訳を短くする。
- **利用者向けの文面(README・Nexus)では、原作に「翻訳機能」があるように書かない**。原作はメッセージを外部ファイルに出しているだけ。Paths は別 MOD で、方式の変更点を強調しない。FWM は任意の連携先として書き、前提にしない。
- 言語は `sLanguage`(ゲームか各 INI)。JAPANESE のときは `FightWithMePaths_JAPANESE.txt`、ENGLISH のときは同じ内容の `FightWithMe_JA_Paths_ENGLISH.txt`(英語設定のまま日本語化している環境向け。名前は原作の英語ファイルより後に並ぶものにする)が読まれる。`_user.ini` は配らない(個人設定を消すため)。英語版ゲームの利用者には、`FightWithMePaths_user.ini`(FWM も使うなら `FightWithMe_user.ini` にも)への設定を README で案内する。
- 日本語フォントが必須: 原作のテーマ用フォントは日本語を含まない。**翻訳と同じ zip に同梱する**(別ファイルにすると、同じページ名の MOD として MO2 に入れるとき「一つにまとめる/置き換える」のダイアログが出て混乱するため。2026-10-26 に統合)。`tools/make_font_pack.py`(ユーザーが添付する OFL のフォントから作る。フォントは GitHub に置かない。出力は決定的)。

## 作業の進め方
- 手順は skill `lang-text-workflow`(生成・検査・テスト版 zip)と `release-package`(README・zip・Nexus 文面・タグ)。zip 作成は `tools/make_zip.py`。
- **実機(ゲーム内)確認なしにリリースしない**。テスト版は `out/` に `test<N>` で作り(git 管理外)、ユーザーのスクリーンショットと所見で直す。テストの前に、ユーザーの SKSE ログの 1 行目と `[Text] JAPANESE: N lines` を確認する。
- 調査の結果は必ずファイルに残す(`docs/`)。会話には残らない前提で作業する。
- 大きいファイルは全文を読まず、必要な範囲だけ読む。
- 開発用の依存: `pip install -r requirements-dev.txt`(`python3 -I` で実行)。

## Nexus の確認
- WebFetch は Nexus で失敗しやすい(PROVENANCE_REQUIRED)。使えない場合は、ユーザーに確認(貼り付け・スクリーンショット)を依頼する。
- API で引く手段: skill `nexus-check`(`tools/nexus_query.py`、キー不要、版・ファイル一覧は実測済み)。環境が api.nexusmods.com を許可している必要がある。**権限(Permissions)と配布 zip のダウンロードは API で取れない**(後者は非プレミアムで 403)→ ブラウザかユーザー確認、zip はユーザーが添付。詳細は `docs/nexus-api-notes.md`。
- ページの権限・版・ファイル名・更新時刻は、実際に読み取ったものだけを事実として扱う。
