import pytest
from datetime import datetime
from core.bill import Bill


class TestBills:
    def test_failed_creation(self):
        with pytest.raises(TypeError) as e:
            Bill()

    def test_creation(self):
        Bill("test", datetime.now())
