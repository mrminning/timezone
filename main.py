from xml.dom.minidom import parse

# Load calendar file from URL
# Save file to path
# .env file for download URL
# .env file for upload path
# https://stackoverflow.com/questions/68335/how-to-copy-a-file-to-a-remote-server-in-python-using-scp-or-ssh

file_in = open('calendar.vcal', 'r')
file_out = open('calendar_out.vcal', 'w')
count = 0
TZCOLON = "TZID:"
TZEQUALS = "TZID="

def loadTimeZoneData():
    # File from here https://github.com/unicode-org/cldr/blob/main/common/supplemental/windowsZones.xml
    # https://raw.githubusercontent.com/unicode-org/cldr/main/common/supplemental/windowsZones.xml
    timezones = dict()
    with parse("windowsZones.xml") as dom:
        for zone in dom.getElementsByTagName("mapZone"):
            if zone.getAttribute("territory") == "001":
                timezones[zone.getAttribute("other")]= zone.getAttribute("type")
    return timezones

def getTimeZone(line):
    if TZCOLON in line:
        start = line.find(TZCOLON)
        currentTimeZone = line[start + len(TZCOLON):]
        return currentTimeZone
    elif TZEQUALS in line:
        start = line.find(TZEQUALS)
        end = line.find(":", start + len(TZEQUALS))
        currentTimeZone = line[start + len(TZEQUALS):end]
        return currentTimeZone
    else:
        print("Error: Could not process line:")
        return None


timezones = loadTimeZoneData()
print(len(timezones))

while True:
    count += 1

    line = file_in.readline()
    if not line:
        break
    if "TZID" in line:
        timezone = getTimeZone(line.strip())
        iana_timezone = timezones[timezone]
        line = line.replace(timezone, iana_timezone)
    file_out.writelines(line)
file_in.close()
file_out.close()
