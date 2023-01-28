vbox_settings_filepath = r"\VirtualBox\Portable-VirtualBox\data\.VirtualBox\Machines\LinuxLive\LinuxLive.vbox"
vboxwarn_return = 0

def VBox_CloseWarning():
    if ReadSetting("Advanced","skip_vboxwarning") == "Yes":
        return 0

    if VBox_isRunning() and vboxwarn_return != 2:
        vboxwarn_return = MsgBox(49,Translate("Please read"),Translate("VirtualBox is running and should be closed") + "." + "\n" + "=> " + Translate("Close it then click OK") + "." + "\n" + "=> " + Translate("Click cancel to ignore this warning") + ".")
        if vboxwarn_return == 2:
            SendReport("Warning : VirtualBox is running and user has ignored it")
        else:
            SendReport("Warning : VirtualBox is running")

def VBox_isRunning():
    if ProcessExists("VirtualBox.exe"):
        return True
    else:
        return False

def VBox_SetRam(recommended_ram):
    FileReplaceBetween(usb_letter + vbox_settings_filepath,'Memory RAMSize="','"',recommended_ram)

def VBox_SetStorageController(type_of_disk):
    FileReplaceBetween(usb_letter + vbox_settings_filepath,'name="LILI-DISK" type="','"',type_of_disk)
    FileReplaceBetween(usb_letter + vbox_settings_filepath,'name="LILI-DISK" type="' + type_of_disk + '" PortCount="','"',VBox_GetStorageControllerPortCount(type_of_disk))

def VBox_SetOSType(os_type):
    if os_type=="32-bit":
        vbox_os_type="Linux"
    elif os_type=="64-bit":
        vbox_os_type="Linux_64"
    else:
        vbox_os_type=os_type
    FileReplaceBetween(usb_letter + vbox_settings_filepath,'OSType="','"',vbox_os_type)

def VBox_GetStorageControllerPortCount(controller):
    if controller == "PIIX4":
        return 2
    elif controller == "ICH6":
        return 2
    elif controller == "PIIX3":
        return 2
    elif controller == "LsiLogicSas":
        return 8
    elif controller == "AHCI":
        return 16
    else:
    # For LsiLogic / BusLogic / SCSI
        return 16
