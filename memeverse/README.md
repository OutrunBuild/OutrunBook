# Memeverse at a glance

> The omnichain community consensus launcher: what gets launched is not a token, but an on-chain community with its own liquidity, yield, and governance.

## What is Memeverse

Most people treat Memecoins as gambling chips. Memeverse sees it differently.

A Memecoin can rally millions of people behind a single symbol, but today it runs as a casino: pumps turn into dumps, the price goes to zero once the hype fades, and consensus earns no yield, no governance, and no treasury.

**What Memeverse does is give community consensus an engine that runs itself**: once a Memecoin launches here, it comes with deep liquidity, ongoing yield rights, and community governance rights.

## Three engines

Fair launch builds the market, yield tokenization keeps capital earning, and stakers decide their own community's next move:

1. **Fair launch**: no Creator privileges, no pre-allocation. Standard, leveraged, and Preorder participation all flow into the same fair Genesis; once the target is met, the four pools are created and the primary pool is locked for 365 days. See [standard Genesis](genesis.md), [leveraged Genesis](polend.md), and [Preorder](preorder.md).
2. **Yield tokenization**: the locked primary-pool liquidity is split into PT (Principal Token) and YT (Yield Token), turning future cash flows into assets tradable today. The POLend (leveraged Genesis) market is built on top of them. See [POL split](pol-splitter.md), [leveraged Genesis](polend.md), and [YT Flash Swap](yt-flash-swap.md).
3. **Staking and DAO governance**: trading fees are distributed to stakers and the DAO treasury. Staking plus delegation grants governance rights. The community claims epoch rewards, and the treasury is governed by the community. See [Memecoin Staking](memecoin-staking.md) and [DAO governance](dao-governance.md).

The third engine routes trading fees to stakers and the DAO treasury: the more active the trading, the more resources the community has at its disposal. See [DAO governance](dao-governance.md).

## Who takes part, and how

- **Launchers**: launch a Memecoin on multiple chains at the same time, with each chain raising funds and building pools independently; no entry threshold, no Creator privileges.
- **Genesis participants**: commit uAsset in [standard Genesis](genesis.md) to earn additional returns under the principal-conserving model; they can also add leverage to amplify their share, or lock in Memecoin early through a Preorder.
- **Stakers / governors**: after launch, stake Memecoin into the YieldVault to earn fee income; delegate to gain DAO voting power and help build the community.

People with different risk appetites have different participation paths. See [Participation and risk appetite](../ecosystem/playbooks.md).

## uAsset's role in Memeverse

uAsset (the stablecoin minted by OutStake) is the fuel Memeverse runs on:

- **Genesis funding**: when a Memecoin launches, participants' uAsset goes into the liquidity pools.
- **Leverage interest**: in leveraged Genesis, interest is paid in uAsset (or GenesisCredit).
- **Settlement denomination**: unified settlement and principal redemption are both denominated in uAsset.
- **Treasury income**: the uAsset-denominated portion of a Memecoin's trading fees flows into that Memecoin's DAO treasury, governed by the community.

OutStake mints uAsset, Memeverse consumes it, and this is how consensus flows.

## Core concepts

| Concept | In one sentence | Details |
|---|---|---|
| **Lifecycle** | The full journey from Genesis to unlock | [Launch lifecycle](lifecycle.md) |
| **Standard Genesis** | uAsset principal conservation + additional upside | [Standard Genesis](genesis.md) |
| **Four pools** | A liquidity structure of one primary pool + three auxiliary pools | [Four-pool liquidity](four-pools.md) |
| **Dynamic fee hook** | A manipulation-resistant trading layer built on Uniswap V4 | [Dynamic fee hook](hook.md) |
| **Preorder** | Lock in Memecoin before Genesis | [Preorder](preorder.md) |
| **Leveraged Genesis (POLend)** | Pay interest to amplify your Genesis share | [Leveraged Genesis](polend.md) |
| **POL split** | Split POL into principal (PT) and yield (YT) | [POL split](pol-splitter.md) |
| **GenesisCredit** | A cross-chain participation credit | [GenesisCredit](genesis-credit.md) |
| **Memecoin Staking** | Stake to earn fees; delegate to gain governance rights | [Memecoin Staking](memecoin-staking.md) |
| **DAO governance** | The community governs the treasury and direction | [DAO governance](dao-governance.md) |
