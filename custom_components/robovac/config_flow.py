
"""Robovac Integration – Enhanced Config Flow"""
from __future__ import annotations

import logging
import socket
from typing import Any

from homeassistant import config_entries
from homeassistant.const import CONF_IP_ADDRESS, CONF_NAME
from homeassistant.core import callback
import voluptuous as vol

from .const import (
    DOMAIN,
    CONF_ACCESS_TOKEN,
    CONF_ID,
    CONF_MODEL,
    MODEL_NAMES,
)

_LOGGER = logging.getLogger(__name__)


def _ping_device(ip: str) -> bool:
    """Simple TCP ping to check if the robot is reachable."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1.0)
        result = sock.connect_ex((ip, 6668))  # Tuya default port
        sock.close()
        return result == 0
    except Exception:
        return False


class RobovacFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    """UI config handler for Robovac."""
    VERSION = 1

    async def async_step_user(self, user_input: dict[str, Any] | None = None):
        errors = {}

        if user_input is not None:
            ip = user_input.get(CONF_IP_ADDRESS)
            model = user_input.get(CONF_MODEL)

            # Validate model
            if model not in MODEL_NAMES:
                errors["base"] = "unsupported_model"

            # Ping check
            if not errors:
                alive = await self.hass.async_add_executor_job(_ping_device, ip)
                if not alive:
                    errors["base"] = "cannot_connect"

            if not errors:
                return self.async_create_entry(
                    title=user_input.get(CONF_NAME),
                    data=user_input,
                )

        data_schema = vol.Schema({
            vol.Required(CONF_NAME): str,
            vol.Required(CONF_ID): str,
            vol.Required(CONF_MODEL, default="T2277"): vol.In(MODEL_NAMES),
            vol.Required(CONF_IP_ADDRESS): str,
            vol.Required(CONF_ACCESS_TOKEN): str,
        })

        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
            errors=errors,
        )


@callback
def async_get_options_flow(entry):
    return RobovacOptionsFlow(entry)


class RobovacOptionsFlow(config_entries.OptionsFlow):
    def __init__(self, entry):
        self.entry = entry

    async def async_step_init(self, user_input=None):
        return await self.async_step_user(user_input)

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({}),
        )
