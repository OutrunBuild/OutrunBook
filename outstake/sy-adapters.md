# SY：标准化收益与适配器矩阵

## SY 是什么

各类生息代币长得都不一样：Aave 的 aToken、Lido 的 wstETH、EtherFi 的 weETH、Sky 的 sUSDS……它们来自不同协议，记账方式不同，支持的兑换资产也不同。

**SY（Standardized Yield，标准化收益）** 是 OutStake 给这些生息代币套上的一层统一外壳。无论底层是哪个协议，SY 对外都呈现同一种形态：存入资产得到 SY、用 SY 赎回资产、随时可查它当前值多少底层资产。

这样，上层（uAsset 的铸造、质押、跨链）就不必为每个协议单独适配，只对接 SY 一层即可。

## 支持哪些协议

每接入一个协议，就配一个对应的 SY 适配器。当前已支持：

| 协议 | 生息代币 | 底层资产 |
|---|---|---|
| **Aave V3** | aToken（如 aUSDC） | 美元 |
| **Lido** | wstETH | ETH |
| **EtherFi** | weETH | ETH |
| **Sky** | sUSDS | 美元 |
| **Ethena** | sUSDe | 美元 |
| **Lista** | slisBNB | BNB |
| **Aster** | asBNB | BNB |

其中 Lido、Sky 在 L2 上通过 oracle 读取 L1 汇率，因此各有 L1 与 L2 两个版本。

## 灵活的进出

SY 适配器接受多种输入：你可以直接用底层资产(ETH、USDC、BNB)进入，也可以用已有的生息代币(wstETH、sUSDS)进入，部分适配器还支持跨币种（例如在 L2 上用 USDC 进入 Sky）。适配器内部完成所有换算，你不需要自己处理。

## 为什么这样设计

- **统一流动性**：同类底层资产（如 ETH 类的 wstETH / weETH）汇入同一个 uAsset(UETH)，不再各建各的池子。
- **可扩展**：新增协议只需加一个适配器，不影响已有逻辑。
- **入口友好**：用户用手里已有的任意支持资产就能参与，无需提前换成特定代币。
