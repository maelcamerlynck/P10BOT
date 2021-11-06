#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "784cc329-cc2e-4e09-8a47-2bfcf783769e")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "H{4gpX0K-3S9tf(j^FnG6]o*7>&")
    LUIS_APP_ID = os.environ.get("LuisAppId", "b18d0106-84f2-409d-9ab8-34931a946bf0")
    LUIS_API_KEY = os.environ.get("LuisAPIKey", "bc9f746c79564223889a7f7b5344ddcd")
    # LUIS endpoint host name, ie "westeurope.api.cognitive.microsoft.com"
    LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName", "westeurope.api.cognitive.microsoft.com")
    APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get("InstrumentationKey", 'c5b691e9-1311-4755-a74a-55c3eb7d2a18')
    
