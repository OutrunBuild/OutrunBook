# Memeverse 概览

> 全链社区共识启动器 —— 启动的不是一枚代币，而是一个拥有流动性、收益与治理的链上社区。

## Memeverse 是什么

大多数人把 Memecoin 当赌博筹码。Memeverse 不这么看。

Memecoin 是这个时代最强的共识凝聚机制 —— 它不靠白皮书、不靠 VC，只靠一个让千万人愿意站台的符号。但今天的 Memecoin 是一座赌场：拉盘即砸盘，共识被少数人收割，社区在 PVP 中互相消耗，热度一过归零收场。它有最强的社区，却最缺乏把共识转化为长期价值的机制。

**Memeverse 要做的，是给社区共识装上自我运转的引擎。** 它不是一个 Memecoin 启动平台，而是一个**全链社区共识启动器**：启动的不是一枚代币，而是一个拥有流动性、收益与治理的链上社区。一个 Memecoin 在这里上线，即同时拥有深度流动性、持续收益权和社区治理权 —— 从投机符号，变成一个能自我维持的社区国度。

## 三套引擎

1. **四池流动性 + 动态费率** —— 启动即建立深度、抗抢跑抗夹的流动性。详见 [四池流动性](four-pools.md)、[动态费率 Hook](hook.md)。
2. **杠杆创世(POLend)** —— 用 uAsset 或创世积分付利息，放大创世参与，到期统一结算。详见 [杠杆创世](polend.md)。
3. **Memecoin Staking + DAO 治理** —— 交易手续费分配给质押者与 DAO 国库；Memecoin 同时成为治理代币，社区按周期获得激励，国库由社区共治。详见 [Memecoin Staking](memecoin-staking.md)、[DAO 治理](dao-governance.md)。

第三套引擎是 Memeverse 的灵魂 —— 它把投机能量转化为建设能量，让 Memecoin 真正"长出"持续价值。详见 [DAO 治理](dao-governance.md)。

## 谁参与，怎么参与

- **发起人**：在多条链上同时启动一个 Memecoin，无门槛、无 Creator 特权。
- **创世参与者**：用 uAsset 稳定币参与创世（普通创世无风险博收益：本金 uAsset 守恒，与 Memecoin 涨跌无关），或加杠杆放大份额，或预购提前锁定。
- **质押者 / 治理者**：上线后把 Memecoin 质押进收益库，赚手续费收益，并获得 DAO 投票权，参与社区共建。

不同风险偏好的人有不同参与路径，详见 [参与方式与风险偏好](../ecosystem/playbooks.md)。

## uAsset 在 Memeverse 里的角色

uAsset（OutStake 铸造的稳定币）是 Memeverse 运转的燃料：

- **创世资金**：启动 Memecoin 时，参与者的 uAsset 注入流动性池。
- **杠杆利息**：加杠杆创世时，用 uAsset（或创世积分）支付利息。
- **结算计价**：到期结算、本金赎回都以 uAsset 计价。
- **国库收入**：Memecoin 交易手续费中 uAsset 计价的部分，流入该 Memecoin 的 DAO 国库，由社区共治。

OutStake 铸造 uAsset，Memeverse 消耗 uAsset，共识由此流动。

## 核心概念

| 概念 | 一句话 | 详解 |
|---|---|---|
| **生命周期** | 从创世到解锁的完整流程 | [启动生命周期](lifecycle.md) |
| **四池** | 主池 + 三个辅助池的流动性结构 | [四池流动性](four-pools.md) |
| **动态费率 Hook** | 基于 Uniswap V4 的抗操纵交易层 | [动态费率 Hook](hook.md) |
| **预购 Preorder** | 创世前提前锁定 Memecoin | [预购](preorder.md) |
| **杠杆创世 POLend** | 付利息放大创世份额 | [杠杆创世](polend.md) |
| **POL 拆分** | 把 POL 拆成本金(PT)和收益(YT) | [POL 拆分](pol-splitter.md) |
| **创世积分** | 可跨链的创世参与凭证 | [创世积分](genesis-credit.md) |
| **Memecoin Staking** | 质押赚手续费 + 获得治理权 | [Memecoin Staking](memecoin-staking.md) |
| **DAO 治理** | 社区共治国库与方向 | [DAO 治理](dao-governance.md) |
