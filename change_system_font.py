import _winreg

FONTS_PATH = "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Fonts"
FONTS_SUB_PATH = "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\FontSubstitutes"

def set_reg(reg_path, name, value):
    print "Setting {} to {}".format(name, repr(value))
    _winreg.CreateKey(_winreg.HKEY_LOCAL_MACHINE, reg_path)
    registry_key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, reg_path, 0, 
                                   _winreg.KEY_WRITE)
    _winreg.SetValueEx(registry_key, name, 0, _winreg.REG_SZ, value)
    _winreg.CloseKey(registry_key)

def get_reg(reg_path, name):
    print "Getting {}".format(name)
    registry_key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, reg_path, 0, _winreg.KEY_READ)
    value, regtype = _winreg.QueryValueEx(registry_key, name)
    _winreg.CloseKey(registry_key)
    return value

def restore_segoe():
    print "Restoring Segoe UI..."
    set_reg(reg_path=FONTS_PATH,     name="Segoe UI (TrueType)",             value="segoeui.ttf")
    set_reg(reg_path=FONTS_PATH,     name="Segoe UI Bold (TrueType)",        value="segoeuib.ttf")
    set_reg(reg_path=FONTS_PATH,     name="Segoe UI Bold Italic (TrueType)", value="segoeuiz.ttf")
    set_reg(reg_path=FONTS_PATH,     name="Segoe UI Italic (TrueType)",      value="segoeuii.ttf")
    set_reg(reg_path=FONTS_PATH,     name="Segoe UI Light (TrueType)",       value="segoeuil.ttf")
    set_reg(reg_path=FONTS_PATH,     name="Segoe UI Semibold (TrueType)",    value="seguisb.ttf")
    set_reg(reg_path=FONTS_PATH,     name="Segoe UI Symbol (TrueType)",      value="seguisym.ttf")
    set_reg(reg_path=FONTS_SUB_PATH, name="Segoe UI",                        value="Segoe UI")

def clear_segoe():
    set_reg(reg_path=FONTS_PATH,     name="Segoe UI (TrueType)",             value="")
    set_reg(reg_path=FONTS_PATH,     name="Segoe UI Bold (TrueType)",        value="")
    set_reg(reg_path=FONTS_PATH,     name="Segoe UI Bold Italic (TrueType)", value="")
    set_reg(reg_path=FONTS_PATH,     name="Segoe UI Italic (TrueType)",      value="")
    set_reg(reg_path=FONTS_PATH,     name="Segoe UI Light (TrueType)",       value="")
    set_reg(reg_path=FONTS_PATH,     name="Segoe UI Semibold (TrueType)",    value="")
    set_reg(reg_path=FONTS_PATH,     name="Segoe UI Symbol (TrueType)",      value="")

def change_system_font(font):
    print "Changing system font to {}...".format(font)
    clear_segoe()
    set_reg(reg_path=FONTS_SUB_PATH, name="Segoe UI", value=font)

#change_system_font("SF UI Display")
#change_system_font("SF Display")
#change_system_font("SF Pro Text")
restore_segoe()
print "Log off and log in for changes to take effect."
raw_input()
