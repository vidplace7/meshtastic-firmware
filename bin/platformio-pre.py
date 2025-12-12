#!/usr/bin/env python3
# trunk-ignore-all(ruff/F821)
# trunk-ignore-all(flake8/F821): For SConstruct imports
from readprops import readProps
Import("env")
platform = env.PioPlatform()
prefsLoc = env["PROJECT_DIR"] + "/version.properties"
verObj = readProps(prefsLoc)

if platform.name == "native":
    env.Replace(PROGNAME="meshtasticd")
else:
    env.Replace(PROGNAME=f"firmware-{env.get('PIOENV')}-{verObj['long']}")
    print(f"PROGNAME: {env.get('PROGNAME')}")
    if platform.name == "espressif32":
        env.Replace(ESP32_FS_IMAGE_NAME=f"littlefs-{env.get('PIOENV')}-{verObj['long']}")
        print(f"ESP32_FS_IMAGE_NAME: {env.get('ESP32_FS_IMAGE_NAME')}")
    elif platform.name == "raspberrypi":
        env.Replace(PICO_FS_IMAGE_NAME=f"littlefs-{env.get('PIOENV')}-{verObj['long']}")
        print(f"PICO_FS_IMAGE_NAME: {env.get('PICO_FS_IMAGE_NAME')}")
