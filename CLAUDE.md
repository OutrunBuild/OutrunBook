# CLAUDE.md — OutrunBook

OutrunBook 是 Outrun 生态**面向用户的中文产品文档**（GitBook 结构），不是合约 API / 技术参考。讲"能做什么、得到什么、为什么"，不讲代码实现。

## 仓库关系与代码真相源

文档的内容真相来自隔壁两个 Foundry 代码仓库，**改任何机制描述前必须以代码 / spec 为准**：

| 仓库 | 路径 | 角色 | 文档对齐 commit |
|---|---|---|---|
| **MemeverseV2** | `/home/azkrale/Web3Project/MemeverseV2` | 全链社区共识启动器（四池/Hook/POLend/POLSplitter/YieldVault/DAO/跨链） | `50b9d6066af8a226b30a68e9bcbd6cd1560fdbaa`(`50b9d60`，docs(spec): rename local launcher yield dispatch to distributeSameChain) |
| **OutStakeV2** | `/home/azkrale/Web3Project/OutStakeV2` | 收益基础设施（SY 适配器/uAsset/双质押/drawUAsset/keeper/跨链） | `0e55609b23dc5a533ad99a79d0af9837d501cf5f`(`0e55609`) |

> 当代码仓库更新后，需在此更新 commit hash 并同步核对文档是否仍对齐。

### MemeverseV2 的真相源文档（优先读，比代码更接近设计意图）
- `docs/spec/protocol.md`、`docs/spec/verse/accounting.md`、`docs/spec/verse/config-matrix.md`
- `docs/spec/polend/core.md`、`genesis.md`、`settlement-and-fees.md`、`pt-yt-splitter.md`
- `docs/spec/governance/governance-yield-details.md`、`docs/spec/swap/swap-flow.md`、`yt-flash-swap.md`
- `docs/ARCHITECTURE.md`、`docs/GLOSSARY.md`
- OutStakeV2 无 spec，看 `src/` 合约 NatSpec。

## 写作规范（用户明确要求，务必遵守）

1. **面向用户产品语言**：禁出现函数名(`stake()`)、变量名(`amountInSY`)、行号、代码公式、"代码参考"小节。
2. **中文标点**：中文语境用全角标点(，。：；！？（）)，除非特殊情况（代码、URL、数字间比例 `2:3:2`、英文术语内部）。`Memeverse`/`YT`/`DAO` 等英文术语后的标点也是中文标点。
3. **术语保留英文**：uAsset / SY / PT / YT / POL / Hook / POLend / Preorder / GenesisCredit / YieldVault 等不翻译。
4. **举例**：用「用户」/角色名，**不要用虚构人名**（老王/小李）；Memecoin 示例用泛指「Memecoin」，**不要具体代号**(FROGGY)。

## 关键机制决策（均经代码核实或用户确认，改文档时勿推翻）

- **uAsset = 锚定型稳定币**（UETH/UUSD/UBNB 锚 ETH/USD/BNB）。UETH/UBNB 锚波动资产，非法币稳定币。代码层是 debt-tracked receipt，产品层用稳定币叙事；不叫"债务凭证"。
- **飞轮 = uAsset 供需双向咬合**（OutStake 供给 ↔ Memeverse 创造用途），**非收益回流**。两个模块收益各自独立，不互相回流。
- **普通创世 = 无风险**：投入的 uAsset 100% 进四池守恒，Memecoin 是全新铸造的；归零只损失"Memecoin 预期收益"，本金按份额原数拿回。机制依据是**资金守恒**（不是 PT 锚定 —— 普通创世者领 YT+辅助池 LP，不持 PT）。杠杆创世才承担风险，且**仅利息成本**（无本金、无清算）。
- **收益流向**：交易费 LP 65% / 协议 35%；协议费 uAsset 计价→DAO 国库、Memecoin 计价→Staking 收益库、POL 计价→销毁、有推荐人则总费 10%→返佣；执行者奖励 = 主池 uAsset 费 0.25%；杠杆利息→协议自留国库（非 DAO 国库）。
- **三金库**：Memecoin Staking 收益库（质押者）/ DAO 国库（uAsset 费，社区治）/ 协议自留国库（杠杆利息，协议方）。
- **四池比例**：主池 Memecoin/uAsset 占创世资金 70%；POL 2:3:2；拆出 PT 1:2。
- **split/merge 仅 Locked 阶段**（Unlocked/settled 后 revert）。
- **YT Flash Swap**：锁定期 YT 二级市场通道。独立 Router 复用 PT/POL 池（不建第二个 AMM、不设独立 YT 池），单笔 unlock 内完成换腿 + split/merge；两入口：POL→精确 YT（实际成本 = y−R 结算，不预扣预算）、精确 YT→POL（minPOLOut 保护）；费用/referral 与普通 PT/POL swap 完全一致（不二次收费），但费用按完整 PT 腿规模计、杠杆下相对实际支付本金占比放大；须有活动 account session（智能账户原子包裹，principal = msg.sender）；仅 Locked 阶段可用；YT 有效价格 = 1 POL − PT 市价。**YT = 杠杆资产**：花价差一小部分买到完整份额的结算残值暴露，残值小变动→YT 回报大变动（对应 Pendle 官方文档 "leveraged exposure to yield"，买 YT = 做多结算残值，双向放大）。
- **参与三档**：稳健（无风险）/ 平衡（杠杆，仅利息成本）/ 共建（买币质押治理）。曾用"激进"，用户嫌难听改"共建"。
- **DAO**：标准 token 投票（质押 Memecoin 份额），非旧"sMemecoin+POL 双轨 TVP 公式"（代码已无）。

## 文档结构

```
README.md / vision.md / SUMMARY.md（目录）
outstake/    OutStake 各机制章
memeverse/   Memeverse 各机制章
ecosystem/   飞轮 / 商业模式 / 受众 / 参与方式(playbooks)
reference/   术语表 / 参与方式总览 / FAQ
.claude/internal/gap-analysis.md   内部工作稿（不在公开书）
```

- 改文档后注意全书一致（同一机制多处描述会漂移，如普通创世"无风险"、三金库术语）。
- 标点批量修复脚本思路见 git 历史；**注意**：句号转换须保留"前字符是 CJK"前置，否则会把列表项 `1.` 误换成 `1。`。
