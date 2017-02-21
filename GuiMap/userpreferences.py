

"""
@Author: Minh.nguyen
@Created Date: March 12, 2015
@Description: All elements on user preferences panel

@Name: 
@Change Date:
@Changes:

@Name: 
@Change Date:
@Chagnes:  
"""



UserPreferences = '//div[@id="AppSetting"]'
UserPreferences_SharingDefaults = UserPreferences + '//ul[@role="tablist"]/li/a[text()="Sharing Defaults"]'
UserPreferences_NotificationSettings = UserPreferences + '//ul[@role="tablist"]/li/a[text()="Notification Settings"]'
UserPreferences_LinkedDevices = UserPreferences + '//ul[@role="tablist"]/li/a[text()="Linked Devices"]'
UserPreferences_SharingDefaults_ReShareRadioButton = UserPreferences + '//div[@id="sharing-default"]//input[@value="reshare"]'
UserPreferences_SharingDefaults_ViewOnlyRadioButton = UserPreferences + '//div[@id="sharing-default"]//input[@value="view"]'
UserPreferences_SharingDefaults_AllowPrinting_Enable = UserPreferences + '//div[@id="sharing-default"]/div[2]//i[@class="icon-check"]'
UserPreferences_SharingDefaults_AllowPrinting_Disable = UserPreferences + '//div[@id="sharing-default"]/div[2]//i[@class="icon-cancel"]'
UserPreferences_SharingDefaults_DisplayWatermark_Enable = UserPreferences + '//div[@id="sharing-default"]/div[3]//i[@class="icon-check"]'
UserPreferences_SharingDefaults_DisplayWatermark_Disable = UserPreferences + '//div[@id="sharing-default"]/div[3]//i[@class="icon-cancel"]'






UserPreferences_CancelButton = '//div[@id="AppSetting"]//div[@class="modal-footer"]/button[text()="Cancel"]'
UserPreferences_SaveButton = '//div[@id="AppSetting"]//div[@class="modal-footer"]/button[text()="Save"]'


