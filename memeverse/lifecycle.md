# Launch lifecycle

A Memecoin passes through a few clearly defined stages from launch to circulation. This page walks through them in order: what happens in each stage, and who can do what.

## Phases at a glance

<iframe src="../assets/diagrams/verse-lifecycle.html" loading="lazy" style="width:100%;height:800px;border:1px solid #e5e7eb;border-radius:8px" title="Memecoin lifecycle: from Genesis to steady state"></iframe>

### Phases × available operations

| Operation | Availability |
|---|---|
| Join Genesis (standard or leveraged), Preorder | Genesis only |
| Refund claim (once per address) | Refund only |
| Claim YT (standard or leveraged), claim auxiliary-pool fee share, claim accumulated LP fees, add liquidity and mint POL, claim Preorder allocation (linear), trigger fee distribution, stake Memecoin | From Locked |
| YT split / merge | Locked only |
| Public trading | From Locked (paused during the 24-hour protection window at unlock) |
| Burn POL to redeem, one-time claim of auxiliary-pool LP plus residual POL/PT, redeem PT for uAsset, claim YT residual value | From Unlocked |

## 1. Genesis

The launcher sets the rules (which chains, the initial pricing, the minimum raise), and Genesis opens.

- Participants deposit uAsset to join **standard Genesis**, the base participation mode.
- Those who are bullish can **leverage up** with uAsset or GenesisCredit, amplifying their share on top of standard Genesis (paying interest).
- Anyone can also lock in Memecoin early through **Preorder**: a separate settlement track that can be combined with standard or leveraged Genesis.
- Standard Genesis capital, leverage interest, and Preorder funds are accounted for separately and never combined for the success check.

This stage is where consensus gathers: who joins early and how much they commit determine the Memecoin's starting size.

### How Genesis meets its threshold

Genesis reaches its success threshold if either condition holds:

```text
standard Genesis capital >= minimum success threshold
or
leverage interest >= minimum success threshold
```

The two thresholds are evaluated independently; the amounts are not added together. Neither Preorder funds nor the leverage debt principal derived from the leverage interest counts toward the threshold.

The three amounts serve different purposes:

| Bucket | How it is computed | What it is used for |
|---|---|---|
| Success check | Standard Genesis capital or leverage interest independently reaches the minimum success threshold | Decides whether the launch proceeds to Locked or Refund |
| Pool funding | Standard Genesis capital + leverage debt principal | Builds the four-pool liquidity after a successful Genesis |
| Preorder funds | Tracked separately | Buys Memecoin in one aggregated order once the primary pool is live; takes no part in the success check or the initial four-pool funding |

Advancing to the next phase requires an on-chain transaction to trigger it; it does not happen automatically over time:

- With **Fast Genesis** enabled, the phase can be triggered as soon as either threshold is met, before the deadline, moving the launch into Locked early.
- Without Fast Genesis, even if a threshold is met early, the trigger waits until the Genesis deadline has passed.
- When triggered after the deadline: either threshold met means Locked; neither threshold met means Refund.

## 2. Locked: Genesis met its threshold

When standard Genesis capital or leverage interest independently reaches the minimum success threshold and the phase advance has been triggered, Genesis succeeds and the launch enters the Locked phase:

- The protocol deploys **four-pool liquidity**, pairing the Memecoin with uAsset to open a real trading market.
- The liquidity is locked for **365 days** (a hard constraint enforced by the contract). No party can withdraw the funds during the lock-up, so the classic "pull the liquidity" rug path is cut off.
- The Memecoin trades on a protected market (see the [dynamic fee Hook](hook.md)).

**Once Locked, each type of participant can claim and act:**

| Who | What they can do |
|---|---|
| Standard Genesis participants | Claim initial YT (the yield rights) and the auxiliary-pool fee share |
| Leveraged Genesis participants | Claim leveraged YT |
| Anyone | Add uAsset + Memecoin as liquidity, mint POL to become an LP, and earn fees |
| Memecoin holders | Stake Memecoin into the YieldVault and earn fee yield |
| LPs | Claim accumulated LP fees |
| Preorder participants | Claim Memecoin progressively on a linear unlock schedule |
| Executors | Trigger fee distribution and earn an executor reward of 0.25% of the primary pool's uAsset fees (current default) |

**What the guarantees cover**: liquidity during the lock-up period. What they block is the pull-liquidity rug path. The protocol team retains administrative powers: Genesis parameters (minimum success threshold, initial pricing, and so on) can be adjusted before the Genesis decision, fee defaults are configurable by the protocol, and the protocol itself remains upgradeable. These powers do not change the constraint that the funds are locked, but they sit within the protocol team's administrative scope.

## 3. Refund: Genesis missed its threshold

After the Genesis deadline, if neither standard Genesis capital nor leverage interest has independently reached the minimum success threshold, the triggered phase advance sends the launch into Refund:

- The uAsset deposited by standard Genesis participants is returned to the beneficiary recorded on the participation record.
- The interest paid by leveraged Genesis participants is refunded as well (uAsset interest refunded in uAsset, GenesisCredit interest in GenesisCredit).
- Preorder funds are refunded in full.
- No one loses principal.
- When someone else paid for a participation, the refund still goes to the beneficiary on the participation record, not to the payer's account.

Joining Genesis **carries no risk of a failed raise**: the launch advances only if the threshold is met, and everything is refunded in full if it is not.

## 4. Unlocked

When the lock-up period ends, the launch enters the Unlocked phase, and each type of participant exits and settles:

| Who | What they can do |
|---|---|
| POL holders | Burn POL to redeem primary-pool liquidity (Memecoin + uAsset) |
| Standard Genesis participants | Make a one-time claim of auxiliary-pool LP shares plus the residual POL/PT allocation |
| PT holders (auxiliary-pool LPs) | Redeem PT for uAsset (PT mostly serves as auxiliary-pool LP liquidity, not as a principal claim for standard Genesis participants) |
| YT holders | Receive their share of the residual value after settlement (uAsset + Memecoin) |
| Leveraged participants | Claim settlement residual value in proportion to the interest they paid |

Once the launch instance (the Verse) has actually entered Unlocked and unified settlement has completed, a **24-hour liquidity protection window** opens. The four pools pause public trading during the window, but claiming entitlements, removing liquidity, and redeeming PT/YT/POL stay open. Standard Genesis participants can therefore exit their principal while the pools are static. When redeeming POL and splitting the primary-pool liquidity into Memecoin and uAsset on the spot, you must set a minimum output amount and a deadline as slippage protection. The operation is rejected if either is missing. When the window closes, the four pools resume public trading, and any price or liquidity outcome of holding or exiting after the window is on the user. See [Standard Genesis](genesis.md).

From there the Memecoin settles into steady-state operation: trading keeps generating fees, stakers keep earning, and DAO governance keeps running.

## Example: one Memecoin's full life

> The launcher of a Memecoin opens Genesis on 3 chains, with a minimum success threshold of 50,000 UUSD.
> - **The three buckets**: standard Genesis capital comes to 60,000 UUSD and leverage interest to 20,000 UUSD; the leverage debt principal derived from that interest is 200,000 UUSD; Preorder funds are 80,000 UUSD.
> - **Success check**: standard Genesis capital of 60,000 UUSD already meets the threshold on its own, so Genesis succeeds; leverage interest and Preorder funds are not added to it. With Fast Genesis enabled, the phase could be triggered right then; otherwise it waits for the deadline.
> - **Pool funding and Preorder**: initial four-pool funding is 60,000 of standard Genesis capital + 200,000 of leverage debt principal, 260,000 UUSD in total. The 80,000 UUSD of Preorder funds is kept separate for the aggregate buy after the primary pool goes live.
> - **Locked**: the four pools are deployed and the Memecoin goes live; LPs add liquidity to the primary pool and earn fees. Standard Genesis participants claim YT and the auxiliary-pool fee share; leveraged participants claim leveraged YT; anyone holding the Memecoin can stake it in the YieldVault for fee yield.
> - **Unlocked**: the lock-up ends and unified settlement completes; standard Genesis participants claim auxiliary-pool LP shares plus the residual allocation and exit their principal within the 24-hour liquidity protection window. After the window, free trading resumes, stakers keep earning fees, and DAO governance keeps running.
> - **A failed launch**: standard Genesis capital of 30,000 UUSD, leverage interest of 30,000 UUSD, Preorder funds of 200,000 UUSD. The three together exceed 50,000, but neither success threshold is met independently. After the deadline, the triggered phase advance sends the launch into Refund, and the three groups are refunded from their respective ledgers.

The whole lifecycle is orchestrated by on-chain rules: phase advances are triggered by public on-chain transactions, and both the state and the accounting of funds are verifiable.
