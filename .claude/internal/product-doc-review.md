# OutrunBook 产品文档审查清单（临时）

### D-01 `P0` 缺少部署状态、入口和合约地址

- 状态：`TODO`
- 问题：用户无法判断内容属于设计、测试网还是主网，也缺少支持链、产品入口、部署地址和版本。
- 完成条件：建立版本化 deployments/status 页面，并由发布流程维护。

### D-02 `P0` 缺少集中风险、权限和可升级性披露

- 状态：`TODO`
- 问题：owner 可配置参数、pause、oracle、keeper、LayerZero、upgradeability 等信任面散落或缺失。
- 完成条件：建立统一风险与权限页面，各功能页只保留本流程特有风险并链接过去。

### D-04 `P1` 缺少审计与实现版本关联

- 状态：`TODO`
- 问题：即使列出审计，也需标明报告对应 commit、部署和未覆盖变更。
- 完成条件：审计页可从报告追踪到目标 commit 和部署版本。

### D-07 `P2` 发布流程基线漂移检查

- 状态：`已完成`
- 修订：`scripts/check-baseline.sh` 已建并接入 CLAUDE.md（仓库关系表手动提醒已指向脚本）；发布前运行 `bash scripts/check-baseline.sh`，漂移则更新 CLAUDE.md 对齐 commit（全 hash）并复核受影响机制页。
- 完成条件：发布清单实际执行一次基线检查并记录结果；脚本对漂移返回非零退出码。
- 执行记录（2026-08-19）：
  - 漂移复现（更新前）：`bash scripts/check-baseline.sh` → `MemeverseV2 落后 50 提交 / OutStakeV2 落后 66 提交`，`exit 1`，符合“漂移返回非零”要求（`scripts/check-baseline.sh:46-54`）。
  - 基线对齐：`CLAUDE.md:11-12` 已更新至 `MemeverseV2 6994d7bab186b456db119348d9c262feaec196fb`（`6994d7b chore(lint): ignore test paths...`）/ `OutStakeV2 61f11bc682c7ccb30995b9c0981c9d9eccae8d9f`（`61f11bc test(deploy): skip router-default test...`）。
  - 复核结果（`22332ef..6994d7b` / `daf4aaa..61f11bc` 区间）：主要为 harness/CI/slither 基线、OZ `ReentrancyGuardTransient`、UUPS 代理化、`PoolManager` 探针重构等内部实现与 NatSpec 同步，已在 `docs/spec` 层同步（`MemeverseV2:9d37682`）；OutrunBook 用户文档层面唯一可感知变更为 `a8c89fe GenesisCredit pause`，已补 `memeverse/genesis-credit.md: 新增“暂停与恢复”`（用户语言，不涉函数名），其余四池比例、费用流向、24h 保护、YT 报价等关键决策未变。
  - 重新校验（更新后）：`bash scripts/check-baseline.sh` → `MemeverseV2 OK / OutStakeV2 OK`，`check-baseline: 全部对齐，通过。`，`exit 0`。
  - 补充（2026-08-19）：`memeverse/genesis-credit.md` 新增暂停说明后重跑 `bash scripts/check-absolute-words.sh` 通过（30 组合 `exit 0`），确认未引入需白名单的绝对词。
  - 执行记录（2026-08-29，深度对齐 `6994d7b..768b957` / `61f11bc..76d0b7d`）：
    - 漂移复现（更新前）：两仓库落后基线（MemeverseV2 落后 57 提交 / OutStake 落后 59 提交），`exit 1`。
    - 基线对齐：`CLAUDE.md:11-12` 更新至 `MemeverseV2 768b957db21816be720836f137bc41c2f4a7fce1` / OutStake `76d0b7d8ed3ab023f0587e6ca4c0a131ff8e6d54`；同时修正两处事实——OutStake 磁盘目录已由 `OutStakeV2` 重命名为 `OutStake`；OutStakeV2 现有 `docs/spec/`（此前记为"无 spec"）。
    - 本轮产品级修订（其余上游变更均为索引器/运维/内部加固层，用户文档不动）：
      - `outstake/sy-adapters.md`：Sky L2 计价由"PSM3 挂钩"改为"SSR 跨链镜像计价 + 与 PSM3 报价互校（偏差超当前 1% 上限暂停）"；异常清单补两路价格偏差。
      - `outstake/omnichain.md`：跨链示例链 Arbitrum → Base（产品链集合 Ethereum/BSC/Base）。
      - `memeverse/memecoin-staking.md`：提交赎回申请即销毁份额、按当时价值锁定、等待期不增值、投票权立即消失。
      - `memeverse/dao-governance.md`：国库单次支出上限不可经预授权绕过（非收益库 spender 的 approve 提案执行即拒）。
      - `memeverse/genesis.md` + `memeverse/lifecycle.md`：烧 POL 当场拆解主池 LP 须设最低到账与截止时间（旧无保护入口回滚 `SlippageProtectionRequired`）。
      - `outstake/router.md`：原生币（ETH/BNB）存入预览含约 0.5% 保守余量（50 bps 贴现），实际到账通常不低于预览。
      - `reference/faq.md`：新增误转代币找回 FAQ（部分合约支持协议方 sweep，非全部可找回）。
    - 核对未变项：四池 70/30、POL 2:3:2、PT 1:2、LP 65/35、返佣默认 10%、激励划拨 25%、锁定约 365 天、赎回延迟 1 天、5 笔上限、执行者 0.25%、暂停跨链不对称、退款退受益人（代付语义：付款方自付资金、受益人记名，与新 `TransferFromNotCaller` 守卫一致）。
    - 重新校验：`check-baseline` 两仓库 OK（`exit 0`）；`check-absolute-words` 30 组合通过（`exit 0`）。

## 图片与图示任务

> **2026-08-29 起：本节 I-01～I-10 与「暂不新增图片」已由 `.claude/internal/diagram-plan.md`（v2，经代码红队核验）取代，勿按本节执行。** 已知本节数字错误：I-09「默认 50%」实为默认 25%。

当前公开文档主要依赖 5 张 Mermaid 图，没有独立图片资产。先补解释机制和风险的图，不制作装饰图或未定版前端截图。

### I-01 `P0` 普通 Genesis 资金流与最终权益图

- 状态：`TODO`
- 页面：`memeverse/four-pools.md`，并由 README、lifecycle、pol-splitter 链接。
- 内容：uAsset 70/30；主池 POL 的 2/7、3/7、2/7；PT 的后续分配；budget 与 actual spend；普通用户最终收到的三类 LP、residual、YT/fee 权益。
- 目标：替换“本金守恒/原数拿回”的错误心智模型。

### I-02 `P0` OutStake 债务闭环图

- 状态：`TODO`
- 页面：`outstake/staking-modes.md`。
- 内容：deposit -> position/debt -> draw 增债 -> 持有或使用 uAsset -> reacquire -> burn uAsset -> redeem SY；并列 lock、wrap、keeper 分支。
- 目标：让用户在 draw 前理解未来赎回所需资产。

### I-03 `P0` 跨链失败状态图

- 状态：`TODO`
- 页面：Memeverse 和 OutStake 的 omnichain 页面。
- 内容：source send、`lzReceive`、`lzCompose`、retry、裸币 fallback、recoverable failure、不可恢复 failure；标注源链和目标链余额变化。
- 目标：区分发送、mint、质押三个成功状态。

### I-04 `P0` 生命周期与门槛图更新

- 状态：`TODO`
- 页面：`memeverse/lifecycle.md`。
- 内容：OR 门槛、preorder 排除、`flashGenesis`、permissionless `changeStage`、`endTime`、实际 unlock tx 和其后 24 小时。
- 目标：用户可以根据链上数值判断下一阶段和退款路径。

### I-05 `P1` 质押、委托、投票和赎回双流程图

- 状态：`TODO`
- 页面：`memeverse/memecoin-staking.md`。
- 内容：`deposit -> shares -> delegate -> votes`；`requestRedeem -> 1 day -> executeRedeem`；旁注空 vault burn、virtual share 吸收和最多 5 个请求。

### I-06 `P1` POLend 结算瀑布图

- 状态：`TODO`
- 页面：`memeverse/polend.md`。
- 内容：recover -> repay debt -> bounded dust reserve -> residual，或 reserve 不足 -> revert -> 补充后重试。

### I-07 `P1` Hook 费率组件与默认衰减曲线

- 状态：`TODO`
- 页面：`memeverse/hook.md`。
- 内容：launch fee decay、price impact、3 秒地址批次、EWVWAP 方向条件；所有数字标“当前默认、owner 可改”。
- 禁止：画“攻击者必亏”或“普通用户必得最低费率”的效果图。

### I-08 `P1` Preorder 聚合成交与归属图

- 状态：`TODO`
- 页面：`memeverse/preorder.md`。
- 内容：多用户资金 -> 聚合为主池第一笔 swap -> 1% fee -> 按资金比例分配统一平均成交结果 -> custody/vesting -> claim。

### I-09 `P1` DAO 周期奖励流程图

- 状态：`TODO`
- 页面：`memeverse/dao-governance.md`。
- 内容：cast vote -> 90 日周期 -> permissionless finalize -> 默认 50% reward ledger -> 按票数比例 claim -> 未领取余额回卷。

### I-10 `P2` 参与路径选择泳道图

- 状态：`TODO`
- 页面：`ecosystem/playbooks.md` 或 `reference/participation-map.md`。
- 内容：按目标、可承受锁定、需要持有的资产、主动操作、退出条件选择普通 Genesis、杠杆、preorder、staking、LP。
- 前置：M-01、M-02、M-03、O-01、O-02 修订完成后再画，避免固化错误叙述。

## 暂不新增图片

- `memeverse/yt-flash-swap.md` 已有两张 Mermaid 时序图；补报价、滑点、MEV、capacity 注释即可。
- 不添加装饰性生态插画。
- 不添加真实产品截图，直到 UI、网络和部署版本稳定且可持续更新。
