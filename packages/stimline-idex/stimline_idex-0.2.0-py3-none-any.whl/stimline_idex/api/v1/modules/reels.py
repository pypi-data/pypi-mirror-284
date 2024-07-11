import logging
from typing import Any, Optional, Union, overload

from ....data_schemas.v1.assets import Reel
from ....data_schemas.v1.events import JobHistory, Maintenance, ScheduledJob
from ..api import IDEXApi


class Reels:
    def __init__(self, api: IDEXApi) -> None:
        self._api = api

    @overload
    def get(self, *, id: str) -> Reel: ...
    @overload
    def get(
        self,
        *,
        filter: Optional[str] = None,
        select: Optional[list[str]] = None,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        order_by: Optional[str] = None,
    ) -> list[Reel]: ...

    def get(
        self,
        id: Optional[str] = None,
        filter: Optional[str] = None,
        select: Optional[list[str]] = None,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        order_by: Optional[str] = None,
    ) -> Union[Reel, list[Reel]]:
        """
        Get `Reel` object(s).

        Parameters
        ----------
        id : Optional[str]
            Reel to retrieve.
        filter : Optional[str]
            OData filter string.
        select : list[str] | None
            Provide a list of columns to retrieve from output.
        top : Optional[int]
            Limit the number of results returned.
        skip : Optional[int]
            Skip the first N results.
        order_by : Optional[str]
            Order the results by columns.

        Returns
        -------
        Union[Reel, list[Reel]]
            The `Reel` object(s).

        """
        if id is not None:
            logging.debug(f"Getting Reel with ID: {id}")
            data = self._api.get(url=f"Reels/{id}")
            return Reel.model_validate(data.json())

        params: dict[str, Any] = {}
        if filter is not None:
            params["$filter"] = filter
        if select is not None:
            select = self._check_select(select)
            params["$select"] = ",".join(select)
        if top is not None:
            params["$top"] = top
        if skip is not None:
            params["$skip"] = skip
        if order_by is not None:
            params["$orderby"] = order_by

        data = self._api.get(url="Reels", params=params)

        if data.status_code == 204:
            return []

        return [Reel.model_validate(row) for row in data.json()]

    def _check_select(self, select: list[str]) -> list[str]:
        important_fields = ["id"]
        for field in important_fields:
            if field not in select:
                select.append(field)
        return select

    def get_maintenances(self, reel: Optional[Reel] = None, reel_id: Optional[str] = None) -> list[Maintenance]:
        if reel is not None:
            id = reel.id
        elif reel_id is not None:
            id = reel_id
        else:
            raise ValueError("Invalid input. Must provide either a Reel object or a reel_id.")

        logging.debug(f"Getting Maintenances for Reel with ID: {id}")
        data = self._api.get(url=f"Reels/{id}/Maintenances")
        if data.status_code == 204:
            return []

        return [Maintenance.model_validate(row) for row in data.json()]

    def get_job_history(self, reel: Optional[Reel] = None, reel_id: Optional[str] = None) -> list[JobHistory]:
        if reel is not None:
            id = reel.id
        elif reel_id is not None:
            id = reel_id
        else:
            raise ValueError("Invalid input. Must provide either a Reel object or a reel_id.")

        logging.debug(f"Getting JobHistory for Reel with ID: {id}")
        data = self._api.get(url=f"Reels/{id}/JobHistory")
        if data.status_code == 204:
            return []

        return [JobHistory.model_validate(row) for row in data.json()]

    def get_scheduled_jobs(self, reel: Optional[Reel] = None, reel_id: Optional[str] = None) -> list[ScheduledJob]:
        if reel is not None:
            id = reel.id
        elif reel_id is not None:
            id = reel_id
        else:
            raise ValueError("Invalid input. Must provide either a Reel object or a reel_id.")

        logging.debug(f"Getting ScheduledJobs for Reel with ID: {id}")
        data = self._api.get(url=f"Reels/{id}/ScheduledJobs")
        if data.status_code == 204:
            return []

        return [ScheduledJob.model_validate(row) for row in data.json()]
