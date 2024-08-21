invalid_token = 'iuriuyiuytiuyt'
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


TEST_DATA_UPDATE = {
    "id": 200,
    "text": "Updated password",
    "url": "https://static.independent.co.uk/s3fs-public/thumbnails/image/2010/07/01/16/405231.jpg",
    "tags": ["updated - password", "updated - shrek"],
    "info": {"0003333": ["1113333", "1111222"]}
}

NEGATIVE_DATA_CREATE = [
    {
        "text": 12399,
        "url": "https://static.independent.co.uk/s3fs-public/thumbnails/image/2010/07/01/16/405231.jpg",
        "tags": ["password", "dog"],
        "info": {"False": [True, "low"]}
    },
    {
        "url": "https://static.independent.co.uk/s3fs-public/thumbnails/image/2010/07/01/16/405231.jpg",
        "tags": ["password", "cat"],
        "info": {"url": [False, "tags"]}
    },
    {
        "text": (1, 3),
        "url": 1234,
        "tags": ["password", "wolf"],
        "info": {"smol": ["red", "big"]}
    },
    {
        "text": None,
        "url": "https://static.independent.co.uk/s3fs-public/thumbnails/image/2010/07/01/16/405231.jpg",
        "tags": ["password", "scorpion"],
        "info": {"extremal": ["relax", "sport"]}
    },
    {
        "text": (1, 3),
        "url": None,
        "tags": ["password", "wolf"],
        "info": {"smol": ["red", "big"]}
    },
    {
        "text": (1, 3),
    },
]

NEGATIVE_DATA_UPDATE = [
    {
        "text": 1,
        "url": "https://static.independent.co.uk/s3fs-public/thumbnails/image/2010/07/01/16/405231.jpg",
        "tags": ["updated - password", -0.5],
        "info": {"222222222": ["22222222222222", "3333333333333333"]}
    },
    {
        "id": {"000": ["111", "222"]},
        "text": " enter a password",
        "url": "https://static.independent.co.uk/s3fs-public/thumbnails/image/2010/07/01/16/405231.jpg",
        "tags": ["updated - password", "updated"],
        "info": {"4444444444444": ["33333333333", "9999999999"]}
    },
    {
        "id": None,
        "text": "Updated  password",
        "url": "<scr<script>ipt>alert('1')</script>",
        "tags": ["updated - password", '1000$'],
        "info": {"00000000000000": ["44444444444444444", "77777777777"]}
    },
    {
        "id": "string",
        "text": "Updated  password",
        "url": "https://static.independent.co.uk/s3fs-public/thumbnails/image/2010/07/01/16/405231.jpg",
        "tags": ["updated - password", "golf"],
        "info": {"33333333": ["33333333333", "111111111111111"]}
    },
    {
        "id": 1,
        "text": 123,
        "url": "2' union SELECT concat(user_id, ':' ,first_name, ':' ,last_name),"
               " concat(user, ':' ,password) from dvwa.users -- '",
        "tags": ["updated - password", "golf"],
        "info": {"5555555555": ["555555555555", "55555555555555"]}
    }
]
