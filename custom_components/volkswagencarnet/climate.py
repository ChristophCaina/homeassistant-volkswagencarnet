"""Climate support for Volkswagen Connect integration."""

import logging

from homeassistant.components.climate import ClimateEntity, HVACMode, ClimateEntityFeature
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import EntityCategory

from . import VolkswagenEntity
from .const import DATA, DATA_KEY, DOMAIN, UPDATE_CALLBACK

_LOGGER = logging.getLogger(__name__)
