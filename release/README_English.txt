Path of the Companions - Japanese Translations Patch 1.0.0-1 (for Path of the Companions 1.0.0)
=====================================================================
A Japanese translation for Path of the Companions 1.0.0. The original keeps its messages in external text files; this patch is the Japanese version of those files, so no DLL is changed (just files to place).
Original mods:
- Path of the Companions (Paths)  https://www.nexusmods.com/skyrimspecialedition/mods/196635
- Fight With Me (optional companion)  https://www.nexusmods.com/skyrimspecialedition/mods/194766
Original author: hashhbbrown (GitHub: fatalCMD)

Requirements
- Path of the Companions 1.0.0 and POTC Effects 1.0.21 or newer (required by the original)
- SKSE Menu Framework 3 with Japanese enabled: [Fonts] EnableJapanese = true, PrimaryFont = NotoSansJP-Medium.ttf (or similar) in SKSEMenuFramework.ini.
- A Japanese font: included in this patch (see "Japanese font (included)" below).

Japanese font (included)
The original draws its screens with theme fonts (Lora / Spectral / BarlowSemiCondensed) that have no Japanese glyphs, so Japanese would show as "?".
This patch includes a Japanese-capable font under the same names (based on Noto Sans JP, SIL OFL; full text in FONT-LICENSE.txt); it replaces the original's fonts.
Mod order: original -> this patch, so the font wins over the original's fonts. Latin letters will look different too.
To use your own font, disable the three files in SKSE/Plugins/Fonts/ of this patch and put a Japanese-capable TTF under the same three names.
The Fight With Me Japanese patch contains the same font (identical files, so having both is fine; if you are asked to overwrite, either choice is the same).

If you also use Fight With Me (optional)
Paths works without Fight With Me 0.5.0. If you use both, install the Fight With Me Japanese patch (a separate page) too, so Fight With Me's own screens (battle plan, ...) are translated.
This patch already contains most of Fight With Me's screen texts; having both is fine (for shared texts the Fight With Me patch is read later and wins).

Recommended: [Fonts] EnableChinese = true (SMF v3.18+), so kanji outside the Japanese glyph range in game-supplied strings (spell and companion names) do not show as "?".

If it stays English
The language follows the game (sLanguage in Skyrim.ini); the file is read when it is JAPANESE. If your game is not set to JAPANESE, add this to SKSE/Plugins/FightWithMePaths_user.ini (create it if missing; restart the game). If you also use Fight With Me, put the same in SKSE/Plugins/FightWithMe_user.ini (each DLL reads its own):
    [Interface]
    sLanguage = JAPANESE
The SKSE log should show "[Text] JAPANESE: N lines from ..." if the file was read.

Install
Install as a mod (MO2, Vortex, ...). Files placed:
SKSE/Plugins/FightWithMe/Translations/FightWithMePaths_JAPANESE.txt    the Paths trees, abilities, traits, panel, settings and notices
SKSE/Plugins/Fonts/Lora-SemiBold.ttf, Spectral-SemiBold.ttf, BarlowSemiCondensed-SemiBold.ttf    a Japanese-capable font (replaces the original fonts of the same names)
FONT-LICENSE.txt    the font's license (SIL OFL)
No DLL, INI or save is touched; disable it to go back to English.
When the original updates you do not have to remove the patch, but new texts stay in English until the patch is updated. Keep versions matched: the version follows the original, with a suffix (x.x.x-1) for patch-only fixes.

SHA-256 of the text file:
  FightWithMePaths_JAPANESE.txt  {SHA_JA}

What is not in Japanese
- The role / focus / position dropdowns on the Party settings page (the choices and their hover tooltips). This screen is shared with Fight With Me, and the original does not read these texts from its external message files, so they stay English until it is fixed upstream.
- Theme names (Vanilla / Oxblood / Nordic) are kept as in the original.
- Key names and button labels (Tab, Esc, ...), logs, INI comments.
- Strings that come from the game or other mods (spell and companion names).
- Texts the original added after this version.

Rights, source and credits
Original author: hashhbbrown (GitHub: fatalCMD). All original strings, trees and game design belong to the author.
This unofficial translation follows the permissions shown on the Path of the Companions page (checked by the user on 2026-10-26: modification, asset use and uploading to other sites allowed with credit).
This patch contains no file of the originals (no DLL or images), only the original's English strings (the left column of the message file), the Japanese translation and a Japanese font.
Distributed on Nexus Mods only, as a translation page. Please do not re-upload it. GitHub holds only the source (scripts and the translation table), not this file or the font.
Please do not contact the original author about problems with this patch. It will be removed promptly if the author asks. No warranty.
Original source (declared GPL-3.0-or-later): https://github.com/fatalCMD/potc
Scripts and translation table: https://github.com/dolphag/Skyrim-POTC-JP-Patch
The Japanese translation and scripts are GPL-3.0-or-later; the English column is the original author's and is not covered.
The Japanese font (included) is based on Noto Sans JP (Copyright 2014-2021 Adobe) with its internal names changed; SIL Open Font License 1.1, full text in FONT-LICENSE.txt.

AI disclosure
The translation and this text were made with AI assistance (Claude, Anthropic). Checked in game, but mistakes may remain; please report them in the Nexus comments.

Changelog
1.0.0-1: First release, for Path of the Companions 1.0.0 (trees, abilities, traits, guide, settings and notices translated).
