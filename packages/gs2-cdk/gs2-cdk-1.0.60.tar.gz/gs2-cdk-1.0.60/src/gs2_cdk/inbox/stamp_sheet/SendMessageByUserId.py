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
from ..model.TimeSpan import TimeSpan


class SendMessageByUserId(AcquireAction):

    def __init__(
        self,
        namespace_name: str,
        metadata: str,
        read_acquire_actions: Optional[List[AcquireAction]] = None,
        expires_at: Optional[int] = None,
        expires_time_span: Optional[TimeSpan] = None,
        user_id: Optional[str] = "#{userId}",
    ):
        properties: Dict[str, Any] = {}

        properties["namespaceName"] = namespace_name
        properties["metadata"] = metadata
        properties["readAcquireActions"] = read_acquire_actions
        properties["expiresAt"] = expires_at
        properties["expiresTimeSpan"] = expires_time_span
        properties["userId"] = user_id

        super().__init__(
            "Gs2Inbox:SendMessageByUserId",
            properties,
        )
