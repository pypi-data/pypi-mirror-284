# pylint: disable
# flake8: noqa
from __future__ import annotations
from enum import Enum
from typing import Annotated, List, Optional, Union

from pydantic import BaseModel, Field

from llamazure.azrest.models import AzList, ReadOnly, Req, default_list, default_dict



class DashboardParts(BaseModel):
	"""A dashboard part."""
	class Position(BaseModel):
		"""The dashboard's part position."""

		x: int
		y: int
		rowSpan: int
		colSpan: int
		metadata: Optional[dict] = None

		def __eq__(self, o) -> bool:
			return (
				isinstance(o, self.__class__)
				and self.x == o.x
				and self.y == o.y
				and self.rowSpan == o.rowSpan
				and self.colSpan == o.colSpan
				and self.metadata == o.metadata
			)


	position: Position
	metadata: Optional[dict] = None

	def __eq__(self, o) -> bool:
		return (
			isinstance(o, self.__class__)
			and self.position == o.position
			and self.metadata == o.metadata
		)



class MarkdownPartMetadata(BaseModel):
	"""Markdown part metadata."""

	inputs: Annotated[List[dict],default_list] = []
	settings: Optional[dict] = None

	def __eq__(self, o) -> bool:
		return (
			isinstance(o, self.__class__)
			and self.inputs == o.inputs
			and self.settings == o.settings
		)



class DashboardLens(BaseModel):
	"""A dashboard lens."""

	order: int
	parts: Annotated[List[DashboardParts],default_list] = []
	metadata: Optional[dict] = None

	def __eq__(self, o) -> bool:
		return (
			isinstance(o, self.__class__)
			and self.order == o.order
			and self.parts == o.parts
			and self.metadata == o.metadata
		)



class Dashboard(BaseModel):
	"""The shared dashboard resource definition."""
	class Properties(BaseModel):
		"""The shared dashboard properties."""

		lenses: Annotated[List[DashboardLens],default_list] = []
		metadata: Optional[dict] = None

		def __eq__(self, o) -> bool:
			return (
				isinstance(o, self.__class__)
				and self.lenses == o.lenses
				and self.metadata == o.metadata
			)


	properties: Properties
	rid: ReadOnly[str] = Field(alias="id", default=None)
	name: ReadOnly[str] = None
	type: ReadOnly[str] = None
	location: str
	tags: Optional[dict] = None

	def __eq__(self, o) -> bool:
		return (
			isinstance(o, self.__class__)
			and self.properties == o.properties
			and self.location == o.location
			and self.tags == o.tags
		)



class PatchableDashboard(BaseModel):
	"""The shared dashboard resource definition."""
	class Properties(BaseModel):
		"""The shared dashboard properties."""

		lenses: Annotated[List[DashboardLens],default_list] = []
		metadata: Optional[dict] = None

		def __eq__(self, o) -> bool:
			return (
				isinstance(o, self.__class__)
				and self.lenses == o.lenses
				and self.metadata == o.metadata
			)


	properties: Properties
	tags: Optional[dict] = None

	def __eq__(self, o) -> bool:
		return (
			isinstance(o, self.__class__)
			and self.properties == o.properties
			and self.tags == o.tags
		)



class ResourceProviderOperation(BaseModel):
	"""Supported operations of this resource provider."""
	class Display(BaseModel):
		"""Display metadata associated with the operation."""

		provider: Optional[str] = None
		resource: Optional[str] = None
		operation: Optional[str] = None
		description: Optional[str] = None

		def __eq__(self, o) -> bool:
			return (
				isinstance(o, self.__class__)
				and self.provider == o.provider
				and self.resource == o.resource
				and self.operation == o.operation
				and self.description == o.description
			)


	name: Optional[str] = None
	isDataAction: Optional[str] = None
	display: Optional[Display] = None

	def __eq__(self, o) -> bool:
		return (
			isinstance(o, self.__class__)
			and self.name == o.name
			and self.isDataAction == o.isDataAction
			and self.display == o.display
		)



class ErrorResponse(BaseModel):
	"""Error response."""

	error: Optional[ErrorDefinition] = None

	def __eq__(self, o) -> bool:
		return (
			isinstance(o, self.__class__)
			and self.error == o.error
		)



class ErrorDefinition(BaseModel):
	"""Error definition."""

	code: ReadOnly[int] = None
	message: ReadOnly[str] = None
	details: Annotated[List[ErrorDefinition],default_list] = []

	def __eq__(self, o) -> bool:
		return (
			isinstance(o, self.__class__)
			and self.details == o.details
		)



DashboardListResult = AzList[Dashboard]

ResourceProviderOperationList = AzList[ResourceProviderOperation]

DashboardParts.model_rebuild()

MarkdownPartMetadata.model_rebuild()

DashboardLens.model_rebuild()

Dashboard.model_rebuild()

PatchableDashboard.model_rebuild()

ResourceProviderOperation.model_rebuild()

ErrorResponse.model_rebuild()

ErrorDefinition.model_rebuild()

DashboardListResult.model_rebuild()

ResourceProviderOperationList.model_rebuild()


class AzOperations:
	apiv = "2020-09-01-preview"
	@staticmethod
	def List() -> Req[ResourceProviderOperationList]:
		"""The Microsoft Portal operations API."""
		r = Req.get(
			name="Operations.List",
			path=f"/providers/Microsoft.Portal/operations",
			apiv="2020-09-01-preview",
			ret_t=ResourceProviderOperationList
		)

		return r



class AzDashboards:
	apiv = "2020-09-01-preview"
	@staticmethod
	def Get(subscriptionId: str, resourceGroupName: str, dashboardName: str) -> Req[Dashboard]:
		"""Gets the Dashboard."""
		r = Req.get(
			name="Dashboards.Get",
			path=f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Portal/dashboards/{dashboardName}",
			apiv="2020-09-01-preview",
			ret_t=Dashboard
		)

		return r

	@staticmethod
	def CreateOrUpdate(subscriptionId: str, resourceGroupName: str, dashboardName: str, dashboard: Dashboard) -> Req[Dashboard]:
		"""Creates or updates a Dashboard."""
		r = Req.put(
			name="Dashboards.CreateOrUpdate",
			path=f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Portal/dashboards/{dashboardName}",
			apiv="2020-09-01-preview",
			body=dashboard,
			ret_t=Dashboard
		)

		return r

	@staticmethod
	def Delete(subscriptionId: str, resourceGroupName: str, dashboardName: str) -> Req[None]:
		"""Deletes the Dashboard."""
		r = Req.delete(
			name="Dashboards.Delete",
			path=f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Portal/dashboards/{dashboardName}",
			apiv="2020-09-01-preview",
			ret_t=None
		)

		return r

	@staticmethod
	def Update(subscriptionId: str, resourceGroupName: str, dashboardName: str, dashboard: PatchableDashboard) -> Req[Dashboard]:
		"""Updates an existing Dashboard."""
		r = Req.patch(
			name="Dashboards.Update",
			path=f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Portal/dashboards/{dashboardName}",
			apiv="2020-09-01-preview",
			body=dashboard,
			ret_t=Dashboard
		)

		return r

	@staticmethod
	def ListByResourceGroup(subscriptionId: str, resourceGroupName: str) -> Req[DashboardListResult]:
		"""Gets all the Dashboards within a resource group."""
		r = Req.get(
			name="Dashboards.ListByResourceGroup",
			path=f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Portal/dashboards",
			apiv="2020-09-01-preview",
			ret_t=DashboardListResult
		)

		return r

	@staticmethod
	def ListBySubscription(subscriptionId: str) -> Req[DashboardListResult]:
		"""Gets all the dashboards within a subscription."""
		r = Req.get(
			name="Dashboards.ListBySubscription",
			path=f"/subscriptions/{subscriptionId}/providers/Microsoft.Portal/dashboards",
			apiv="2020-09-01-preview",
			ret_t=DashboardListResult
		)

		return r

