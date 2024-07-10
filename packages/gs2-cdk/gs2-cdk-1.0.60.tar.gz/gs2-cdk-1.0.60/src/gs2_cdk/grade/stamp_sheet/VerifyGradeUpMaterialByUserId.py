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

from ...core.model import AcquireAction, ConsumeAction


class VerifyGradeUpMaterialByUserId(ConsumeAction):

    def __init__(
        self,
        namespace_name: str,
        grade_name: str,
        verify_type: str,
        property_id: str,
        material_property_id: str,
        user_id: Optional[str] = "#{userId}",
    ):
        properties: Dict[str, Any] = {}

        properties["namespaceName"] = namespace_name
        properties["gradeName"] = grade_name
        properties["verifyType"] = verify_type
        properties["propertyId"] = property_id
        properties["materialPropertyId"] = material_property_id
        properties["userId"] = user_id

        super().__init__(
            "Gs2Grade:VerifyGradeUpMaterialByUserId",
            properties,
        )
