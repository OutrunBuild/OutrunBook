# Rounds 6–8 — final review cycle and exit

Scope: all 13 diagrams (`assets/diagrams/`, baked SVGs are the reader-facing artifacts). Rounds 1–2 ran in a previous session; rounds 3–5 are reported in `round3-report.md` / `round4-report.md`.

## Round 6 — full independent re-review (13 fresh reviewers)

**9 PASS / 4 FAIL.** All round-4 P1s verified fixed. New P1s traced to three exporter defects introduced by the round-3 typography upgrade, plus two spec-level leftovers:

- exporter baked CSS dedup rules carried `font-size` → one rule forced the first element's fitted size onto its whole signature group (hook-fee 3 node titles overflowed their boxes);
- card titles rendered single-line at 14px with no width check → titles overflowed/collided across cards (ecosystem-bite, fee-split, genesis-rights, omnichain-stages, verse-lifecycle);
- `render_svg_title` had no width constraint and no reserved band (polend: 81-char title clipped 105 units past the right edge and overlapped a label chip);
- verse-lifecycle: step badges "01"/"04" on the same text row as long titles; card 4 body line forced past its card by the 20-char wrap floor;
- omnichain-stages: edge-0 verticals crossed band-title glyphs (round-5 fixed only edge-3's corridor).

## Round 7 — repair

Central (exporter `scripts/export-static-diagrams.py`, renderer `.agents/skills/archify`):

1. `font-size` never emitted in deduped baked CSS — per-element attributes govern (sizes now render exactly as fitted/validated).
2. Card titles measured against real card interior and wrapped (≤2 lines, card height grows); card body wrap floor of 20 chars removed (narrow 4-card rows wrapped correctly).
3. `svg-title` moved into a reserved headroom band (content shifted via `translate(0, headroom)`, viewBox grown), width-aware two-line wrap.
4. Lifecycle step badge moved to its own row (badge y+13, title y+27) — no same-row collisions possible.
5. verse-lifecycle + omnichain-stages re-delivered to pick up renderer changes.

Per-diagram spec fixes (all validate 0 errors / 0 warnings, 9/9 showcase checks): dao-cycle (all 8 titles at 15 units; "Unclaimed" centered; gate→rollover rerouted to merge with the claim riser — crossing eliminated; boxes ≥8 off lane borders), hook-fee ("Volatility fee"/"Short-term fee"/"Dynamic fee" at 15 units; sum semantics carried by lane title + sublabel; card 1 title shortened), uasset-supply (Leveraged Genesis box 160 → title 14.83 effective; label pad off the Memeverse corner; card orphans; PSM asset list → card, edge label "4 assets" on its line), omnichain-stages (edge-0 rerouted via x=48/358 high corridor — pixel-verified zero glyph intersections; "Fee inexact" chip on its line; legend wording "purple dashed"), verse-lifecycle (at-deadline channel visible and symmetric), yt-flash-buy/sell (byte-identical legends; buy rows evened to 60px mirroring sell; sell sublabel back to 12.5), ecosystem-bite (demand channel lowered, worst dead band 70→37px).

## Round 8 — final review at the 8-round cap (13 fresh reviewers)

**12 PASS / 1 FAIL.** All four round-6 P1s confirmed fixed (genesis card titles, omnichain corridor/badges, verse badges/card wrap, hook-fee/uasset titles). The single FAIL was polend-settlement: the new svg-title block had been emitted *inside* the headroom translate group, so the title rode down with the content (band empty; second title line crossed the edge-8 corridor).

**Post-cap close-out:** exporter nesting fixed deterministically (title emitted after the translate closes; cards baked before the title), re-exported and re-rendered; structural check confirms title baselines y=30/54 inside the 0–68 band on polend (y=30 in the 0–44 band on the yt-flash pair), and a fresh targeted verifier re-audited polend end-to-end: **PASS** — title band clean, no new overlaps from the 68-unit shift, all previously passing items unchanged, render matches source pixel-for-pixel.

## Final state: 13/13 PASS

Effective-size floors hold everywhere (min text 11.06–13.67px effective; node-title tiers 13.82–17.08). Render uniqueness verified per round (md5). Chapter facts re-verified against the linked md pages in every round.

## Leftover register (图 → 未解决发现 → 原因)

| 图 | 遗留 | 级别 | 原因 |
|---|---|---|---|
| 全部 13 图 | 家族视觉体系为 archify 预设（底色 #020617 + emerald 强调 + JetBrains Mono 单一字族），非蒸馏基准的 #0A0A10/#FCEE0A + Saira/Plex 分工 | P2 | 需书籍级决策；13 图跨图一致性成立，单图不改 |
| polend-settlement | 节点标题有效 13.82、边标签 11.98（目标 14/12） | P2 备案 | viewBox 890 是「右轨距 lane 框 ≥14」下的最小 hug；两轮终审判不可感知 |
| omnichain-stages | edge-7 箭头被 Bare tokens 节点遮罩吞没（仅 ~1px 箭尖可见） | P2 | 既有几何，落点需改节点右缘/底边；8 轮上限前未再派修复 |
| omnichain-stages | edge-3 箭头贴主轨、edge-4 dash 擦主轨箭头 | P2 | 渲染器固定锚点几何，spec 层唯一解会触发 micro-segment 硬门 |
| omnichain-stages | 主轨起点与 Send 盒间 ~26px 空隙；基础层 step 徽章默认隐藏 | P2 | 渲染器常量 / 查看器 detail 档行为（静态 SVG 全量显示） |
| hook-fee | EWVWAP 盒中心偏 lane 中心 75；"sum" 链式边可被误读为时序（泳道公式+副标签+卡片三重消歧） | P2 | colXs 无 450 列；展示级零交叉门下的接受取舍 |
| four-pools | aux→PT/uAsset 直连边删除（事实由边标签+副标签 "Aux uAsset + PT"+卡片三重承载） | P2 备案通过 | 重加该边必然产生 showcase 禁止的计数交叉（拓扑穷举） |
| dao-cycle | "One missing: full rollover" 标签偏段中点 ~41px（段内、无碰撞）；rollover 底边双箭头重叠呈单箭头 | P2 | 既有接受状态 |
| preorder-flow | 卡 2 "not eligible for referral rebate" 为无源增强（章节未明示专通道豁免返佣） | P2 域问题 | 需产品侧确认；多轮在案 |
| ecosystem-bite | 卡 3 正文最紧行距卡缘 ~10px；supply lane 左缩进 38px | P2 | 画布/schema 下限 |
| 卡片正文 | 12 单位档在窄画布图（dao/polend/hook/omni）有效值 11.06–11.5（≥11 红线 ✓，低于 12 名义档） | P2 | 家族统一档位，需一次全书决策 |

## Artifacts

- Diagrams: `assets/diagrams/*.svg`（13，读者所见）+ `*.html`（交互源）+ `src/*.json`（规格真相源）
- Reports: `round3-report.md`、`round4-report.md`、本文件
- Working renders: `/tmp/diagram-png/r3|r4|r6|r8|r9-*.png`（会话临时）
- 未提交 git：所有改动留在工作区待审（渲染脚本修复在 /tmp/render-diagram.py；archify 渲染器与导出器的修改见上述文件）
