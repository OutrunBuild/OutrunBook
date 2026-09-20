# Memeverse 概览

> 全链社区共识启动器 —— 启动的不是一枚代币，而是一个拥有流动性、收益与治理的链上社区。

## Memeverse 是什么

大多数人把 Memecoin 当赌博筹码。Memeverse 不这么看。

Memecoin 能靠一个符号让千万人站台，但今天的它是一座赌场：拉盘即砸盘，热度一过归零，共识换不来收益、治理或国库。

**Memeverse 要做的，是给社区共识装上自我运转的引擎**：一个 Memecoin 在这里上线，即同时拥有深度流动性、持续收益权和社区治理权。

## 三套引擎

公平发射建立市场，收益代币化让资本持续生息，质押者决定各自社区的下一步：

1. **公平发射** —— 没有 Creator 特权、没有预分配。普通、杠杆与预购参与汇入同一次公平创世，达标即建四池，主池锁定 365 天。详见 [普通创世](genesis.md)、[杠杆创世](polend.md)、[预购](preorder.md)。
2. **收益代币化** —— 锁定的主池流动性拆分为 PT（本金代币）与 YT（收益代币），让未来现金流成为当下即可交易的资产，并以此建立 POLend（杠杆创世）市场。详见 [POL 拆分](pol-splitter.md)、[杠杆创世](polend.md)、[YT 闪电兑换](yt-flash-swap.md)。
3. **质押与 DAO 治理** —— 交易手续费分配给质押者与 DAO 国库；质押并委托后获得治理权，社区按周期领取激励，国库由社区共治。详见 [Memecoin Staking](memecoin-staking.md)、[DAO 治理](dao-governance.md)。

第三套引擎让交易手续费流向质押者与 DAO 国库：交易越活跃，社区可支配的资源越多。详见 [DAO 治理](dao-governance.md)。

## 谁参与，怎么参与

- **发起人**：可在多条链上同时启动一个 Memecoin，各链独立募资、独立建池，无门槛、无 Creator 特权。
- **创世参与者**：用 uAsset 参与[普通创世](genesis.md)，在本金守恒模型下博取额外收益；也可加杠杆放大份额，或通过预购提前锁定 Memecoin。
- **质押者 / 治理者**：上线后把 Memecoin 质押进收益库，赚手续费收益；完成委托后获得 DAO 投票权，参与社区共建。

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
| **普通创世** | uAsset 本金守恒 + 额外上行权益 | [普通创世 Genesis](genesis.md) |
| **四池** | 主池 + 三个辅助池的流动性结构 | [四池流动性](four-pools.md) |
| **动态费率 Hook** | 基于 Uniswap V4 的抗操纵交易层 | [动态费率 Hook](hook.md) |
| **预购 Preorder** | 创世前提前锁定 Memecoin | [预购](preorder.md) |
| **杠杆创世 POLend** | 付利息放大创世份额 | [杠杆创世](polend.md) |
| **POL 拆分** | 把 POL 拆成本金（PT）和收益（YT） | [POL 拆分](pol-splitter.md) |
| **创世积分** | 可跨链的创世参与凭证 | [创世积分](genesis-credit.md) |
| **Memecoin Staking** | 质押赚手续费，委托后获治理权 | [Memecoin Staking](memecoin-staking.md) |
| **DAO 治理** | 社区共治国库与方向 | [DAO 治理](dao-governance.md) |
