import random

# Reviews are built by combining one hand-written line from each bucket
# below, so the output is longer and varies a lot between visits without
# ever calling an AI model at runtime — every sentence here was written
# by hand. "{business}" is filled in with the visiting store's
# short_name from config.STORE_CONFIG.

OPENERS = [
    "Had a really lovely first visit to {business}.",
    "I've been buying from {business} for a while now and keep coming back.",
    "Stopped by {business} on a friend's recommendation and I'm glad I did.",
    "{business} was exactly what I was hoping for when I walked in.",
    "Visited {business} this week and wanted to share a few thoughts.",
    "Dropped into {business} on a whim and ended up staying a while.",
]

STORE_EXPERIENCE = [
    "The store itself is neat, clean, and has a really calm, welcoming feel to it.",
    "It's well organised and plastic-free, which I really appreciated.",
    "Everything was well stocked — moisturisers, serums, face wash, lip balms, the works.",
    "The space is soothing and doesn't feel crowded or pushy like a lot of other stores.",
    "It's a small store but every shelf is thoughtfully laid out.",
]

STAFF_EXPERIENCE = [
    "The staff took the time to actually understand my skin type before suggesting anything.",
    "Nobody rushed me, and the team explained the products clearly without any pressure to buy.",
    "The team was patient and answered every question I had.",
    "Whoever helped me clearly knew the products inside out.",
    "The person at the counter genuinely seemed to know what she was talking about.",
]

PRODUCT_MENTIONS = [
    "I picked up the Milk Drops Serum on a recommendation and it's been great so far.",
    "Tried the Powder Face Wash and my skin has genuinely felt better since.",
    "The Blue Pea Serum was suggested to me and I'm already noticing a difference.",
    "Grabbed a goat milk soap and shampoo too, both worth trying.",
    "Ended up leaving with a few new favourites I wasn't expecting to buy.",
    "Been using what I bought for a couple of weeks now and no complaints so far.",
]

CLOSERS = [
    "Would definitely recommend it if you're starting out with skincare.",
    "Will be back again for sure.",
    "Overall a really solid experience, worth the visit.",
    "Happy to have found a store that actually cares about what works for you.",
    "Already planning to go back for a refill.",
]


def _compose(short_name: str) -> str:
    parts = [
        random.choice(OPENERS),
        random.choice(STORE_EXPERIENCE),
        random.choice(STAFF_EXPERIENCE),
        random.choice(PRODUCT_MENTIONS),
        random.choice(CLOSERS),
    ]
    return " ".join(parts).format(business=short_name)


def random_review(short_name: str, exclude: str | None = None) -> str:
    for _ in range(10):
        text = _compose(short_name)
        if text != exclude:
            return text
    return _compose(short_name)
