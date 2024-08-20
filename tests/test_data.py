invalid_token = 'cregwergcwcg'
another_user_token = 'L2a8xedTtvSNYoh'

TEST_DATA_CREATE = [
    {
        "text": "animals",
        "url": "https://static.independent.co.uk/s3fs-public/thumbnails/image/2010/07/01/16/405231.jpg",
        "tags": ["dog", "dogs", "dog1"],
        "info": {"wolf": ["grey", "power"]}
    },
    {
        "text": "How to you a password",
        "url": "https://static.independent.co.uk/s3fs-public/thumbnails/image/2010/07/01/16/405231.jpg",
        "tags": ["password", "shrek"],
        "info": {"password": ["new_password", "wrong_password"]}
    },
    {
        "text": "Pops",
        "url": "https://static.independent.co.uk/s3fs-public/thumbnails/image/2010/07/01/16/405231.jpg",
        "tags": ["rap", "jazz", "rock"],
        "info": {"secrets": ["drive", "extremal"]}
    },
    {
        "text": "How to you a password",
        "url": "https://static.independent.co.uk/s3fs-public/thumbnails/image/2010/07/01/16/405231.jpg",
        "tags": ["password", "shrek"],
        "info": {"password": ["new_password", "wrong_password"]}
    }
]

NEGATIVE_DATA_CREATE = [
    {
        "text": 12399,
        "url": "https://static.independent.co.uk/s3fs-public/thumbnails/image/2010/07/01/16/405231.jpg",
        "tags": ["password", "shrek"],
        "info": {"False": ["True", "low"]}
    },
    {
        "text": ["password", "shrek"],
        "url": "https://static.independent.co.uk/s3fs-public/thumbnails/image/2010/07/01/16/405231.jpg",
        "tags": ["password", "shrek"],
        "info": {"url": ["info", "tags"]}
    },
    {
        "text": (1, 3),
        "url": "https://static.independent.co.uk/s3fs-public/thumbnails/image/2010/07/01/16/405231.jpg",
        "tags": ["password", "shrek"],
        "info": {"smol": ["red", "big"]}
    },
    {
        "text": None,
        "url": "https://static.independent.co.uk/s3fs-public/thumbnails/image/2010/07/01/16/405231.jpg",
        "tags": ["password", "shrek"],
        "info": {"extremal": ["relax", "sport"]}
    }
]

TEST_DATA_UPDATE = {
    "id": 200,
    "text": "Updated password",
    "url": "https://static.independent.co.uk/s3fs-public/thumbnails/image/2010/07/01/16/405231.jpg",
    "tags": ["updated - password", "updated - shrek"],
    "info": {"0003333": ["1113333", "1111222"]}
}

NEGATIVE_DATA_UPDATE = [
    {
        "text": "Updated - How to enter a password",
        "url": "https://static.independent.co.uk/s3fs-public/thumbnails/image/2010/07/01/16/405231.jpg",
        "tags": ["updated - password", "updated - shrek"],
        "info": {"222222222": ["22222222222222", "3333333333333333"]}
    },
    {
        "id": {"000": ["111", "222"]},
        "text": " enter a password",
        "url": "https://static.independent.co.uk/s3fs-public/thumbnails/image/2010/07/01/16/405231.jpg",
        "tags": ["updated - password", "updated - shrek"],
        "info": {"4444444444444": ["33333333333", "9999999999"]}
    },
    {
        "id": None,
        "text": "Updated  password",
        "url": "https://static.independent.co.uk/s3fs-public/thumbnails/image/2010/07/01/16/405231.jpg",
        "tags": ["updated - password", "updated - shrek"],
        "info": {"00000000000000": ["44444444444444444", "77777777777"]}
    },
    {
        "id": "string",
        "text": "Updated  password",
        "url": "https://static.independent.co.uk/s3fs-public/thumbnails/image/2010/07/01/16/405231.jpg",
        "tags": ["updated - password", "updated - shrek"],
        "info": {"33333333": ["33333333333", "111111111111111"]}
    },
    {
        "id": 1,
        "text": 123,
        "url": "https://static.independent.co.uk/s3fs-public/thumbnails/image/2010/07/01/16/405231.jpg",
        "tags": ["updated - password", "updated - shrek"],
        "info": {"5555555555": ["555555555555", "55555555555555"]}
    }
]
