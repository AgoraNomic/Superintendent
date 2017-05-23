# Superintendent
Superintendent's report and event log

## super.py
Currently produces a reasonable version of the weekly and monthly report based on events.csv
Still need to work on reporting changes to individual parts of an agency

## events.csv

Handles the following events
- *c* - Change
- *e* - Establish
- *m* - Monthly Report
- *r* - Revoke
- *w* - Weekly Report


Full Events ( c, e ): `DATE,EVENT,HEAD,NAME,ACRONYM,AGENTS,"POWERS"`

Reports ( m, w ): `DATE,EVENT`

Revoking ( r ): `DATE,EVENT,ACTOR,NAME,ACRONYM`


