# uAsset：锚定型稳定币

## uAsset 是什么

**uAsset** 是 OutStake 铸造的统一稳定币，分三类，各自锚定一种底层资产：

| uAsset | 锚定 | 底层生息资产来源 |
|---|---|---|
| **UETH** | ETH | wstETH 等 ETH 类生息资产 |
| **UUSD** | USD | sUSDS / sUSDe / aUSDC 等美元收益资产 |
| **UBNB** | BNB | slisBNB / asBNB 等 BNB 类生息资产 |

**锚定的含义：1 枚 uAsset 始终对应 1 单位底层资产价值。** 1 UETH 对应 1 ETH 的价值，1 UUSD 对应 1 美元，1 UBNB 对应 1 BNB。这一对应按面值记账：铸造按实时价值足额换算，赎回按仓位比例销债，兑换按面值双向进出。

> 注意：这里的"稳定币"指**相对底层资产保持稳定价值**，而非锚定法币。UUSD 是美元稳定币；但 UETH、UBNB 锚定的是 ETH、BNB，会随底层资产价格波动 —— 它们是 ETH/BNB 计价的稳定凭证，不是法币稳定币。

## 锚定是怎么做到的

uAsset 有三条供给路径，彼此独立：

- **创世质押铸造**：存入生息资产，按其当前价值面值铸出 uAsset（价值 1 ETH 的 wstETH → 1 UETH）。同族的不同生息资产按各自实时价值换算，汇入同一个 uAsset，流动性不再碎片化。详见[创世质押](staking-modes.md)。
- **PSM 储备兑换**：用 USDC、USDT、ETH、BNB 等储备资产，按 1:1 面值双向兑换 uAsset。兑换池由协议持有的储备逐额背书。详见 [PSM 锚定兑换](psm.md)。
- **杠杆创世供给**：Memeverse 侧杠杆创世的债务额度也会铸成 uAsset 进入创世，由协议统一结算（详见[杠杆创世](../memeverse/polend.md)）。

<iframe src="../assets/diagrams/uasset-supply.html" loading="lazy" style="width:100%;height:800px;border:1px solid #e5e7eb;border-radius:8px" title="uAsset 三条供给路径"></iframe>

## 铸币上限，防止超发

每个仓位管理器与每个 PSM 兑换池都有**铸造额度上限**：未偿铸币量不能超过设定额度。铸造时增加额度占用，赎回（销毁 uAsset）时释放。这是 uAsset 作为稳定币的保障之一 —— 有上限、可审计、不会无限增发。

## 全链流通

uAsset 基于 **LayerZero OFT** 标准，可在不同链之间 1:1 流转。你可以在一条链铸出 UUSD，跨到另一条链上使用。详见 [跨链与速率限制](omnichain.md)。

## uAsset 在生态中的角色

uAsset 不只是 OutStake 的产物，它是整个 Outrun 的价值媒介：

- **Memeverse 创世资金**：启动 Memecoin 时用 uAsset 注入流动性。
- **杠杆创世利息**：在 Memeverse 加杠杆时，uAsset 作为利息支付币。
- **创世积分结算**：积分型杠杆也以 uAsset 计价。
- **USR 储蓄**：闲置的 uAsset 可以存进储蓄金库吃利息（详见 [USR 储蓄](usr.md)）。

OutStake 铸造，uAsset 流向 Memeverse，构成生态资本循环的起点。

## 举例

> 用户有 5 个 wstETH(Lido)，当时每个约值 1.05 ETH，合计约 5.25 ETH。他在 OutStake 创世质押，铸出约 5.25 UETH（锚定 ETH）。抵押的 wstETH 在仓位里继续生息，敞口全归他；需要时归还等值 UETH 即可赎回。同族的不同生息资产按各自实时价值换算，汇入同一个 UETH，流动性不再碎片化。
>
> 另一位用户手里只有 USDC：他经 PSM 按面值换成 UUSD（扣一笔小额兑换费），直接去参与 Memeverse 创世，全程不建仓位。
