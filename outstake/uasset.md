# uAsset：锚定型稳定币

## uAsset 是什么

**uAsset** 是 OutStake 铸造的统一稳定币，分三类，各自锚定一种底层资产：

| uAsset | 锚定 | 底层生息资产来源 |
|---|---|---|
| **UETH** | ETH | wstETH / weETH 等 ETH 类生息资产 |
| **UUSD** | USD | sUSDS / sUSDe / aUSDC 等美元收益资产 |
| **UBNB** | BNB | slisBNB / asBNB 等 BNB 类生息资产 |

**锚定的含义：1 枚 uAsset 始终对应 1 单位底层资产价值。** 1 UETH 对应 1 ETH 的价值，1 UUSD 对应 1 美元，1 UBNB 对应 1 BNB。这一对应按面值记账；把 uAsset 兑回底层资产时，实际兑付受共享池余额与底层汇率制约 —— 正常机制下可足额兑付，极端市场条件下底层汇率长期大幅回落时按比例兑付（详见 [双质押模式](staking-modes.md) 的风险说明）。

> 注意：这里的"稳定币"指**相对底层资产保持稳定价值**，而非锚定法币。UUSD 是美元稳定币；但 UETH、UBNB 锚定的是 ETH、BNB，会随底层资产价格波动 —— 它们是 ETH/BNB 计价的稳定凭证，不是法币稳定币。

## 锚定是怎么做到的

uAsset 的铸造量，严格按质押资产的**当前价值**计算，而非按代币数量。底层生息资产的汇率会随收益上升（例如 wstETH 因 stETH 质押收益而越来越值钱），铸造时就按这个实时价值换算：

- 质押价值 1 ETH 的 wstETH → 铸出 1 UETH。
- 无论这 wstETH 来自 Lido 还是 EtherFi，只要值 1 ETH，就铸 1 UETH。

不同来源、同类底层的收益，由此汇入**同一个 uAsset**，流动性不再碎片化。

## 铸币上限，防止超发

每个质押管理器都有**铸币上限**：其未偿铸币量不能超过设定额度。铸造时增加额度占用，赎回（销毁 uAsset）时释放。这是 uAsset 作为稳定币的保障之一 —— 有上限、可审计、不会无限增发。

## 全链流通

uAsset 基于 **LayerZero OFT** 标准，可在不同链之间 1:1 流转。你可以在一条链铸出 UUSD，跨到另一条链上使用。详见 [跨链与速率限制](omnichain.md)。

## uAsset 在生态中的角色

uAsset 不只是 OutStake 的产物，它是整个 Outrun 的价值媒介：

- **Memeverse 创世资金**：启动 Memecoin 时用 uAsset 注入流动性。
- **杠杆创世利息**：在 Memeverse 加杠杆时，uAsset 作为利息支付币。
- **创世积分结算**：积分型杠杆也以 uAsset 计价。

OutStake 铸造，uAsset 流向 Memeverse，构成生态资本循环的起点。

## 举例

> 用户有 5 个 wstETH(Lido)，当时每个约值 1.05 ETH，合计约 5.25 ETH。他在 OutStake 质押，铸出约 5.25 UETH（锚定 ETH）。一个月后 wstETH 继续生息升值，仓位值涨到约 5.3 ETH，他可以把多出来的约 0.05 ETH 等值的 UETH 提取出来（锁仓质押下），本金继续留在仓位生息。无论这 wstETH 来自 Lido 还是 EtherFi，只要等值 1 ETH 就铸 1 UETH —— 不同来源的同类收益汇入同一个 UETH。
