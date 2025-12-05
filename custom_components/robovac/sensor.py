"""Battery-only Sensor"""
from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.restore_state import RestoreEntity
import logging
_LOGGER=logging.getLogger("custom_components.robovac")
class RoboBatterySensor(RestoreEntity,SensorEntity):
    _attr_native_unit_of_measurement="%"
    _attr_icon="mdi:battery"
    def __init__(self, coordinator,name,model,entry_id):
        self.coordinator=coordinator
        self._name=f"{name} Battery"
        self._unique_id=f"{entry_id}_battery"
        self._state=None
        self._available=False
    @property
    def name(self): return self._name
    @property
    def unique_id(self): return self._unique_id
    @property
    def native_value(self): return self._state
    async def async_update(self):
        data=self.coordinator.data or {}
        b=None
        if "battery" in data: b=data.get("battery")
        if b is not None:
            try: self._state=int(b); self._available=True
            except: self._state=None; self._available=False
        else:
            self._state=None; self._available=False
