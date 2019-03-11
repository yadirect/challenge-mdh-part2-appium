
from time import sleep

from appium import webdriver

from appium.webdriver.common.touch_action import TouchAction

desired_caps = {
    "automationName": "Appium",
    "platformName": "Android",
    "deviceName": "Android Emulator",
    "appPackage": "ru.mdh.mtsamarket2memory.android.debug_prod",
    "appActivity": "ru.mdh.mtsamarket2memory.android.init.activity.InitActivity",
    "app": "C:\\Users\\root\\PycharmProjects\\challenge-mdh-part2-appium\\src\\apps\\app398.apk"
}


driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
touch = TouchAction(driver)
driver.implicitly_wait(30)


# ================ Initial activity ================

print('Initial activity\n')

# Tap on "Try by hand" button
driver.find_element_by_id("ru.mdh.mtsamarket2memory.android.debug_prod:id/btnHand").click()


# Enter a Valid Phone Number and tap "Next" button
driver.find_element_by_id("ru.mdh.mtsamarket2memory.android.debug_prod:id/etPhone").send_keys("1110000083")
driver.find_element_by_id("ru.mdh.mtsamarket2memory.android.debug_prod:id/activate_action").click()


# Enter a Valid PIN and tap "Next" button
driver.find_element_by_id("ru.mdh.mtsamarket2memory.android.debug_prod:id/pin_field").send_keys("0000")
driver.find_element_by_id("ru.mdh.mtsamarket2memory.android.debug_prod:id/confirm_pin_action").click()


# Assert "Activated" text
# driver.find_element_by_id("ru.mdh.mtsamarket2memory.android.debug_prod:id/card_tariff_activated")


# Tap "Next" button
driver.find_element_by_id("ru.mdh.mtsamarket2memory.android.debug_prod:id/start_app_btn").click()


# PopUp Window "Allow Photos, Media, and Files on device?" > ALLOW
driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()


# PopUp Window "Allow Access to Contacts?" > DENY
driver.find_element_by_id("com.android.packageinstaller:id/permission_deny_button").click()


# Assert "Main Toolbar"
# driver.find_element_by_id("ru.mdh.mtsamarket2memory.android.debug_prod:id/main_toolbar")


# ================ Start upload Photos ================

print('Uploading Started\n')

# Tap "ADD" button
sleep(2)
# driver.find_element_by_id("ru.mdh.mtsamarket2memory.android.debug_prod:id/fab").click()
touch.tap(x=958, y=1668).perform()

# Tap "Add from gallery" button
sleep(2)
driver.find_element_by_id("ru.mdh.mtsamarket2memory.android.debug_prod:id/ivPickGallery").click()


# Tap "Select all" on Toolbar
sleep(2)
driver.find_element_by_id("ru.mdh.mtsamarket2memory.android.debug_prod:id/menu_select_all").click()


# Tap "ADD" button
sleep(2)
# driver.find_element_by_id("ru.mdh.mtsamarket2memory.android.debug_prod:id/fab").click()
touch.tap(x=958, y=1668).perform()

# Wait for upload ending
sleep(4)
print('Photos Successfully Uploaded\n')


# ================ Prepare assertion that Photos successfully uploaded ================

print('Prepare assertion\n')

# Tap on "Hamburger" menu upper left
sleep(2)
# driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='Открыть навигационное меню']").click()
# driver.find_element_by_accessibility_id("Открыть навигационное меню").click()
touch.tap(x=70, y=140).perform()

# Tap "Files" on icon
sleep(2)
# driver.find_element_by_xpath("(//android.widget.ImageView[@content-desc='Раздел'])[3]").click()
touch.tap(x=80, y=680).perform()

# Tap "Photos" text
sleep(4)
# driver.find_element_by_xpath("//android.widget.TextView[@content-desc='Директория Фото']").click()
# driver.find_element_by_accessibility_id("Директория Фото").click()
touch.tap(x=200, y=720).perform()


# ================ Assert photos filenames by Attribute "text" and Value "filename" ================

print('Assert photos\n')

filename = driver.find_element_by_xpath('//android.widget.TextView[@content-desc="Изображение photo_01.jpg"]').\
    get_attribute("text")
# driver.find_element_by_accessibility_id("Изображение photo_01.jpg")
print(filename)
assert filename == "photo_01.jpg", "The filename doesn't match"


filename = driver.find_element_by_xpath('//android.widget.TextView[@content-desc="Изображение photo_02.jpg"]').\
    get_attribute("text")
# driver.find_element_by_accessibility_id("Изображение photo_02.jpg")
print(filename)
assert filename == "photo_02.jpg", "The filename doesn't match"


filename = driver.find_element_by_xpath('//android.widget.TextView[@content-desc="Изображение photo_03.jpg"]').\
    get_attribute("text")
# driver.find_element_by_accessibility_id("Изображение photo_03.jpg")
print(filename)
assert filename == "photo_03.jpg", "The filename doesn't match"

print('\nPhotos Uploading Successfully Asserted\n')


# ================ Make a Custom Gallery "TAG" and Apply it to the second gallery item ================

print('Make and Apply a Custom gallery \"TAG\"\n')

# Tap on "Hamburger" menu upper left
sleep(2)
touch.tap(x=70, y=140).perform()

# Tap on "Gallery" menu item
sleep(2)
touch.tap(x=88, y=400).perform()

# Tap "Select" on Toolbar
sleep(2)
driver.find_element_by_id("ru.mdh.mtsamarket2memory.android.debug_prod:id/menu_check").click()

# Tap on the second gallery item
sleep(2)
touch.tap(x=540, y=500).perform()

# Tap on the second gallery item
sleep(2)
touch.tap(x=320, y=1720).perform()

# Tap "+" button
sleep(2)
touch.tap(x=1010, y=134).perform()

# Locate "Tag" field, enter text "instagram", tap "Ready" button
sleep(2)
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget."
                             "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget."
                             "FrameLayout/android.widget.EditText").send_keys("instagram")
driver.find_element_by_id("android:id/button1").click()

# Select Tag "instagram" and tap "OK" bottom right
sleep(2)
driver.find_element_by_id("ru.mdh.mtsamarket2memory.android.debug_prod:id/imgCardTagStatus").click()
touch.tap(x=958, y=1668).perform()

# Observe results
sleep(20)


# ================ Clean device after test ================

print('Clean Device\n')

# Close app
driver.close_app()

# Remove app from device
# driver.remove_app('ru.mdh.mtsamarket2memory.android.debug_prod')
# sleep(4)

print('Well Done!')

# sleep(1)

# Close driver session
driver.quit()
