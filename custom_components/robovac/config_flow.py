"""Minimal Config Flow"""
from homeassistant import config_entries
from .const import DOMAIN, CONF_NAME, CONF_ID, CONF_MODEL, CONF_IP_ADDRESS, CONF_ACCESS_TOKEN

class RobovacFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION=1
    async def async_step_user(self, user_input=None):
        if user_input:
            return self.async_create_entry(title=user_input.get(CONF_NAME,"Robovac"), data=user_input)
        return self.async_show_form(step_id="user", data_schema=None, errors={})
