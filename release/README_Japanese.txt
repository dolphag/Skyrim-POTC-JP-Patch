Path of the Companions - Japanese Translations Patch 1.0.0-2 (対象: Path of the Companions 1.0.0)
=====================================================================
Path of the Companions 1.0.0 を日本語化するパッチです。原作がメッセージを外部のテキストファイルに分けて読み込んでいるので、その日本語版を置きます。DLL は変更しません(ファイルを置くだけです)。
原MOD:
- Path of the Companions (Paths)  https://www.nexusmods.com/skyrimspecialedition/mods/196635
- Fight With Me(任意の連携先)  https://www.nexusmods.com/skyrimspecialedition/mods/194766
原作者: hashhbbrown (GitHub: fatalCMD)

■ 必須
- Path of the Companions 1.0.0 と、POTC Effects 1.0.21 以上(原作の必須ファイル)
- SKSE Menu Framework 3(日本語を表示する設定を含む)。SKSEMenuFramework.ini の [Fonts] で EnableJapanese = true、PrimaryFont = NotoSansJP-Medium.ttf など。
  日本語環境を導入済みなら追加の設定は不要です。作者は 2game 様の日本語化ファイルで動作を確認しています。
  https://skyrimspecialedition.2game.info/detail.php?id=120352
- 日本語フォント: 本パッチに同梱しています(下の「日本語フォント(同梱)」を参照)。

■ 日本語フォント(同梱)
原作の画面は、日本語の字形を持たないテーマ用フォント(Lora / Spectral / BarlowSemiCondensed)で描かれるため、そのままだと日本語が「?」になります。
本パッチには、同じ名前の日本語対応フォント(Noto Sans JP を元にしています。SIL OFL。全文は FONT-LICENSE.txt)が入っていて、原作のフォントを置き換えます。
MOD の優先順位は「原作 → 本パッチ」の順にして、フォントが原作のフォントに勝つようにしてください。英字の見た目も、このフォントに変わります。
自分のフォントを使いたい場合は、本パッチの SKSE/Plugins/Fonts/ の3つのファイルを無効にし、日本語対応の TTF を同じ3つの名前で置いてください。
Fight With Me の日本語化パッチにも同じフォントが入っています(同一のファイルなので、両方入れても問題ありません。上書きの確認が出たら、どちらを選んでも同じです)。

■ Fight With Me を併用する場合(任意)
Paths は Fight With Me(0.5.0)がなくても動きます。併用するときは、Fight With Me 用の日本語化パッチ(別ページ)も入れてください。バトルプランなど、Fight With Me の画面が日本語になります。
この zip の訳にも、Fight With Me の画面の文言の大部分が含まれています。両方を入れても問題ありません(共通の文言は、Fight With Me 用パッチのほうが後に読まれて優先されます)。

■ 推奨
- SKSEMenuFramework.ini の [Fonts] で EnableChinese = true を設定(SMF v3.18 以降)。
  魔法名・従者名など、ゲームや他の MOD から取得する文字列は本パッチでは変更できず、日本語グリフ範囲外の漢字が「?」になります。
- 姉妹MODの日本語化パッチ: Walk With Me - Japanese Translations Patch  https://www.nexusmods.com/skyrimspecialedition/mods/194872

■ 日本語にならないとき
言語は、ゲームの設定(Skyrim.ini の sLanguage)に従います。JAPANESE のときは FightWithMePaths_JAPANESE.txt、ENGLISH のとき(英語版ゲームのまま日本語化している環境など)は、同じ内容の FightWithMe_JA_Paths_ENGLISH.txt が読まれます。どちらも、ファイルを置くだけで日本語になります。
それ以外の言語名(FRENCH など)のときは、次のファイルに書いてください(無ければ新規作成。反映はゲームの再起動後)。
  SKSE/Plugins/FightWithMePaths_user.ini(Paths 用)
  Fight With Me も使う場合は、SKSE/Plugins/FightWithMe_user.ini にも同じ内容を書いてください(DLL ごとに別々に読みます)。
      [Interface]
      sLanguage = JAPANESE
この設定が効くのは、Path of the Companions の画面の文言だけです。SKSE Menu Framework 全体や、ゲーム本体の言語、魔法名などのゲーム由来の文字列には影響しません。
SKSE のログ(Documents/My Games/Skyrim Special Edition/SKSE)に「[Text] JAPANESE: N lines from ...」(ENGLISH のときは「[Text] ENGLISH: ...」)と出ていれば、日本語のファイルは読まれています。
この行が無い、または「no translation files, so English」なら、ファイルの置き場所を確認してください。

■ 導入
MOD として入れてください(MO2・Vortex など)。置かれるファイルは次のとおりです。
SKSE/Plugins/FightWithMe/Translations/FightWithMePaths_JAPANESE.txt    Paths のツリー・アビリティ・特性・パネル・設定・通知の文言
SKSE/Plugins/FightWithMe/Translations/FightWithMe_JA_Paths_ENGLISH.txt    上と同じ内容(言語名が ENGLISH のときに読まれる)
SKSE/Plugins/Fonts/Lora-SemiBold.ttf, Spectral-SemiBold.ttf, BarlowSemiCondensed-SemiBold.ttf    日本語対応フォント(原作の同名のフォントを置き換えます)
FONT-LICENSE.txt    フォントのライセンス(SIL OFL)
ファイルを置くだけで、DLL・INI・セーブには影響しません。無効にすれば元に戻ります。
原作を更新するときは、パッチを外す必要はありません。ただし、新しく増えた文言は英語のまま表示されます(パッチの更新をお待ちください)。
本体とパッチのバージョンは合わせてください。バージョン番号は原則として本体と同じで、パッチだけを修正したときは x.x.x-1 のように枝番をつけます。

訳文ファイルの SHA-256:
  FightWithMePaths_JAPANESE.txt  {SHA_JA}

■ 日本語にならないもの
- パーティ設定ページの、役割・注目対象・位置取りのドロップダウン(選択肢と、その説明のホバー表示)。Fight With Me と共通の画面で、原作のこの部分がメッセージのファイルを通していないため、英語のままです(原作側の修正が必要です)。
- テーマ名(Vanilla / Oxblood / Nordic)は、原文のままにしています。
- キー名・ボタン表示(Tab / Esc など)、ログ、INI のコメント。
- ゲームや他の MOD から取得する文字列(魔法名、従者名など)。
- 原作の更新で増えた文言(パッチの更新まで英語)。
「スキル」は、バニラのスキルと混同しないよう、Paths のものは「アビリティ」に統一しています。
アビリティ名は公式日本語訳に合わせています(例: 武装解除)。新しいアビリティ名(ケイオスダウン、最後の砦、風渡り、爆裂矢 など)は意訳を含み、一部は暫定です。ご意見をお寄せください。
訳文は、SKSE Menu Framework の日本語グリフ範囲(約3000字)内の漢字だけで書いています。

■ 権利・ソース・クレジット
原作者: hashhbbrown (GitHub: fatalCMD)。原作のすべての文言・ツリー・ゲームデザインは原作者のものです。
本パッチは、Path of the Companions の Nexus ページの権限表示(2026-10-26 にユーザーが確認: 改変・素材の利用・他サイトへの転載は作者のクレジット表記で可)に従って作った非公式の翻訳です。
本パッチに、原作のファイル(DLL・画像など)は含まれません。含まれるのは、原作の英語の文言(メッセージのファイルの左側)と、日本語訳、日本語フォントです。
本パッチは Nexus Mods の翻訳ページでのみ配布します。他サイトへの転載はご遠慮ください。
GitHub にはソースコード(生成スクリプトと翻訳表)のみを置き、配布用のファイルやフォントは置いていません。
原作者に本パッチの不具合を問い合わせないでください。作者から削除の依頼があれば速やかに対応します。無保証です。
原作のソース(GPL-3.0-or-later と宣言されています): https://github.com/fatalCMD/potc
パッチの生成スクリプトと翻訳表: https://github.com/dolphag/Skyrim-POTC-JP-Patch (版ごとにタグがあります)
日本語訳と生成スクリプトは GPL-3.0-or-later です。英語の列は原作者のもので、この対象ではありません。
日本語フォント(本パッチに同梱)は、Noto Sans JP(Copyright 2014-2021 Adobe)を元に、内部の名前を付け替えたものです。SIL Open Font License 1.1。全文は FONT-LICENSE.txt にあります。

■ AIの利用
訳文と本説明文の作成にAI(Claude, Anthropic)を使用しています。
ゲーム内で確認していますが、見落としがあるかもしれません。誤訳や表示崩れがあれば、Nexus のコメントでお知らせください。

■ 謝辞
素晴らしいMODを公開してくださっている原作者 hashhbbrown さんに心から感謝します。
日本語でも楽しめるようにと、感謝を込めて作った非公式の翻訳です。

■ 更新履歴
1.0.0-2: 英語設定(sLanguage=ENGLISH)のまま日本語化している環境でも、ファイルを置くだけで日本語になるようにした(言語名が ENGLISH のときに読まれる、同じ内容のファイルを追加)。
1.0.0-1: 初版。Path of the Companions 1.0.0 用。ツリー・アビリティ・特性・ガイド・設定・通知を日本語化。
