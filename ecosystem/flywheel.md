# The growth flywheel

## The core of the flywheel

Outrun's two modules, OutStake and Memeverse, are connected through uAsset, but **not by yields flowing back and forth between them**. The connection is the **interlock of uAsset supply and demand**: OutStake is the supply side of uAsset; Memeverse is where it gets used. The deeper uAsset liquidity runs, the better both sides work.

> ⚠️ A common misconception: that the money earned in Memeverse flows back to OutStake stakers. **It does not.** Participants in each module earn their own returns (see "Independent yield loops" below). The flywheel's axle is uAsset liquidity, not yields flowing back.

## The main flywheel: a two-way interlock of uAsset supply and demand

The flywheel is not a one-way transmission; it is a **two-way interlock**, with the supply side and the use side powering each other:

```
        ┌───────── supply drives use ──────────┐
        ▼                                      │
OutStake (supply)                             Memeverse (use)
mint uAsset ──── deeper uAsset liquidity ────► smoother Genesis / fuel for leverage / smoother cross-chain flow
   ▲                                          │
   │  more use → holding uAsset is worth      │  generates trading and
   │  more → stronger minting and staking     │  leverage activity
   └────────── use drives supply ─────────────┘
```

**Supply drives use**: the more OutStake supplies, the deeper uAsset liquidity runs → the more smoothly Memeverse launches Memecoins (Genesis well funded, cross-chain transfers flow freely) → more uses for uAsset emerge.

**Use drives supply**: Memeverse makes uAsset useful, above all through [standard Genesis](../memeverse/genesis.md). Standard Genesis lets users pursue Memecoin-ecosystem returns under the principal-conserving model: YT plus auxiliary-pool fees, and a full exit inside the 24-hour protection window after a successful unlock. That is uAsset's core draw over an ordinary stablecoin. Holding uAsset carries extra value → more people are willing to mint and stake on OutStake → supply grows.

The two ends feed each other: Memeverse's prosperity makes uAsset useful; uAsset being useful drives more people to mint on OutStake; and the uAsset they mint makes Memeverse launches run more smoothly. That is how the flywheel reinforces itself.

## OutStake's growth comes from Memeverse

OutStake is not a standalone LST wrapper; its growth comes precisely from the uses Memeverse creates.

- Without Memeverse, OutStake would merely unify various yield-bearing assets into uAsset: useful, but lacking a distinctive growth engine.
- It is Memeverse that gives uAsset real uses (Genesis, leverage, settlement, the treasury). Holding uAsset thus offers one thing an ordinary stablecoin does not: a risk-free shot at Memecoin returns (standard Genesis: exit completed inside the protection window, principal conserved). That is what gives OutStake a lasting reason to attract supply.

The reverse holds as well: **without OutStake, Memeverse has no stablecoin fuel**. No funding for Genesis, no interest for leverage, no unit of account for settlement. Each module is incomplete on its own; together they close the loop.

## Independent yield loops

Participants in the two modules **earn their own returns**; yields do not flow back and forth:

**OutStake participants** earn yield on their collateral and savings interest:
- Genesis Staking: the yield-bearing asset posted as collateral keeps earning, and the exposure stays entirely with the user.
- USR savings: idle uAsset earns at the per-family rate.
- PSM swaps generate no yield; PSM is the at-par entry and exit channel.

**Memeverse participants** earn from trading and leverage activity in the Memecoin ecosystem. Each trading fee is split at fixed ratios among:
- liquidity providers (LPs)
- standard Genesis participants (a share of auxiliary-pool fees)
- Memecoin stakers (fees denominated in Memecoin)
- the DAO treasury (fees denominated in uAsset)
- fees denominated in POL are **burned** directly

Interest from leveraged Genesis goes to the protocol treasury (not the DAO treasury). All of these yields circulate and are distributed **inside Memeverse**; none flows back to OutStake.

**Yields do not flow back, but uAsset supply and demand bind the two modules tightly together**: OutStake stakers never receive Memeverse fees, yet the more prosperous Memeverse becomes, the more useful uAsset gets, and the stronger OutStake's pull.

## Memeverse's internal flywheel

Memeverse has positive loops of its own:

- More trading → more fees → higher Memecoin staking yield → greater willingness to hold → steadier liquidity → more trading.
- Fees denominated in uAsset flow into the DAO treasury → epoch rewards → governance participation → community health → a more valuable Memecoin.

## The acquisition engine: referral rebates

A portion of the protocol's share of trading fees is paid out as referral rebates, rewarding the referrers who bring in new users: referral → the new user trades → the referrer earns a rebate → more referrals. Rebates are funded from fees already collected, with nothing extra minted, so they keep feeding new users into the flywheel on a sustainable basis.

## The flywheel's guardrails

For the flywheel to keep turning, it needs protection built into the mechanisms:

- **Dynamic fees + high fees at pool opening**: counters front-running and sandwich attacks, keeping the trading market healthy.
- **Liquidity lock-up + Genesis refund**: guards against rug pulls and protects participant trust.
- **Settlement reserve**: tops up only the bounded integer-rounding gaps in leverage settlement, and only within the current balance and the configured cap. If the balance falls short, the unlock settlement reverts and can be retried once the reserve is replenished.
- **uAsset mint caps + PSM swap caps + cross-chain rate limits**: prevent over-issuance, keep any single pool from being drained, and block abnormal outflows, protecting the stablecoin's credibility.

## The flywheel in full

Outrun's flywheel is not a loop of yields flowing back. It is a **two-way interlock of uAsset supply and demand plus independent yield loops within each module**: OutStake supplies the omnichain stablecoins, Memeverse creates the uses and the activity, and uAsset liquidity binds the two tightly together, each with self-contained economic incentives. The longer the flywheel turns, the deeper uAsset liquidity grows, the more prosperous the Memeverse ecosystem becomes, and the deeper the moat.
