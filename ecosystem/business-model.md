# Business model

## Value proposition

Outrun serves two needs within a single closed loop:

- **Yield-bearing asset holders**: they want a unified, liquid, cross-chain stablecoin (uAsset), and they want their assets to keep growing in value.
- **Memecoin communities**: they want a fair, rug-resistant launchpad that builds lasting value, not a zero-sum casino.

Within Outrun, the two needs meet through uAsset. OutStake supplies uAsset; Memeverse creates its uses and its activity.

## Revenue streams

Outrun's revenue comes from real economic activity inside the ecosystem, not from token-emission subsidies:

| Revenue stream | Description |
|---|---|
| **Trading fees (protocol fee)** | The protocol fee on every Memeverse trading fee, including dynamic fees, pool-opening decay fees, and Preorder settlement fees |
| **Leveraged Genesis interest** | The uAsset interest paid by leverage participants, which accrues to the protocol treasury at Genesis lock |

There is also the **settlement reserve** (not revenue): it is funded from liquidity deployment balances and covers leverage settlement shortfalls; whatever goes unused stays in reserve and never enters a treasury.

Key characteristic: **revenue is positively correlated with ecosystem activity** — the more trading and the more leverage, the higher the revenue, moving in the same direction as the flywheel.

## Don't mix up the three treasuries

Outrun has three distinct pools of funds, each with different beneficiaries. Don't conflate them:

| Treasury | Source of funds | Beneficiary / controller |
|---|---|---|
| **Memecoin staking YieldVault** | Trading fees denominated in Memecoin | Memecoin stakers (share price appreciation) |
| **DAO treasury** | Trading fees denominated in uAsset | The community (spending decided by proposal votes) |
| **Protocol treasury** | uAsset interest from leveraged Genesis | Kept by the protocol (not community-governed) |

**Note**: interest from leveraged Genesis goes to the **protocol treasury**, not to the Memeverse community's DAO treasury. The two are separate pools with separate controllers. All of these proceeds are distributed inside Memeverse and **never flow back to OutStake participants** (OutStake participants earn yield on their collateral exposure plus USR savings interest; see the [growth flywheel](flywheel.md)).

## Where a single payment goes (the core)

This is the key to understanding Outrun's economic model. A single Memecoin trading fee splits along **two orthogonal dimensions**:

**Dimension 1: the split between LPs and the protocol** (a percentage split of the fee)
- LPs take 65%, the protocol takes 35%.
- If a referrer is involved, the referral rebate is carved out of the protocol's 35% (by default equal to 10% of the total fee), leaving the protocol treasury with about 25%.

**Dimension 2: routing by denomination** (where the protocol's share goes depends on which token the fee is denominated in)
- **uAsset-denominated** → the DAO treasury. Within this, 0.25% of the primary pool's uAsset fees (the current default) goes to the executor who triggers distribution, as the executor reward.
- **Memecoin-denominated** → the Memecoin staking YieldVault (for stakers)
- **POL-denominated** → burned directly (deflationary)

Stack the two dimensions and you have the complete journey of one fee:

<iframe src="../assets/diagrams/fee-split.html" loading="lazy" style="width:100%;height:800px;border:1px solid #e5e7eb;border-radius:8px" title="Where a trading fee goes"></iframe>

One more detail:
- During the Locked phase, part of the protocol fee on the auxiliary pools (POL/uAsset, PT/uAsset, PT/POL) is also shared with **standard Genesis participants** (pro rata by share); the rest goes to the DAO treasury.

## Where the revenue goes

- **Flowing back to Memeverse participants**: staker yield (Memecoin fees), the standard Genesis share (auxiliary-pool fees), DAO epoch rewards (uAsset fees), and referral rebates, keeping the ecosystem attractive to participants over time.
- **Retained by the protocol**: treasury reserves, ongoing development, and a risk buffer.

Returning most of the revenue to ecosystem participants is the economic foundation that lets Memeverse's internal flywheel reinforce itself.

## Key resources

- **uAsset liquidity**: the bedrock of the entire ecosystem. The deeper the liquidity, the better every feature works.
- **Multi-protocol adapters**: the variety of yield-bearing assets OutStake integrates determines how wide uAsset supply can reach.
- **Memecoin communities**: activity in Memeverse drives uAsset consumption and yield production.
- **Mechanism safety**: guardrails such as dynamic fees, lock-ups, and the settlement reserve are what trust is built on.

## Customers and participants

By risk appetite there are three tiers. **Conservative**: stake on OutStake to mint uAsset, plus standard Genesis; after a successful unlock, exit fully within the 24-hour protection window, with uAsset principal conserved. **Balanced**: leveraged Genesis plus Preorder, with interest as the only cost. **Co-build**: buy and stake Memecoin, take part in DAO governance, and participate deeply as a co-builder. There are also specialized roles such as launchers, LPs, and executors. See [participation modes and risk appetite](playbooks.md).

## Sustainability

Traditional DeFi often attracts liquidity with token-emission subsidies, which cannot last. Outrun's revenue comes from real trading and leverage activity, and most of it flows back to ecosystem participants, forming a positive loop. As long as the ecosystem is running, revenue keeps coming; the more prosperous the ecosystem, the more revenue. The business model and the growth flywheel point the same way.
