# DO NOT EDIT! This file is automatically generated
import typing

from commercetools._schemas._graph_ql import GraphQLResponseSchema
from commercetools.helpers import RemoveEmptyValuesMixin
from commercetools.types._graph_ql import GraphQLResponse
from commercetools.typing import OptionalListStr

from . import abstract, traits


class GraphqlService(abstract.AbstractService):
    """The commercetools™ platform provides a GraphQL API"""

    def create(self) -> GraphQLResponse:
        """Execute a GraphQL query

        The commercetools™ platform provides a GraphQL API
        """
        params = {}
        return self._client._post(
            endpoint="graphql", params=params, response_schema_cls=GraphQLResponseSchema
        )
