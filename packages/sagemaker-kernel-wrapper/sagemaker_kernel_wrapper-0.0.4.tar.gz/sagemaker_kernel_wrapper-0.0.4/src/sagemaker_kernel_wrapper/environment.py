# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

import logging

logging.basicConfig()
logger = logging.getLogger("environment")
logger.setLevel(logging.INFO)


class RuntimeEnvironment:
    """Class used to retrieve different types of tags."""

    def __init__(self, client):
        self._client = client

    def get_execution_role_arn(self, domain_id, user_profile):
        try:
            if user_profile:
                response = self._client.describe_user_profile(
                    DomainId=domain_id, UserProfileName=user_profile
                )
                if "UserSettings" in response.keys():
                    if "ExecutionRole" in response["UserSettings"].keys():
                        return response["UserSettings"]["ExecutionRole"]

            response = self._client.describe_domain(DomainId=domain_id)
            if "DefaultUserSettings" in response.keys():
                if "ExecutionRole" in response["DefaultUserSettings"].keys():
                    return response["DefaultUserSettings"]["ExecutionRole"]
            if "DefaultSpaceSettings" in response.keys():
                if "ExecutionRole" in response["DefaultSpaceSettings"].keys():
                    return response["DefaultSpaceSettings"]["ExecutionRole"]
        except Exception as error:
            err_msg = (
                f"Error while retrieving execution role arn. This does not block Glue Interactive "
                f"Session kernel launch and Glue session still functions. Error: {error}"
            )
            logger.warning(err_msg)

        return None
