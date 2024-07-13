from typing import Any, List, Tuple

from bpkio_api.caching import cache_api_results
from bpkio_api.consumer import BpkioSdkConsumer
from bpkio_api.helpers.list import get_all_with_pagination
from bpkio_api.helpers.search import SearchMethod, search_array_with_filters
from bpkio_api.models.Tenants import Tenant
from bpkio_api.response_handler import postprocess_response
from uplink import Query, get, response_handler, returns, post


@response_handler(postprocess_response)
class TenantsApi(BpkioSdkConsumer):
    def __init__(self, base_url="", **kwargs):
        super().__init__(base_url, **kwargs)

    @returns.json(List[Tenant])
    @get("admin/tenants")
    def get_page(self, offset: Query = 0, limit: Query = 5) -> List[Tenant]:  # type: ignore
        """List all tenants"""

    @returns.json(Tenant)
    @get("admin/tenants/{tenant_id}")
    def retrieve(self, tenant_id) -> Tenant:
        """Get a single tenant, by ID"""

    @returns.json(Tenant)
    @get("tenants/me")
    def retrieve_self(self) -> Tenant:
        """Get the tenant information for the current user"""

    @post("admin/tenants/{tenant_id}/reset-quotas")
    def reset_quotas(self, tenant_id) -> None:
        """Reset quotas for a tenant, by ID"""

    # === Helpers ===

    @cache_api_results("list_tenants")
    def list(self):
        return get_all_with_pagination(self.get_page)

    def search(
        self,
        value: Any | None = None,
        field: str | None = None,
        method: SearchMethod = SearchMethod.STRING_SUB,
        filters: List[Tuple[Any, str | None, SearchMethod | None]] | None = None,
    ) -> List[Tenant]:
        """Searches the list of tenants for those matching a particular filter query

        You can search for full or partial matches in all or specific fields.
        All searches are done as string matches (regarding of the actual type of each field)

        Args:
            value (Any, optional): The string value to search. Defaults to None.
            field (str, optional): The field name in which to search for the value.
                Defaults to None.
            method (SearchMethod, optional): How to perform the search.
                SearchMethod.STRING_SUB searches for partial string match. This is the default.
                SearchMethod.STRING_MATCH searches for a complete match (after casting to string).
                SearchMethod.STRICT searches for a strict match (including type)
            filters (List[Tuple[Any, Optional[str], Optional[SearchMethod]]], optional):
                Can be used as an alternatitve to using `value`, `field` and `method`,
                in particular if multiple search patterns need to be specified
                (which are then treated as logical `AND`). Defaults to None.

        Returns:
            List[Tenant]: List of matching sources
        """
        if not filters:
            filters = [(value, field, method)]

        sources = self.list()
        return search_array_with_filters(sources, filters=filters)
