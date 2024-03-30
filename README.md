# timezone
Tool (more like a POC really) to translate timezone from Microsoft to IANA (standard timezones) on exported calendars.
This will hopefully make meetings and event show up on the correct time if you follow/subscribe to an Office 365 calendar in Google Calendar.

## Prerequisite
Pull down this data conversion file in the working directory.
```
wget https://raw.githubusercontent.com/unicode-org/cldr/main/common/supplemental/windowsZones.xml
```

## Suggested usage
Get calendar from Office via curl or something. The URL can be found in bottom of the email you get when you share the calendar. Look for "this URL". 

Save the exported calendar to filename calendar.vcal.

```
curl -o calendar.vcal https://office365.url/to/shared/calendar
```

Run program
```
python3 main.py
```

Upload converted file somewhere where you can reach it from Google Calendar of whatever you are using.
