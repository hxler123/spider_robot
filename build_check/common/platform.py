
VERSION = ["2.7.1.2", "2.7.2"]

PLATFORMS = {
    "2.7.1.2": {
        "ios": {
            "audio_only": {
                "Premium": ".*premium.*ipa",
                "Wayang": ".*Wayang.*ipa"
            },
            "default": {
                "Premium": ".*premium.*ipa",
                "Wayang": ".*Wayang.*ipa"
            },
            "ffmpeg_player": {
                "Premium": ".*premium.*ipa",
                "Wayang": ".*Wayang.*ipa"
            }
        },
        "android": {
            "audio_only": {
                "Premium": ".*premium.*apk",
                "Wayang": ".*Wayang.*apk"
            },
            "default": {
                "Premium": ".*premium.*apk",
                "Wayang": ".*Wayang.*apk"
            },
            "ffmpeg_player": {
                "Premium": ".*premium.*apk",
                "Wayang": ".*Wayang.*apk"
            }
        },
        "mac": {
            "default": {
                "Premium": ".*Premium.*zip",
                "Wayang": ".*Wayang.*zip",
                "Agoplay": ".*Agoplay.*zip"
            },
            "ffmpeg_player": {
                "Premium": ".*Premium.*zip",
                "Wayang": ".*Wayang.*zip"
            }
        },
        "windows": {
            "audio_only": {
                "Wayang_x64": ".*Wayang.*x64.*zip",
                "Wayang_x86": ".*Wayang.*x86.*zip"
            },
            "default": {
                "Wayang_x64": ".*Wayang.*x64.*zip",
                "Wayang_x86": ".*Wayang.*x86.*zip",
                "Agoplay_x64": ".*Agoplay.*x64.*zip",
                "Agoplay_x86": ".*Agoplay.*x86.*zip",
                "Openlive_x86": ".*Openlive.*x86.*zip",
                "Openlive_x64": ".*Openlive.*x64.*zip",
            },
            "ffmpeg_player": {
                "Openlive_x86": ".*Openlive.*x86.*zip",
                "Openlive_x64": ".*Openlive.*x64.*zip",
                "Wayang_x64": ".*Wayang.*x64.*zip",
                "Wayang_x86": ".*Wayang.*x86.*zip"
            }
        }
    },
    "2.7.2": {
        "ios": {
            "audio_only": {
                "Premium": ".*premium.*ipa",
                "Wayang": ".*Wayang.*ipa"
            },
            "default": {
                "Premium": ".*premium.*ipa",
                "Wayang": ".*Wayang.*ipa"
            }
        },
        "android": {
            "audio_only": {
                "Premium": ".*premium.*apk",
                "Wayang": ".*Wayang.*apk"
            },
            "default": {
                "Premium": ".*premium.*apk",
                "Wayang": ".*Wayang.*apk"
            }
        },
        "windows": {
            "audio_only": {
                "Wayang_x64": ".*Wayang.*x64.*zip",
                "Wayang_x86": ".*Wayang.*x86.*zip"
            },
            "default": {
                "Wayang_x64": ".*Wayang.*x64.*zip",
                "Wayang_x86": ".*Wayang.*x86.*zip",
                "Openlive_x86": ".*Openlive.*x86.*zip",
                "Openlive_x64": ".*Openlive.*x64.*zip"
            }
        }
    }
}


