from datetime import datetime

import pytest

from snowflake import Snowflake


@pytest.fixture
def sample_obj():
    return Snowflake(
        timestamp=datetime(2016, 4, 30, 4, 18, 25, 796000),
        worker_id=1,
        process_id=0,
        increment=7,
    )


@pytest.fixture
def sample_snowflake():
    return "175928847299117063"


def test_parse(sample_snowflake, sample_obj):
    parsed = Snowflake.parse(sample_snowflake)
    assert parsed.timestamp == sample_obj.timestamp
    assert parsed.worker_id == sample_obj.worker_id
    assert parsed.process_id == sample_obj.process_id
    assert parsed.increment == sample_obj.increment


def test_format(sample_obj, sample_snowflake):
    check = sample_obj.format()
    assert check == sample_snowflake
