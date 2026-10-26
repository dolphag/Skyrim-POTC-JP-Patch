# Path of the Companions - Japanese Translations Patch (tools and translation table)

Nexus Mods page: *(not published yet; the link will be added here)*

Sister patches: Fight With Me <https://www.nexusmods.com/skyrimspecialedition/mods/194874> (tools: <https://github.com/dolphag/Skyrim-Fight-With-Me-Japanese-translations-patch>), Walk With Me <https://www.nexusmods.com/skyrimspecialedition/mods/194872> (tools: <https://github.com/dolphag/Skyrim-Walk-With-Me-Japanese-translations-patch>)

[日本語は下](#日本語)

Scripts and the translation table for the Japanese translation patch for
[Path of the Companions](https://www.nexusmods.com/skyrimspecialedition/mods/196635) (Paths) **1.0.0** by **hashhbbrown** (GitHub: fatalCMD).
Fight With Me is an optional companion of Paths, not a prerequisite; it has its own patch.
The original keeps its messages in external text files (`SKSE/Plugins/FightWithMe/Translations/`); the patch is the Japanese version of those files, so no DLL is changed.
The patch files are distributed **only on Nexus Mods**, following the permissions on the original page.
**This repository is source code only: it contains no files of the original mod, no distribution zips and no fonts**:
only the scripts that build the Japanese message file, and the English → Japanese table.

## Credits
- **Path of the Companions** and **Fight With Me**: created by **hashhbbrown** (GitHub: [fatalCMD](https://github.com/fatalCMD)). All original strings, perk trees and game design belong to the author.
  - Path of the Companions: <https://www.nexusmods.com/skyrimspecialedition/mods/196635>
  - Fight With Me: <https://www.nexusmods.com/skyrimspecialedition/mods/194766>
  - Source (declared GPL-3.0-or-later): <https://github.com/fatalCMD/potc>
- Japanese translation, tools: dolphag (with AI assistance, see Notes).
- Japanese UI font (bundled in the distribution zip, not in this repository): based on Noto Sans JP (Copyright 2014-2021 Adobe), SIL Open Font License 1.1, internal name changed.

## Files
- `translations_en_ja.csv`: all string pairs (1099). The English column is the original author's and is not covered by the license of this repository.
- `tools/lang_build.py`: builds `FightWithMePaths_JAPANESE.txt` from the original zip and the table, with checks (missing translations, format fields, kanji range).
- `tools/make_zip.py`: test and distribution zips (the distribution zip bundles the font). `tools/make_font_pack.py`: renames and copies an OFL Japanese font under the three theme font names (the font itself is supplied by the user and not committed).
- `release/`: README templates and the Nexus text. `docs/`: findings about the original (format, fonts, packaging), glossary, a draft report for the original author (not sent).

## Versions
Patch versions follow Path of the Companions: **1.0.0-1** is for Paths 1.0.0.
Recommended for users: Japanese enabled in `SKSEMenuFramework.ini` (`EnableJapanese = true`), plus `EnableChinese = true` (SMF v3.18+) for kanji outside the Japanese glyph range in game-supplied strings. A Japanese UI font is bundled in the distribution zip, because the original's theme fonts have no Japanese glyphs.

## How it works (short)
The original reads `*_<LANGUAGE>.txt` (one line per message: English, a tab, the translation) from the folder and replaces the English by the translation when the language is `JAPANESE` (`sLanguage` in Skyrim.ini, or in the plugin INI). Paths ships two English lists: `FightWithMePaths_ENGLISH.txt` (trees, abilities, traits) and `FightWithMe_ENGLISH.txt` (shared panel and settings texts that the Paths DLL also uses; the original README documents this). The patch merges both into one `FightWithMePaths_JAPANESE.txt`, so it does not depend on, or collide with, the Fight With Me patch (files are read in file-name order; `FightWithMePaths_` comes before `FightWithMe_`, so the Fight With Me patch wins for shared texts).
Long Japanese lines get ASCII spaces at phrase boundaries (janome), because the UI wraps only at spaces. The build fails if a translation uses a kanji outside the glyph range (`tools/jp_kanji.txt`; such kanji would show as "?").

## Reproduce (Python 3.11+, `pip install -r requirements-dev.txt`)
```
python3 -I tools/lang_build.py --paths "<Path of the Companions zip>" --out out/ja
python3 -I tools/make_font_pack.py --font NotoSansJP-Medium.ttf --license OFL.txt --out out/font
python3 -I tools/make_zip.py release out/ja --font-dir out/font --version 1.0.0-1
```

## Notes
- The role / focus / position dropdowns on the Party settings page (shared with Fight With Me) are not read from the message files by the original, so they stay English (`docs/upstream-report-draft.md`).
- Log lines, key names and theme names are intentionally left in English.
- Translations were produced with AI assistance (Claude, Anthropic) and checked in game.
- The scripts and the Japanese column of the table are provided under GPL-3.0-or-later, as stated in [`LICENSE`](LICENSE). The English column reproduces strings of Path of the Companions, which belong to their author; it is included only so that the patch can be reproduced.
- This repository was split off from the Fight With Me patch repository, where the 0.5.0-era work on both mods was done; the history up to the split is there.

## 日本語
Nexus Mods のページ: (公開後にリンクを追記します)

姉妹MODのパッチ: Fight With Me <https://www.nexusmods.com/skyrimspecialedition/mods/194874>(ツール: <https://github.com/dolphag/Skyrim-Fight-With-Me-Japanese-translations-patch>)、Walk With Me <https://www.nexusmods.com/skyrimspecialedition/mods/194872>(ツール: <https://github.com/dolphag/Skyrim-Walk-With-Me-Japanese-translations-patch>)

[Path of the Companions](https://www.nexusmods.com/skyrimspecialedition/mods/196635)(Paths)**1.0.0** の日本語化パッチのスクリプトと翻訳表です。原作者は **hashhbbrown**(GitHub: fatalCMD)。
Fight With Me は Paths の任意の連携先で、前提ではありません(Fight With Me には別のパッチがあります)。
原作はメッセージを外部のテキストファイル(`SKSE/Plugins/FightWithMe/Translations/`)に分けています。本パッチはその日本語版で、DLL は変更しません。
パッチのファイルは、原MODページの権限表示に従い、**Nexus Mods でのみ配布**します。
**このリポジトリはソースコードのみです。原MODのファイル、配布用の zip、フォントは含みません**。日本語のメッセージファイルを作るスクリプトと、英日対応表だけを置いています。

### クレジット
- **Path of the Companions** と **Fight With Me**: **hashhbbrown**(GitHub: [fatalCMD](https://github.com/fatalCMD))作。原作のすべての文言・ツリー・ゲームデザインは原作者のものです。
  - Path of the Companions: <https://www.nexusmods.com/skyrimspecialedition/mods/196635>
  - Fight With Me: <https://www.nexusmods.com/skyrimspecialedition/mods/194766>
  - ソース(GPL-3.0-or-later と宣言されています): <https://github.com/fatalCMD/potc>
- 日本語訳・ツール: dolphag(AI の支援あり。上の Notes を参照)。
- 日本語フォント(配布 zip に同梱。このリポジトリには含みません): Noto Sans JP(Copyright 2014-2021 Adobe)を元に、内部の名前を付け替えたもの。SIL Open Font License 1.1。

### ファイル
- `translations_en_ja.csv`: 英日の全組(1099)。英語の列は原作者のもので、このリポジトリのライセンスの対象外です。
- `tools/lang_build.py`: 原作の zip と対応表から `FightWithMePaths_JAPANESE.txt` を作ります(未訳・書式欄・漢字範囲の検査つき)。
- `tools/make_zip.py`: テスト版と配布用の zip(配布用にはフォントを同梱)。`tools/make_font_pack.py`: OFL の日本語フォントを、テーマ用フォントの 3 つの名前で書き出します(フォント本体は利用者が用意し、コミットしません)。
- `release/`: README の雛形と Nexus 用文面。`docs/`: 原作の調査(形式・フォント・同梱)、用語集、原作者向け報告の文案(未送信)。

### 版
パッチの版は Path of the Companions に連動します。**1.0.0-1** は Paths 1.0.0 用です。
利用者への推奨: `SKSEMenuFramework.ini` で日本語を有効にする(`EnableJapanese = true`)。ゲーム由来の文字列の、日本語範囲外の漢字には `EnableChinese = true`(SMF v3.18 以降)。日本語フォントは配布 zip に同梱します(原作のテーマ用フォントは日本語を含まないため)。

### しくみ(短く)
原作は、フォルダ内の `*_<言語名>.txt`(1 行 = 英語、タブ、訳)を読み、言語が `JAPANESE` のとき(Skyrim.ini またはプラグインの INI の `sLanguage`)英語を訳に置き換えます。Paths の zip には英語の一覧が 2 つ入っています。`FightWithMePaths_ENGLISH.txt`(ツリー・アビリティ・特性)と、`FightWithMe_ENGLISH.txt`(Paths の DLL も使う共通のパネル・設定の文言。原作の README にも書かれています)。本パッチはその両方を 1 本の `FightWithMePaths_JAPANESE.txt` にまとめるので、Fight With Me 用パッチに依存せず、ファイル名も衝突しません(ファイル名順に読まれ、`FightWithMePaths_` が `FightWithMe_` より先なので、共通の文言は Fight With Me 用パッチが優先されます)。
画面は半角スペースでしか折り返さないため、長い日本語には文節の切れ目に半角スペースを入れます(janome)。範囲外の漢字を使うと(「?」になるため)ビルドが失敗します(`tools/jp_kanji.txt`)。

### 再現(Python 3.11+、`pip install -r requirements-dev.txt`)
上の「Reproduce」を参照してください。

### 補足
- パーティ設定ページの、役割・注目対象・位置取りのドロップダウン(Fight With Me と共通の画面)は、原作がメッセージのファイルを通していないため、英語のままです(`docs/upstream-report-draft.md`)。
- ログ・キー名・テーマ名は、意図的に英語のままにしています。
- 訳文は AI(Claude, Anthropic)の支援で作り、ゲーム内で確認しています。
- スクリプトと翻訳表の日本語の列は GPL-3.0-or-later です([`LICENSE`](LICENSE))。英語の列は Path of the Companions の文言で、原作者のものです。パッチを再現できるようにするためだけに含めています。
- このリポジトリは、Fight With Me のパッチのリポジトリから分けたものです。分離までの履歴(両 MOD の 0.5.0 / 1.0 期の作業)は、そちらにあります。
