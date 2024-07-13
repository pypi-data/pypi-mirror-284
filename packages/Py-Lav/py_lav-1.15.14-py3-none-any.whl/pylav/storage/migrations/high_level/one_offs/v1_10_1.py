from __future__ import annotations

from typing import TYPE_CHECKING

from packaging.version import Version

# noinspection PyProtectedMember
from pylav.constants.node import NODE_DEFAULT_SETTINGS
from pylav.constants.versions import VERSION_0_0_0, VERSION_1_10_1
from pylav.storage.migrations.logging import LOGGER

if TYPE_CHECKING:
    from pylav.core.client import Client


async def migration_v_1_10_1(client: Client, current_version: Version) -> None:
    if current_version >= VERSION_1_10_1 or current_version == VERSION_0_0_0:
        return

    LOGGER.info("Running %s migration", VERSION_1_10_1)
    config = client.node_db_manager.bundled_node_config()
    yaml_data = await config.fetch_yaml()
    yaml_data["spring"] = NODE_DEFAULT_SETTINGS["spring"]
    await config.update_yaml(yaml_data)
    await client.lib_db_manager.update_bot_dv_version(VERSION_1_10_1)
