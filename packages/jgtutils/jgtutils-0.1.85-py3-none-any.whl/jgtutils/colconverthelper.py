from jgtconstants import MFI_SQUAT, MFI_FAKE, MFI_FADE, MFI_GREEN, MFI_SQUAT_STR, MFI_FAKE_STR, MFI_FADE_STR, MFI_GREEN_STR, MFI_SQUAT_ID, MFI_FAKE_ID, MFI_FADE_ID, MFI_GREEN_ID



def mfi_str_to_id(mfi_str:str):
    if mfi_str == MFI_SQUAT_STR:
        return MFI_SQUAT_ID
    elif mfi_str == MFI_FAKE_STR:
        return MFI_FAKE_ID
    elif mfi_str == MFI_FADE_STR:
        return MFI_FADE_ID
    elif mfi_str == MFI_GREEN_STR:
        return MFI_GREEN_ID
    else:
        return 0

def mfi_signal_to_str(mfi_signal:int):
    if mfi_signal == MFI_SQUAT:
        return MFI_SQUAT_STR
    elif mfi_signal == MFI_FAKE:
        return MFI_FAKE_STR
    elif mfi_signal == MFI_FADE:
        return MFI_FADE_STR
    elif mfi_signal == MFI_GREEN:
        return MFI_GREEN_STR
    else:
        return "0"

from jgtconstants import ZONE_INT,ZONE_BUY_STR,ZONE_BUY_ID,ZONE_SELL_STR,ZONE_SELL_ID,ZONE_NEUTRAL_STR,ZONE_NEUTRAL_ID

def zone_str_to_id(zone_str:str):
    if zone_str == ZONE_BUY_STR:
        return ZONE_BUY_ID
    elif zone_str == ZONE_SELL_STR:
        return ZONE_SELL_ID
    elif zone_str == ZONE_NEUTRAL_STR:
        return ZONE_NEUTRAL_ID
    else:
        return ZONE_NEUTRAL_ID

def zone_id_to_str(zone_id:int):
    if zone_id == ZONE_BUY_ID:
        return ZONE_BUY_STR
    elif zone_id == ZONE_SELL_ID:
        return ZONE_SELL_STR
    elif zone_id == ZONE_NEUTRAL_ID:
        return ZONE_NEUTRAL_STR
    else:
        return ZONE_NEUTRAL_STR

