import random
import json
from Tests import Tests

API_URL = "https://livesurf.ru:8183/api/client"
API_KEYS = [
    "QFWIDeEgJAtcUy8g8Pj8FLOsMxpUOKxWuAOpMuPTABtLVC8E3R1G6suUGI4wLe14s1ZFU2wOYlRkfoQQNxdQcencuv6v510zBQgRQjrDK5XPd6VbQCqtKH3oFy2iho8YMX16bGobRWPXanXdYOXrdTJ4HCK2R0jupmFcSpyGVJiO5cuQiA8zTe8HoDMzLNaAsXeJDAd5IpBh4xTZnlQkKe4powvfT6qypflBatptPoenlxpVx4wL6wVcbcJ1YAW", 
    "Wlm4HZAxqKX70TplQiGNeA7FL8hJb2MwilzQGnfXPzwpbNbk1AKRwZ1vC2yqSXs8VdgTkQDCsQLWg2CbVZOoemUjh9iLj59PF5s4hdjCFohn23PfDySQD9iSQQhfWiwjMeJPdkfrY8WRwtuvXyDk0L0wvZE2ohXLVeEot3ztBY4TaH34gLWmMnR5uSxkbaXnSG5TPpVnsLrniO3B8Tr7Jjdg1zUV7eGXn0NjO2HCVHfQbDsaYCPExcKeFuLO1KT"
]
API_KEY = API_KEYS[1]

if __name__ == "__main__":
    tests = Tests(API_URL, API_KEY, True)

    tests.run_test(
        'GET',
        'categories',
        [
            {
                "id": "int",
                "name": "string",
                "parent": "int",
                "active": "bool"
            }
        ],
        200
    )

    tests.run_test(
        'GET',
        'countries',
        [
            {
                "id": "int",
                "country": "string",
                "region": "string",
                "city": "string",
                "name": "string"
            }
        ],
        200
    )

    tests.run_test(
        'GET',
        'languages',
        [
            {
                "id": "int",
                "name": "string",
                "translate_name": "string"
            }
        ],
        200
    )

    tests.run_test(
        'GET',
        'sources/ad',
        [
            {
                "name": "string",
                "default": "bool",
                "payload": "string",
                "enable": "bool"
            }
        ],
        200
    )

    tests.run_test(
        'GET',
        'sources/messengers',
        [
            {
                "name": "string",
                "default": "bool",
                "payload": "string",
                "enable": "bool"
            }
        ],
        200
    )

    tests.run_test(
        'GET',
        'sources/search',
        [
            {
                "id": "int",
                "name": "string",
                "default": "string",
                "payload": "string",
                "enable": "bool"
            }
        ],
        200
    )

    tests.run_test(
        'GET',
        'sources/social',
        [
            {
                "name": "string",
                "default": "bool",
                "payload": "string",
                "enable": "bool"
            }
        ],
        200
    )

    tests.run_test(
        'GET',
        'user',
        {
            "user_id": "int",
            "credits": "string",
            "workmode": "int",
            "type": "int",
            "experience": "int",
            "token": "string"
        },
        200
    )

    tests.run_test(
        'POST',
        'user/automode',
        "int",
        202
    )

    tests.run_test(
        'POST',
        'user/manualmode',
        "int",
        202
    )

    tests.run_test(
        'GET',
        'group/all',
        [
            {
                "name": "string",
                "hour_limit": "int",
                "day_limit": "int",
                "uniq_ip": "int",
                "moby_ratio": "int",
                "geo": "string",
                "stopping_hours": [
                    "int"
                ],
                "autocalc_visits": "bool",
                "use_profiles": "bool",
                "timezone": "string",
                "category": "int",
                "language": "int",
                "bookmarks": [
                    "int",
                    "int"
                ],
                "users": {
                    "global": "int",
                    "current": "int"
                }
            }
        ],
        200
    )

    group = tests.run_test(
        'POST',
        'group/create',
        {
            "name": "string",
            "hour_limit": "int",
            "day_limit": "int",
            "uniq_ip": "int",
            "moby_ratio": "int",
            "autocalc_visits": "bool",
            "timezone": "string",
            "category": "int",
            "language": "int",
            "only_proxy": "bool",
            "low_pf": "bool",
            "retention": "bool",
            "description": "string",
            "credits": "int",
            "id": "int"
        },
        201,
        {
            "name": "Группа " + str(random.randint(1, 1000)),     
            "hour_limit": 0, 
            "day_limit": 10000,             
            "uniq_ip": 168,             
            "moby_ratio": 50,               
            "geo": [1],                    
            "autocalc_visits": True,         
            "use_profiles": True,            
            "retention": True,                 
            "description": "Описание группы", 
            "timezone": "Europe/Moscow",     
            "stopping_hours": [1, 2, 3],      
            "category": 1,                  
            "language": 1,                    
            "bookmarks": [10, 20],          
            "autolimit": [-500, 500],
            "low_pf": False,    
            "use_profiles": True,
            "schedules": [[1, "07.02.2026 14:17"],[0, "07.02.2026 15:17"]],
            "sources": {
                "keywords": {
                    "value": 1,
                    "enabled": True,
                    "settings": {
                        "list": ["ключевая фраза 1", "ключевая фраза 2"],
                        "search_engines": {"1": 1.0, "2": 0.5, "3": 0.5}
                    }
                },
                "adsystems": {
                    "value": 1,
                    "enabled": True,
                    "settings": ["B2BContext"]
                },
                "backlinks": {
                    "value": 1,
                    "enabled": True,
                    "settings": {
                        "list": ["https://test.com"]
                    }
                },
                "messengers": {
                    "value": 1,
                    "enabled": True,
                    "settings": ["telegram"]
                },
                "clickunders": {
                    "value": 1,
                    "enabled": True
                },
                "emailanalytics": {
                    "value": 1,
                    "enabled": True
                },
                "socialanalytics": {
                    "value": 1,
                    "enabled": True,
                    "settings": [
                        "instagram",
                        "tiktok",
                        "pinterest"
                    ]
                }
            },
            "pages":[{
                "url": ["https://example.com/", "https://example.com/page2"]
            }]
        },
    )

    tests.run_test(
        'POST',
        'group/create',
        {
            "name": "string",
            "hour_limit": "int",
            "day_limit": "int",
            "uniq_ip": "int",
            "moby_ratio": "int",
            "autocalc_visits": "bool",
            "timezone": "string",
            "category": "int",
            "language": "int",
            "only_proxy": "bool",
            "low_pf": "bool",
            "retention": "bool",
            "description": "string",
            "credits": "int",
            "id": "int"
        },
        201,
        {
            "name": "Группа " + str(random.randint(1, 1000)),     
            "hour_limit": 0, 
            "day_limit": 10000,             
            "uniq_ip": 168,             
            "moby_ratio": 50,               
            "geo": [1, 2, 3],                    
            "autocalc_visits": True,         
            "use_profiles": True,            
            "retention": True,                 
            "description": "Описание группы", 
            "timezone": "Europe/Moscow",     
            "stopping_hours": [1, 2, 3],      
            "category": 1,                  
            "language": 1,                    
            "bookmarks": [10, 20],          
            "autolimit": [-500, 500],
            "low_pf": False,    
            "use_profiles": True,
            "schedules": [[1, "07.02.2026 14:17"],[0, "07.02.2026 15:17"]],
            "sources": {
                "keywords": {
                    "value": 1,
                    "enabled": True,
                    "settings": {
                        "list": ["ключевая фраза 1", "ключевая фраза 2"],
                        "search_engines": {"1": 1.0, "2": 0.5, "3": 0.5}
                    }
                },
                "adsystems": {
                    "value": 1,
                    "enabled": True,
                    "settings": ["B2BContext"]
                },
                "backlinks": {
                    "value": 1,
                    "enabled": True,
                    "settings": {
                        "list": ["https://test.com"]
                    }
                },
                "messengers": {
                    "value": 1,
                    "enabled": True,
                    "settings": ["telegram"]
                },
                "clickunders": {
                    "value": 1,
                    "enabled": True
                },
                "emailanalytics": {
                    "value": 1,
                    "enabled": True
                },
                "socialanalytics": {
                    "value": 1,
                    "enabled": True,
                    "settings": [
                        "instagram",
                        "tiktok",
                        "pinterest"
                    ]
                }
            },
            "pages":[{
                "url": ["https://example.com/", "https://example.com/page2"]
            }]
        },
    )

    tests.run_test(
        'POST',
        'group/create',
        {},
        400,
        {
            "name": "Группа " + str(random.randint(1, 1000)),     
            "hour_limit": -1, 
            "day_limit": 10000,             
            "uniq_ip": 168,             
            "moby_ratio": 50,               
            "geo": [1],                    
            "autocalc_visits": True,         
            "use_profiles": True,            
            "retention": True,                 
            "description": "Описание группы", 
            "timezone": "Europe/Moscow",     
            "stopping_hours": [1, 2, 3],      
            "category": 1,                  
            "language": 1,                    
            "bookmarks": [10, 20],          
            "autolimit": [-500, 500],
            "low_pf": False,    
            "use_profiles": True,
            "schedules": [[1, "07.02.2026 14:17"],[0, "07.02.2026 15:17"]],
            "sources": {
                "keywords": {
                    "value": 1,
                    "enabled": True,
                    "settings": {
                        "list": ["ключевая фраза 1", "ключевая фраза 2"],
                        "search_engines": {"1": 1.0, "2": 0.5, "3": 0.5}
                    }
                },
                "adsystems": {
                    "value": 1,
                    "enabled": True,
                    "settings": ["B2BContext"]
                },
                "backlinks": {
                    "value": 1,
                    "enabled": True,
                    "settings": {
                        "list": ["https://test.com"]
                    }
                },
                "messengers": {
                    "value": 1,
                    "enabled": True,
                    "settings": ["telegram"]
                },
                "clickunders": {
                    "value": 1,
                    "enabled": True
                },
                "emailanalytics": {
                    "value": 1,
                    "enabled": True
                },
                "socialanalytics": {
                    "value": 1,
                    "enabled": True,
                    "settings": [
                        "instagram",
                        "tiktok",
                        "pinterest"
                    ]
                }
            },
            "pages":[{
                "url": ["https://example.com/", "https://example.com/page2"]
            }]
        },
    )

    tests.run_test(
        'POST',
        'group/create',
        {},
        400,
        {
            "name": "Группа " + str(random.randint(1, 1000)),     
            "hour_limit": 1, 
            "day_limit": 10000,             
            "uniq_ip": 168,             
            "moby_ratio": 50,               
            "geo": [1],                    
            "autocalc_visits": True,         
            "use_profiles": True,            
            "retention": True,                 
            "description": "Описание группы", 
            "timezone": "Europe/Moscow",     
            "stopping_hours": [1, 2, 3],      
            "category": -1,                  
            "language": 1,                    
            "bookmarks": [10, 20],          
            "autolimit": [-500, 500],
            "low_pf": False,    
            "use_profiles": True,
            "schedules": [[1, "07.02.2026 14:17"],[0, "07.02.2026 15:17"]],
            "sources": {
                "keywords": {
                    "value": 1,
                    "enabled": True,
                    "settings": {
                        "list": ["ключевая фраза 1", "ключевая фраза 2"],
                        "search_engines": {"1": 1.0, "2": 0.5, "3": 0.5}
                    }
                },
                "adsystems": {
                    "value": 1,
                    "enabled": True,
                    "settings": ["B2BContext"]
                },
                "backlinks": {
                    "value": 1,
                    "enabled": True,
                    "settings": {
                        "list": ["https://test.com"]
                    }
                },
                "messengers": {
                    "value": 1,
                    "enabled": True,
                    "settings": ["telegram"]
                },
                "clickunders": {
                    "value": 1,
                    "enabled": True
                },
                "emailanalytics": {
                    "value": 1,
                    "enabled": True
                },
                "socialanalytics": {
                    "value": 1,
                    "enabled": True,
                    "settings": [
                        "instagram",
                        "tiktok",
                        "pinterest"
                    ]
                }
            },
            "pages":[{
                "url": ["https://example.com/", "https://example.com/page2"]
            }]
        },
    )

    tests.run_test(
        'POST',
        'group/create',
        {},
        400,
        {
            "name": "Группа " + str(random.randint(1, 1000)),     
            "hour_limit": 1, 
            "day_limit": 10000,             
            "uniq_ip": 168,             
            "moby_ratio": 50,               
            "geo": [1],                    
            "autocalc_visits": True,         
            "use_profiles": True,            
            "retention": True,                 
            "description": "Описание группы", 
            "timezone": "Europe/Moscow",     
            "stopping_hours": [1, 2, 3],      
            "category": 1,                  
            "language": 1,                    
            "bookmarks": [10, 20],          
            "autolimit": [-501, 501],
            "low_pf": False,    
            "use_profiles": True,
            "schedules": [[1, "07.02.2026 14:17"],[0, "07.02.2026 15:17"]],
            "sources": {
                "keywords": {
                    "value": 1,
                    "enabled": True,
                    "settings": {
                        "list": ["ключевая фраза 1", "ключевая фраза 2"],
                        "search_engines": {"1": 1.0, "2": 0.5, "3": 0.5}
                    }
                },
                "adsystems": {
                    "value": 1,
                    "enabled": True,
                    "settings": ["B2BContext"]
                },
                "backlinks": {
                    "value": 1,
                    "enabled": True,
                    "settings": {
                        "list": ["https://test.com"]
                    }
                },
                "messengers": {
                    "value": 1,
                    "enabled": True,
                    "settings": ["telegram"]
                },
                "clickunders": {
                    "value": 1,
                    "enabled": True
                },
                "emailanalytics": {
                    "value": 1,
                    "enabled": True
                },
                "socialanalytics": {
                    "value": 1,
                    "enabled": True,
                    "settings": [
                        "instagram",
                        "tiktok",
                        "pinterest"
                    ]
                }
            },
            "pages":[{
                "url": ["https://example.com/", "https://example.com/page2"]
            }]
        },
    )

    group_id = json.loads(group)['id']

    tests.run_test(
        'GET',
        'group/' + str(group_id),
        {
            "name": "string",
            "hour_limit": "int",
            "day_limit": "int",
            "uniq_ip": "int",
            "moby_ratio": "int",
            "geo": "string",
            "stopping_hours": [
                "int"
            ],
            "autocalc_visits": "bool",
            "use_profiles": "bool",
            "timezone": "string",
            "category": "int",
            "language": "int",
            "bookmarks": [
                "int",
                "int"
            ],
            "users": {
                "global": "int",
                "current": "int"
            }
        },
        200
    )

    tests.run_test(
        'GET',
        'group/' + str(group_id + 1),
        {
            "errors": {
                "detail": "string"
            }
        },
        404
    )

    tests.run_test(
        'PATCH',
        'group/' + str(group_id),
        {
            "name": "string",
            "hour_limit": "int",
            "day_limit": "int",
            "uniq_ip": "int",
            "moby_ratio": "int",
            "autocalc_visits": "bool",
            "timezone": "string",
            "category": "int",
            "language": "int",
            "only_proxy": "bool",
            "low_pf": "bool",
            "retention": "bool",
            "description": "string",
            "credits": "int",
            "id": "int"
        },
        202,
        {
            "name": "Группа " + str(random.randint(1, 1000)),     
            "hour_limit": 0, 
            "day_limit": 10000,             
            "uniq_ip": 168,             
            "moby_ratio": 50,               
            "geo": [1],                    
            "autocalc_visits": True,         
            "use_profiles": True,            
            "retention": True,                 
            "description": "Описание группы", 
            "timezone": "Europe/Moscow",     
            "stopping_hours": [1, 2, 3],      
            "category": 1,                  
            "language": 1,                    
            "bookmarks": [10, 20],          
            "autolimit": [-500, 500],
            "low_pf": False,    
            "use_profiles": True,
            "schedules": [[1, "07.02.2026 14:17"],[0, "07.02.2026 15:17"]],
            "sources": {
                "keywords": {
                    "value": 1,
                    "enabled": True,
                    "settings": {
                        "list": ["ключевая фраза 1", "ключевая фраза 2"],
                        "search_engines": {"1": 1.0, "2": 0.5, "3": 0.5}
                    }
                },
                "adsystems": {
                    "value": 1,
                    "enabled": True,
                    "settings": ["B2BContext"]
                },
                "backlinks": {
                    "value": 1,
                    "enabled": True,
                    "settings": {
                        "list": ["https://test.com"]
                    }
                },
                "messengers": {
                    "value": 1,
                    "enabled": True,
                    "settings": ["telegram"]
                },
                "clickunders": {
                    "value": 1,
                    "enabled": True
                },
                "emailanalytics": {
                    "value": 1,
                    "enabled": True
                },
                "socialanalytics": {
                    "value": 1,
                    "enabled": True,
                    "settings": [
                        "instagram",
                        "tiktok",
                        "pinterest"
                    ]
                }
            },
            "pages":[{
                "url": ["https://example.com/", "https://example.com/page2"]
            }]
        },
    )

    tests.run_test(
        'PATCH',
        'group/' + str(group_id + 1),
        {
            "errors": {
                "detail": "string"
            }
        },
        404,
        {
            "name": "Группа " + str(random.randint(1, 1000)),     
            "hour_limit": 0, 
            "day_limit": 10000,             
            "uniq_ip": 168,             
            "moby_ratio": 50,               
            "geo": [1],                    
            "autocalc_visits": True,         
            "use_profiles": True,            
            "retention": True,                 
            "description": "Описание группы", 
            "timezone": "Europe/Moscow",     
            "stopping_hours": [1, 2, 3],      
            "category": 1,                  
            "language": 1,                    
            "bookmarks": [10, 20],          
            "autolimit": [-500, 500],
            "low_pf": False,    
            "use_profiles": True,
            "schedules": [[1, "07.02.2026 14:17"],[0, "07.02.2026 15:17"]],
            "sources": {
                "keywords": {
                    "value": 1,
                    "enabled": True,
                    "settings": {
                        "list": ["ключевая фраза 1", "ключевая фраза 2"],
                        "search_engines": {"1": 1.0, "2": 0.5, "3": 0.5}
                    }
                },
                "adsystems": {
                    "value": 1,
                    "enabled": True,
                    "settings": ["B2BContext"]
                },
                "backlinks": {
                    "value": 1,
                    "enabled": True,
                    "settings": {
                        "list": ["https://test.com"]
                    }
                },
                "messengers": {
                    "value": 1,
                    "enabled": True,
                    "settings": ["telegram"]
                },
                "clickunders": {
                    "value": 1,
                    "enabled": True
                },
                "emailanalytics": {
                    "value": 1,
                    "enabled": True
                },
                "socialanalytics": {
                    "value": 1,
                    "enabled": True,
                    "settings": [
                        "instagram",
                        "tiktok",
                        "pinterest"
                    ]
                }
            },
            "pages":[{
                "url": ["https://example.com/", "https://example.com/page2"]
            }]
        }
    )

    tests.run_test(
        'PATCH',
        'group/' + str(group_id),
        {},
        400,
        {
            "name": "Группа " + str(random.randint(1, 1000)),     
            "hour_limit": -1, 
            "day_limit": 10000,             
            "uniq_ip": 168,             
            "moby_ratio": 50,               
            "geo": [1],                    
            "autocalc_visits": True,         
            "use_profiles": True,            
            "retention": True,                 
            "description": "Описание группы", 
            "timezone": "Europe/Moscow",     
            "stopping_hours": [1, 2, 3],      
            "category": 1,                  
            "language": 1,                    
            "bookmarks": [10, 20],          
            "autolimit": [-500, 500],
            "low_pf": False,    
            "use_profiles": True,
            "schedules": [[1, "07.02.2026 14:17"],[0, "07.02.2026 15:17"]],
            "sources": {
                "keywords": {
                    "value": 1,
                    "enabled": True,
                    "settings": {
                        "list": ["ключевая фраза 1", "ключевая фраза 2"],
                        "search_engines": {"1": 1.0, "2": 0.5, "3": 0.5}
                    }
                },
                "adsystems": {
                    "value": 1,
                    "enabled": True,
                    "settings": ["B2BContext"]
                },
                "backlinks": {
                    "value": 1,
                    "enabled": True,
                    "settings": {
                        "list": ["https://test.com"]
                    }
                },
                "messengers": {
                    "value": 1,
                    "enabled": True,
                    "settings": ["telegram"]
                },
                "clickunders": {
                    "value": 1,
                    "enabled": True
                },
                "emailanalytics": {
                    "value": 1,
                    "enabled": True
                },
                "socialanalytics": {
                    "value": 1,
                    "enabled": True,
                    "settings": [
                        "instagram",
                        "tiktok",
                        "pinterest"
                    ]
                }
            },
            "pages":[{
                "url": ["https://example.com/", "https://example.com/page2"]
            }]
        },
    )

    tests.run_test(
        'PATCH',
        'group/' + str(group_id),
        {},
        400,
        {
            "name": "Группа " + str(random.randint(1, 1000)),     
            "hour_limit": 1, 
            "day_limit": 10000,             
            "uniq_ip": 168,             
            "moby_ratio": 50,               
            "geo": [1],                    
            "autocalc_visits": True,         
            "use_profiles": True,            
            "retention": True,                 
            "description": "Описание группы", 
            "timezone": "Europe/Moscow",     
            "stopping_hours": [1, 2, 3],      
            "category": -1,                  
            "language": 1,                    
            "bookmarks": [10, 20],          
            "autolimit": [-500, 500],
            "low_pf": False,    
            "use_profiles": True,
            "schedules": [[1, "07.02.2026 14:17"],[0, "07.02.2026 15:17"]],
            "sources": {
                "keywords": {
                    "value": 1,
                    "enabled": True,
                    "settings": {
                        "list": ["ключевая фраза 1", "ключевая фраза 2"],
                        "search_engines": {"1": 1.0, "2": 0.5, "3": 0.5}
                    }
                },
                "adsystems": {
                    "value": 1,
                    "enabled": True,
                    "settings": ["B2BContext"]
                },
                "backlinks": {
                    "value": 1,
                    "enabled": True,
                    "settings": {
                        "list": ["https://test.com"]
                    }
                },
                "messengers": {
                    "value": 1,
                    "enabled": True,
                    "settings": ["telegram"]
                },
                "clickunders": {
                    "value": 1,
                    "enabled": True
                },
                "emailanalytics": {
                    "value": 1,
                    "enabled": True
                },
                "socialanalytics": {
                    "value": 1,
                    "enabled": True,
                    "settings": [
                        "instagram",
                        "tiktok",
                        "pinterest"
                    ]
                }
            },
            "pages":[{
                "url": ["https://example.com/", "https://example.com/page2"]
            }]
        },
    )

    tests.run_test(
        'PATCH',
        'group/' + str(group_id),
        {},
        400,
        {
            "name": "Группа " + str(random.randint(1, 1000)),     
            "hour_limit": 1, 
            "day_limit": 10000,             
            "uniq_ip": 168,             
            "moby_ratio": 50,               
            "geo": [1],                    
            "autocalc_visits": True,         
            "use_profiles": True,            
            "retention": True,                 
            "description": "Описание группы", 
            "timezone": "Europe/Moscow",     
            "stopping_hours": [1, 2, 3],      
            "category": 1,                  
            "language": 1,                    
            "bookmarks": [10, 20],          
            "autolimit": [-501, 501],
            "low_pf": False,    
            "use_profiles": True,
            "schedules": [[1, "07.02.2026 14:17"],[0, "07.02.2026 15:17"]],
            "sources": {
                "keywords": {
                    "value": 1,
                    "enabled": True,
                    "settings": {
                        "list": ["ключевая фраза 1", "ключевая фраза 2"],
                        "search_engines": {"1": 1.0, "2": 0.5, "3": 0.5}
                    }
                },
                "adsystems": {
                    "value": 1,
                    "enabled": True,
                    "settings": ["B2BContext"]
                },
                "backlinks": {
                    "value": 1,
                    "enabled": True,
                    "settings": {
                        "list": ["https://test.com"]
                    }
                },
                "messengers": {
                    "value": 1,
                    "enabled": True,
                    "settings": ["telegram"]
                },
                "clickunders": {
                    "value": 1,
                    "enabled": True
                },
                "emailanalytics": {
                    "value": 1,
                    "enabled": True
                },
                "socialanalytics": {
                    "value": 1,
                    "enabled": True,
                    "settings": [
                        "instagram",
                        "tiktok",
                        "pinterest"
                    ]
                }
            },
            "pages":[{
                "url": ["https://example.com/", "https://example.com/page2"]
            }]
        },
    )

    tests.run_test(
        'GET',
        'group/' + str(group_id),
        {
            "name": "string",
            "hour_limit": "int",
            "day_limit": "int",
            "uniq_ip": "int",
            "moby_ratio": "int",
            "geo": "string",
            "stopping_hours": [
                "int"
            ],
            "autocalc_visits": "bool",
            "use_profiles": "bool",
            "timezone": "string",
            "category": "int",
            "language": "int",
            "bookmarks": [
                "int",
                "int"
            ],
            "users": {
                "global": "int",
                "current": "int"
            }
        },
        200
    )

    clone_group = tests.run_test(
        'POST',
        'group/' + str(group_id) + '/clone',
        {
            "name": "string",
            "hour_limit": "int",
            "day_limit": "int",
            "uniq_ip": "int",
            "moby_ratio": "int",
            "autocalc_visits": "bool",
            "timezone": "string",
            "category": "int",
            "language": "int",
            "only_proxy": "bool",
            "low_pf": "bool",
            "retention": "bool",
            "description": "string",
            "credits": "int",
            "id": "int"
        },
        201,
        {
            "name": "Группа " + str(random.randint(1, 1000)),
        }
    )

    tests.run_test(
        'POST',
        'group/' + str(group_id) + '/clone',
        {
            "name": ["string"]
        },
        400,
        {
            "name": "Группа _______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________" + str(random.randint(1, 1000)),
        }
    )

    # tests.run_test(
    #     'POST',
    #     'group/' + str(group_id + 2) + '/clone',
    #     {
    #         "errors": {
    #             "detail": "string"
    #         }
    #     },
    #     404,
    #     {
    #         "name": "Группа " + str(random.randint(1, 1000)),
    #     }
    # )

    tests.run_test(
        'POST',
        'group/' + str(group_id) + '/add_credits',
        'int',
        202,
        {
            "credits": 100
        }
    )

    tests.run_test(
        'POST',
        'group/' + str(group_id) + '/add_credits',
        'int',
        202,
        {
            "credits": -99
        }
    )

    tests.run_test(
        'POST',
        'group/' + str(group_id) + '/add_credits',
        {
            "errors":{
                "credits": ["string"]
            }
        },
        400,
        {
            "credits": -1
        }
    )

    tests.run_test(
        'POST',
        'group/' + str(group_id + 2) + '/add_credits',
        {
            "errors": {
                "detail": "string"
            }
        },
        404,
        {
            "credits": 100
        }
    )

    clone_group_id = json.loads(clone_group)['id']

    tests.run_test(
        'DELETE',
        'group/' + str(group_id),
        "int",
        205
    )

    tests.run_test(
        'DELETE',
        'group/' + str(group_id),
        {
            "errors": {
                "detail": "string"
            }
        },
        404
    )

    page = tests.run_test(
        'POST',
        'page/create',
        {
            "id": "int"
        },
        201,
        {
            'group_id': clone_group_id,
            'state': 1,
            'break_chain': 100,
            'url': [
                'https://example.com/' + str(random.randint(5, 500)),
                'https://example.com/' + str(random.randint(501, 1000)),
            ],
            'showtime': [15, 30],
            'behavior': {
                "mode": "neural",
                "settings": {
                    "reading_up": True,
                    "clicks": { 
                        "list": [
                            "a", 
                            ".css-class"
                        ] 
                    },
                }
            }
        }
    )

    tests.run_test(
        'POST',
        'page/create',
        {},
        400,
        {
            'group_id': clone_group_id,
            'state': -1,
            'break_chain': 100,
            'url': [
                'https://example.com/' + str(random.randint(5, 500)),
                'https://example.com/' + str(random.randint(501, 1000)),
            ],
            'showtime': [15, 30],
            'behavior': {
                "mode": "neural",
                "settings": {
                    "reading_up": True,
                    "clicks": { 
                        "list": [
                            "a", 
                            ".css-class"
                        ] 
                    },
                }
            }
        }
    )

    tests.run_test(
        'POST',
        'page/create',
        {},
        400,
        {
            'group_id': clone_group_id,
            'state': 1,
            'break_chain': 1000,
            'url': [
                'https://example.com/' + str(random.randint(5, 500)),
                'https://example.com/' + str(random.randint(501, 1000)),
            ],
            'showtime': [15, 30],
            'behavior': {
                "mode": "neural",
                "settings": {
                    "reading_up": True,
                    "clicks": { 
                        "list": [
                            "a", 
                            ".css-class"
                        ] 
                    },
                }
            }
        }
    )

    tests.run_test(
        'POST',
        'page/create',
        {},
        400,
        {
            'group_id': clone_group_id,
            'state': 1,
            'break_chain': 100,
            'url': [
                'https://example.com/' + str(random.randint(5, 500)),
                'https://example2.com/' + str(random.randint(501, 1000)),
            ],
            'showtime': [15, 30],
            'behavior': {
                "mode": "neural",
                "settings": {
                    "reading_up": True,
                    "clicks": { 
                        "list": [
                            "a", 
                            ".css-class"
                        ] 
                    },
                }
            }
        }
    )

    tests.run_test(
        'POST',
        'page/create',
        {},
        400,
        {
            'group_id': clone_group_id,
            'state': 1,
            'break_chain': 100,
            'url': [
                'https://example.com/' + str(random.randint(5, 500)),
                'https://example.com/' + str(random.randint(501, 1000)),
            ],
            'showtime': [10, 40],
            'behavior': {
                "mode": "neural",
                "settings": {
                    "reading_up": True,
                    "clicks": { 
                        "list": [
                            "a", 
                            ".css-class"
                        ] 
                    },
                }
            }
        }
    )

    tests.run_test(
        'POST',
        'page/create',
        {},
        400,
        {
            'group_id': clone_group_id,
            'state': 1,
            'break_chain': 100,
            'url': [
                'https://example.com/' + str(random.randint(5, 500)),
                'https://example.com/' + str(random.randint(501, 1000)),
            ],
            'showtime': [15, 30],
            'behavior': {
                "mode": "neural",
                "settings": {
                    "reading_up": True,
                    "clicks": { 
                        "list": [
                            "a", 
                            ".css-class",
                            "#css_id"
                        ] 
                    },
                }
            }
        }
    )

    page_id = json.loads(page)['id']

    tests.run_test(
        'GET',
        'page/' + str(page_id),
        {
            "id": "int",
            "state": "int",
            "url": [
                "string"
            ],
            "showtime": [
                "int"
            ],
            "break_chain": "int",
            "adult": "bool",
            "group_id": "int",
            "behavior": {
                "mode": "string",
                "settings": {
                    "reading_up": "bool",
                    "clicks": { "list": ["string"] },
                    "manual": { "actions": {} }
                }
            }
        },
        200
    )

    tests.run_test(
        'GET',
        'page/' + str(page_id + 1),
        {
            "errors": {
                "detail": "string"
            }
        },
        404
    )

    page = tests.run_test(
        'PATCH',
        'page/' + str(page_id),
        {
            "id": "int"
        },
        202,
        {
            'group_id': clone_group_id,
            'state': 1,
            'break_chain': 100,
            'url': [
                'https://example.com/' + str(random.randint(5, 500)),
                'https://example.com/' + str(random.randint(501, 1000)),
            ],
            'showtime': [15, 30],
            'behavior': {
                "mode": "neural",
                "settings": {
                    "reading_up": True,
                    "clicks": { 
                        "list": [
                            "a", 
                            ".css-class"
                        ] 
                    },
                }
            }
        }
    )

    page = tests.run_test(
        'PATCH',
        'page/' + str(page_id + 1),
        {
            "errors": {
                "detail": "string"
            }
        },
        404,
        {
            'group_id': clone_group_id,
            'state': 1,
            'break_chain': 100,
            'url': [
                'https://example.com/' + str(random.randint(5, 500)),
                'https://example.com/' + str(random.randint(501, 1000)),
            ],
            'showtime': [15, 30],
            'behavior': {
                "mode": "neural",
                "settings": {
                    "reading_up": True,
                    "clicks": { 
                        "list": [
                            "a", 
                            ".css-class"
                        ] 
                    },
                }
            }
        }
    )

    tests.run_test(
        'PATCH',
        'page/' + str(page_id),
        {},
        400,
        {
            'group_id': clone_group_id,
            'state': -1,
            'break_chain': 100,
            'url': [
                'https://example.com/' + str(random.randint(5, 500)),
                'https://example.com/' + str(random.randint(501, 1000)),
            ],
            'showtime': [15, 30],
            'behavior': {
                "mode": "neural",
                "settings": {
                    "reading_up": True,
                    "clicks": { 
                        "list": [
                            "a", 
                            ".css-class"
                        ] 
                    },
                }
            }
        }
    )

    tests.run_test(
        'PATCH',
        'page/' + str(page_id),
        {},
        400,
        {
            'group_id': clone_group_id,
            'state': 1,
            'break_chain': 1000,
            'url': [
                'https://example.com/' + str(random.randint(5, 500)),
                'https://example.com/' + str(random.randint(501, 1000)),
            ],
            'showtime': [15, 30],
            'behavior': {
                "mode": "neural",
                "settings": {
                    "reading_up": True,
                    "clicks": { 
                        "list": [
                            "a", 
                            ".css-class"
                        ] 
                    },
                }
            }
        }
    )

    tests.run_test(
        'PATCH',
        'page/' + str(page_id),
        {},
        400,
        {
            'group_id': clone_group_id,
            'state': 1,
            'break_chain': 100,
            'url': [
                'https://example.com/' + str(random.randint(5, 500)),
                'https://example2.com/' + str(random.randint(501, 1000)),
            ],
            'showtime': [15, 30],
            'behavior': {
                "mode": "neural",
                "settings": {
                    "reading_up": True,
                    "clicks": { 
                        "list": [
                            "a", 
                            ".css-class"
                        ] 
                    },
                }
            }
        }
    )

    tests.run_test(
        'PATCH',
        'page/' + str(page_id),
        {},
        400,
        {
            'group_id': clone_group_id,
            'state': 1,
            'break_chain': 100,
            'url': [
                'https://example.com/' + str(random.randint(5, 500)),
                'https://example.com/' + str(random.randint(501, 1000)),
            ],
            'showtime': [10, 40],
            'behavior': {
                "mode": "neural",
                "settings": {
                    "reading_up": True,
                    "clicks": { 
                        "list": [
                            "a", 
                            ".css-class"
                        ] 
                    },
                }
            }
        }
    )

    tests.run_test(
        'PATCH',
        'page/' + str(page_id),
        {},
        400,
        {
            'group_id': clone_group_id,
            'state': 1,
            'break_chain': 100,
            'url': [
                'https://example.com/' + str(random.randint(5, 500)),
                'https://example.com/' + str(random.randint(501, 1000)),
            ],
            'showtime': [15, 30],
            'behavior': {
                "mode": "neural",
                "settings": {
                    "reading_up": True,
                    "clicks": { 
                        "list": [
                            "a", 
                            ".css-class",
                            "#css_id"
                        ] 
                    },
                }
            }
        }
    )

    tests.run_test(
        'GET',
        'page/' + str(page_id),
        {
            "id": "int",
            "state": "int",
            "url": [
                "string"
            ],
            "showtime": [
                "int"
            ],
            "break_chain": "int",
            "adult": "bool",
            "group_id": "int",
            "behavior": {
                "mode": "string",
                "settings": {
                    "reading_up": "bool",
                    "clicks": { "list": ["string"] },
                    "manual": { "actions": {} }
                }
            }
        },
        200
    )

    clone_page = tests.run_test(
        'POST',
        'page/' + str(page_id) + '/clone',
        {
            "id": "int"
        },
        201
    )
    
    clone_page_id = json.loads(clone_page)['id']

    tests.run_test(
        'POST',
        'page/' + str(page_id + 2) + '/clone',
        {
            "errors": {
                "detail": "string"
            }
        },
        404
    )

    tests.run_test(
        'POST',
        'page/' + str(page_id) + '/up',
        'int',
        202
    )

    tests.run_test(
        'POST',
        'page/' + str(page_id + 2) + '/up',
        {
            "errors": {
                "detail": "string"
            }
        },
        404
    )

    tests.run_test(
        'POST',
        'page/' + str(page_id) + '/down',
        'int',
        202
    )

    tests.run_test(
        'POST',
        'page/' + str(page_id + 2) + '/down',
        {
            "errors": {
                "detail": "string"
            }
        },
        404
    )

    tests.run_test(
        'POST',
        'page/' + str(page_id) + '/start',
        'int',
        202
    )

    tests.run_test(
        'POST',
        'page/' + str(page_id + 2) + '/start',
        {
            "errors": {
                "detail": "string"
            }
        },
        404
    )

    tests.run_test(
        'POST',
        'page/' + str(page_id) + '/stop',
        'int',
        202
    )

    tests.run_test(
        'POST',
        'page/' + str(page_id + 2) + '/stop',
        {
            "errors": {
                "detail": "string"
            }
        },
        404
    )

    tests.run_test(
        'GET',
        'pages-compiled-stats',
        [
            {
                "page_id": "int",
                "count": "int"
            }
        ],
        200,
        {
            'page_id': page_id,
            'date': '2024-12-31'
        }
    )

    tests.run_test(
        'GET',
        'pages-compiled-stats',
        [
            {
                "page_id": "int",
                "count": "int"
            }
        ],
        200,
        {
            'page_id': page_id,
            'date_from': '2024-12-28',
            'date_to': '2024-12-31',
        }
    )

    tests.run_test(
        'GET',
        'pages-compiled-stats',
        [
            {
                "page_id": "int",
                "count": "int"
            }
        ],
        200,
        {
            'group_id': clone_group_id,
            'date': '2024-12-31'
        }
    )

    tests.run_test(
        'GET',
        'pages-compiled-stats',
        [
            {
                "page_id": "int",
                "count": "int"
            }
        ],
        200,
        {
            'group_id': clone_group_id,
            'date_from': '2024-12-28',
            'date_to': '2024-12-31',
        }
    )

    tests.run_test(
        'GET',
        'pages-compiled-stats',
        {
            "errors": {
                "detail": "string"
            }
        },
        404,
        {
            'page_id': page_id + 2,
            'date': '2024-12-31'
        }
    )

    tests.run_test(
        'GET',
        'pages-compiled-stats',
        {},
        400,
        {
            'page_id': page_id,
            'date': '2025-01-01'
        }
    )

    tests.run_test(
        'GET',
        'pages-compiled-stats',
        {},
        400,
        {
            'page_id': page_id,
            'date_from': '2025-01-01',
            'date_to': '2025-01-05',
        }
    )

    tests.run_test(
        'GET',
        'pages-compiled-stats',
        {},
        400,
        {
            'page_id': page_id,
            'date': '2024-13-01'
        }
    )

    tests.run_test(
        'GET',
        'pages-compiled-stats',
        {},
        400,
        {
            'page_id': page_id,
            'date_from': '2024-13-01',
            'date_to': '2024-13-05',
        }
    )

    tests.run_test(
        'GET',
        'pages-compiled-stats',
        {},
        400,
        {
            'page_id': page_id,
            'date_from': '2024',
            'date_to': '2024',
        }
    )

    tests.run_test(
        'GET',
        'pages-compiled-stats',
        {
            "errors":{
                "group_id":["string"]
            }
        },
        400,
        {
            'group_id': clone_group_id + 2,
            'date': '2024-12-31'
        }
    )

    tests.run_test(
        'GET',
        'pages-compiled-stats',
        {
            'page_id': page_id,
            'date': '2024-13-01'
        },
        200,
        {
            'group_id': clone_group_id,
            'date': '2025-01-01'
        }
    )

    tests.run_test(
        'GET',
        'pages-compiled-stats',
        {
            'page_id': page_id,
            'date': '2024-13-01'
        },
        200,
        {
            'group_id': clone_group_id,
            'date_from': '2025-01-01',
            'date_to': '2025-01-05',
        }
    )

    tests.run_test(
        'GET',
        'pages-compiled-stats',
        {
            "errors":{
                "date":["string"]
            }
        },
        400,
        {
            'group_id': clone_group_id,
            'date': '2024-13-01'
        }
    )

    tests.run_test(
        'GET',
        'pages-compiled-stats',
        {
            "errors":{
                "date_from":["string"],
                "date_to":["string"],
            }
        },
        400,
        {
            'group_id': clone_group_id,
            'date_from': '2024-13-01',
            'date_to': '2024-13-05',
        }
    )

    tests.run_test(
        'GET',
        'pages-compiled-stats',
        {
            "errors":{
                "date_from":["string"],
                "date_to":["string"],
            }
        },
        400,
        {
            'group_id': clone_group_id,
            'date_from': '2024',
            'date_to': '2024',
        }
    )

    tests.run_test(
        'DELETE',
        'page/' + str(page_id),
        "int",
        205
    )

    tests.run_test(
        'DELETE',
        'page/' + str(clone_page_id),
        "int",
        205
    )

    tests.run_test(
        'DELETE',
        'page/' + str(page_id),
        {
            "errors": {
                "detail": "string"
            }
        },
        404
    )

    tests.run_test(
        'DELETE',
        'group/' + str(clone_group_id),
        "int",
        205
    )

    tests.save_report('report_API_KEY2')