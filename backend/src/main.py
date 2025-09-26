from dotenv import load_dotenv

load_dotenv()

# These do important side-effects, so best include them asap
import telemetry  # noqa
import feature_flags  # noqa
from feature_flags import FeatureFlagsDep

from typing import Union
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(flags: FeatureFlagsDep, item_id: int, q: Union[str, None] = None ):
    return {"item_id": item_id, "q": q, "flag": flags.get_string_details("test_feature_one", "Not Available")}
