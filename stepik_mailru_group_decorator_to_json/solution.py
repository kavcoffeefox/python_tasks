# -*- coding: UTF-8 -*-
import json
import functools


def to_json(f):
    @functools.wraps(f)
    def new_f(*args, **kwargs):
        return json.dumps(f(*args, **kwargs))
    return new_f


@to_json
def get_data():
  return {
    'data': 42
  }


if __name__ == "__main__":
    print(get_data())
