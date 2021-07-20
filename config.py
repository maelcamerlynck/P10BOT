#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    LUIS_APP_ID = os.environ.get("LuisAppId", "54274c86-3ec4-48f0-9fca-54bd034537dc")
    LUIS_API_KEY = os.environ.get("LuisAPIKey", "7bccf58a81bf4e43bedb92e2272fe87f")
    # LUIS endpoint host name, ie "westus.api.cognitive.microsoft.com"
    LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName", "westus.api.cognitive.microsoft.com")
    APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get("InstrumentationKey", 'e1695f15-df98-4bc0-918a-75dfb8c1aa79')
    
