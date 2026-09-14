# OutStake 概览

> 把多协议生息资产，统一铸成锚定型稳定币 uAsset。

OutStake 是 Outrun 的收益基础设施。它解决一个老问题：**Aave、Lido、Sky、Ethena、Lista、Aster** 各协议的生息代币（aToken、wstETH、sUSDS、sUSDe……）各自为政，收益和流动性都被切碎。OutStake 用一层标准化接口把它们统一，再铸成可在全链流通的 uAsset 稳定币。

## 三步看懂 OutStake

1. **收资产** —— [SY 标准化收益层](sy-adapters.md)把不同协议的生息代币，用统一接口包装起来。
2. **铸稳定币** —— [创世质押](staking-modes.md)存入生息资产，按其当前价值面值铸出 [uAsset](uasset.md)(UETH / UUSD / UBNB)，每枚锚定 1 单位底层资产；或经 [PSM](psm.md)用储备资产按面值直接兑换。
3. **管起来** —— 仓位随时赎回（无锁定期、无清算），闲置 uAsset 可进 [USR 储蓄](usr.md)吃利息，[一站式入口](router.md)把全链路合成一次操作。

## 核心概念

| 概念 | 一句话 | 详解 |
|---|---|---|
| **SY** | 把各类生息代币统一包装的标准层 | [SY 适配器矩阵](sy-adapters.md) |
| **uAsset** | 锚定型稳定币（UETH / UUSD / UBNB） | [uAsset](uasset.md) |
| **创世质押** | Memeverse 专用的质押铸造：面值铸出、无利息、无清算、无锁定期 | [创世质押](staking-modes.md) |
| **PSM** | 储备资产与 uAsset 按 1:1 面值双向兑换，无仓位无债务 | [PSM 锚定兑换](psm.md) |
| **USR** | uAsset 储蓄金库：存 uAsset 拿份额吃利息，随存随取 | [USR 储蓄](usr.md) |
| **跨链** | uAsset 基于 LayerZero，全链流通 | [跨链与速率限制](omnichain.md) |

## uAsset 去了哪里

uAsset 不只留在 OutStake。它是 Outrun 生态的统一价值媒介，会流向 [Memeverse](../memeverse/README.md)：作为 Memecoin 创世的资金、杠杆创世的利息、创世积分的支付币。OutStake 负责"铸造"，Memeverse 负责"消耗" —— 两者通过 uAsset 的供需互相咬合（收益各自独立，不互相回流，详见[增长飞轮](../ecosystem/flywheel.md)）。

## 为什么不直接持有 wstETH？

DeFi 用户的第一反应往往是："我直接持有 wstETH 也能拿 Lido 的质押收益，为什么要过 OutStake？" 答案在三个增量价值：

- **统一与跨链**：wstETH 只在以太坊原生；过 OutStake 后变成 UETH，基于 LayerZero 全链流通，可在任意支持的链上使用，不必各自攒流动性。
- **抵押生息不停**：创世质押后，抵押的生息资产继续生息，敞口 100% 归你 —— 拿 uAsset 去用的同时，底层收益一份不少。
- **接入 Memeverse 的门票**：UETH / UUSD / UBNB 是 Memeverse 创世、杠杆、结算的计价币。持 uAsset 可以参与[普通创世](../memeverse/genesis.md)，在成功解锁后的 24 小时保护期内完成退出，以本金守恒方式博取 Memecoin 生态收益 —— 这是直接持 wstETH 拿不到的。

换言之，OutStake 不只是"换个壳持 LST"，而是把生息资产**升级成全链可用、生息不停、可接入社区启动的统一媒介**。
