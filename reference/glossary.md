# 术语表

Outrun 文档中常见术语的速查。专有词保留英文，解释用中文。

## 核心概念

| 术语 | 含义 |
|---|---|
| **uAsset** | Outrun 的锚定型稳定币，分 UETH（锚定 ETH）、UUSD（锚定 USD）、UBNB（锚定 BNB）。由 OutStake 铸造，全链流通。 |
| **SY** | Standardized Yield，把各类生息代币统一包装的标准层。 |
| **OFT** | Omnichain Fungible Token，基于 LayerZero 的全链代币标准，uAsset、Memecoin、创世积分都基于它。 |
| **LayerZero** | 跨链消息与资产传输协议，Outrun 全链能力的底层。 |

## OutStake

| 术语 | 含义 |
|---|---|
| **锁仓质押(Lock)** | 存入生息资产即铸出 uAsset（本金等值），本金继续生息，可随时提取增值，到期赎回。 |
| **质押锁仓期** | OutStake 锁仓质押的锁定期，天数由用户自选，可选档位以界面为准（例如 90 天）。 |
| **流动性锁定期** | Memeverse 创世达标后的流动性锁定，固定约 365 天，期间项目方无法抽走。 |
| **包装质押(Wrap)** | 把生息资产投入共享池，无锁定期，即时进出。 |
| **提取增值** | 锁仓期内把生息资产的增值部分提取成 uAsset。 |
| **keeper** | 锁定超时达到一定时间后协议代为赎回仓位的机制。 |
| **收益收割** | 协议从包装质押共享池收取超债务的增值收益。 |
| **铸币上限** | 每个质押管理器铸 uAsset 的额度上限，防超发。 |

## Memeverse

| 术语 | 含义 |
|---|---|
| **创世(Genesis)** | Memecoin 启动的初始阶段，参与者用 uAsset 参与。 |
| **四池** | 创世达标时建立的四个流动性池：主池(Memecoin/uAsset)、POL/uAsset、PT/uAsset、PT/POL。 |
| **POL** | 锁定流动性的所有权凭证。 |
| **PT** | 本金代币，POL 拆分而来，代表本金索取权，锚定 uAsset。 |
| **YT** | 收益代币，POL 拆分而来，代表收益索取权，杠杆资产，结算后按份额赎回残值。 |
| **YT Flash Swap（YT 闪电兑换）** | 锁定期内用 POL 买卖 YT 的交易通道，复用 PT/POL 池流动性，不设独立 YT 池。 |
| **POL 拆分** | 把 1 个 POL 拆成 1 个 PT + 1 个 YT。 |
| **POLend（杠杆创世）** | 付利息（uAsset 或创世积分）放大创世份额的机制。 |
| **Preorder（预购）** | 创世前提前锁定 Memecoin，固定低费率结算，线性解锁。 |
| **动态费率 Hook** | 基于 Uniswap V4 的交易层，费率随波动与冲击动态调整。 |
| **GenesisCredit（创世积分）** | 可跨链的参与凭证，用于抵扣杠杆创世利息。 |
| **Memecoin Staking** | 把 Memecoin 质押进收益库，赚交易手续费收益。 |
| **YieldVault（收益库）** | Memecoin Staking 的 ERC-4626 收益库。 |
| **DAO Governor** | 每个 Memecoin 社区的链上治理合约，管理提案、投票、国库。 |
| **结算** | 锁定期满后，协议统一回收资金、偿还债务、分配剩余的过程。 |
| **创世退款** | 创世未达标时，参与者资金退还给参与记录的受益人。 |
