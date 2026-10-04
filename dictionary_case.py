users = [
    {
        "id": 1,
        "total": 150,
        "coupon": "P20"
    },
    {
            "id": 1,
            "total": 100,
            "coupon": "P30"
    },
    {
                "id": 1,
                "total": 250,
                "coupon": "P40"
    }
]

discounts = {
    "P20": (0.2, 0),
    "P30": (0.5, 0),
    "P40": (0, 10)
}

for user in users:
    percent, fixed = discounts.get(user["coupon"], (0,0))
    discount = user["total"] * percent + fixed
    print(discount)