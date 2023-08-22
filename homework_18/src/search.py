def search_record(dataset, search_type, value):  # value - is part or full number (1)
    result = {}
    if search_type == 'sp':
        for phone in dataset:
            if value in phone:
                result.update({phone: dataset[phone]})
    elif search_type == 'sf':
        for phone, data in dataset.items():
            if value.lower() in data['first_name'].lower():
                result.update({phone: dataset[phone]})
    elif search_type == 'sl':
        for phone, data in dataset.items():
            if value.lower() in data['last_name'].lower():
                result.update({phone: dataset[phone]})
    elif search_type == 'sfl':
        for phone, data in dataset.items():
            if value[0].lower() in data['first_name'].lower() and value[1].lower() in data['last_name'].lower():
                result.update({phone: dataset[phone]})
    elif search_type == 'sct':
        for phone, data in dataset.items():
            if value.lower() in data['city'].lower():
                result.update({phone: dataset[phone]})
    elif search_type == 'sc':
        for phone, data in dataset.items():
            if value.lower() in data['country'].lower():
                result.update({phone: dataset[phone]})
    return result
