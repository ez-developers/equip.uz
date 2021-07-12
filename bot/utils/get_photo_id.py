

def get_max_file_size(array: list):
    sizes = []
    for i in array:
        sizes.append(i.file_size)
    return max(sizes)


def get_photo_id(array: list):
    for i in array:
        if i.file_size == get_max_file_size(array):
            return i.file_id
