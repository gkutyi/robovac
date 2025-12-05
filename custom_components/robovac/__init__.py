"""Robovac integration (patched for L60 minimal support)."""
from __future__ import annotations

from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from custom_components.robovac.const import DOMAIN
import logging

_LOGGER = logging.getLogger("custom_components.robovac")

PLATFORMS = ["sensor"]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = entry.data
    for p in PLATFORMS:
        hass.async_create_task(hass.config_entries.async_forward_entry_setup(entry, p))
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    ok = all(await hass.config_entries.async_forward_entry_unload(entry, p) for p in PLATFORMS)
    if ok:
        hass.data[DOMAIN].pop(entry.entry_id)
    return ok
