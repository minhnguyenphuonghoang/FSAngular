from navigation import *
from userpreferences import *
from reshare import *
from viewrecipients import *
from toolbar import *
from collectname import *
from fileviewer import *
from common_message import *
from usersettings import *

#Common element
Msg_Error = '//div[@class = "alert alert-danger fade in"]'
Msg_Success = '//div[@class = "alert alert-success fade in"]'
Btn_LogOut = '//*[@id="logout"]'
Btn_StringFile = '//*[@id="openStringFile"]'
CbBx_ReShare = '//label[text()[contains(.,"Re-Share")]]'
CbBx_ViewOnly = '//label[text()[contains(.,"View")]]'
CbBx_ViewSpaceOnly='//label[text()[contains(.,"View Only")]]'
Screen_Loading = ''
AllFile_Btn_Info = '//a[@id="tab-panel-btn"]'
AllFile_Btn_Filter = ''
Btn_AllFile = '//li[@id="allFile"]/a'
Btn_People = '//li[@id="peopleView"]/a'
ProgressBar = '//div[@id="nprogress"]'
Btn_UserSettings = '//a[@id="user-settings"]'
Btn_UserPreferences = '//*[@id="settings-preferences"]/a'
Btn_AccountMenu = '//*[@id="toggle-account-menu"]'

#New UI
Btn_Settings = '//*[@id="switch-view"]/li[contains(.//text(),"Settings")]' #new UI
Btn_SettingsInfo = '//*[@id="settings-info"]' #new UI
Btn_SettingsPreferences = '//*[@id="settings-preferences"]' #new UI
Btn_MyFilesLibrary = '//*[@id="switch-view"]/li[contains(.//text(),"My Files Library")]'


#Signin Screen
Signin_Txt_Username = '//input[@placeholder = "Email Address"]'
Signin_Txt_Password = '//input[@placeholder="Password"]'
Signin_Btn_Login = '//input[@value = "Sign In"]'
Signin_Link_SignUp = '//a[text() = "Sign up now"]'
Signin_Link_ResetPassword = '//a[text() = "Forgot Your Password?"]'

#Signup Screen
Signup_Txt_FirstName =  '//input[@placeholder = "First Name"]'
Signup_Txt_LastName =  '//input[@placeholder = "Last Name"]'
Signup_Txt_Email = '//input[@placeholder = "Your Email Address"]'
Signup_Txt_Password = '//input[@placeholder = "Create a Password"]'
Signup_Btn_Signup = '//button[text() = "Sign Up Free"]'
Signup_Link_Login  = '//a[text() = "Login!"]'

#String File Modal
StringFile_Mdl = '//div[@id="StringFile"]'
StringFile_Txt_Recipients = '//input[@placeholder="Enter names or email addresses (separated by commas)"]'
StringFile_Txt_FilePath = '//input[@id="selectFile"]'
StringFile_Txt_Expiration = '//div[@id="stringExpiration"]/input'
StringFile_ChkBx_Printing = '//*[@id="StringFile"]//div[contains(./label,"Allow Printing")]//input'
StringFile_ChkBx_Watermark = '//*[@id="StringFile"]//div[contains(./label,"Display Watermark")]//input'
StringFile_Btn_String = '//div[@id="StringFile"]//button[contains(., "String") and not(@disabled)]'
StringFile_Btn_Cancel = '//div[@id="StringFile"]//button[contains(.,"Cancel")]'
StringFile_Btn_Stringing = '//div[@id="StringFile"]//button[contains(., "Stringing")]'
StringFile_Btn_Success = '//div[@id="StringFile"]//button[contains(@class, "state-success")]'
StringFile_ProgressBar_Success = ''
StringFile_ProgressBar_Error = ''
StringFile_TxtAr_Note = '//*[@id="StringFile"]/div/div/div[2]/textarea'
StringFile_PrgBar_Upload_Done = '//*[@id="fileAPI"]//span[contains(@class,"upload-progress")]/span[@style="width: 100%;"]'
StringFile_Btn_Close = '//*[@id="StringFile"]//button[contains(.,"Close")]'

#Change Right Modal
ChangeRight_Mdl = '//div[@id="EditRecipient"]'


#Tab panel File Info
FileInfo_Tab_Details = '//*[@id="tab-panel"]//a[text()="Details"]'
FileInfo_Tab_Recipients = '//*[@id="tab-panel"]//a[contains(text(),"Recipient")]'
FileInfo_Recipient = '//*[@class="tab-panel expand"]//a[@href = "#recipients"]'
FileInfo_Panel = '//*[@class="tab-panel expand"]'
FileInfo_SprinnerLoading = '//div[@class = "spinner spinner-icon hidden"]'


#Viewer
Viewer_Btn_Close = ''

#Toolbar
Toolbar = ''

"""
@Author: Linh.nguyen
@Date Created: March 12, 2015
@Description: 
"""
#Reset Password Screen
ResetPassword_Screen = '//div[@class="login-form"]'
ResetPassword_EdtPassword = '//input[@placeholder="New Password"]'
ResetPassword_EdtConfirmPassword = '//input[@placeholder="Confirm Password"]'
ResetPassword_BtnReset = '//button[text() = "Reset"]'
ResetPassword_BtnBackToSignIn = '//a[contains(., "Back to Sign In")]'


#Forgot Password
ForgotPassword_EdtEmail = '//input[@placeholder="Your Email Address" and not(@tabindex)]'
ForgotPassword_BtnRequestResetLink = '//button[text() = "Request Reset Link"]'
ForgotPassword_TxtBackToSignIn = '//strong[text() = "Back to Sign In"]'
ForgotPassword_EdtEmailError = '//input[@class = "form-control email danger"]'

#All Files
AllFiles_Details = '//a[@id="tab-panel-btn"]'
AllFiles_FileStringReceivedFiles = '//a[@title = "FileString Received Files"]'
AllFile_FileInfo = '//*[@class="tab-panel expand"]'

DynamicPath_FileInfo_RecipientName = '//p[text()="recipientname"]'
#Select Revoke or Change right
DynamicPath_FileInfo_RevokeAccess = '//p[text()="recipientname"]/../..//a[@class="icon-revoke"]'
DynamicPath_FileInfo_ChangeRights = '//p[text()="recipientname"]/../..//a[@class="icon-pencil"]'
DynamicPath_FileInfo_IconCheck = '//p[text()="recipientname"]/../..//a[@class="icon-check"]'
DynamicPath_FileInfo_IconCancel = '//p[text()="recipientname"]/../..//a[@class="icon-cancel"]'
DynamicPath_FileInfo_InactiveRecipient = '//li[@class="inactive"]//p[text()="recipientname"]'
FileInfo_CheckDeleteRecipient = '//li[@class="delete"]//a[@class="icon-check"]'

#List recipient when view Recipient from right click on file
RecipientScreenWhenRightClickOnFileAndViewRecipient = '//div[@class="modal fade recipients in" and @style = "display: block;" ]'
MenuWhenRightClickOnRecipient_RestoreAccess = '//*[@id="recipient-context-menu"]//a[@class="icon-restore"]'
MenuWhenRightClickOnRecipient_TrackFileViews = '//*[@id="recipient-context-menu"]//a[@class="icon-chart"]'

#Restore Access Screen
RestoreAccess_Mdl = '//div[@id="RestoreAccess"]'
RestoreAccess_Screen = '//div[@id="RestoreAccess" and @style = "display: block;" ]'
RestoreAccess_Btn_Restore = '//button[text()="Restore"]'
RestoreAccess_Close = '//div[@id = "RestoreAccess"]//button[@class="btn btn-default btn-wide" and text() = "Close"]'
RestoreAccess_ViewOnly_Check = '//div[@id="RestoreAccess"]//div[@class="modal-body" ]//label[contains(@class, "checked") and text()[contains(.,"View-Only")]]'
RestoreAccess_ReShare_Check = '//div[@id="RestoreAccess"]//div[@class="modal-body" ]//label[contains(@class, "checked") and text()[contains(.,"Re-Share")]]'
RestoreAccess_AllowPrinting_On = '//div[@id="RestoreAccess"]//div[./label[contains(text(),"Allow Printing")]]//div[contains(@class, "switch-on")]'
RestoreAccess_AllowPrinting_ChkBx='//*[@id="RestoreAccess"]//div[contains(./label,"Allow Printing")]//input'
RestoreAccess_DisplayWatermark_ChkBx='//*[@id="RestoreAccess"]//div[contains(./label,"Display Watermark")]//input'
RestoreAccess_DisplayWatermark_On = '//div[@id="RestoreAccess"]//div[./label[contains(text(),"Display Watermark")]]//div[contains(@class, "switch-on")]'
#'//div[@id = "RestoreAccess"]//div[@class ="modal-header"]//span[text() = "Close"]'
#Revoke Access
Warning_RevokeAccess = '//div[@id="RevokeWarning" and @style = "display: block;" ]'
RevokeAccess_Btn_Revoke= '//div[@id = "RevokeWarning"]//button[text() ="Revoke"]'
RevokeAccess_Btn_Close = '//div[@id = "RevokeWarning"]//button[text() ="Close"]'

#User Settings Modal
Account_Menu='//*[@id="toggle-account-menu"]'
Account_Menu_Form='//*[@id="account-menu"]/div'
User_Setting='//*[@id="switch-view"]/li[1]/a'
User_Info='//*[@id="settings-info"]'
UserSettings_Mdl = '//div[@id="AccountSetting"]'
UserSettings_Txt_PrimaryEmail = '//div[@id="AccountSetting"]//div[contains(./label, "Primary Email")]/input'
UserSettings_Btn_Close = '//div[@id="AccountSetting"]//button[contains(./text(), "Close")]'
First_Name = '//*[@id="FirstName"]'
Last_Name = '//*[@id="LastName"]'
SaveBtn = '//*[@id="saveBasicInfo"]'
Secondary_Email= '//*[@id="addSecondEmail"]'
CloseBtn = '//*[@id="AccountSetting"]/div/div/div[1]/button/span[1]'
Change_Password = '//div[@id="AccountSetting"]/div/div/div[5]/a'
ChangePass_Form = '//*[@id="password"]'
Current_Password = '//*[@id="password"]/input[1]'
New_Password = '//*[@id="password"]/input[2]'
Confirm_Password = '//*[@id="password"]/input[3]'
SavePassBtn ='//*[@id="password"]/button'
Add_Secondary_Email_Btn= '//div[@id="AccountSetting"]/div/div/div[6]/div[1]/span/span/span'
Add_Secondary_Email_Form = '//*[@id="MessageBox"]/div/div'
Add_Secondary_Email_Message = '//*[@id="MessageBox"]/div/div/div[1]/p'
Add_Secondary_Email_OKBtn = '//*[@id="MessageBox"]/div/div/div[2]/button'
Add_Secondary_Email_Label = '//div[@id="AccountSetting"]/div/div/div[6]/div[3]/label'
#Add_Secondary_Email_Label = '//*[@id="account-menu"]/div/span[2]/strong/strong'
Add_Secondary_Email_Remove_Email_Btn = '//div[@id="AccountSetting"]/div/div/div[6]/div[3]/button[2]'
Add_Secondary_Email_Send_Verification_Email_Btn ='//div[@id="AccountSetting"]/div/div/div[6]/div[3]/button[1]'
Add_Duplicate_2nd_Email_Message = '//*[@id="MessageBox"]/div/div/div[1]/p'
Edit_First_Name_And_Last_Name_Form = '//div[@id="AccountSetting"]/div/div/div[3]/div'
Edit_First_Name_And_Last_Name_Msg='//*[@id="AccountSetting"]/div/div/div/div[2]/div/text()'
Verify_Email_Msg='/html/body/div/div[1]'
Personal_Tab ='//*[@id="settings-info"]/a'

#User Preperences

User_Preference_Link = '//*[@id="settings-preferences"]/a'
User_Preference_Form ='user-preferences'
User_Pre_Cancel_Btn ='//*[@id="AppSetting"]/div/div/div[3]/button[1]'
User_Pre_Allow_Printing_CheckBox ='//*[@id="sharing-default"]/div[2]/div/div/input'
User_Pre_Display_Watermark_CheckBox = '//*[@id="sharing-default"]/div[3]/div/div/input'
User_Pre_Reshare_RadioBtn ='//*[@id="sharing-default"]/div[1]/label[3]/input'
User_Pre_View_Only_RadioBtn = '//*[@id="sharing-default"]/div[1]/label[2]/input'
User_Pre_Save_Btn = '//*[@id="AppSetting"]/div/div/div[3]/button[2]'



#User Preferences Modal
UserPreferences_Mdl = '//div[@id="AppSetting"]'
UserPreferences_ChkBx_Printing = '//*[@id="AppSetting"]//div[contains(./label,"Allow Printing")]//input'
UserPreferences_ChkBx_Watermark = '//*[@id="AppSetting"]//div[contains(./label,"Display Watermark")]//input'
UserPreferences_Tab_SharingDefault = '//*[@id="sharing-default"]'
UserPreferences_Btn_Cancel = '//*[@id="AppSetting"]//button[contains(.,"Cancel")]'


MenuWhenRightClickOnAFile = '//div[@id="context-menu"]'
MenuWhenRightClickOnAFile_Open = '//div[@id="context-menu"]//a[@class="icon-view"]'
MenuWhenRightClickOnAFile_String = '//div[@id="context-menu"]//a[@class="icon-add-user"]'
MenuWhenRightClickOnAFile_ViewRecipients = '//div[@id="context-menu"]//a[@class="icon-users"]'
MenuWhenRightClickOnAFile_TrackFileViews = '//div[@id="context-menu"]//a[@class="icon-chart"]'
MenuWhenRightClickOnAFile_RevokeAccess = '//div[@id="context-menu"]//a[@class="icon-revoke"]'
MenuWhenRightClickOnAFile_Delete = '//div[@id="context-menu"]//a[@class="icon-trash"]'
MenuWhenRightClickOnAFile_PushFileUpdate = '//div[@id="context-menu"]//a[@class="icon-push-update"]'
MenuWhenRightClickOnAFile_Restore = '//div[@id="context-menu"]//a[@class="icon-restore"]'
MenuWhenRightClickOnAFile_ReShare = '//div[@id="context-menu"]//a[@class="icon-reshare"]'


RevokeAccess = '//div[@id="PeopleRevoke"]'
RevokeAccess_CancelButton = RevokeAccess + '//button[text()="Cancel"]'
RevokeAccess_RevokeButton = RevokeAccess + '//button[text()="Revoke"]'


MenuWhenRightClickOnARecipient = '//div[@id="recipient-context-menu"]'
MenuWhenRightClickOnARecipient_TrackFileViews = MenuWhenRightClickOnARecipient + '//a[@class="icon-chart"]'
MenuWhenRightClickOnARecipient_ChangeRights = MenuWhenRightClickOnARecipient + '//a[@class="icon-pencil"]'
MenuWhenRightClickOnARecipient_Restore = MenuWhenRightClickOnARecipient + '//a[@class="icon-restore"]'
MenuWhenRightClickOnARecipient_Revoke = MenuWhenRightClickOnARecipient + '//a[@class="icon-revoke"]'

#Change Rights
ChangeRight_Screen = '//div[@id="EditRecipient"]'
ChangeRight_ViewOnly_Check = '//div[@id="EditRecipient"]//div[@class="modal-body" ]//label[contains(@class, "checked") and text()[contains(.,"View Only")]]'
ChangeRight_ReShare_Check = '//div[@id="EditRecipient"]//div[@class="modal-body" ]//label[contains(@class, "checked") and text()[contains(.,"Re-Share")]]'
ChangeRight_AllowPrinting_On = '//div[@id="EditRecipient"]//div[./label[contains(text(),"Allow Printing")]]//div[contains(@class, "switch-on")]'
ChangeRight_AllowPrinting_ChkBx='//*[@id="EditRecipient"]//div[contains(./label,"Allow Printing")]//input'
ChangeRight_DisplayWatermark_ChkBx='//*[@id="EditRecipient"]//div[contains(./label,"Display Watermark")]//input'
ChangeRight_DisplayWatermark_On = '//div[@id="EditRecipient"]//div[./label[contains(text(),"Display Watermark")]]//div[contains(@class, "switch-on")]'
ChangeRight_Save_Button = '//button[text()="Save"]'


RevokeMessage_CloseButton = '//div[@id="PeopleRevoke"]//button[text()="Close"]'

#Ask Name
AskName_Mdl = '//*[@id="AskName"]'
AskName_Txt_FirstName = AskName_Mdl + '//input[@placeholder = "First Name"]'
AskName_Txt_LastName = AskName_Mdl + '//input[@placeholder = "Last Name"]'
AskName_Btn_Cancel = AskName_Mdl + '//button[text()="Cancel"]'
AskName_Btn_Save = AskName_Mdl + '//button[text()="Save & Continue"]'

#Personal Info
PersonalInfo_Txt_Add2ndEmail = '//*[@id="addSecondEmail"]'
PersonalInfo_Btn_Add2ndEmail = '//*[@id="AccountSetting"]/div/div/div[6]/div[1]/span/span/span'

#Delete warnming
Warning_DeleteFile = '//div[@id="DeleteWarning" and @style = "display: block;"]'
DelWarning_Btn_Delete = '//*[@id="DeleteWarning"]//button[contains(., "Delete")]'
Warning_BtnDelete = '//div[@id="DeleteWarning"]//button[text() = "Delete"]'

#Cancel string file warning
Warning_Btn_Yes = '//*[@id="WarningBox"]//button[contains(.,"Yes")]'
Warning_Btn_No = '//*[@id="WarningBox"]//button[contains(.,"No")]'

# Revoke warning
RevokeWarning_Mdl = '//*[@id="RevokeWarning"]'
RevokeWarning_Btn_Revoke = RevokeWarning_Mdl + '//button[contains(., "Revoke")]'
RevokeWarning_Btn_Close = RevokeWarning_Mdl + '//button[contains(., "Close")]'

#Message box
MessageBox_Mdl = '//*[@id="MessageBox"]'
MessageBox_Btn_Ok = MessageBox_Mdl + '//button[contains(., "OK")]'
