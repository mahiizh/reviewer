import random

# Reviews are built by combining one hand-written line from each bucket
# below, so the output is longer and varies a lot between visits without
# ever calling an AI model at runtime — every sentence here was written
# by hand.

OPENERS = [
    "Had a really lovely first visit to Vilvah Store.",
    "I've been buying from Vilvah Store for a while now and keep coming back.",
    "Stopped by Vilvah Store on a friend's recommendation and I'm glad I did.",
    "Vilvah Store was exactly what I was hoping for when I walked in.",
    "Visited Vilvah Store this week and wanted to share a few thoughts.",
    "Dropped into Vilvah Store on a whim and ended up staying a while.",
]

STORE_EXPERIENCE = [
    "The store itself is neat, clean, and has a really calm, welcoming feel to it.",
    "It's well organised and plastic-free, which I really appreciated.",
    "Everything was well stocked — moisturisers, serums, face wash, lip balms, the works.",
    "The store had such a nice, soft smell to it — really pleasant to walk into.",
    "They were playing really nice music in the store, added to the whole experience.",
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
    "Picked up the goat milk shampoo too and it's honestly one of the better ones I've used.",
    "Grabbed their sunscreen as well and it doesn't leave any white cast, which was a relief.",
    "The under eye cream was suggested to me and I've already started noticing a difference.",
    "Ended up buying the serum and face wash combo, works out really well together.",
]

OFFERS = [
    "There were some exciting offers running and I really liked that.",
    "I thought the discounts would only be on the website, but the store had a lot of offers too.",
    "Bought the products at a nice combo discount price.",
    "They have a policy where if you bring back 5 empty bottles they give an extra discount — thought that was a nice touch.",
    "Bought products at a flat 20% off, was really nice.",
    "Didn't expect them to have this kind of discount running, but glad they did.",
]

CLOSERS = [
    "Would definitely recommend it if you're starting out with skincare.",
    "Will be back again for sure.",
    "Overall a really solid experience, worth the visit.",
    "Happy to have found a store that actually cares about what works for you.",
    "Already planning to go back for a refill.",
]


def _compose() -> str:
    parts = [
        random.choice(OPENERS),
        random.choice(STORE_EXPERIENCE),
        random.choice(STAFF_EXPERIENCE),
        random.choice(PRODUCT_MENTIONS),
        random.choice(OFFERS),
        random.choice(CLOSERS),
    ]
    return " ".join(parts)


def random_review(exclude: str | None = None) -> str:
    for _ in range(10):
        text = _compose()
        if text != exclude:
            return text
    return _compose()
