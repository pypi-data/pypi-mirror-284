from sqlparse.sql import Function, Token

from starlineage.core.holders import SubQueryLineageHolder
from starlineage.core.parser.sqlparse.handlers.base import CurrentTokenBaseHandler
from starlineage.core.parser.sqlparse.models import SqlParseTable
from starlineage.utils.helpers import escape_identifier_name


class SwapPartitionHandler(CurrentTokenBaseHandler):
    """
    a special handling for swap_partitions_between_tables function of Vertica SQL dialect.
    """

    def handle(self, token: Token, holder: SubQueryLineageHolder) -> None:
        if (
            isinstance(token, Function)
            and token.get_name().lower() == "swap_partitions_between_tables"
        ):
            _, parenthesis = token.tokens
            _, identifier_list, _ = parenthesis.tokens
            identifiers = list(identifier_list.get_identifiers())
            holder.add_read(
                SqlParseTable(escape_identifier_name(identifiers[0].normalized))
            )
            holder.add_write(
                SqlParseTable(escape_identifier_name(identifiers[3].normalized))
            )
