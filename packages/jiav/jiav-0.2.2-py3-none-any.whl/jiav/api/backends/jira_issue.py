#!/usr/bin/env python

from collections import namedtuple

from jiav import logger
from jiav.api.backends import BaseBackend
from jiav.api.schemas.jira_issue import schema
from jiav.utils.jira import JiraConnection

MOCK_STEP = {"issue": "TEST-1", "status": "Done"}

jiav_logger = logger.subscribe_to_logger()


class JiraIssueBackend(BaseBackend):
    """
    JiraIssueBackend object

    Checks that a Jira issue is in a desired status

    Attributes:
        name   - Backend name
        schema - json_schema to be used to verify that the supplied step is
                 valid according to the backends's requirements
        step   - Backend excution instructions
    """

    def __init__(self):
        self.name = "jira_issue"
        self.schema = schema
        self.step = MOCK_STEP
        super().__init__(self.name, self.schema, self.step)

    # Overrdie method of BaseBackend
    def execute_backend(self):
        """
        Execute backend

        Returns a namedtuple describing the jiav manifest execution
        """
        # Parse required arugments
        issue = self.step["issue"]
        issue_status = self.step["status"]
        # Create a namedtuple to hold the execution result output and errors
        result = namedtuple("result", ["successful", "output", "errors"])
        output = list()
        errors = list()
        successful = False
        # Reusing the original JiraConnection object since the class is a singleton
        jira_connection = JiraConnection()
        remote_issue, remote_issue_status = None, None
        jiav_logger.debug(f"Issue: {issue}")
        jiav_logger.debug(f"Status: {issue_status}")
        try:
            remote_issue = jira_connection.jira.issue(id=issue)
            remote_issue_status = str(remote_issue.get_field("status"))
            if remote_issue_status != issue_status:
                jiav_logger.error(
                    " ".join(
                        [
                            f"Issue '{issue}' status '{remote_issue_status}' does",
                            f"not match the desired status '{issue_status}'",
                        ]
                    )
                )
                errors.append(
                    (
                        f"Issue '{issue}' status '{remote_issue_status}' does",
                        f"not match the desired status '{issue_status}'",
                    )
                )
            else:
                successful = True
                output.append(
                    f"Jira issue '{issue}' is in the desired status '{issue_status}'"
                )
        except Exception as e:
            jiav_logger.error(e.text)  # pyright: ignore # pylint: disable=E1101
            errors.append(e.text)  # pyright: ignore # pylint: disable=E1101
        self.result = result(successful, output, errors)
