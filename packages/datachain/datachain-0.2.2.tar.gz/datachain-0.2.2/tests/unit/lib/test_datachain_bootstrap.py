import pytest

from datachain.lib.dc import DataChain
from datachain.lib.udf import Mapper


class MyMapper(Mapper):
    DEFAULT_VALUE = 84
    BOOTSTRAP_VALUE = 1452
    TEARDOWN_VALUE = 98763

    def __init__(self):
        super().__init__()
        self.value = MyMapper.DEFAULT_VALUE
        self._had_teardown = False

    def process(self, *args) -> int:
        return self.value

    def setup(self):
        self.value = MyMapper.BOOTSTRAP_VALUE

    def teardown(self):
        self.value = MyMapper.TEARDOWN_VALUE


def test_udf():
    vals = ["a", "b", "c", "d", "e", "f"]
    chain = DataChain.from_features(key=vals)

    udf = MyMapper()
    res = chain.map(res=udf).collect_one("res")

    assert res == [MyMapper.BOOTSTRAP_VALUE] * len(vals)
    assert udf.value == MyMapper.TEARDOWN_VALUE


@pytest.mark.skip(reason="Skip until tests module will be importer for unit-tests")
def test_udf_parallel():
    vals = ["a", "b", "c", "d", "e", "f"]
    chain = DataChain.from_features(key=vals)

    res = chain.settings(parallel=4).map(res=MyMapper()).collect_one("res")

    assert res == [MyMapper.BOOTSTRAP_VALUE] * len(vals)


def test_no_bootstrap_for_callable():
    class MyMapper:
        def __init__(self):
            self._had_bootstrap = False
            self._had_teardown = False

        def __call__(self, *args):
            return None

        def bootstrap(self):
            self._had_bootstrap = True

        def teardown(self):
            self._had_teardown = True

    udf = MyMapper()

    chain = DataChain.from_features(key=["a", "b", "c"])
    chain.map(res=udf).collect()

    assert udf._had_bootstrap is False
    assert udf._had_teardown is False
