# -*- coding: UTF-8 -*-
import csv
import os


class CarBase:
    """This class for read file"""
    def __init__(self, brand, photo_file_name, carrying):
        self.photo_file_name = photo_file_name
        self.car_type = None
        self.brand = brand
        self.carrying = carrying

    def get_photo_file_ext(self):
        return str(os.path.splitext(self.photo_file_name)[1].split('.')[1])


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count
        self.car_type = "car"


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super.__init__(brand, photo_file_name, carrying)
        self._split_body_whl(body_whl)
        self.car_type = "truck"

    def _split_body_whl(self, body_whl):
        if body_whl:
            self.body_length, self.body_width, self.body_height = map(float, str(body_whl).split('x'))
        else:
            self.body_length, self.body_width, self.body_height = 0, 0, 0

    def get_body_volume(self):
        return float(self.body_length * self.body_width * self.body_height)


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super.__init__(brand, photo_file_name, carrying)
        self.extra = extra
        self.car_type = "spec_machine"


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            print(row)
    return car_list


if __name__ == "__main__":
    print(get_car_list("week3_cars.csv"))
    # unittest.main()

