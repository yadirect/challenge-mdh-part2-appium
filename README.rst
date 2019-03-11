
=======================================

PyCharm and Python
https://www.python.org/downloads/
https://www.jetbrains.com/pycharm/
File > Settings > Project > Interpreter
Appium-Python-Client
or
pip install Appium-Python-Client


=======================================

Android Studio and SDK tools
https://developer.android.com/studio

SDK tools
C:\Users\root\AppData\Local\Android\Sdk\platform-tools

File > Settings > Appearance & Behavior > System Settings > Android SDK > SDK Tools
Android Emulator

AVD Manager > Make: Pixel 2, API 25, 1080x1920: 420dpi, Android 7.1.1 > Run device

View > Tool Windows > Device File Explorer or click the Device File Explorer
/storage/self/primary/DCIM
AVD > Settings > Storage > Virtual SD Card > Format
/sdcard/DCIM
Upload photos somewhere.
Restart device if needed.

Drag an APK file onto the emulator screen.
Make an exploratory testing session.

https://developer.android.com/reference/android/view/KeyEvent


=======================================

CMD / Git-Bash

adb start-server
adb kill-server
adb devices

adb shell "dumpsys window windows | grep -E 'mCurrentFocus'"

mCurrentFocus=Window{9206ce1 u0 ru.mdh.mtsamarket2memory.android.debug_prod/ru.mdh.mtsamarket2memory.android.auth.activity.FirstActivity}
ru.mdh.mtsamarket2memory.android.debug_prod
ru.mdh.mtsamarket2memory.android.auth.activity


=======================================

Appium test automation framework
http://appium.io/

https://github.com/appium/appium-desktop/releases/tag/v1.11.0
Windows 10, version 1803
appium-desktop-setup-1.11.0.exe

Appium Desired Capabilities
http://appium.io/docs/en/writing-running-appium/caps/

Edit configurations
ANDROID_HOME
C:\Users\root\AppData\Local\Android\Sdk

Start Appium server
http://localhost:4723

Start Inspector Session (upper right)

Desired Capabilities > Edit Raw JSON Representation
{
  "automationName": "Appium",
  "platformName": "Android",
  "deviceName": "Android Emulator",
  "appPackage": "ru.mdh.mtsamarket2memory.android.debug_prod",
  "appActivity": "ru.mdh.mtsamarket2memory.android.init.activity.InitActivity",
  "app": "C:\\Users\\root\\PycharmProjects\\challenge-mdh-part2-appium\\src\\apps\\app398.apk"
}

Save As...
Start Session

http://appium.io/docs/en/commands/device/files/push-file/
http://appium.io/docs/en/commands/device/app/close-app/

=======================================
