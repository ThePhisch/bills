import pytest
from core.tag import Tag


class TestTag:
    def test_failed_creation():
        with pytest.raises(TypeError) as e:
            Tag()

    def test_creation():
        tag = Tag("payment_method", ["cash", "card"])
        assert tag.name == "payment_method"
        assert tag.values == ["cash", "card"]

    def test_shortform():
        tag = Tag(
            "payment_method",
            ["cash", "card"],
            shortform="pm",
            shortform_values={"cash": "b", "card": "k"},
        )
        assert tag.shortform == "pm"
        assert tag.shortform_values == {"cash": "b", "card": "k"}