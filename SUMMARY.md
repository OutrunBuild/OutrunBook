# Table of contents

> OutrunBook —— Outrun 生态面向用户的产品文档。中文撰写，术语保留英文。

---

## Overview

* [Outrun 概览](README.md)
  —— 双模块生态：OutStake（收益基础设施）+ Memeverse（全链社区共识启动器），uAsset 是连接血线
* [产品愿景](vision.md)
  —— Outrun 要解决什么、为何是这两个模块、uAsset 作为统一价值媒介的意义

## OutStake — 收益基础设施

* [OutStake 概览](outstake/README.md)
  —— 把多协议生息资产统一铸成锚定型稳定币 uAsset；含「为什么不直接持 wstETH」
* [SY 标准化收益与适配器矩阵](outstake/sy-adapters.md)
  —— 统一接口包装 Aave/Lido/EtherFi/Sky/Ethena/Lista/Aster 的生息代币
* [uAsset 锚定型稳定币](outstake/uasset.md)
  —— UETH/UUSD/UBNB 的锚定机制、铸币上限、跨链流通
* [双质押模式：锁仓与包装](outstake/staking-modes.md)
  —— 锁仓吃增值 vs 包装求流动；含共享池偿付模型
* [提取增值](outstake/draw-uasset.md)
  —— 锁仓期内把生息增值提前变成 uAsset
* [Keeper 代偿](outstake/keeper.md)
  —— 锁定超时达到一定时间后协议代为赎回，增值归仓位主人
* [一站式操作入口](outstake/router.md)
  —— 从任意代币到质押/赎回的全链路聚合
* [跨链与速率限制](outstake/omnichain.md)
  —— uAsset 全链流通与安全约束

## Memeverse — 全链社区共识启动器

* [Memeverse 概览](memeverse/README.md)
  —— 启动的不是代币，而是拥有流动性、收益与治理的链上社区
* [启动生命周期](memeverse/lifecycle.md)
  —— 创世 → 锁定/退款 → 解锁的完整流程
* [普通创世 Genesis](memeverse/genesis.md)
  —— uAsset 本金守恒、24 小时流动性保护与完整退出步骤
* [四池流动性模型](memeverse/four-pools.md)
  —— 主池 + 三个辅助池的资金结构与手续费归属
* [动态费率 Hook](memeverse/hook.md)
  —— 基于 Uniswap V4 的抗操纵交易层（EWVWAP 豁免、防夹、开池保护）
* [预购 Preorder](memeverse/preorder.md)
  —— 创世前提前锁定 Memecoin，固定费率结算，线性解锁
* [杠杆创世 POLend](memeverse/polend.md)
  —— 付利息放大创世份额，无清算风险
* [POL 拆分：PT 与 YT](memeverse/pol-splitter.md)
  —— 把 POL 拆成本金（PT）与收益（YT）两种凭证
* [YT 闪电兑换 Flash Swap](memeverse/yt-flash-swap.md)
  —— 锁定期内用 POL 买卖 YT，复用 PT/POL 池
* [创世积分 GenesisCredit](memeverse/genesis-credit.md)
  —— 可跨链的参与凭证，用于抵扣杠杆利息
* [Memecoin Staking](memeverse/memecoin-staking.md)
  —— 质押赚交易手续费，委托后获得治理权
* [Memecoin DAO 治理](memeverse/dao-governance.md)
  —— 社区共治国库与方向，周期激励，投机转化为建设
* [跨链互操作](memeverse/omnichain.md)
  —— 多链启动、跨链质押与收益聚合
* [vs Pump.fun](memeverse/vs-pump-fun.md)
  —— 与 Pump.fun 的机制维度对比

## Ecosystem — 生态协同

* [增长飞轮](ecosystem/flywheel.md)
  —— uAsset 供需双向咬合 + 各模块独立收益闭环（非收益回流）
* [参与方式与风险偏好](ecosystem/playbooks.md)
  —— 稳健 / 平衡 / 共建三档参与路径与举例
* [商业模式](ecosystem/business-model.md)
  —— 收入来源与一笔交易费的完整流向
* [目标受众](ecosystem/audience.md)
  —— 不同角色在生态中的需求与参与方式

## Reference — 参考

* [术语表](reference/glossary.md)
  —— 核心术语速查
* [参与方式总览](reference/participation-map.md)
  —— 三档参与 × 各模式主映射表 + POL/PT/YT 兑付时间线
* [FAQ](reference/faq.md)
  —— 常见问题
