# Participation at a glance

The tables on this page tie together the classification schemes scattered across earlier chapters, so you can see at a glance, for each risk appetite: which staking mode, which Genesis mode, whether to Preorder, and whether to enter the DAO.

## Three participation tiers × specific modes

| Tier | OutStake staking mode | Memeverse Genesis mode | Preorder | DAO governance | Principal risk |
|---|---|---|---|---|---|
| **Conservative** | Genesis Staking to mint uAsset (or PSM swap, USR savings) | standard Genesis | Optional | No direct participation | **No risk within the product model** (full exit within the protection window) |
| **Balanced** | Mint uAsset and pay interest | leveraged Genesis | Yes | No direct participation | Interest cost; a Memecoin crash |
| **Co-build** | Not necessarily via OutStake | (buy after listing) | Not necessarily | Buy and stake Memecoin, vote on proposals | Holds Memecoin directly; price volatility |

> "No direct participation" means the Conservative and Balanced tiers hold yield claims (YT, auxiliary-pool fees, settlement residual value), not Memecoin shares with voting power. Only the Co-build tier enters the DAO, by staking Memecoin and delegating voting power.
>
> On principal: on the OutStake staking side the principal stays pegged to the underlying asset; on the standard Genesis side, the uAsset committed is conserved within the four-pool portfolio. After a Verse unlocks successfully, users must unwind all portfolio claims within the 24-hour liquidity protection window to restore principal pro rata. See [standard Genesis](../memeverse/genesis.md).

## A user's full path (example)

The example follows one DeFi user from cautious beginnings to deep participation, tying all the actions together:

1. In OutStake, **Genesis Staking** of wstETH → mint UETH (**Conservative**: principal stays pegged, collateral keeps earning)
2. Bridge part of the UETH cross-chain, or swap it for UUSD, and join a Memecoin's **standard Genesis** → a risk-free shot at the upside (**Conservative**, full exit within the protection window)
3. For the ones they believe in most, **leveraged Genesis + Preorder** with UUSD to amplify early share (**Balanced**)
4. Once the Memecoin lists, buy and **stake it into the YieldVault** → earn fees, gain voting power, participate in the DAO (**Co-build**)

All four steps can run at the same time, chained together within a single uAsset system.

## POL / PT / YT redemption timeline

Memeverse has three claim tokens. When each one pays out, and into what, is easy to mix up; the table below lines them up:

| Token | When acquired | When redeemable | Redeems into | Risk profile |
|---|---|---|---|---|
| **POL** | At Genesis lock-up (primary-pool LP, representing a share of the locked liquidity) | After unlock | Burn POL to redeem primary-pool liquidity (Memecoin + uAsset), or trade it | Tracks the Memecoin price |
| **PT** (Principal Token) | From splitting POL; enters the auxiliary pools as LP at deployment | After the unlock settlement | uAsset at par (1 PT = 1 uAsset) | Pegged to uAsset, but PT sits mostly in the auxiliary pools and is not issued directly to standard Genesis participants |
| **YT** (Yield Token) | From splitting POL; allocated to standard/leveraged Genesis participants pro rata by capital | Tradeable during the lock-up (Flash Swap); redeemable pro rata after the unlock settlement | A pro-rata share of the post-settlement residual assets (uAsset + Memecoin) | Bets on the Memecoin rising; no yield if it goes to zero |

Key points:
- During the lock-up period, POL can be split into PT + YT, or merged back into POL.
- **At four-pool deployment, PT goes mostly into the auxiliary pools as the LP asset**, not directly to standard Genesis participants as a principal-protected claim. Standard Genesis participants receive **YT + a share of auxiliary-pool fees + auxiliary-pool liquidity shares after unlock**.
- The principal uAsset committed in standard Genesis is conserved within the four-pool portfolio. After a successful unlock, the four pools pause public trading for 24 hours; users who unwind LP, PT, POL, and YT within that window restore their principal pro rata. A failed Genesis gets a full refund. See [standard Genesis](../memeverse/genesis.md).
- YT is a bet on the settlement surplus from a rising Memecoin price: the more it rises, the larger the share; if it does not rise, YT can go to zero.
- Leveraged Genesis participants mainly receive YT (a bet on the upside).
- During the lock-up, YT can be bought and sold using POL via Flash Swap (see [YT Flash Swap](../memeverse/yt-flash-swap.md)), without waiting for settlement; the post-settlement redemption rules are unchanged.

For more, see [standard Genesis](../memeverse/genesis.md), [POL split](../memeverse/pol-splitter.md), and [launch lifecycle](../memeverse/lifecycle.md).
