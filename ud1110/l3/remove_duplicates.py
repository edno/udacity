# Define the remove_duplicates function
def remove_duplicates(values):
    dedup = []
    for value in values:
        if value not in dedup:
            dedup.append(value)
    return dedup
