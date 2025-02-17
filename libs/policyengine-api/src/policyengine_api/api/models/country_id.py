from pydantic import validator
from policyengine_api.api.utils.constants import COUNTRIES


class CountryId(str):

    @validator("country_id")
    def validate_country_id(cls, v):
        if v not in COUNTRIES:
            raise ValueError("Invalid country ID")
        return v
