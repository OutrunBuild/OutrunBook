# vs Pump.fun

Pump.fun is one of the best-known Memecoin launch platforms today, notable for bonding curve issuance, a low entry barrier, and pure market speculation. Memeverse takes a different path: it is not competing on who can speculate harder, but on who can grow lasting value for a Memecoin.

## Core differences

| Dimension | Pump.fun model | Memeverse |
|---|---|---|
| **Liquidity** | bonding curve issuance, then migration to a single PumpSwap pool at graduation; in BOOST mode, a back-loaded buyback at graduation injects about 20% liquidity | Four pools built at Genesis; deep primary pool, with auxiliary pools supporting PT/YT trading |
| **Price protection** | Fixed 1% fee on the bonding curve; the open is easily front-run and sandwiched | Dynamic fees + a high fee at pool opening, actively defending against front-running and sandwich attacks |
| **Asset sustainability** | The meme token itself offers no yield and no governance (the protocol side has separate Creator revenue share and PUMP income payouts) | Memecoin Staking earns fees + DAO governance rights |
| **Capital efficiency** | One unit of capital, one unit of participation | Leveraged Genesis can amplify early share at lower cost |
| **Principal and yield** | Cannot be separated | POL splits into PT (principal) / YT (yield); take whichever you need |
| **When protection takes effect** | Only about 1% of tokens ever "graduate", and LP lock/burn takes effect only after graduation. Most tokens die on the bonding curve, unprotected | Effective at Genesis: four pools built, 365-day lock, full refund if the target is missed |
| **Chain coverage** | Solana only | Natively omnichain: multi-chain launches + cross-chain staking + yield aggregation |

## Different design philosophies

- **Pump.fun** treats the Memecoin as a **vehicle for speculation**: whoever smells the opportunity first and clicks fastest makes the money. The result is a handful of winners and a mass of Memecoins that go to zero.
- **Memeverse** treats the Memecoin as a **community asset**: locked liquidity builds trust, dynamic fees keep the market healthy, and Staking and DAO let long-term holders benefit continuously.

## Key protections

- **Rug resistance**: Pump.fun's LP lock takes effect only after "graduation"; about 99% of tokens never graduate and die on the bonding curve with no protection, while the team/Creator still holds a large supply to sell. Memeverse's protection starts at Genesis: the four pools are established, and liquidity is locked for 365 days, a hard constraint in the contract; during the lock-up period no party can withdraw it. If Genesis misses its target, all three classes of funds are refunded in full.
- **Front-running resistance**: the high fee at pool opening plus dynamic fees make queue-jumpers pay for cutting in. The aggregated Preorder buy order is filled in the same transaction that creates the primary pool, so snipers cannot build a position ahead of public trading.
- **Fair settlement**: Preorders go through a dedicated channel with a fixed 1% fee, and all Preorder participants share the average price of the same aggregated fill (see [Preorder](preorder.md)).

## Who it's for

- Users who enjoy **fast speculation and short-term trading** will find Pump.fun's model more direct.
- Users who value **long-term value, community governance, and sustainable yield** get a complete path from meme to asset in Memeverse.

Memeverse does not deny the speculative nature of Memecoins. It adds a mechanism layer on top: liquidity, fees, leverage, Staking, DAO, and cross-chain. The speculation goes on as before, but trading fees now flow to stakers and the treasury, and governance rights sit with holders.
