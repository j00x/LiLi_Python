def WriteSetting(category, key, value):
    if IniRead(settings_ini, "Advanced", "lili_portable_mode", "no") == "yes" or not RegWrite("HKEY_CURRENT_USER\SOFTWARE\LinuxLive\"&" + category, key, "REG_SZ", value):
        # Portable mode active : writing settings to INI file
        IniWrite(settings_ini, category, key, value)
    else:
        # Writing to both in order to be more portable
        IniWrite(settings_ini, category, key, value)
        RegWrite("HKEY_CURRENT_USER\SOFTWARE\LinuxLive\"&" + category, key, "REG_SZ", value)

def ReadSetting(category, key):
    if IniRead(settings_ini, "Advanced", "lili_portable_mode", "no") == "yes" or (RegRead("HKEY_CURRENT_USER\SOFTWARE\LinuxLive\"&" + category, key) == "" and @error):
        # Portable mode active : writing settings to INI file
        val = IniRead(settings_ini, category, key, "")
    else:
        val = RegRead("HKEY_CURRENT_USER\SOFTWARE\LinuxLive\"&" + category, key)
        IniWrite(settings_ini, category, key, val)
    return StringStripWS(val, 3)
