import json
import sys
from random import randint
from time import time

import aiohttp
from WikiRobot import aiohttpsession
from aiohttp import ClientSession

from google_trans_new import google_translator
from Python_ARQ import ARQ
from search_engine_parser import GoogleSearch

from WikiRobot import BOT_ID, OWNER_ID, ARQ_API_URL, ARQ_API_KEY
from WikiRobot import pbot

ARQ_API = "PYHQUD-CYCYBG-GAMOLE-GUSSCA-ARQ"
ARQ_API_KEY = "PYHQUD-CYCYBG-GAMOLE-GUSSCA-ARQ"
SUDOERS = OWNER_ID
ARQ_API_URL = "https://thearq.tech"

# Aiohttp Client
print("[INFO]: INITIALZING AIOHTTP SESSION")
aiohttpsession = ClientSession()
# ARQ Client
print("[INFO]: INITIALIZING ARQ CLIENT")
arq = ARQ(ARQ_API_URL, ARQ_API_KEY, aiohttpsession)

app = pbot
import socket
