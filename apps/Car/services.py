import os


def images_car_upload(instance, file) -> str:
    return os.path.join(str(instance.car.id), 'car', file)
