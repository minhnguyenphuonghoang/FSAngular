

"""
@Author: Minh.nguyen
@Created Date: March 21, 2015
@Description: All elements on collect name model

@Name: 
@Change Date:
@Changes:

@Name: 
@Change Date:
@Chagnes:  
"""


CollectName = '//div[@id="AskName"]'
CollectName_Title = CollectName + '//h4[@class="modal-title"]'
CollectName_Message = CollectName + '//div[@class="modal-body"]/p'
CollectName_FirstName = CollectName + '//input[@name="first_name"]'
CollectName_LastName = CollectName + '//input[@name="last_name"]'
CollectName_CancelButton = CollectName + '//button[text()="Cancel"]'
CollectName_SaveAndContinueButton = CollectName + '//button[text()="Save & Continue"]'
CollectName_ErrorMessage = CollectName + '//div[@role="alert"]'



