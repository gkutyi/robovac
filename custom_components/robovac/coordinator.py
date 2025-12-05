"""Basic coordinator"""
from datetime import timedelta
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
import logging
_LOGGER=logging.getLogger("custom_components.robovac")
class RobovacCoordinator(DataUpdateCoordinator):
    def __init__(self,hass,name,update_interval=60):
        super().__init__(hass,_LOGGER,name=name,update_interval=timedelta(seconds=update_interval))
        self.data={}
    async def _async_update_data(self):
        return self.data
