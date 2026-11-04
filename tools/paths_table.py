# -*- coding: utf-8 -*-
"""Paths の英日対照表(PATHS_TABLE.md)を作る。

使い方:
  python3 -I tools/paths_table.py --src <fatalCMD/potc の clone> [--csv translations_en_ja.csv] > PATHS_TABLE.md

読むもの:
- ノードの構造(種別・段・最大ランク)と数値: 原作の公開ソース include/FWM/Paths.h、src/Paths.cpp(Primary / Secondary)。
  **公開ソースは 1.0.0 時点で、配布版 1.2.0 より古い**(スカルドは無い)。数値は 1.0.0 のもの。
- 日本語名: translations_en_ja.csv(正本)。
- 効果の日本語の要約: このファイルの EFFECTS(自分の言葉で書いたもの。原作の英文は写さない)。
- スカルド(1.2.0 で追加)は公開ソースに無いので、文言の一覧(CSV)から名前と効果だけを SKALD に手で書いている。
  段・ランク・数値は未確認。

英語名のうち、CSV に無いものがあれば失敗する(版が変わって名前が変わった合図)。
"""
import argparse
import csv
import os
import re
import sys

ap = argparse.ArgumentParser()
ap.add_argument('--src', required=True, help='fatalCMD/potc の作業コピー')
ap.add_argument('--csv', default=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'translations_en_ja.csv'))
args = ap.parse_args()

JA = {r[0]: r[1] for r in list(csv.reader(open(args.csv, encoding='utf-8-sig')))[1:] if len(r) >= 2}


def ja(en):
    if en not in JA:
        sys.exit('CSV に無い英語名: %r(版が変わった可能性)' % en)
    return JA[en].replace(' ', '')


# ---------- 原作の公開ソースを読む ----------
header = open(os.path.join(args.src, 'include/FWM/Paths.h'), encoding='utf-8').read()
cpp = open(os.path.join(args.src, 'src/Paths.cpp'), encoding='utf-8').read()


def parse_ranks(fn_name):
    """Primary / Secondary の switch を読み、{Perk名: (r1, r2, r3)} にする。"""
    start = cpp.index('Ranks %s(Perk a_perk)' % fn_name)
    end = cpp.index('Ranks Secondary(Perk a_perk)') if fn_name == 'Primary' else cpp.index('constexpr std::array<std::string_view, 4> kTiers')
    body = cpp[start:end]
    out, labels = {}, []
    for line in body.splitlines():
        for m in re.finditer(r'case Perk::(\w+):', line):
            labels.append(m.group(1))
        m = re.search(r'return\s*\{([^}]*)\}', line)
        if m:
            vals = []
            for tok in m.group(1).split(','):
                tok = tok.strip()
                if not tok:
                    continue
                if tok.startswith('ArrowArtsFx::Damage'):
                    # include/FWM/ArrowArtsFx.h: Damage = {24, 36, 50}
                    vals.append({'1': 24.0, '2': 36.0, '3': 50.0}[re.search(r'\((\d)\)', tok).group(1)])
                else:
                    vals.append(float(re.sub(r'f$', '', tok)))
            for lab in labels:
                out[lab] = tuple(vals) if vals else (0, 0, 0)
            labels = []
        elif 'default:' in line:
            labels = []
    return out


PRIMARY = parse_ranks('Primary')
SECONDARY = parse_ranks('Secondary')


def fmt(x):
    return ('%g' % x)


def V(perk, secondary=False, scale=1.0, n=3):
    """ランク I/II/III の値を「a/b/c」にする。"""
    t = (SECONDARY if secondary else PRIMARY)[perk]
    vals = [fmt(x * scale) for x in t[:n]]
    return '/'.join(vals)


# 公開ソースの Paths.h からノードの構造を読む
ROLES = [('Fighter', 'Path of the Blade'), ('Tank', 'Path of the Shield'), ('Healer', 'Path of the Mender'),
         ('Bruiser', 'Path of the Hammer'), ('Archer', 'Path of the Arrow'), ('Mage', 'Path of the Storm')]
LEADS = re.findall(r'\{ "(Path of the \w+)", "([^"]+)" \}', header)
LEAD = dict(LEADS)
body = header[header.index('inline constexpr std::array<Path, kRoles> paths{'):]
body = body[:body.index('[[nodiscard]] constexpr const Path& PathOf')]
parts = re.split(r'// (?:Fighter|Tank|Healer|Bruiser|Archer|Mage): the \w+', body)[1:]
assert len(parts) == 6, len(parts)
call = re.compile(r'detail::([ABTCE])\(([^)]*)\)')


def split_args(s):
    return [a.strip().strip('"') for a in re.split(r',\s*(?=(?:[^"]*"[^"]*")*[^"]*$)', s)]


# ---------- 効果の要約(日本語、数値は I/II/III) ----------
# (効果, 再使用時間)。再使用時間は src/Paths.cpp の Cooldown() の値(1.0.0)。
# ソース以外に数値を持つもの(DragonBreath.h、MoonFx.h、WindstepFx.h、RiposteFx.h、Blast.h、RejuvenatePolicy.h、
# ArrowArtsFx.h)は、そのファイルの値を直に書いている。
EFFECTS = {
    # --- ファイター ---
    'kDisarm': ('敵の武器を叩き落とす。自分より最大 %s レベル上の敵まで有効' % V('kDisarm'), '40/35/30秒'),
    'kDisarmExpose': ('武装解除した敵の防御力が10秒間 -%s' % V('kDisarmExpose'), ''),
    'kDisarmSweep': ('武装解除と同時に、敵を転倒させる', ''),
    'kSecondWind': ('戦闘中に息を整え、体力 %s%% とスタミナ %s%% を回復' % (V('kSecondWind'), V('kSecondWind', True)), '60秒(不屈で短縮)'),
    'kSecondWindResolve': ('使用後10秒間、防御力 +%s' % V('kSecondWindResolve'), ''),
    'kSecondWindUnyielding': ('立て直しの再使用時間が %s 秒短くなる' % V('kSecondWindUnyielding'), ''),
    'kRiposte': ('最長 %s 秒間、次の近接攻撃に備えて構え、受けると攻撃者を反撃で 1.5/2.5/3.5 秒倒れさせ、着地時に武器の基本ダメージの 0.5/1.0/1.5 倍を与える' % V('kRiposte'), '30秒'),
    'kRiposteCounter': ('反撃が、ノックバックの前に武器の基本ダメージの %s 倍も与える' % V('kRiposteCounter'), ''),
    'kRiposteDisarming': ('最初にいなした攻撃の相手の武器も落とす(奪える武器のみ)', ''),
    'kSpectralWolf': ('標的の正面に立っているときだけ。狼の霊の頭が現れて噛みつき、武器ダメージの %s 倍を与えて %s 秒固まらせ、体力の %s%% を 8 秒かけて出血させる(ボスは出血が半分)' % (V('kSpectralWolf'), '2.5/2.5/3.3', V('kSpectralWolf', True)), '40秒'),
    'kWolfMaul': ('狼に捕らえられた相手が、1.5 秒長く固まる', ''),
    'kWolfHemorrhage': ('狼の傷口からの出血が、同じ勢いで %s 秒長く続く' % V('kWolfHemorrhage'), ''),
    'kFlanker': ('相手の側面に回り込み、与ダメージ +%s%%' % V('kFlanker'), ''),
    'kEndurance': ('戦闘中のスタミナ回復 +%s%%' % V('kEndurance'), ''),
    'kOpportunist': ('ひるんだ/武器を落とした相手への与ダメージ +%s%%' % V('kOpportunist'), ''),
    # --- タンク ---
    'kTaunt': ('射程内の敵すべてを挑発。捕まえた敵は %s 秒間、自分に襲いかかる' % V('kTaunt'), '16/13/10秒'),
    'kTauntBrace': ('挑発が効いている間、自分の防御力 +%s' % V('kTauntBrace'), ''),
    'kTauntIntimidate': ('挑発で捕まえた敵の与ダメージ -%s%%' % V('kTauntIntimidate'), ''),
    'kBodyguard': ('%s 秒間、本人と本人を攻撃した敵の武器・魔法ダメージが %s%% 減る。敵の弱体化は攻撃後も 8/10/12 秒続く' % (V('kBodyguard', True), V('kBodyguard')), '40秒'),
    'kBodyguardInterpose': ('戦意喪失の持続が %s 秒延びる' % V('kBodyguardInterpose'), ''),
    'kBodyguardRush': ('戦意喪失を受けた敵が、最後の攻撃から 4 秒長く弱体化したままになる', ''),
    'kChaosDown': ('タンクから 250 以内の敵の移動と武器攻撃を %s%% 遅くする(8 秒)。重ねて使っても加算されず、更新される' % V('kChaosDown'), '25秒'),
    'kChaosDownWide': ('ケイオスダウンの範囲 +%s' % V('kChaosDownWide'), ''),
    'kChaosDownLingering': ('ケイオスダウンの減速が %s 秒長く続く' % V('kChaosDownLingering'), ''),
    'kStandFast': ('近く(800 以内)の生存した味方の体力が 25%% 未満になると、8 秒間その守護者になり、近くのパーティが受けるダメージの %s%% を肩代わりする。同時に 1 人まで。吸収したダメージで自分が倒れることもある' % V('kStandFast'), '60秒'),
    'kStandFastUnbroken': ('最後の砦が守る範囲 +%s' % V('kStandFastUnbroken'), ''),
    'kStandFastBreath': ('最後の砦の持続 +%s 秒' % V('kStandFastBreath'), ''),
    'kIronHide': ('戦闘中、防御力 +%s' % V('kIronHide'), ''),
    'kShieldMaster': ('シールドバッシュの頻度が %s 倍になり、盾を構えるのも早くなる' % V('kShieldMaster'), ''),
    'kLastStand': ('戦闘中1度、体力が1/4を下回ると %s%% 回復し、8秒間 防御力 +100' % V('kLastStand'), ''),
    # --- ヒーラー ---
    'kHeal': ('12 秒間続く癒しの光の円を、最も効く場所に作る。円の中のあなた・従者・召喚物が毎秒体力の %s%% を回復し、アンデッドは毎秒 1/1.5/2%% 焼かれる(ボスは半分)。発動時にマジカを使う' % V('kHeal'), '40秒'),
    'kHealInvigorate': ('円の中で、毎秒スタミナも最大値の %s%% 戻る' % V('kHealInvigorate'), ''),
    'kHealWide': ('円の範囲 +%s' % V('kHealWide'), ''),
    'kRenewal': ('射程内の全員が 12 秒間、毎秒 体力の %s%% を回復' % V('kRenewal'), '45秒'),
    'kRenewalRoots': ('癒しの雨の持続 +%s 秒' % V('kRenewalRoots'), ''),
    'kRenewalLifeline': ('癒しの雨の開始時に倒れている者を、体力1/3で即座に立ち上がらせる', ''),
    'kRejuvenate': ('円の中にいる間、毎秒最大マジカの 2/3.5/5%%(毎秒 最大 6/12/20)を回復。持続 %s 秒。重なった円は加算されない' % V('kRejuvenate'), '50/55/60秒'),
    'kRejuvenateWellspring': ('マジカ回復強化の開始時に、近くの味方のマジカを %s%%(最大 30)即時回復。すでに円の中にいる味方には再度かからない' % V('kRejuvenateWellspring'), ''),
    'kRejuvenateVigor': ('マジカ回復強化の間、毎秒スタミナも最大値の %s%%(最大 6)回復' % V('kRejuvenateVigor'), ''),
    'kWard': ('幽体のウィスプマザーが、12/14/16 m 以内のあなたと従者を 10/12/14 秒間祝福し、敵の攻撃が %s%% の確率でダメージ 0 になる。祝福は重複しない' % V('kWard'), '90秒'),
    'kWardShared': ('アズラの月の範囲 +2/4/6 m', ''),
    'kWardSpellward': ('アズラの祝福の持続 +%s 秒' % V('kWardSpellward'), ''),
    'kTriage': ('癒しの円と癒しの雨が、体力1/3未満の者に +%s%% 多く効く' % V('kTriage'), ''),
    'kSerenity': ('戦闘中、自分のマジカ回復 +%s%%' % V('kSerenity'), ''),
    'kGuardianSpirit': ('戦闘中1度、あなたの体力が20%%を下回ると、どこにいても体力の %s%% を即座に回復' % V('kGuardianSpirit'), ''),
    # --- ブルーザー ---
    'kWarCry': ('周囲 %s 以内の敵をひるませる(強さ %s)' % (V('kWarCry'), V('kWarCry', True)), '30秒'),
    'kWarCryRally': ('雄叫びで、周囲800以内の味方のスタミナを %s%% 回復' % V('kWarCryRally'), ''),
    'kWarCryUnnerve': ('ひるませた敵の与ダメージが 8秒間 -%s%%' % V('kWarCryUnnerve'), ''),
    'kBerserk': ('10秒間、与ダメージ +%s%%、チャンスのたびに強攻撃' % V('kBerserk'), '45秒'),
    'kBerserkBloodlust': ('バーサーク中、1キルごとに体力 %s%% 回復し、3秒延長' % V('kBerserkBloodlust'), ''),
    'kBerserkThickSkull': ('バーサーク中、防御力 +%s' % V('kBerserkThickSkull'), ''),
    'kSunder': ('標的の守りを破る一撃。12秒間、標的の防御力 -%s(全員の攻撃が通りやすくなる)' % V('kSunder'), '25秒'),
    'kSunderCrack': ('鎧砕きがひるみ(軽い/中程度/強い)も与える', ''),
    'kSunderShatter': ('鎧砕きが、標的の魔法・炎・冷気・電撃耐性も %s%% 奪う' % V('kSunderShatter'), ''),
    'kEarthshaker': ('地面を叩き、%s 以内の敵を転倒させて武器ダメージの %s 倍を与える。ランクIIIは軽い相手を空中に投げ上げる' % (V('kEarthshaker'), V('kEarthshaker', True)), '40秒'),
    'kEarthshakerAftershock': ('1.5秒後の2度目の揺れが、立っている敵をひるませる', ''),
    'kEarthshakerFault': ('地鳴らしの範囲 +%s' % V('kEarthshakerFault'), ''),
    'kHeavyHands': ('強攻撃の頻度が %s 倍' % V('kHeavyHands'), ''),
    'kMomentum': ('1キルごとに体力 %s%% 回復' % V('kMomentum'), ''),
    'kExecutioner': ('体力30%%未満の敵への与ダメージ +%s%%' % V('kExecutioner'), ''),
    # --- アーチャー ---
    'kVolley': ('標的へ矢を %s 本連射。アーチャーとメイジ全員が %s 秒間その標的を狙う' % (V('kVolley'), V('kVolley', True)), '45秒'),
    'kVolleyRallyFire': ('一斉射撃の間、あなたとパーティの武器ダメージ +%s%%' % V('kVolleyRallyFire'), ''),
    'kVolleyBroadhead': ('一斉射撃の間、標的の防御力 -%s' % V('kVolleyBroadhead'), ''),
    'kDeadeye': ('12秒間、次の弓の一射を強化。矢が着弾点で爆発し、最大 %s の魔法ダメージと、3/3.5/4 m 以内の敵のひるみを与える(距離と魔法耐性で弱まる)' % V('kDeadeye'), '40秒'),
    'kDeadeyeHawkeye': ('爆発の範囲 +%s m' % V('kDeadeyeHawkeye'), ''),
    'kDeadeyePatience': ('爆裂矢の爆発ダメージ +%s%%' % V('kDeadeyePatience'), ''),
    'kPinningShot': ('最大 3/3.5/4 m 退避する。幽体のアーチャーが 4/5/6 秒間、攻撃してくる敵の注意をそらす。%s 秒間 移動速度 +30%%、ランクII/IIIは受けるダメージも 20/30%% 減る。ランクIIIは終わりに周囲をひるませる突風' % V('kPinningShot'), '25秒'),
    'kPinningHeavy': ('風渡りの移動速度上昇と防護の持続 +%s 秒' % V('kPinningHeavy'), ''),
    'kPinningTwin': ('風渡りの移動速度上昇が +30% ではなく +40%', ''),
    'kArrowRain': ('ポータルが前方へ速い矢を放ち、標的の周囲の敵を覆う(魔力の矢で、矢筒は減らない。かすめた矢は半分のダメージ)。本数・時間・範囲は 1.2.0 で変更(数値は未確認)', '50秒'),
    'kArrowRainDownpour': ('矢の雨の本数 +%s' % V('kArrowRainDownpour'), ''),
    'kArrowRainPinning': ('矢の雨に当たった敵すべてがひるむ', ''),
    'kSteadyBreath': ('戦闘中のスタミナ回復 +%s%%' % V('kSteadyBreath'), ''),
    'kFineArrows': ('弓用の矢が無制限(ランクI/II/III: 鋼鉄/エルフ/エボニー)。渡した良い矢はそのまま使う', ''),
    'kSpellTouched': ('矢が %s%% の確率で炎・冷気・電撃を帯び、防がれなければ属性ダメージ +8(耐性で減る)' % V('kSpellTouched'), ''),
    # --- メイジ ---
    'kSurge': ('12秒間、マジカ回復が %s 倍' % V('kSurge'), '40秒'),
    'kSurgeOverflow': ('使用時に、マジカを %s%% 即時回復' % V('kSurgeOverflow'), ''),
    'kSurgeConduit': ('持続中、あなたとパーティのマジカ回復も +%s%%' % V('kSurgeConduit'), ''),
    'kBurst': ('得意な属性(炎・冷気・電撃)の破壊魔法を標的の足元に放つ。範囲 200/280/380、中心のダメージ 24/36/48(ランクI/II/III: アプレンティス/アデプト/エキスパート相当)。ランクIIIは壮大な演出', '30秒'),
    'kBurstSearing': ('命中した敵の炎・冷気・電撃耐性が 12秒間 -%s%%' % V('kBurstSearing'), ''),
    'kBurstTwin': ('2発目が 50% のダメージで続き、近くに別の敵がいればそちらへ', ''),
    'kDragonBreath': ('幽体の竜が属性のブレスを 2.4/2.8/3.2 秒吐き、射程 600/850/1100 の敵に毎秒 %s のダメージ。冷気はスタミナ、電撃はマジカも奪う。ランクIIIは赤いアルドゥイン' % V('kDragonBreath'), '38秒'),
    'kBreathReach': ('ドラゴンブレスの射程 +%s%%(幅も広がる)' % V('kBreathReach'), ''),
    'kBreathLingering': ('ドラゴンブレスの持続 +%s 秒' % V('kBreathLingering'), ''),
    'kMagnus': ('マグナスの力。%s 秒間マジカが尽きない。ランクII/III: 破壊魔法の威力 +15/30%%、ランクIII: 魔法耐性 +50%%' % V('kMagnus'), '120秒'),
    'kArcaneFlow': ('戦闘中、マジカ回復 +%s%%' % V('kArcaneFlow'), ''),
    'kSpellShield': ('魔法耐性 %s%% と、自分に向けられた魔法の %s%% の吸収' % (V('kSpellShield'), V('kSpellShield', True)), ''),
    'kUnravel': ('戦っている間、相手の炎・冷気・電撃耐性を %s%% 下げる' % V('kUnravel'), ''),
}

# 公開ソースに無いスカルド(1.2.0 で追加)。名前と効果は文言の一覧(CSV)から。段・ランク・数値は未確認。
# 分岐 8 つの対応(どのリョードの分岐か)は、文言の並びと意味からの推定。
SKALD = [
    # (種別, English, 効果)
    ('アビリティ', 'Ljodh of Fervor', '地面に広がる波で、味方の攻撃速度を上げる。波が 3/5/10 回当たると効果は 1/1.5/2 倍(8秒間、波が当たるたびに更新)'),
    ('分岐(推定)', 'Spellweave', '魔法の準備動作が短くなる(熱狂のスタックに応じて)'),
    ('分岐(推定)', 'Relentless Rhythm', '強攻撃のスタミナ消費が減る(熱狂のスタックに応じて)'),
    ('アビリティ', 'Ljodh of Echoes', '地面に広がる波で、従者のアビリティ(プレイヤーはシャウト)の再使用の回復を速める。リョードは除く'),
    ('分岐(推定)', 'Encore', '最後の和音が、リョード以外のアビリティの再使用時間を縮める(残響のスタックに応じて)'),
    ('分岐(推定)', 'Inspired Casting', '次に使うリョード以外のアビリティの消費が減る(残響のスタックに応じて。1回の演奏につき1回)'),
    ('アビリティ', 'Ljodh of the Hollow', '地面に広がる波で、敵のダメージを弱める。終曲で1回ひるませる'),
    ('分岐(推定)', 'Leadfoot Verse', '敵を遅くする(虚ろのスタックに応じて)'),
    ('分岐(推定)', 'Broken Concentration', '終曲が、敵の最大マジカの一部を奪う(虚ろのスタックに応じて)'),
    ('アビリティ', 'Ljodh of Glory', '地面に広がる波で、クリティカルダメージとクリティカル率(5%)を上げる(10秒間)'),
    ('分岐(推定)', 'Keen Chorus', 'クリティカル率が上がる(栄光のスタックに応じて)'),
    ('分岐(推定)', 'Victorious Verse', 'クリティカルの一撃が、最大スタミナかマジカの一部を回復する(1秒に1回まで)'),
    ('特性(推定)', 'Spectral Aegis', '演奏中、最大体力の一部までのダメージを吸収する個人用の盾を得る'),
    ('特性(推定)', 'Lingering Verse', '獲得したリョードのスタックの持続が延びる'),
    ('特性(推定)', 'Gift of the Old Tongue', '新しく獲得したスタックが、一定の確率で効果が 2 倍になる(受け手ごとに独立)'),
]

UNLOCK = {0: '最初から', 1: 'レベル35', 2: 'レベル50'}
KIND_JA = {'A': 'アビリティ', 'B': '分岐', 'T': '特性', 'C': 'アビリティ(最上位)'}

out = []
w = out.append
w('# Paths 日本語化 対照表 / Paths Japanese name table\n')
w('Path of the Companions(Paths)**1.2.0** のツリーの、英語名・日本語名・効果の対照表です。')
w('ファイター・タンク・ヒーラー・ブルーザー・アーチャー・メイジの6本(88ノード)に、1.2.0 で加わったスカルドを加えています。')
w('日本語名は日本語化パッチ(1.2.0-1)の表示と同じです。効果は要約で、数値は「ランクI / II / III」の値です(距離はゲーム内単位。約70で1m)。\n')
w('**ご意見・ご要望をお待ちしています**(名前の言い換え案、効果の説明の不足・誤りなど)。GitHub の Issues、または Nexus Mods のコメントでお知らせください。\n')
w('> **数値について**: 原作の公開ソースは 1.0.0 時点のもので、配布版 1.2.0 の数値とは、まだ照合できていません。')
w('> 1.2.0 で変わったとされる点(矢の雨の本数、切り返し、ドラゴンブレスなど)や、表と画面が食い違うところに気づいたら、お知らせください。')
w('> スカルドは公開ソースに無いため、名前と効果の文言だけを載せています(段・ランク・数値は未確認)。\n')

w('## 用語\n')
w('| English | 日本語 | 備考 |\n|---|---|---|')
for e, j, n in [('Path (the tree of a role)', 'ツリー', '役割ごとに1本。「スキルツリー」とは呼ばない(バニラのスキル/パークと紛らわしいため)'),
                ('Ability', 'アビリティ', '戦闘に2つ持ち込む能動スキル。バニラの「スキル」(片手武器など)と区別するため'),
                ('Branch', '分岐', 'アビリティを強化する。元のアビリティのランクを超えられない'),
                ('Trait', '特性', '常時有効'),
                ('Perk / perk points', 'パーク / パークポイント', 'バニラのパークの仕組みに合わせたため、同じ語'),
                ('Capstone(Magnus)', '最上位', 'ほかのすべてのノードを習得すると解放'),
                ('Rank / Mastered', 'ランク / 習熟', ''),
                ('Role', '役割', 'ファイター / タンク / ヒーラー / ブルーザー / アーチャー / メイジ。1.2.0 でスカルドが加わった')]:
    w('| %s | %s | %s |' % (e, j, n))

w('\n## 解放のしくみ\n')
w('- **パークポイント**: 従者は、レベルが10を超えた分、1レベルにつき1ポイントを得る(INI の `iPointsAboveLevel` で変更可)。同じポイントを6本のツリーのどれにも使える。')
w('- **費用**: アビリティはランクI・II・IIIで 1・2・3 ポイント。分岐と特性は1ランクにつき1ポイント。')
w('- **アビリティの解放**: 各ツリーの先頭2つは最初から習得できる。3つ目は従者のレベル **35**、4つ目は **50** が必要。分岐は、そのアビリティのランクを超えられない。')
w('- **特性**: ランクIは最初から、ランクIIはレベル **25**、ランクIIIはレベル **50** が必要。')
w('- **最上位(マグナス)**: レベル50に加えて、メイジのほかのすべてのノードを習得している必要がある。')
w('- 旧版(Paths 0.1.0)にあった「ツリーに5/10ポイント使うと次の段が開く」は、レベルによる解放に変わっています。\n')

w('## 命名メモ\n')
w('- **やり込め**(Unnerve)、**解きほぐし**(Unravel)、**結集する雄叫び**(Rallying Roar)など、日本語で定着した訳語がある語は、それに合わせています。「咆」「哮」はゲームのフォントに無いため、「雄叫び」にしています。')
w('- ウォークライ(War cry)、シャウト名と共通のアビリティ名は、Fight With Me 本体と共通の表記です。')
w('- 役割名(ファイター/タンク/ヒーラー/ブルーザー/アーチャー/メイジ)は Fight With Me 本体の表記です。ツリー名は「〜の道」で、「槌の道」(Path of the Hammer)は暫定です。')
w('- 「カイナレスの顎」(Kynareth\'s Maw)の「カイナレス」は、公式の表記を未確認です。「リョード」(Ljodh)の読みも暫定です。\n')

total = 0
for (role_en, title_en), part in zip(ROLES, parts):
    w('## %s (%s) / %s(%s)\n' % (ja(title_en), title_en, ja(role_en), role_en))
    w(ja(LEAD[title_en]) + '\n')
    w('| 種別 | English | 日本語 | 解放 | 効果 | 再使用 |\n|---|---|---|---|---|---|')
    for kind, a in call.findall(part):
        if kind == 'E':
            continue
        al = split_args(a)
        perk = al[0].replace('Perk::', '')
        if kind in 'AC':
            # A(perk, ability, tier, name, glyph) / C(perk, ability, cost, step, name, glyph)
            tier = int(al[2]) if kind == 'A' else 2
            name, most = al[3] if kind == 'A' else al[4], 3
        elif kind == 'B':
            tier, most, name = int(al[2]), int(al[3]), al[4]
        else:  # T(perk, tier, name, glyph)
            tier, most, name = int(al[1]), 3, al[2]
        if perk not in EFFECTS:
            sys.exit('EFFECTS に無いノード: %s(%s)' % (perk, name))
        eff, cd = EFFECTS[perk]
        if kind == 'T':
            unlock = 'I: 最初から / II: Lv25 / III: Lv50'
        elif kind == 'C':
            unlock = 'レベル50 + ほかの全ノード'
        else:
            unlock = UNLOCK[tier]
            if kind == 'A' and tier == 0:
                unlock = '最初から'
        label = KIND_JA[kind]
        if kind == 'A' and tier == 0:
            label += '(初期)'
        if kind == 'B' and most == 1:
            label += '(ランク1のみ)'
        w('| %s | %s | **%s** | %s | %s | %s |' % (label, name, ja(name), unlock, eff, cd or '―'))
        total += 1
    w('')

w('## スカルド (Path of the Skald) / スカルド(Skald)\n')
w('1.2.0 で加わった、リュートを使う支援役。解放には、従者がリュートを持っていることと、10 ポイントが必要です(解放後も、リュートは所持品に残ります)。')
w('スカルドは役割の一つとして割り当て、専用のツリー(スカルドの道)を持ちます。従者の画面に解放ボタンが出ます。')
w('**この節は公開ソースに無いため、文言の一覧から書いています。** 段・ランク・数値・再使用時間は未確認で、4アビリティ・分岐8・特性3という形と名前の順序は、配布版 DLL 内の文字列の並び(他のツリーと同じ、アビリティ→分岐→特性の順)で確かめました。「(推定)」は、効果の文をどの名前に当てたかが、文言の並びと意味からの割り当てであることを示します。\n')
w('| 種別 | English | 日本語 | 効果 |\n|---|---|---|---|')
for kind, en, eff in SKALD:
    w('| %s | %s | **%s** | %s |' % (kind, en, ja(en), eff))
w('')
w('関連する名前: スカルド(Skald)、単音(Single Note: 狙った相手にリュートの波動を放ち、移動を1秒間30%遅くする基本の動作)、リョード(Ljodh)、スタック(stack)、終曲(finale)、最後の和音(final chord)。\n')

w('---\n')
w('英語名は Path of the Companions の表示文字列です(原作者 hashhbbrown に帰属)。日本語名・効果の要約は日本語化パッチの作者による訳・要約で、GPL-3.0-or-later です。')
sys.stdout.write('\n'.join(out) + '\n')
sys.stderr.write('ノード %d 件(スカルド除く)\n' % total)
