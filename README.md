# trunk-recorder-configs
Example config.json files for Trunk Recorder


## Naming
Name your config like so
> SITE_NAME.SYSTEM_NAME.SITE_ID.Type[P25,Smartnet,dmr,conventional].json

Example:
> Lincoln_Main.NESRS.023.P25.json


## Structure
State/Systems-Misc (For State level Talkgroup files)
State/County/ (For County level configs and Talkgroup files)
State/County/City (For City level configs and Talkgroup files)

**Put City speific configs in the city folders and county level configs in the county folder even if the repeater is in a city**
**Put Talkgroup files for State systems in the state/Systems-Misc/<SYSTEM Name> Folder**
**Put Talkgroup files for Local/Conventional systems in the state/<COUNTY>/ OR state/<COUNTY>/<CITY> Folder**


