def recursive_search(src: dict, find_val: str, deep: int, parent=None):
    for key, value in src.items():
        parent = key
        if isinstance(value, dict):
            return recursive_search(value, find_val, deep + 1)
        elif isinstance(value, list):
            for i in value:
                if i == find_val:
                    return f'Значение {i} найдено на глубине {deep}, key = {parent}'
                if isinstance(i, dict):
                    return recursive_search(i, find_val, deep+1)
        else:
            if value == find_val:
                return f'Значение {value} найдено на глубине {deep}, key = {parent}'


get_source_dict = {
        "key1": "John",  # deep 0
        'key2': {
            'key3': 'Ann',  # deep 1
            'key4': {
                'key5': ['Kate', 'Mary'],  # deep 2
                'key6': {
                    'key7': [
                        'Bob',  # deep 3
                        'Duke',
                        {
                            'key8': {  # deep 4
                                'key9': [  # deep 5
                                    'Lisa',
                                    {
                                        'key10': ['Mark', 'Alex']  # deep 6
                                    }
                                ],
                                "key11": "Louisa",  # deep 5
                            }
                        },
                        "Alex",  # deep 3
                    ]
                },
            },
            'key12': 'Robert'  # deep 1
        },
        "key13": "Ronaldo"  # deep 0
    }


print(recursive_search(get_source_dict, "Bob", 0, None))
