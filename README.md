# trunk-recorder-configs
Community Shared Configs for Trunk-Recorder

**When submiting a new PR please make sure to do the following:**
- [ ] Follow the folder structure 
- [ ] Follow the naming schema
- [ ] Update index.md with your added sites


---
## Naming
Name your config like so
> SITE_NAME.SYSTEM_NAME.SITE_ID.Type[P25,Smartnet,dmr,conventional].json

Example:
> Lincoln_Main.NESRS.023.P25.json

---
## Folder structure

We submitting a new PR, please make these folder if the dont exist
- `configs/<state>/<county>/cities`
- `configs/<state>/systems-misc/<System Name>` (Only if state level system)


### State Level System Resources
Put state level resources in `config/<state>/systems-misc/<System Name>`

*ie. talkgroup files*

### State System County Sites & County Systems
Put state system county sites & county systems configs in `config/<state>/<COUNTY>`

### City Only Configs
Put city only configs in `config/<state>/<COUNTY>/cities/<city>`
**DONT PUT CONFIGS THAT SERVICE THE COUNTY HERE**





