from typing import Literal, Optional

from datachain.lib.dc import C, DataChain
from datachain.lib.feature import Feature


class NestedFeature(Feature):
    value: str


class Embedding(Feature):
    value: float
    nested: NestedFeature = NestedFeature(value="nested_value")
    literal_field: Optional[Literal["end_turn", "max_tokens", "stop_sequence"]] = None


# ToDO: make it parallel
ds_name = "feature_class"
ds = (
    DataChain.from_storage("gs://dvcx-datalakes/dogs-and-cats/")
    .filter(C.name.glob("*cat*.jpg"))  # type: ignore [attr-defined]
    .limit(5)
    .settings(cache=True, parallel=2)
    .map(emd=lambda file: Embedding(value=512), output=Embedding)
    .save(ds_name)
)

for row in ds.results():
    print(row[5])
