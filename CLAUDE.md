# Path of the Companions 日本語化パッチ(このリポジトリ)

Path of the Companions(Paths。Nexus 196635)の日本語化パッチ。原作者は hashhbbrown(GitHub: fatalCMD)。Fight With Me(FWM、Nexus 194766)は任意の連携先で、Paths の前提ではない。
FWM の日本語化パッチは別リポジトリ(dolphag/Skyrim-Fight-With-Me-Japanese-translations-patch)。Paths 旧版(0.1.0)の DLL パッチは、そちらの `legacy/0.3.0/` と履歴にある(この MOD の旧版とは別物)。
**方式**: DLL は触らない。原作が外部ファイルに分けたメッセージ(`Translations` フォルダ)の日本語版 `FightWithMePaths_JAPANESE.txt` を置く。経緯と仕様は `docs/FWM-0.5.0_Paths-1.0-findings.md`。
常時読み込まれるので短く保つ。手順は `.claude/skills/`、用語は `docs/GLOSSARY.md`、版ごとの調査は `docs/` に置く。

## 確認済みの環境の事実
- テスト版の受け渡し: SendUserFile で zip を渡せる。
- **タグの push は、このクラウド環境から 403 で拒否される**。GitHub MCP にもタグ作成は無い。タグ(GitHub Release)はユーザーが main の HEAD の commit に付ける。迂回しない。
- 原 MOD の zip は毎回ユーザーが添付する。**翻訳のもとになる一覧は配布 zip を正とする**(原作 git `fatalCMD/potc` は配布版より古いことがある)。

## 応答のしかた
- 日本語。率直・技術的に正確に。褒めない・慰めない。誤りは、どの前提が誤りだったかを示して認める。
- 事実が不確かなら推測せず確認する(Nexus の権限・版・更新時刻、上流の状態など)。確認できなかったことは「未確認」と書く。
- 作業の最後に、やったこと/やっていないこと/ユーザーが判断すること、を分けて報告する。
- リポジトリのドキュメントと既存のコードに矛盾がある場合は、既存のコードで採用されている規約に従い、最終的な返信では、ドキュメントとコードの間で見つけた不一致を一つずつ指摘する。

## 権利・配布(絶対に守る)
- **GitHub はソースのみ。DLL・zip・フォントはコミットしない**(`.gitignore` で除外)。配布物は Nexus のみ。生成した `FightWithMePaths_JAPANESE.txt` も `out/`(git 管理外)。
- 英日対応表(`translations_en_ja.csv`)の英語列は原作者のもの。原作 git は GPL-3.0 を宣言しているが、Nexus ページの権限は別に確認する。README に英語列の扱いを明記し続ける。
- リリースごとに、原 MOD の Nexus ページの権限(Permissions and credits)をその時点で確認し、確認日を README に書く。変わっていたら止めてユーザーに報告。
- 原作者クレジット(hashhbbrown / GitHub fatalCMD)を、README・Nexus 説明・Nexus の **File credits 欄**の 3 か所に入れる(フォントのファイルには Noto Sans JP / Adobe も)。
- **ユーザーの許可なしにしない**: main への push、タグ、Nexus 投稿、原作者への連絡、削除。作業ブランチへの push は可。
- ユーザーが添付した元ファイルは編集しない。コピーで作業する。

## 版番号
- Paths に連動する(Paths 1.2.0 → パッチ 1.2.0-N)。パッチだけの修正は枝番。タグは `v1.2.0-1` の形。
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
- **実機(ゲーム内)確認なしにリリースしない**。テスト版は `out/` に `<版>_test<N>` で作り(ファイル名とメモ1行目に版を入れる)(git 管理外)、ユーザーのスクリーンショットと所見で直す。テストの前に、ユーザーの SKSE ログの 1 行目と `[Text] JAPANESE: N lines` を確認する。
- 調査の結果は必ずファイルに残す(`docs/`)。会話には残らない前提で作業する。
- 大きいファイルは全文を読まず、必要な範囲だけ読む。
- 開発用の依存: `pip install -r requirements-dev.txt`(`python3 -I` で実行)。

## Nexus のページ説明文(`release/NEXUS_DESCRIPTION.bbcode.txt`)のルール
- **版に依存しない書き方にする**。Paths・FWM・POTC Effects の版番号、権限の確認日、「新しい」「同時に更新」、版ごとの既知の未確認事項は書かない。対応版は、ファイル一覧・更新履歴(`NEXUS_TEXT_<版>.md`)と zip 内 README に書く。版のたびにページ説明を書き直さないため。
- 姉妹 MOD の日本語化パッチのリンク(Walk With Me、Fight With Me)を入れる。FWM は任意の連携先として、「版に合った最新のパッチ」と書く。
- 日本語・英語の両方を同じ内容にする。対照表へのリンクと注記を、アビリティ名の注記のすぐ後に置く。

## 対照表(`PATHS_TABLE.md`)のルール
- 日本語訳へのご指摘(違和感など)をいただく際の参照用。`python3 -I tools/paths_table.py --src <fatalCMD/potc の clone>` で作る(構造・数値は原作の公開ソース、日本語名は CSV、効果の要約はスクリプト内の `EFFECTS`)。手で表を直さず、スクリプトを直して再生成する。
- 原作の英文(説明文)は写さない。英語は名前だけ。効果は自分の言葉で要約する。
- **公開ソースは配布版より古いことがある**(1.2.0 の時点で 1.0.0)。数値が配布版と未照合である旨の注意書きを、表の冒頭に残す(ユーザー決定)。スカルドのように公開ソースに無いものは「(推定)」「未確認」と明記する。確認できていない数値を事実として書かない。
- Paths の版が上がったら、新しい公開ソースがあれば `--src` を替えて再生成し、無ければ実機で照合してから `EFFECTS` を直す。調査の経緯は `docs/Paths-<版>-findings.md` に残す。
- リンクは `main` 上の `PATHS_TABLE.md`(README・ページ説明・`NEXUS_TEXT`)。

## Nexus の確認
- WebFetch は Nexus で失敗しやすい(PROVENANCE_REQUIRED)。使えない場合は、ユーザーに確認(貼り付け・スクリーンショット)を依頼する。
- API で引く手段: skill `nexus-check`(`tools/nexus_query.py`、キー不要、版・ファイル一覧は FWM リポジトリで実測済み)。環境が api.nexusmods.com を許可している必要がある。**権限(Permissions)は API に無い** → ブラウザかユーザー確認。ダウンロード(`NEXUS_API_KEY` 要)は未検証。詳細は `docs/nexus-api-notes.md`。
- ページの権限・版・ファイル名・更新時刻は、実際に読み取ったものだけを事実として扱う。
