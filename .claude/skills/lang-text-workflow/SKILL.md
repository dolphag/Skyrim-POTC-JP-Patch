---
name: lang-text-workflow
description: Path of the Companions 1.0 以降の日本語化(メッセージの日本語版 FightWithMePaths_JAPANESE.txt)を作る・直す・検証するときの手順。訳の追加、新しい版への追従、テスト版 zip。
---

# 日本語版メッセージファイルの作業手順

DLL は触らない。原作が外部ファイルに分けたメッセージの日本語版を渡す。背景と仕様は `docs/FWM-0.5.0_Paths-1.0-findings.md`。

## 前提
- Paths の zip(`Path Of The Companions - Main File`)をユーザーが添付する。**一覧は配布 zip を正とする**(原作 git は古いことがある)。
- zip には英語の一覧が 2 つある: `FightWithMePaths_ENGLISH.txt`(ツリー・アビリティ・特性)と `FightWithMe_ENGLISH.txt`(Paths の DLL も使う共通のパネル・設定の文言。原作の意図的な同梱。DLL 内に 824/833 件の文字列が実在することを確認済み)。
  本パッチは両方の和集合を `FightWithMePaths_JAPANESE.txt` 1 本にする(FWM 用パッチのファイル名と衝突させないため)。
- 依存: `pip install -r requirements-dev.txt`(janome、fonttools)。実行は `python3 -I`。

## 通常の変更(訳の修正・追加)
1. 訳の正本は `translations_en_ja.csv`(列 `en,ja`。鍵 = 英語全文、`\n` は実改行。ja は折り返し用スペースを入れる前の文)。英語のままにする項目は ja を en と同じ値にする。
2. 生成と検査: `python3 -I tools/lang_build.py --paths <Paths zip> --out out/ja`
   - 未訳、書式欄(`{}` `{:.0f}` `{0}`)の種類・順序の不一致、`tools/jp_kanji.txt` 範囲外の漢字、CSV に残った古い項目があると失敗する。
   - 範囲外の漢字はひらがなにする。番号付き書式(`{1}`)にすれば順序を入れ替えられる。
3. テスト版: メモを `release/TEST_MEMO_TEMPLATE.txt` の形で書き、`python3 -I tools/make_zip.py test out/ja <N> --memo <メモ> --font-dir out/font` → `out/POTC_ja_test<N>.zip`。ユーザーへは SendUserFile で渡す。

## 新しい版へ移行するとき
1. 新しい zip の一覧と旧 CSV を比べる(`lang_build.py` の「未訳」「一覧に無い項目」が差分)。同じ英語は訳が自動で当たる。
2. 変わった英語は訳を直す(数値が変わっただけの文も、鍵が変わるので別項目になる)。古い項目は CSV から外す。
3. 版ごとの調査は `docs/` に残す。新しいセッションで始める。

## 落とし穴
- **テストの前に、ユーザーの SKSE ログ(FightWithMePaths 系 .log)の 1 行目で版を確認する**。古い版が読まれていたら訳は無効。`[Text] JAPANESE: N lines from ...` が出れば読み込み成功。
- 鍵は 1 文字でも違えば当たらない(英語のまま表示される)。文字化けした鍵(`Â·` など、原作側の不具合)もそのまま一致させる。
- 言語が JAPANESE でないと読まれない。各 DLL が自分の INI(`_user.ini` 含む)の `sLanguage` を見る。
- テーマ用フォントは日本語を含まない。同梱の日本語フォントが無い(または原作のフォントが勝つ)と「?」になる。優先順位は 原作 → 本パッチ。
- 折り返しは ASCII スペースのみ。`lang_build.py` が janome で 19 文字以上の行に入れる(`--no-wrap` で無効化)。
- 位置・倍率は原作のレイアウトのまま。窮屈な場所は訳を短くして対応する。
- パーティ設定ページの役割・注目対象・位置取りのドロップダウンは、原作がメッセージの一覧を通していないため英語のまま(Fight With Me と共通の画面)。
