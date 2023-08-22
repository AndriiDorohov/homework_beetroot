def create(dataset: dict, data: dict):
    dataset.update(data)
    return dataset


def update(dataset: dict, data: dict):

    for phone in dataset:
        if list(data.keys())[0] in phone:
            return {**dataset, **data}


def delete(dataset: dict, ph_number):
    if ph_number in dataset:
        del dataset[ph_number]
        print("The entry with this phone number has been deleted")
    else:
        print("This phone number does not exist in the phone book")
    return dataset
