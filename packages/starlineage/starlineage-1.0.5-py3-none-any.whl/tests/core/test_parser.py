from unittest.mock import Mock

from sqlfluff.core import Linter

from starlineage.core.parser.sqlfluff.models import SqlFluffColumn
from starlineage.core.parser.sqlfluff.utils import find_from_expression_element


def test_column_extract_source_columns():
    segment_mock = Mock()
    segment_mock.type = ""
    assert [] == SqlFluffColumn._extract_source_columns(segment_mock)


def test_return_none_find_from_expression_element():
    file_segment = Linter(dialect="ansi").parse_string("TRUNCATE TABLE tab").tree
    assert find_from_expression_element(file_segment) is None
