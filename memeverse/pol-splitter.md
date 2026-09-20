# POL split: PT and YT

## What POL is

Once Genesis reaches its target, the liquidity committed to the primary pool gets locked, and a token called **POL** is minted to represent ownership of that locked liquidity. POL itself can be traded (see the POL/uAsset pool).

## Split: one becomes two

If you hold POL, you can **split** it into two tokens:

- **PT (Principal Token)**: represents the claim on the principal.
- **YT (Yield Token)**: represents the claim on future yield.

The split is 1:1: however much POL you split, you receive the same amount of PT and the same amount of YT. During the lock-up period you can also merge them back into POL (splitting and merging are no longer available after unlock or settlement).

## How PT and YT differ

| | PT (principal) | YT (yield) |
|---|---|---|
| Represents | Claim on the principal | Claim on the yield |
| Anchoring | Anchored to uAsset at a fixed ratio | Shares the post-settlement residual value |
| Risk profile | Plays it safe, locking in the principal's value | Chases upside, betting on yield growth |
| Suited for | Users who want to lock in a stable value early | Users who are bullish on the Memecoin |

## Redemption only after settlement

Splitting itself is available during the lock-up period, but **redemption** has to wait until the Genesis unlock and the protocol's unified settlement:

- **PT redemption**: swap back into uAsset (a stablecoin) at par (1 PT = 1 uAsset).
- **YT redemption**: receive a pro-rata share of the assets left over after settlement (uAsset and Memecoin). The larger the residual value, the more each YT is worth. Intuitively: at settlement the protocol recovers total assets and deducts the PT principal reserve. What remains is the residual value, and YT's value is that residual value distributed in proportion to the YT you hold. The more the Memecoin rises, the more settlement recovers, the more is left after the principal, and the more YT is worth. If the Memecoin falls sharply, the residual value may be small or even zero.

## Trading YT during the lock-up period

During the lock-up period, YT already has a place to trade: **YT Flash Swap** lets you buy YT with POL or sell YT back into POL (see [YT Flash Swap](yt-flash-swap.md)). It reuses the PT/POL pool's liquidity to execute the swap instead of running a separate YT trading pool. After the unlock settlement, YT still redeems its pro-rata share of the settlement residual value.

## Who actually receives PT / YT

This is where readers most often get confused, so read it closely:

- **Standard Genesis participants** receive **YT**, a share of the auxiliary-pool trading fees during the lock-up period, and their auxiliary-pool liquidity after unlock. For how these claims together cover the principal, see [standard Genesis](genesis.md).
- **Leveraged Genesis participants** receive **YT** in proportion to the interest they paid, betting on the upside.
- **PT**: when the four pools are deployed, PT goes mostly into the auxiliary pools (PT/uAsset and PT/POL) as LP assets. PT has a clear use of its own: it trades in the PT/uAsset pool and redeems uAsset at par after settlement. That suits stability-minded users who want to lock in the principal's value. But it is **not the principal claim issued to standard Genesis participants**; what they receive is the YT plus auxiliary-pool shares described above.

In other words, taking part in Genesis does not directly give a standard Genesis participant any PT. PT mostly sits in the auxiliary pools and passes to standard Genesis participants as auxiliary-pool LP after unlock. The yield claim a standard Genesis participant receives directly during the Locked phase is mainly YT. See [standard Genesis](genesis.md) and [participation overview](../reference/participation-map.md).

## Why split

Splitting lets one piece of liquidity serve two kinds of users at the same time:

- Those who want stability and to cash out early: hold PT or sell it.
- Those who want leveraged yield exposure and are bullish on the upside: hold YT.

It also supplies the tradable asset for the PT/uAsset and PT/POL pools among the four pools, letting the principal and the yield each carry an independent market price.

## How this relates to leveraged Genesis

Leveraged Genesis participants receive YT in proportion to the interest each of them paid (see [leveraged Genesis](polend.md)). In other words, the people adding leverage hold the yield claim (YT) and go after the settlement surplus a rising Memecoin produces. That is exactly where the leveraged return comes from.
