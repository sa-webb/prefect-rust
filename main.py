import pyrust

from prefect import flow
from pydantic import BaseModel, model_validator


class Compute(BaseModel):
    a: int
    b: int

    result: int

    @model_validator(mode="before")
    def compute_sum(cls, values):
        result = pyrust.sum(values.get("a"), values.get("b"))
        return {**values, "result": result}


class Place(BaseModel):
    city: str
    state: str

    @model_validator(mode="before")
    def extract_city(cls, values):
        location = values.pop("location")
        city, state = pyrust.extract_city_state(location=location)
        return {"city": city, "state": state}


@flow
def main():
    sum = Compute(a=1, b=2)
    print(sum.result)  # 3

    data = {"location": "New York, NY"}
    place = Place(**data)
    print(place.city)  # New York
    print(place.state)  # NY


if __name__ == "__main__":
    main()
