# OutrunBook 图示总规划（最终版）

- 根目录：`/home/azkrale/Web3Project/OutrunBook`。**全程不执行 git commit**：所有产出（HTML、规格 JSON、md 修改）留在工作区，由用户审阅后自行提交。被替换的 Mermaid 块直接从 md 删除。
- 事实真相源基线：Memeverse `9532d2e`、OutStake `22b6785`（与 CLAUDE.md 基线一致）。动笔前跑 `bash scripts/check-baseline.sh`，不一致先更新基线。

## 事实来源（三层，逐层对齐）

1. **两仓代码（实现真相）**：`/home/azkrale/Web3Project/Memeverse`、`/home/azkrale/Web3Project/OutStake`。图上每个机制断言——数值、顺序、条件、失败语义——以 `src/` 为最终裁判。
2. **两仓 spec 文档（设计意图，优先阅读）**：Memeverse `docs/spec/**`（protocol、verse/accounting、verse/config-matrix、polend/*、governance/*、swap/*、interoperation/*）、OutStake `docs/spec/**`（protocol、position/*、yield/* 等）。各任务「真相源」栏引用的行号出自这里；文件清单的权威列表见 CLAUDE.md「仓库关系与代码真相源」。
3. **本仓文档（嵌入与一致性对象）**：29 页公开书。图的嵌入页面、页面既有表格（lifecycle 操作表、omnichain 失败对照表、hook 费率表、三金库表）以及跨页同机制描述（「普通创世无风险」「三金库」等）必须零矛盾；写作规范与机制决策以 CLAUDE.md 为权威。

## 铁律

- **公开书零 Mermaid。** 每张图 = archify 交互 HTML，经 iframe 直接嵌入 md 页面，嵌入即本体，不放外链。
- 任务描述中的「状态机 / 分流树 / 时序 / 瀑布」仅指形状语义，渲染载体一律为 archify 交互 HTML。

## 嵌入规范

```html
<iframe src="<相对路径>" loading="lazy" style="width:100%;height:800px;border:1px solid #e5e7eb;border-radius:8px" title="<图名>"></iframe>
```

- 路径：根页面用 `assets/diagrams/<名称>.html`；memeverse/、outstake/、ecosystem/ 子页用 `../assets/diagrams/<名称>.html`。
- 规格源码保存：`assets/diagrams/src/<名称>.<类型>.json`，与 HTML 一同放在 assets/diagrams/ 下。
- iframe 下方不加解读图注（「这张图读什么」已全书移除：图的信息必须在正文里能找到，缺的补正文）。

## 评判标准

唯一硬性门槛：**图必须在 30 秒内做到文字做不到的事**。不画：纯线性步骤（有序列表）、静态对照（表格）、装饰插画、未定版 UI 截图。每个机制页至多 1 张主图；图承担后正文冗余段落删减；图不重复正文。

形状只是分类参考，用于决定 archify 的 diagram_type，非穷举：

| 形状 | diagram_type | 本书实例 |
|---|---|---|
| 状态机 | lifecycle | 生命周期、跨链三阶段 |
| 分流树 | dataflow | 四池、费用分流、预购聚合、咬合图 |
| 原子多方时序 | sequence | 闪电兑换买／卖 |
| 失败路径瀑布 | workflow | polend 结算 |
| 双路径对比 | workflow | staking 锁仓 vs 包装 |
| 构成分解 | workflow | hook 费率公式 |
| 周期闭环 | workflow | dao 周期激励 |

出现对照表之外的新结构：先过 30 秒测试，再选最接近的 diagram_type；测试不过就不画。

## 通用规范

1. 主标签用用户语言；函数名 / 变量名 / 错误名不上图、不上公开正文（只允许出现在本文件真相源栏）。
2. 合约固定常量标「固定」；协议方可调参数标「当前默认，可调整」。时长/比例常量用绝对锚点（365 天、90 天、24 小时、1%），不写「约」；「约」只用于人工触发时点与实际成交结果。
3. 中文全角标点；uAsset / POL / PT / YT / Hook / POLend / Preorder / GenesisCredit 等术语保留英文；示例用「用户」「某 Memecoin」。
4. 每图完成后：`bash scripts/check-baseline.sh` 退出 0；`bash scripts/check-absolute-words.sh` 退出 0（注意：脚本不扫 assets/diagrams/*.html，HTML 内的绝对词与代码标识须人工核对）；图内无反引号代码标识；公开页 mermaid 代码块零命中；每页嵌入后浏览器实开——iframe 渲染正常、相对路径正确、滚动与高度可接受。

## 任务清单（13 张图，按执行顺序）

### 1. B-2 `outstake/staking-modes.md` 债务与赎回闭环 —— 双路径对比（workflow）

- 锁仓泳道：存入 SY + 自选锁定期（0 天 = 不锁，最低存入额以界面为准）→ 按当时价值立即铸 uAsset → 锁定期内增值可多次一次性提取 → 到期自赎回：归还与累计铸出等值的 uAsset → 取回 SY。分支：增值已花掉 → 自行重新取得等值 uAsset（协议不代买），或 keeper 代偿（债务等值归 keeper、超出归你）。
- 包装泳道：存入共享池 → 立即铸 uAsset（可转让/跨链，无锁定期）→ 增值归协议（收割只取超出债务等值部分）→ 退出 = 卖出 uAsset（市场退路），或 keeper 面值兑付（不足额整笔回退）。
- 图注核心：uAsset 不只是稳定币，也是取回质押资产的凭证——提走的增值 = 赎回时要归还的债务。
- 真相源：`OutrunStakingPositionUpgradeable.sol:253-433, 471-552, 682-711`、`IOutrunStakeManager.sol:50-52`。
- 页面正文已定稿：本任务仅向该页嵌入 iframe，不改写正文。
- 验收：读者能回答「提取过 100 增值并花掉，到期赎回需要什么」；两条泳道退出方式差异可见。

### 2. A-4 `memeverse/polend.md` 到期结算 —— 失败路径瀑布（workflow）

- 上段（解锁那一笔交易，原子）：最后捕获辅助池手续费 → 进入解锁、POL 统一结算 → 有杠杆债务则全局结算 → 开启 24 小时保护窗；任一步失败整笔回滚、保持锁定期。
- 下段（全局结算瀑布，仅有杠杆债务时）：按杠杆债务占比切出辅助池杠杆份额（取整差额归普通侧）→ 平仓回收（POL 烧毁赎回、PT 按锚定比率兑 uAsset）→ 回收 uAsset 先偿还全部杠杆债务（销毁）→ 有结余：残值 = 剩余 uAsset ＋ 全部回收 Memecoin，按付息比例一次性分配、永久可领；有缺口：结算储备金只补有上限的舍入级缺口，超过即整笔回滚 → 任何人补充储备后重试（不受协议暂停限制）。
- 图注：储备金只补舍入缺口、不覆盖资不抵债；盈亏语义由正文承担。
- 真相源：`settlement-and-fees.md:250-269, 415-546`、`polend/core.md:327-344`。
- 验收：无函数名/错误名；回滚→补储备→重试闭环可见。

### 3. A-2 `memeverse/lifecycle.md` 生命周期 —— 状态机（lifecycle）＋ 阶段×操作矩阵表

- 创世期 →（快速创世且任一门槛达标：截止前可提前触发；未开启：截止后触发，任一门槛达标）→ 锁定期（365 天 · 固定）→（锁定期满，任何人触发统一结算）→ 解锁期（统一结算 ＋ 24 小时保护窗 · 固定）→（保护窗到期自动恢复公开交易，无需任何交易）→ 常态运行（终态）。创世期 → 退款（终态）：截止后触发且两门槛均未达标。
- 标注：门槛是「或」——普通创世资金、杠杆利息各自独立与最低成功额度比较，预购资金与杠杆债务本金不计入；除保护窗自动恢复外，阶段推进都要一笔公开交易触发；解锁时刻 = 创世截止 ＋ 365 天（固定），提前进入锁定不改变；24 小时窗口从实际进入解锁的那笔交易起算。
- 同页新增「阶段 × 开放操作」矩阵表（用户语言）。行映射（已对照 spec 与代码核验）：
  - 仅创世期：参与创世（普通／杠杆）、预购
  - 仅退款态：退款领取（每地址一次）
  - 锁定期起：领 YT（普通／杠杆）、辅助池手续费分成、LP 领取已累积手续费、加池铸 POL、预购领取（线性）、触发费分发、质押 Memecoin
  - 仅锁定期：YT 拆分／合并
  - 锁定期起（24 小时窗内暂停）：公开交易
  - 解锁期起：烧 POL 赎回、一次性领辅助池 LP ＋ 剩余、PT 赎 uAsset、YT 领残值
- 同批文字微任务：修正 4 处「约 365 天」为「365 天」（合约固定常量）——memeverse/vs-pump-fun.md 两处、reference/faq.md 一处、reference/glossary.md 一处（该处「固定约 365 天」自相矛盾）。
- 真相源：`state-machines.md:11-72`、`config-matrix.md:82-93`。
- 验收：三口径（成功判定 / 建池 / 预购）可区分；全书无「约 365 天」。

### 4. A-3 `memeverse/four-pools.md` 建池资金流 —— 分流树（dataflow）

- 建池资金 = 普通创世资金 ＋ 杠杆债务本金（预购资金、杠杆利息不计入）→ 约 70% 主池 / 约 30% 辅助池 uAsset → 主池铸出 POL 按约 2:3:2 → 3/7 拆分 PT＋YT（YT 按资金占比，余数归杠杆侧）→ PT 按约 1:2（差额归 PT/POL 侧）；辅助池 uAsset 约 2/3 → POL/uAsset、约 1/3 → PT/uAsset（PT/POL 无 uAsset 侧）。
- 图注：比例以实际建池成交为准；未用完 uAsset 注入结算储备金（超上限进国库）、未用完 Memecoin 销毁。
- 真相源：`polend/genesis.md:339-421`、`verse/accounting.md:52-78`。
- 验收：读者能复述三口径与各级比例。

### 5. B-1 `memeverse/genesis.md` 权益结构与窗口 —— 分流树＋时间线混合（dataflow）

- 三类权益：初始 YT（锁定后可领，永久可领）；辅助池手续费分成（锁定期起持续累计）；解锁后一次性领取辅助池 LP ＋ 建池剩余 POL/PT → 本金守恒锚点（辅助池 uAsset 约 30% ＋ PT 对应主池 uAsset 约 30% ＋ POL 对应主池 uAsset 约 40% ＝ 100%）→ 实际进入解锁的那笔交易（窗口起点）→ 24 小时保护窗（四池暂停公开交易、赎回领取开放、按静态储备）→ 恢复公开交易（期后退出风险自负）。
- 六步完整退出留正文有序列表，图不重复。
- 真相源：`polend/genesis.md:417-468`、`settlement-and-fees.md:99-246`。
- 验收：三类权益各自何时可领、窗口从哪一刻起算，一图可答。

### 6. B-3 `memeverse/omnichain.md` 跨链三阶段 —— 状态机（lifecycle）＋ 失败对照表保留

- 发送（源链）：消息费不精确 / 低于最小精度 → 当笔回退、资金不动；非最小精度整数倍 → 截断发送、余量当笔退回。→ 到账（目标链铸造）：暂时无法接收 → 不撤销源链、重新投递；接收预算配置过低（极端配置，少见）→ 已销毁未铸造，滞留待手动恢复 → 落位（质押）：收益库不存在 → 裸币直转接收人（无份额无票权，就位后可重新发起）；落位失败 → 退回可重试；收益库就位 → 质押成功（核验份额）。
- 结论标注：发送成功 ≠ 到账 ≠ 质押成功；到账后核验收益库份额，不是代币余额。
- 真相源：`interoperation-details.md:47-145`、`layerzero-oapp-oft.md:45-104`。
- 验收：三阶段 × 各失败分支 × 资金位置全覆盖，与页面表格逐行对应。

### 7. B-8 `memeverse/dao-governance.md` 周期激励 —— 周期闭环（workflow）

- 入口：质押份额 →（委托给自己或代表；不委托无票权但计入基数）→ 票权 → 期内投票（票在投票时计入当期周期，90 天 · 固定）→ 周期结束后任何人触发结算（链上操作，自付 gas）→ 三条件门（币种纳入奖励范围 / 当期国库有入账 / 当期有票数，缺一则不划拨、国库全额滚存）→ 按默认 25%（治理可调）划为奖励池 → 按个人票数占比主动领取（仅限本人）→ 只认紧邻上一周期，错过并入国库、无补领。
- 真相源：`governance-yield-details.md:331-376`、`config-matrix.md:46, 95`。
- 验收：「委托 / 触发 / 领取都要人做、错过不补」图上可见；`memecoin-staking.md` 委托一节链接本图。

### 8. B-7 `memeverse/preorder.md` 聚合成交与归属 —— 分流树＋失败分支（dataflow）

- 多用户预购资金（创世期存入，独立记账；总容量 ≈（普通资金 ＋ 杠杆债务本金）× 70% × 协议配置比例，先到先得）→ 建池同一笔交易内：先建主池 → 全部预购资金聚合为主池第一笔买入（固定 1% 结算费 · 固定，仍按 LP 65%／协议 35% 拆分、不参与返佣；公开交易无法插队）→ 所得 Memecoin 按各自资金占比分配 → 托管线性解锁（协议配置时长）→ 主动领取（未领的一直保留）。
- 失败分支：创世未达标 → 原路全额退给参与记录的受益人；无法完整成交 → 整笔启动回滚、无部分结算。
- 图注：固定的是费率，不是价格。
- 真相源：`polend/genesis.md:40-98`、`verse/accounting.md:80-99, 225-235`。
- 验收：与 `hook.md` 预购结算通道小节互链一致；容量口径与页面文字一致。

### 9. B-6 `memeverse/hook.md` 费率组件 —— 构成分解（workflow）＋ 衰减五行小表

- 实际费率 ＝ max（动态费，开池衰减费）；动态费 ＝ 基础费率 1%（合约固定）＋ 逆向冲击费（按地址 × 池，3 秒窗口累积合并，拆单无效）＋ 波动费（按池）＋ 短期冲击费（按池，≤2% 免征，15 秒衰减叠加）；EWVWAP 方向豁免：池内有成交历史且交易让价格回归均衡 → 跳过全部动态费只付基础费率，首笔不豁免；总上限 100%（固定）；衰减配置低于 1% 时 1% 底价仍生效。
- 附五行衰减表（0/1/5/10/15 分钟 → 50% / 约 38% / 约 13% / 约 3.6% / 1%；shape=4 归一化指数衰减，见 `DynamicFeeMath.sol:223-227`；两端为当前默认，协议方可调）。
- 真相源：`verse/accounting.md:186-244`、`DynamicFeeMath.sol:39-52`、`config-matrix.md:33-38, 90`。
- 验收：不画攻击者必亏／用户必得的效果图；无绝对化表述；所有可调数字带限定语。

### 10. A-6 `ecosystem/business-model.md` 费用分流 —— 分流树（dataflow）

- 维度一：LP 65% ／ 协议 35%（固定）；有推荐人从协议份额切返佣（默认总费 10%）。
- 维度二（协议份额按计价币）：uAsset 计价 → DAO 国库（主池 uAsset 费扣 0.25% · 当前默认，给执行者）；Memecoin 计价 → Staking 收益库；POL 计价 → 销毁；辅助池 uAsset/PT 计价费（锁定期）→ 按杠杆债务占比切分：普通侧按创世份额分成、杠杆侧归 DAO 国库。
- 图注：解锁后辅助池非 POL 费全归 DAO 国库，普通用户仅可补领锁定期累计；杠杆利息归协议自留国库，不属交易费。
- 真相源：`settlement-and-fees.md:9-33`、`verse/accounting.md:122-148, 213-215`。
- 验收：与三金库表、`four-pools.md` 手续费小节、`hook.md` 费率表零矛盾。

### 11. A-7 `memeverse/yt-flash-swap.md` 买 YT —— 原子多方时序（sequence）

- 借（卖 y 个 PT 换 R 个 POL）→ 拆（凑 y 个 POL 拆出 y PT ＋ y YT）→ 还（y 个 PT 归还）→ 到手（y 个 YT，实际支付 y − R 个 POL）。
- 注解（消息 note ＋ 图注）：买入设最高支付上限，另可设保护线与过期时限，超出整笔回滚；报价仅供参考，未超保护线仍按更差成交（MEV／市场变动）；一次底层交易一次费，按完整 PT 腿规模计（相对本金放大）；受池深度影响任意数量不保证成交（诚实失败）；仅锁定期可用；智能账户会话前置。
- 真相源：`docs/spec/swap/yt-flash-swap.md`、CLAUDE.md YT Flash Swap 条目。
- 验收：无「保证成交价」表述；杠杆属性在正文不在图。

### 12. A-8 `memeverse/yt-flash-swap.md` 卖 YT —— 原子多方时序（sequence）

- 借（花 Q 个 POL 买入 y 个 PT）→ 合（y PT ＋ y YT 合并回 y POL）→ 还（归还 Q）→ 到手（y − Q 个 POL）。注解同上，下限语义替换上限。
- 真相源、验收同 A-7。

### 13. A-1 `README.md` 双模块咬合 —— 分流树＋回环（dataflow）

- OutStake 供给端（多协议生息资产）→ 质押（锁仓／包装）铸出 → uAsset（UETH / UUSD / UBNB，连接两个模块的血线）→ 创世资金 · 杠杆利息 · 预购 · 结算计价 → Memeverse 用途端（四池 · 杠杆创世 · Staking · DAO）；回环虚线：供需双向咬合（非收益回流）。
- 验收：虚线咬合标注保留；与 flywheel 页 ASCII 主轮零矛盾（该页 ASCII 保留，不配图）。

## 明确不画

flywheel ASCII 主轮、对照类（lock/wrap、keeper、暂停影响、三档参与、凭证时间线，一律表格）、uAsset 铸币债务记账、OutStake 跨链限流、Router 入口、sy-adapters / vs-pump-fun / glossary / faq / vision / audience。
