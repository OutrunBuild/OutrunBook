# Outrun

> 统一生息资产，启动链上共识。

Outrun 是一个全链 DeFi 生态，由两个互为驱动的模块组成：

- **OutStake** —— 收益基础设施。把 Aave、Lido、Sky、Ethena、Lista、Aster 等多协议的生息资产统一，铸成锚定型稳定币 **uAsset**(UETH / UUSD / UBNB)。
- **Memeverse** —— 全链社区共识启动器。普通、杠杆与预购汇入一次公平发射；Memecoin 上线即拥有四池流动性、可拆分交易的 PT/YT、质押收益与 DAO 治理。

两个模块并非简单并列 —— **uAsset 是连接它们的血线**：OutStake 铸造 uAsset，Memeverse 在创世与杠杆中消耗 uAsset，两端通过 uAsset 的供需互相咬合。资本在闭环里被反复利用，而不是躺在 isolated 的池子里。

---

## OutStake — 把生息资产统一成稳定币

不同协议的生息代币（aToken、wstETH、sUSDS、sUSDe……）各自为政，收益和流动性都被切碎。OutStake 用一层标准化接口把它们统一，铸成可在全链流通的 uAsset 稳定币。

三种参与方式：

- **创世质押**：存入生息资产，按当前价值面值铸出 uAsset（本金等值），铸出的 uAsset 直接送进 Memeverse 创世；抵押的资产继续生息，敞口全归你。无利息、无清算、无锁定期，仓位随时可赎回。
- **PSM 兑换**：用 USDC、USDT、ETH、BNB 等储备资产，按 1:1 面值直接换 uAsset。不建仓位、不产生债务。
- **USR 储蓄**：闲置的 uAsset 存进储蓄金库吃利息，随存随取。

详见 [OutStake 概览](outstake/README.md)。

## Memeverse — 让社区共识长成一个国度

Memeverse 让任何人在多条链上同时启动一个 Memecoin，上线即同时拥有三套引擎：

- **公平发射**：没有 Creator 特权、没有预分配。普通、杠杆与预购参与汇入同一次公平创世，达标即建四池，主池锁定 365 天。
- **收益代币化**：锁定的主池流动性拆分为 PT（本金）与 YT（收益），让未来现金流成为当下即可交易的资产，并以此建立 POLend（杠杆创世）市场。
- **质押与 DAO 治理**：交易手续费流向质押者与社区国库；质押并委托后获得治理权，社区按周期领取激励。

详见 [Memeverse 概览](memeverse/README.md)。

---

## uAsset：连接两个模块的血线

uAsset（UETH / UUSD / UBNB）是 Outrun 的锚定型稳定币体系，分别锚定 ETH / USD / BNB，基于 LayerZero OFT 可跨链流转：

<iframe src="assets/diagrams/ecosystem-bite.html" loading="lazy" style="width:100%;height:800px;border:1px solid #e5e7eb;border-radius:8px" title="双模块咬合：uAsset 是血线"></iframe>

- OutStake 端：质押生息资产，铸出 uAsset。
- Memeverse 端：uAsset 作为创世资金、杠杆利息、创世积分的支付币被消耗。
- 两端咬合：Memeverse 让 uAsset 有用 → 持有它有价值 → 更多人去 OutStake 铸造；OutStake 供给越足 → Memeverse 启动越顺。**收益不互相回流**，各自独立闭环（详见[增长飞轮](ecosystem/flywheel.md)）。

uAsset 让"生息"与"启动"不再是两件事，而是同一个资本循环的两端。

---

## 这份文档怎么读

| 你是 | 建议路径 |
|---|---|
| 第一次了解 Outrun | 本文 → [产品愿景](vision.md) → [OutStake 概览](outstake/README.md) → [Memeverse 概览](memeverse/README.md) |
| 想参与质押 / 铸 uAsset | [OutStake](outstake/README.md) 各章 |
| 想启动 / 参与 Memecoin | [Memeverse](memeverse/README.md) 各章 |
| 关注生态经济模型 | [增长飞轮](ecosystem/flywheel.md) → [商业模式](ecosystem/business-model.md) |
| 想对比同类产品 | [vs Pump.fun](memeverse/vs-pump-fun.md) |
