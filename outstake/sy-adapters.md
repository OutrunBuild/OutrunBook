# SY：标准化收益与适配器矩阵

## SY 是什么

各类生息代币长得都不一样：Aave 的 aToken、Lido 的 wstETH、EtherFi 的 weETH、Sky 的 sUSDS……它们来自不同协议，记账方式不同，支持的兑换资产也不同。

**SY（Standardized Yield，标准化收益）** 是 OutStake 给这些生息代币套上的一层统一外壳。无论底层是哪个协议，SY 对外都呈现同一种形态：存入资产得到 SY、用 SY 赎回资产、正常情况下随时可查它当前值多少底层资产。

这样，上层（uAsset 的铸造、质押、跨链）就不必为每个协议单独适配，只对接 SY 一层即可。

## 支持哪些协议

每接入一个协议，就配一个对应的 SY 适配器。当前已支持：

| 协议 | 生息代币 | 底层资产 | 可存入 | 可赎出成 |
|---|---|---|---|---|
| **Aave V3** | aToken（如 aUSDC） | 美元 | aToken 或底层资产（如 USDC） | aToken 或底层资产 |
| **Lido** | wstETH | ETH | wstETH、stETH 或原生 ETH | wstETH 或 stETH |
| **EtherFi** | weETH | ETH | weETH、eETH 或原生 ETH | weETH 或 eETH |
| **Sky** | sUSDS | 美元 | sUSDS 或 USDS | sUSDS 或 USDS |
| **Ethena** | sUSDe | 美元 | sUSDe 或 USDe | 仅 sUSDe |
| **Lista** | slisBNB | BNB | slisBNB 或原生 BNB | 仅 slisBNB |
| **Aster** | asBNB | BNB | asBNB、slisBNB 或原生 BNB | 仅 asBNB |

其中 Lido、Sky 各有 L1 与 L2 两个版本，L2 版本的价格来源不同：Lido 在 L2 上的汇率来自以太坊主网的汇率源；Sky 则通过 PSM3 稳定模块与美元挂钩，不依赖该汇率源。L2 版本的「可存入」「可赎出成」以对应链实际支持的资产为准（例如 Sky L2 还接受 USDC 进入）。

正常情况下，L2 上的汇率随时可查、按主网价值换算。若汇率源短暂异常或 L2 排序器停机，依赖实时汇率计价的操作（如铸造、提取增值、包装池赎回）会暂时不可用，恢复后自动恢复正常，无需额外操作。汇率源由协议方维护，必要时可更换。

## 灵活的进出

进入的路子很多：你可以直接用底层资产（ETH、USDC、BNB）进入，也可以用已有的生息代币（wstETH、sUSDS）进入，部分适配器还支持跨币种（例如在 L2 上用 USDC 进入 Sky）。适配器内部完成所有换算，你不需要自己处理。

**但能存进去什么，不等于能原样取回什么。** 赎回时最终到手的代币，以上表「可赎出成」为准：部分协议赎回只给出生息代币本身（如 Ethena 只给 sUSDe、Aster 只给 asBNB、EtherFi 给 weETH 或 eETH），不会自动拆回底层资产。想拿回底层资产，需自行到对应协议解押。

各协议的兑换汇率由对应协议官方提供（如 Aave 借贷利率、Lido 质押汇率、EtherFi 流动性池），随市场实时变化。

## 为什么这样设计

- **统一流动性**：同类底层资产（如 ETH 类的 wstETH / weETH）汇入同一个 uAsset(UETH)，不再各建各的池子。
- **可扩展**：新增协议只需加一个适配器，不影响已有逻辑。
- **入口友好**：用户用手里已有的任意支持资产就能参与，无需提前换成特定代币。
