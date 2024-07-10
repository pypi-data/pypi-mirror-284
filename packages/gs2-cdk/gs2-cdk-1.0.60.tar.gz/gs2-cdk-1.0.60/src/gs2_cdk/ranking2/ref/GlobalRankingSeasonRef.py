# Copyright 2016- Game Server Services, Inc. or its affiliates. All Rights
# Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.
from __future__ import annotations
from typing import *

from ...core.func import GetAttr, Join
from .GlobalRankingBorderRef import GlobalRankingBorderRef


class GlobalRankingSeasonRef:
    namespace_name: str
    ranking_name: str
    season: int

    def __init__(
        self,
        namespace_name: str,
        ranking_name: str,
        season: int,
    ):
        self.namespace_name = namespace_name
        self.ranking_name = ranking_name
        self.season = season

    def grn(
        self,
    ) -> str:
        return Join(
            ":",
            [
                "grn",
                "gs2",
                GetAttr.region(
                ).str(
                ),
                GetAttr.owner_id(
                ).str(
                ),
                "ranking2",
                self.namespace_name,
                "global",
                self.ranking_name,
                "ranking",
                "global",
                self.season,
            ],
        ).str(
        )
