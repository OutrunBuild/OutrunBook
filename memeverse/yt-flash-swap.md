# YT Flash Swap

## A trading channel for YT during the lock-up

Memeverse does not run a separate trading pool for YT, but YT is tradable during the lock-up: **YT Flash Swap** reuses the liquidity of the PT/POL pool, so you can buy YT with POL or sell YT back into POL. The channel is always open, but that does **not mean any size can be filled**: feasibility and execution price are decided by the state of the pool at execution time (see Protection and safety below). The entire swap completes in a single atomic transaction. The funds needed for the leg swap are advanced temporarily by the pool and returned before the transaction ends. The round trip is invisible to the user, hence the name "flash".

Standard and leveraged Genesis participants receive **YT** (the yield token) once Genesis locks, but it cannot be redeemed per share before the unlock settlement. Holders who want to cash out early, and users who want to enter partway through the lock, both come and go through this channel.

## How YT is priced: YT = POL − PT

YT pricing rests on one fixed rule: **1 POL = 1 PT + 1 YT** (both split and merge are 1:1).

From this follows the implied price of YT:

> **Implied price of 1 YT (in POL) = 1 POL − the market price of 1 PT**

This relationship is a **theoretical derivation**: grounded in the 1:1 split/merge, it shows where YT's value is anchored, but it is not a promise that you can trade at that price. The real execution price is decided by the pool state at the moment of execution (see Protection and safety below).

Because PT has a market price in the PT/POL pool, YT's implied price is determined along with it, and no separate pool is needed for YT. The closer PT trades to POL par (the more confidently the market expects the principal to be repaid), the cheaper YT tends to be; the deeper PT's discount, the more expensive YT tends to be. In essence, YT is the market's pricing of the **settlement residual value** (what remains of the settlement recovery after the PT principal reserve is deducted; see [POL split](pol-splitter.md)). The higher the expected residual value, the more expensive YT.

## Buying YT (with POL)

You specify the exact amount of YT to buy, **y**, and set a maximum-pay cap. Everything completes in one atomic transaction:

1. **Sell y PT for POL**: y PT are sold at the market price in the PT/POL pool for an amount of POL (call it R). At this point those y PT are "borrowed": you hold no PT yet, so you owe the pool y PT.
2. **Split to cover**: you put up y POL to **split**, receiving y PT + y YT. Those y POL come from two places: the money you actually pay, plus the R from selling PT in step 1.
3. **Repay the borrowing**: the y PT produced by the split repay the y-PT debt to the pool from step 1.
4. **Delivered**: the y YT are yours.

<iframe src="../assets/diagrams/yt-flash-buy.html" loading="lazy" style="width:100%;height:800px;border:1px solid #e5e7eb;border-radius:8px" title="Buy YT: borrow PT → split → repay PT"></iframe>

**What you actually pay = y − R**. The intuition: owning y YT outright would take y POL (to split), but the y PT that come out of the split can be sold back for R POL to cover part of the cost, so you only make up the difference y − R. The more PT is worth (the larger R), the less you top up, and the cheaper YT is for you.

> That is what "flash" means: the PT borrowed in step 1 is repaid before the transaction ends (in step 3). If the books fail to balance along the way (fees or slippage, say), the **entire transaction rolls back unchanged**, and not a cent of your money moves.

## Selling YT (into POL)

You specify the exact amount of YT to sell, **y**, and set a minimum-receive floor. Everything completes in one atomic transaction:

1. **Buy y PT**: an amount of POL (call it Q) is spent in the PT/POL pool to buy y PT. That POL is also "borrowed": you owe the pool Q POL up front.
2. **Merge back into POL**: **merge** the y PT just bought with your y YT, turning them back into y POL.
3. **Repay the borrowing**: Q of those y POL repays the POL debt to the pool from step 1.
4. **Delivered**: the remaining y − Q POL is yours.

<iframe src="../assets/diagrams/yt-flash-sell.html" loading="lazy" style="width:100%;height:800px;border:1px solid #e5e7eb;border-radius:8px" title="Sell YT: buy PT → merge → repay POL"></iframe>

**What you actually receive = y − Q**. The intuition: to turn YT back into POL, each YT needs a matching PT to merge with. Buying those y PT costs Q POL and the merge yields y POL, so you net y − Q. The more expensive PT is (the larger Q), the less you net.

## YT is a leveraged asset

When you buy y YT, you pay only the small difference (y − R), yet you take on the **full** settlement residual-value exposure of y shares. Every small move in the residual value translates into a large move in YT returns. This is what makes it a leveraged long on the Memecoin's settlement residual value. If the call is right, gains are amplified; if it is wrong, losses are amplified just the same. If the Memecoin crashes and the residual value falls short, YT goes to zero.

## Fees: one underlying trade, one fee

Each Flash Swap involves only one real underlying PT/POL trade, so it is charged once, with no extra routing fee or platform fee, and the fee rules are exactly those of a normal PT/POL swap (dynamic fees, EWVWAP exemption, the 65/35 allocation, referral rebates).

Note the cost structure of leverage, though: fees are calculated on the full size of the PT leg, while the principal you actually pay is only the difference. The cheaper YT is (the higher the leverage), the larger the same fee rate becomes relative to your principal. That is the cost of a leveraged instrument, not a hidden charge.

## The two operations

| Operation | What you specify | What you get |
|---|---|---|
| Buy YT with POL | The exact YT amount + a maximum-pay cap | Exactly that many YT, with only the actual cost taken |
| Sell YT into POL | The exact YT amount + a minimum-receive floor | At least the floor amount of POL |

Mind the semantics: buying means "receive exactly the specified amount of YT", not "spend the whole budget for as much YT as possible". If you set a cap of 100 and only 60 is needed, the remaining 40 stays in your wallet; nothing extra is bought.

## Protection and safety

- **Slippage and price protection**: buys carry a maximum-pay cap and sells a minimum-receive floor. You can also set a price-protection limit with an expiry; breaching it rolls back the whole transaction.
- **Quotes are indicative only**: the price you see before trading is a reference price based on the on-chain state at that moment, **not a guaranteed execution price**. The actual fill price is decided by the state at the moment of execution and can be better or worse. Front-running (MEV) or market moves can push the fill away from the reference price. As long as it stays within your protection limit, the trade still executes at the worse price; beyond the limit, the whole transaction rolls back. For large orders, set a tight price-protection limit and execute promptly.
- **Single atomic execution**: all or nothing. The transaction either completes in full or rolls back to the last cent, so there is no "charged but no YT delivered" and no "YT gone but nothing received".
- **No pre-deduction, no refunds**: a buy only pulls the actual cost; the cap is a guardrail.
- **Clean failure**: due to fees, rounding, and pool depth and capacity, some target amounts may have no feasible execution price. The transaction simply reverts; just retry or adjust the amount. You lose nothing.
- **Session precondition**: if the wallet is not a smart account, no session is open, or the session initiator and the transaction sender are not the same wallet, the transaction reverts outright, with no loss of funds.
- **POL only**: the channel does POL ↔ YT only and does not support routing through other tokens.

## Who can use it, and when

- **YT holders** (standard and leveraged Genesis participants): anyone wanting to cash out early during the lock-up can sell YT.
- **Bullish users**: buying YT with POL is a leveraged long on the settlement residual value at a fraction of the price. The better the Memecoin's settlement outcome, the more YT is worth; a deep crash can take it to zero.
- Available only during that Memecoin's **Locked phase**: after unlock or settlement, split/merge closes, Flash Swap becomes unavailable with it, and the settlement-redemption rules take over again.
- The transaction must be initiated by a **smart account**. A plain wallet (an account without deployed contract code, such as a common browser-extension wallet) cannot complete this swap directly; use a smart-account wallet such as Safe. The whole swap wraps three steps, open session → execute swap → close session, into one atomic transaction. The session is wrapped automatically by the frontend and is invisible to the user. If no session is open, or the session initiator and the transaction sender are not the same wallet, the transaction reverts outright, with no loss of funds. This is a uniform requirement of Memeverse's trading layer.

## Division of labor with settlement redemption

Flash Swap is the early entry-and-exit channel of the lock-up. It changes when YT can be bought and sold; it does not change the settlement rules: after the unlock settlement, YT still receives its pro-rata share of the remaining assets, and if the Memecoin goes to zero, YT earns nothing.

## Examples

> After a certain Memecoin's Genesis locks, PT trades at roughly 0.9 POL and YT's implied price at roughly 0.1 POL. A user buys 10,000 YT with 1,000 POL (maximum-pay cap set), taking on full exposure to the settlement residual value of 10,000 shares for a fraction of the price: for every 0.01 POL that the settlement residual value comes in above expectations, the user earns an extra 100 POL (about 10% of the principal). If the residual value falls short, the loss is amplified just the same. If the Memecoin crashes and the residual value declines, YT's value declines with it.
>
> Another user holding Genesis YT wants to cash out while demand is hot: they set the minimum-receive floor and sell 10,000 YT. The system buys an equal amount of PT at the market price, merges it with the user's YT back into POL, deducts the portion owed to the pool, and transfers the net POL to the user's wallet, all in one transaction. If the fill price would fall below the expected floor, it rolls back automatically.
