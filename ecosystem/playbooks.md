# Participation and risk appetite

Outrun does not have a single entry point or a single way to play. People with different risk appetites take entirely different paths through the ecosystem. The rest of this page walks through the **three tiers**: who each tier suits, how to participate, what you earn, and what you risk, with worked examples in concrete numbers.

## The big picture: pick your position by risk

| Tier | What you want to do | Main participation | Yield sources | Downside risk |
|---|---|---|---|---|
| **Conservative** | Preserve principal, earn yield | Prepare uAsset via OutStake + standard Genesis | Collateral keeps earning with exposure retained + YT + auxiliary-pool fees | **No risk within the product model** (full exit inside the protection window) |
| **Balanced** | Amplify early exposure | Leveraged Genesis + Preorder | YT + settlement residual value + Preorder allocation | Interest cost only |
| **Co-build** | Participate deeply in a community | Buy the Memecoin + stake + DAO governance | Staking fees + epoch rewards + governance rights + price upside | Memecoin price volatility |

> **A note on standard Genesis**: standard Genesis carries no risk within the product model. The uAsset you commit is conserved inside the four-pool portfolio, and the Memecoin is newly minted upside on top of principal. After the Verse (the Memecoin's launch instance) unlocks successfully, users who fully unwind LP, PT, POL, and YT within the 24-hour liquidity protection window restore their uAsset principal pro rata. See [standard Genesis](../memeverse/genesis.md) for details.
>
> Note: the underlying yield-bearing assets (such as wstETH and sUSDS) still carry the risks of their own protocols. If Lido, Aave, or another underlying protocol runs into trouble, it propagates to uAsset. That risk is inherent to holding any yield-bearing asset; it is not a risk of Outrun's mechanics.

---

## Conservative: preserve principal and earn yield (no risk within the product model)

**Profile**: you hold yield-bearing assets such as ETH, stablecoins, or BNB, want extra yield on a principal-conserving basis, and prefer not to bear the cost of holding a Memecoin directly.

**How to participate (two steps, both risk-free within the product model):**

1. **Prepare uAsset** (pick one of three, depending on what you hold):
   - Yield-bearing assets → mint uAsset through [Genesis Staking](../outstake/staking-modes.md); the collateral keeps earning and the exposure stays with you.
   - Only reserve assets such as USDC, ETH, or BNB → [swap directly through PSM](../outstake/psm.md), with no position created.
   - Idle uAsset with no Genesis plans for now → park it in [USR to earn interest](../outstake/usr.md); deposit and withdraw anytime.
2. **Standard Genesis**: commit uAsset to a Memecoin's Genesis and pick up extra yield at no risk within the product model.

**Why standard Genesis is risk-free (the core mechanics):**
- **100% of the uAsset you commit goes into the four pools** (primary pool 70% + auxiliary pools 30%), and the Memecoin is **newly minted**.
- **uAsset is conserved inside the four-pool portfolio**: the auxiliary-pool uAsset, together with the primary-pool uAsset behind PT and behind POL, covers the principal.
- After the Verse unlocks successfully, the four pools pause public trading for 24 hours. With the pools static, users can claim and fully unwind auxiliary-pool LP, PT, POL, and YT, recovering the uAsset principal they committed, pro rata.
- When the protection window ends, the four pools resume trading. Any portfolio positions not yet unwound then move with the market, at the user's own risk.
- If Genesis fails, the full amount is refunded.
- On the upside, a rising Memecoin pays you extra through YT and auxiliary-pool shares.

**Yield:**
- On the OutStake side: the collateral keeps earning (exposure retained), or USR savings interest.
- On the standard Genesis side: an **auxiliary-pool fee share** (cash flow as long as the Memecoin trades) plus **YT** (which adds more when the Memecoin rises).
- In short, the more the Memecoin rises, the more you earn. Even if it goes to zero, a full exit inside the protection window still returns your uAsset principal pro rata, and the auxiliary-pool fees accumulated along the way are extra yield on top.

**Worked example**:
> Suppose a user holds wstETH worth 10 ETH. Through Genesis Staking on OutStake they mint about 10 UETH. The wstETH collateral keeps earning inside the position with the exposure retained; the position has no lock-up and can be redeemed anytime. This step anchors principal to ETH and has nothing to do with any Memecoin.
>
> The user then swaps part of that UETH into UUSD (or uses UETH directly) and commits 2000 UUSD to a Memecoin's standard Genesis. If Genesis misses its target, the full amount comes back. If it succeeds, the 2000 UUSD enters the four pools, and a rising Memecoin adds value through YT and auxiliary-pool shares. Even if the Memecoin goes to zero, the user can still fully exit the portfolio within the 24-hour liquidity protection window after the successful unlock and recover the 2000 UUSD principal pro rata. Anything not unwound after the window closes is at the user's own market risk.

---

## Balanced: amplify early exposure

**Profile**: you are bullish on a particular Memecoin and willing to bear a defined cost to scale up your share during Genesis and chase outsized returns.

**How to participate**:
1. **Leveraged Genesis**: pay interest in uAsset (or GenesisCredit) to amplify your Genesis allocation.
2. Add a **Preorder** on top to lock in more early allocation at a fixed low fee.

**Yield:**
- Leverage: you receive leveraged YT in proportion to the interest paid; if the Memecoin rallies hard at settlement, you take a proportional share of the settlement residual value, which can be substantial.
- Preorder: settles at a fixed 1% fee, with the Memecoin unlocking linearly.

**Downside risk**: **interest cost only**. Leveraged Genesis commits no principal; you pay interest in exchange for allocation, so the most you can lose is the interest paid. A deep Memecoin crash only takes the YT and residual value to zero (loss = interest already paid); there is no way to lose more. **No liquidation risk** (no oracle dependency, no way to end up owing anything). If Genesis fails, the interest is refunded in full.

**Worked example**:
> Suppose a user is strongly bullish on a Memecoin and uses leveraged Genesis: they pay 500 UUSD of interest and, at the going rate (assume it corresponds to 5x amplification), receive a Genesis allocation worth about 2500 UUSD. A Preorder locks in more on top. Once the Memecoin is locked, the user receives leveraged YT in proportion to the interest paid; if the price rallies at settlement, they take a sizable share of the settlement residual value.
>
> The cost: the 500 UUSD of interest goes to the protocol treasury upon locking. If the Memecoin goes to zero, the loss is that 500, with no liquidation and no debt left owing. If Genesis misses its target, the 500 UUSD is refunded in full.

---

## Co-build: deep participation in a community

**Profile**: you believe in a Memecoin community's long-term value, are willing to hold the Memecoin directly, and help build it through staking and governance.

**How to participate**:
1. After the Memecoin lists, **buy the Memecoin** on the open market.
2. **Stake the Memecoin into the YieldVault** to earn trading fees.
3. **Delegate** voting power to your own shares, take part in DAO proposals and votes, and help decide the treasury and the community's direction (see [Memecoin Staking](../memeverse/memecoin-staking.md)).

**Yield:**
- **Staking yield**: the Memecoin's trading fees (the portion denominated in Memecoin) flow continuously into the YieldVault, and the share price appreciates.
- **Epoch rewards**: DAO rewards claimed at each epoch settlement, in line with how active you are in governance.
- **A voice in governance**: decide how treasury funds are used and where the community goes.
- **Price upside**: hold the Memecoin directly and benefit when the price rises.

**Downside risk**: **you hold the Memecoin directly and bear its price volatility** (this is the only tier whose principal is exposed to the Memecoin price). A sharp drop shrinks the position's value. Continuous fee earnings from staking plus governance incentives turn pure speculation into long-term community building.

**Worked example**:
> After a Memecoin lists, a user buys it and stakes it in the YieldVault. The more actively the Memecoin trades, the more fees flow into the YieldVault; the share price keeps climbing, and redemption typically returns more Memecoin than was staked. The shares also carry voting power: the user joins proposals (say, deciding to use treasury UUSD for a community airdrop) and claims the epoch rewards each epoch. The cost is holding the Memecoin directly and bearing its price volatility, but what the user is buying into is the community's long-term value, using staking plus governance to turn speculation into community building.

---

## Other roles

Beyond the three participation tiers, the ecosystem has a few specialized roles:

| Role | What they do | What they earn |
|---|---|---|
| **Launcher** | Launch a Memecoin on multiple chains and set its rules | Community consensus (liquidity cannot be pulled during the lock-up) |
| **Liquidity provider (LP)** | Add liquidity in uAsset + the Memecoin after it lists | A share of LP trading fees |
| **Executor** | Anyone who triggers fee distribution | An executor reward of 0.25% of primary-pool uAsset fees (current default) |

---

## You can combine them

The three tiers are not mutually exclusive. One user can do all of the following at once:
1. Mint UETH through Genesis Staking on OutStake (**Conservative**)
2. Use that UETH for standard Genesis and pick up Memecoin yield at no risk (**Conservative**, full exit inside the protection window)
3. Amplify with leverage plus a Preorder on the ones they believe in most (**Balanced**)
4. Buy and stake after listing, and co-build through the DAO (**Co-build**)

The design of Outrun lets all of these moves chain together inside a single uAsset system: people with different needs each take what they want from the same infrastructure, and together they feed the flywheel.
