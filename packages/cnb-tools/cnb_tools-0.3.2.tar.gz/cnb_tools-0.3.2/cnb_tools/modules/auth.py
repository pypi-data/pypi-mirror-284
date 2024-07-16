"""General class representing a Synapse entity."""

import synapseclient
from synapseclient.core.exceptions import SynapseNoCredentialsError


# pylint: disable=unsupported-binary-operation
def check_login() -> synapseclient.Synapse | None:
    try:
        return synapseclient.login(silent=True)
    except SynapseNoCredentialsError as err:
        raise SynapseLoginError(
            f"⛔ {err}\n\n"
            "Steps on how to provide your Synapse credentials to "
            "cnb-tools are available here: "
            "https://sage-bionetworks-challenges.github.io/cnb-tools/#requirements"
        ) from err


def whoami() -> str:
    return syn.getUserProfile().userName
