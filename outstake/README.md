# OutStake 概览

> 把多协议生息资产，统一铸成锚定型稳定币 uAsset。

OutStake 是 Outrun 的收益基础设施。它解决一个老问题：**Aave、Lido、EtherFi、Sky、Ethena、Lista、Aster** 各协议的生息代币(aToken、wstETH、weETH、sUSDS、sUSDe……)各自为政，收益和流动性都被切碎。OutStake 用一层标准化接口把它们统一，再铸成可在全链流通的 uAsset 稳定币。

## 三步看懂 OutStake

1. **收资产** —— [SY 标准化收益层](sy-adapters.md)把不同协议的生息代币，用统一接口包装起来。
2. **铸稳定币** —— 质押生息资产，按其当前价值铸出 [uAsset](uasset.md)(UETH / UUSD / UBNB)，每枚锚定 1 单位底层资产。
3. **质押管理** —— [双质押模式](staking-modes.md)（锁仓 / 包装）、[提取增值](draw-uasset.md)、[keeper 代偿](keeper.md)。

## 核心概念

| 概念 | 一句话 | 详解 |
|---|---|---|
| **SY** | 把各类生息代币统一包装的标准层 | [SY 适配器矩阵](sy-adapters.md) |
| **uAsset** | 锚定型稳定币(UETH / UUSD / UBNB) | [uAsset](uasset.md) |
| **锁仓 / 包装** | 两种质押路径：锁仓吃增值 vs 共享池求流动 | [双质押模式](staking-modes.md) |
| **提取增值** | 锁仓期内把生息增值提前变成 uAsset | [提取增值](draw-uasset.md) |
| **keeper** | 锁定超时达到一定时间后协议代为赎回，增值归仓位主人 | [Keeper 代偿](keeper.md) |
| **跨链** | uAsset 基于 LayerZero，全链流通 | [跨链与速率限制](omnichain.md) |

## uAsset 去了哪里

uAsset 不只留在 OutStake。它是 Outrun 生态的统一价值媒介，会流向 [Memeverse](../memeverse/README.md)：作为 Memecoin 创世的资金、杠杆创世的利息、创世积分的支付币。OutStake 负责"铸造"，Memeverse 负责"消耗" —— 两者通过 uAsset 的供需互相咬合（收益各自独立，不互相回流，详见[增长飞轮](../ecosystem/flywheel.md)）。

## 为什么不直接持有 wstETH？

DeFi 用户的第一反应往往是："我直接持有 wstETH 也能拿 Lido 的质押收益，为什么要过 OutStake？" 答案在三个增量价值：

- **统一与跨链**：wstETH 只在以太坊原生；过 OutStake 后变成 UETH，基于 LayerZero 全链流通，可在任意支持的链上使用，不必各自攒流动性。
- **收益即时变现**：直接持 wstETH，增值锁在底层资产里；锁仓质押后可随时把增值**提取成 UETH 稳定币**，无需解除质押、无需卖出底层。
- **接入 Memeverse 的门票**：UETH / UUSD / UBNB 是 Memeverse 创世、杠杆、结算的计价币。持 uAsset 可以参与[普通创世](../memeverse/genesis.md)，在成功解锁后的 24 小时保护期内完成退出，以本金守恒方式博取 Memecoin 生态收益 —— 这是直接持 wstETH 拿不到的。

换言之，OutStake 不只是"换个壳持 LST"，而是把生息资产**升级成全链可用、可即时变现、可接入社区启动的统一媒介**。
