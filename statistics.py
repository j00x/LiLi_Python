import urllib.parse

def SendInitialStats():
    lang_code = _Language_for_stats()
    custom_data = "&ul=" + lang_code + "&sr=" + str(DesktopWidth) + "x" + str(DesktopHeight) + "&cd1=" + urllib.parse.quote(OSName()) + "&cd2=" + str(CPUArch) + "&cd3=" + str(OSArch)
    SendReportNoLog("stats-t=appview&cd=Start" + custom_data)

def SendDistribStats(distrib):
    custom_data = "&cd4=" + urllib.parse.quote(distrib)
    SendReportNoLog("stats-t=event&ec=General&ea=create-usb&el=Create%20USB" + custom_data)

def SendCreationSpeedStats(duration):
    custom_data = "&utv=usb-creation-time&utc=General&utt=" + str(duration) + "&utl=USB%20Creation%20Speed"
    SendReportNoLog("stats-t=timing" + custom_data)

def SendAppviewStats(content_description, customdata=""):
    custom_data = "&cd=" + urllib.parse.quote(content_description) + customdata
    SendReportNoLog("stats-t=appview" + custom_data)

def SendEventStats(event_category, event_action, event_label, customdata=""):
    custom_data = "&ec=" + event_category + "&ea=" + event_action + "&el=" + urllib.parse.quote(event_label) + customdata
    SendReportNoLog("stats-t=event" + custom_data)

def SendCloseStats():
    SendReportNoLog("stats-sc=end")

def _Language_for_stats():
    use_source = MUILang if MUILang != "0000" else OSLang
    return HumanOSLang(use_source)

def OSName():
    if OSVersion == "WIN_81":
        return "Windows 8.1"
    elif OSVersion == "WIN_8":
        return "Windows 8"
    elif OSVersion == "WIN_7":
        return "Windows 7"
    elif OSVersion == "WIN_VISTA":
        return "Windows Vista"
    elif OSVersion == "WIN_XP":
        return "Windows XP"
    elif OSVersion == "WIN_XPe":
        return "Windows XP Embedded"
    elif OSVersion == "WIN_2012R2":
        return "Windows Server 2012 R2"
    elif OSVersion == "WIN_2012":
        return "Windows Server 2012"
    elif OSVersion == "WIN_2008":
        return "Windows Server 2008"
    elif OSVersion == "WIN_2008R2":
        return "Windows Server 2008 R2"
    elif OSVersion == "WIN_2003":
        return "Windows Server 2003"
    elif OSVersion == "WIN_2000":
        return "Windows 2000"
    else:
        return "Unknown (" + OSVersion + ")"

def _URIEncode(sData):
aData = [i for i in sData]
nChar = ""
sData=""
for i in range(len(aData)):
nChar = ord(aData[i])
if nChar == 45 or nChar == 46 or (48 <= nChar <= 57) or (65 <= nChar <= 90) or nChar == 95 or (97 <= nChar <= 122) or nChar == 126: sData += aData[i]
elif nChar == 32: sData += "+"
else:
sData += "%" + format(nChar, 'x').upper()
return sData
