import os

from fastapi import Depends
from openfeature import api
from openfeature.client import OpenFeatureClient
from openfeature_flagsmith.provider import FlagsmithProvider
from flagsmith import Flagsmith
from typing_extensions import Annotated

api.set_provider(
    FlagsmithProvider(
        client=Flagsmith(
            environment_key=os.environ["FLAGSMITH_ENVIRONMENT_KEY"],
            api_url="http://flagsmith:8000/api/v1/",

        )
    )
)


async def get_client() -> OpenFeatureClient:
    return api.get_client()


FeatureFlagsDep = Annotated[OpenFeatureClient, Depends(get_client)]
