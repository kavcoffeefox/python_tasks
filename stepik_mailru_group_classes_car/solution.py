# -*- coding: UTF-8 -*-
import csv
import os


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.photo_file_name = photo_file_name
        self.car_type = None
        self.brand = brand
        self.carrying = carrying

    def get_photo_file_ext(self):
        return str(os.path.splitext(self.photo_file_name)[1])

    def __str__(self):
        return f"Brand: {self.brand}, Car type: {self.car_type}"

    @classmethod
    def is_valid_args(cls, **kwargs):
        if not kwargs["photo_file_name"]:
            return False
        if not kwargs["brand"]:
            return False
        if not kwargs["carrying"]:
            return False
        return True


class Car(CarBase):
    passenger_seats_count_id = 2

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)
        self.car_type = "car"

    @classmethod
    def is_valid_args(cls, **kwargs):
        return CarBase.is_valid_args(**kwargs) and Car.is_valid_special_arg(kwargs["passenger_seats_count"])

    @classmethod
    def is_valid_special_arg(cls, passenger_seats_count):
        if not passenger_seats_count:
            return False
        else:
            return True

    @classmethod
    def bild_car(cls, **kwargs):
        return cls(kwargs["brand"],  kwargs["photo_file_name"],  kwargs["carrying"],  kwargs["passenger_seats_count"])


class Truck(CarBase):
    body_whl_id = 4

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self._split_body_whl(body_whl)
        self.car_type = "truck"

    def _split_body_whl(self, body_whl):
        if body_whl:
            self.body_length, self.body_width, self.body_height = map(float, str(body_whl).split('x'))
        else:
            self.body_length, self.body_width, self.body_height = 0, 0, 0

    def get_body_volume(self):
        return float(self.body_length * self.body_width * self.body_height)

    @classmethod
    def is_valid_special_arg(cls, body_whl):
        return True

    @classmethod
    def is_valid_args(cls, **kwargs):
        return CarBase.is_valid_args(**kwargs) and Car.is_valid_special_arg(kwargs["body_whl"])

    @classmethod
    def bild_car(cls, **kwargs):
        return cls(kwargs["brand"],  kwargs["photo_file_name"],  kwargs["carrying"],  kwargs["body_whl"])


class SpecMachine(CarBase):
    extra_id = 6

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra
        self.car_type = "spec_machine"

    @classmethod
    def is_valid_special_arg(cls, extra):
        if not extra:
            return False
        else:
            return True

    @classmethod
    def is_valid_args(cls, **kwargs):
        return CarBase.is_valid_args(**kwargs) and Car.is_valid_special_arg(kwargs["extra"])

    @classmethod
    def bild_car(cls, **kwargs):
        return cls(kwargs["brand"], kwargs["photo_file_name"], kwargs["carrying"], kwargs["extra"])


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            if len(row) == 7:
                car_type, brand, passenger_seats_count, photo_file_name, body_whl, carrying, extra = row
                if CarBase.is_valid_args(brand=brand, photo_file_name=photo_file_name, carrying=carrying):
                    if row[0] == 'car':
                        if Car.is_valid_special_arg(passenger_seats_count=passenger_seats_count):
                            car_list.append(
                                Car.bild_car(
                                            brand=brand,
                                            photo_file_name=photo_file_name,
                                            carrying=carrying,
                                            passenger_seats_count=passenger_seats_count))
                    if row[0] == 'truck':
                        if Truck.is_valid_special_arg(body_whl=row[Truck.body_whl_id]):
                            car_list.append(
                                Truck.bild_car(
                                            brand=brand,
                                            photo_file_name=photo_file_name,
                                            carrying=carrying,
                                            body_whl=row[Truck.body_whl_id]))
                    if row[0] == 'spec_machine':
                        if SpecMachine.is_valid_special_arg(extra=row[SpecMachine.extra_id]):
                            car_list.append(
                                SpecMachine.bild_car(
                                            brand=brand,
                                            photo_file_name=photo_file_name,
                                            carrying=carrying,
                                            extra=row[SpecMachine.extra_id]))
    return car_list


if __name__ == "__main__":
    list_car = get_car_list("week3_cars.csv")
    print(list_car)
    for i in list_car:
        print(i.get_photo_file_ext())
        if i.car_type == 'truck':
            print(i.get_body_volume())
        if i.car_type == 'car':
            print(i.passenger_seats_count)
        # unittest.main()
