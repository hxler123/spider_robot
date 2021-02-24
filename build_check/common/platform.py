
platforms = {
    "ios": {
        "audio_only": {
            "Premium": "AgoraPremiumAudio_for_iOS.*ipa</A>",
            "Wayang":"WayangAudio_for_iOS.*ipa</A>"
            },
        "default": {
            "Premium": "AgoraPremium_for_iOS.*ipa</A>",
            "Wayang":"Wayang_for_iOS.*ipa</A>"
            },
        "ffmpeg_player": {
            "Premium": "AgoraPremiumFFmpeg_for_iOS.*ipa</A>",
            "Wayang":"WayangFFmpeg_for_iOS.*ipa</A>"
            }
        },
    "android": {
        "audio_only": {
            "Premium": "Agora_premiumAudio_for_Android.*apk</A>",
            "Wayang":"Agora_WayangAudio_for_Android.*apk</A>"
            },
        "default": {
            "Premium": "Agora_premium_for_Android.*apk</A>",
            "Wayang":">Agora_Wayang_for_Android.*apk</A>"
            },
        "ffmpeg_player": {
            "Premium": "Agora_premium_for_Android.*apk</A>",
            "Wayang":"Agora_Wayang_for_Android.*apk</A>"
            }
        },
    "mac": {
        "default": {
            "Premium": "AgoraPremiumMac.*zip</A>",
            "Wayang": "WayangMac.*zip</A>",
            "Agoplay": "Agoplay_for_Mac.*zip</A>"
            },
        "ffmpeg_player": {
            "Premium": "AgoraPremiumMacFFmpeg.*zip</A>",
            "Wayang":"WayangMacFFmpeg.*zip</A>"
            }
        },
    "windows": {
        "audio_only": {
            "Wayang_x64": "Agora_Wayang_for_Windows_x64.*zip</A>",
            "Wayang_x86":"Agora_Wayang_for_Windows_x86.*zip</A>"
            },
        "default": {
            "Wayang_x64": "Agora_Wayang_for_Windows_x64.*zip</A>",
            "Wayang_x86":"Agora_Wayang_for_Windows_x86.*zip</A>",
            "Agoplay_x64": "Agora_Agoplay_for_Windows_x64.*zip</A>",
            "Agoplay_x86": "Agora_Agoplay_for_Windows_x86.*zip</A>",
            "Openlive_x86": "Agora_Openlive_for_Windows_x86.*zip</A>",
            "Openlive_x64": "Agora_Openlive_for_Windows_x64.*zip</A>",
            },
        "ffmpeg_player": {
            "Openlive_x86": "Agora_Openlive_for_Windows_x86.*zip</A>",
            "Openlive_x64": "Agora_Openlive_for_Windows_x64.*zip</A>",
            "Wayang_x64": "Agora_Wayang_for_Windows_x64.*zip</A>",
            "Wayang_x86": "Agora_Wayang_for_Windows_x86.*zip</A>",
            }
        },
}

if __name__ == "__main__":
    for platform in platforms.keys():
        print(platform)
        for branch in platforms[platform].keys():
            print(branch)
            for check_name in platforms[platform][branch].keys():
                print(check_name)
                check_string = platforms[platform][branch][check_name]
                print(check_string)

