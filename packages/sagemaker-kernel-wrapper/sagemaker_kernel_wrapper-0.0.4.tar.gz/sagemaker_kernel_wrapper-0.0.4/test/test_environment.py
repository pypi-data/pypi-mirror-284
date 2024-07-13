import unittest
from unittest.mock import Mock

from sagemaker_kernel_wrapper.environment import RuntimeEnvironment


class TestRuntimeEnvironment(unittest.TestCase):

    def setUp(self):
        # Create a mock Boto3 client for testing
        self.mock_client = Mock()
        self.runtime_environment = RuntimeEnvironment(self.mock_client)

    def test_get_execution_role_arn_user_profile(self):
        user_profile_execution_role_arn = (
            "arn:aws:iam::123456789012:role/service-role/AmazonSageMakerExecutionRole"
        )
        domain_profile_execution_role_arn = (
            "arn:aws:iam::123456789012:role/service-role/AmazonSageMakerExecutionRole"
        )
        self.mock_client.describe_user_profile.return_value = {
            "UserProfileArn": "arn:aws:sagemaker:us-west-2:123456789012:domain/test-user",
            "UserSettings": {
                "ExecutionRole": user_profile_execution_role_arn,
            },
        }

        self.mock_client.describe_domain.return_value = {
            "DomainArn": "arn:aws:sagemaker:us-west-2:123456789012:domain/test-domain",
            "DefaultUserSettings": {
                "ExecutionRole": domain_profile_execution_role_arn,
            },
        }

        runtime_environment = RuntimeEnvironment(self.mock_client)
        role_arn = runtime_environment.get_execution_role_arn("test-domain", "user-profile")

        self.assertEqual(role_arn, user_profile_execution_role_arn)
        self.mock_client.describe_user_profile.assert_called_once_with(
            DomainId="test-domain", UserProfileName="user-profile"
        )
        self.mock_client.describe_domain.assert_not_called()

    def test_get_execution_role_arn_domain_profile(self):
        domain_profile_execution_role_arn = (
            "arn:aws:iam::123456789012:role/service-role/AmazonSageMakerExecutionRole"
        )
        self.mock_client.describe_user_profile.return_value = {}

        self.mock_client.describe_domain.return_value = {
            "DomainArn": "arn:aws:sagemaker:us-west-2:123456789012:domain/test-domain",
            "DefaultUserSettings": {
                "ExecutionRole": domain_profile_execution_role_arn,
            },
        }

        runtime_environment = RuntimeEnvironment(self.mock_client)
        role_arn = runtime_environment.get_execution_role_arn("test-domain", "user-profile")

        self.assertEqual(role_arn, domain_profile_execution_role_arn)
        self.mock_client.describe_user_profile.assert_called_once_with(
            DomainId="test-domain", UserProfileName="user-profile"
        )
        self.mock_client.describe_domain.assert_called_once_with(DomainId="test-domain")

    def test_get_execution_role_arn_domain_profile_default_space(self):
        space_settings_execution_role_arn = (
            "arn:aws:iam::123456789012:role/service-role/AmazonSageMakerExecutionRole"
        )
        self.mock_client.describe_user_profile.return_value = {}

        self.mock_client.describe_domain.return_value = {
            "DomainArn": "arn:aws:sagemaker:us-west-2:123456789012:domain/test-domain",
            "DefaultSpaceSettings": {
                "ExecutionRole": space_settings_execution_role_arn,
            },
        }

        runtime_environment = RuntimeEnvironment(self.mock_client)
        role_arn = runtime_environment.get_execution_role_arn("test-domain", "user-profile")

        self.assertEqual(role_arn, space_settings_execution_role_arn)
        self.mock_client.describe_user_profile.assert_called_once_with(
            DomainId="test-domain", UserProfileName="user-profile"
        )
        self.mock_client.describe_domain.assert_called_once_with(DomainId="test-domain")

    def test_get_execution_role_arn_no_profile(self):
        self.mock_client.describe_user_profile.return_value = {}
        self.mock_client.describe_domain.return_value = {}

        runtime_environment = RuntimeEnvironment(self.mock_client)
        role_arn = runtime_environment.get_execution_role_arn("test-domain", "user-profile")

        self.assertEqual(role_arn, None)
        self.mock_client.describe_user_profile.assert_called_once_with(
            DomainId="test-domain", UserProfileName="user-profile"
        )
        self.mock_client.describe_domain.assert_called_once_with(DomainId="test-domain")
