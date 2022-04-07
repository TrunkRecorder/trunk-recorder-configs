# trunk-recorder-configs
Example config.json files for Trunk Recorder

---
## Folder structure

We submitting a new PR, please make these folder if the dont exist
- `configs/<state>/<county>/cities`
- `configs/<state>/systems-misc/<System Name>` (Only if state level system)


### State level system resources
please put state level resources in `config/<state>/systems-misc/<System Name>`

ie. talkgroup files 

### State System County Sites & County Systems
please put state system county sites & County Systems configs in `config/<state>/<COUNTY>`

### City only configs
please put  City only configs in `config/<state>/<COUNTY>/cities/<city>`
**DONT PUT CONFIGS THAT SERVICE THE COUNTY HERE**

---
## Naming
Name your config like so
> SITE_NAME.SYSTEM_NAME.SITE_ID.Type[P25,Smartnet,dmr,conventional].json

Example:
> Lincoln_Main.NESRS.023.P25.json



