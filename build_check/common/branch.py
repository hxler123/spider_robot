

class ios():
    Premium = ".*premium.*ipa"
    Wayang = ".*wayang.*ipa"

class android():
    Premium = ".*premium.*apk"
    Wayang = ".*wayang.*apk"

class mac():
    Premium = ".*premium.*zip"
    Wayang = ".*wayang.*zip"
    Agoplay = ".*Agoplay.*zip"

class windows():
    Wayang_x64 = ".*Wayang.*x64.*zip"
    Wayang_x86 = ".*Wayang.*x86.*zip"
    Agoplay_x64 = ".*Agoplay.*x64.*zip"
    Agoplay_x86 = ".*Agoplay.*x86.*zip"
    Openlive_x86 = ".*Openlive.*x86.*zip"
    Openlive_x64 = ".*Openlive.*x64.*zip"

branchDict = {
    "3.4.200": {
        "ios": {
            "audio_only": {
                "Premium": ios.Premium,
                "Wayang": ios.Wayang
            },
            "default": {
                "Premium": ios.Premium,
                "Wayang": ios.Wayang
            },
            "ffmpeg_player": {
                "Premium": ios.Premium,
                "Wayang": ios.Wayang
            }
        },
        "android": {
            "audio_only": {
                "Premium": android.Premium,
                "Wayang": android.Wayang
            },
            "default": {
                "Premium": android.Premium,
                "Wayang": android.Wayang
            },
            "ffmpeg_player": {
                "Premium": android.Premium,
                "Wayang": android.Wayang
            }
        },
        "mac": {
            "default": {
                "Premium": mac.Premium,
                "Wayang": mac.Wayang,
                # "Agoplay": mac.Agoplay
            },
            "ffmpeg_player": {
                "Premium": mac.Premium,
                "Wayang": mac.Wayang
            }
        },
        "windows": {
            "audio_only": {
                "Wayang_x64": windows.Wayang_x64,
                "Wayang_x86": windows.Wayang_x86
            },
            "default": {
                "Wayang_x64": windows.Wayang_x64,
                "Wayang_x86": windows.Wayang_x86,
                # "Agoplay_x64": windows.Agoplay_x64,
                # "Agoplay_x86": windows.Agoplay_x86,
                "Openlive_x86": windows.Openlive_x86,
                "Openlive_x64": windows.Openlive_x64,
            },
            "ffmpeg_player": {
                "Openlive_x86": windows.Openlive_x86,
                "Openlive_x64": windows.Openlive_x64,
                "Wayang_x64": windows.Wayang_x64,
                "Wayang_x86": windows.Wayang_x86
            }
        }
    }
}