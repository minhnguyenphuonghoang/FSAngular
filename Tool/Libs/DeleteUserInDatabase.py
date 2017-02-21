from DatabaseLibrary import ConnectionManager, Query



class DeleteUserInDatabase(object):
	"""
	This class can access into database to delete account, change firstname, lastname...
	"""

	db_connection_string = None
	conn = None

	def __init__(self):
		db_source = 'yxgx5mqv7u.database.windows.net'
		db_name = 'FileString_Staging'
		db_username = 'storycloud@yxgx5mqv7u'
		db_password = 'NasdfsdfVDADasd3325673'
		
		self.db_connection_string = '\'' + 'Provider=SQLOLEDB.1;Data Source=' + db_source + ';Initial Catalog=' \
						+ db_name + ';User Id=' + db_username + ';Password=' + db_password + ';' + '\''

		self.conn = ConnectionManager()
	


	def delete_user_in_database(self, username):
		"""
		Delete account in database
		"""

		self._verify_emailaddress(username)

		sql_string = """
		-- create a variable username & userid
		DECLARE @username AS NVARCHAR(255), @userid AS NVARCHAR(255), @tempuserid AS NVARCHAR(255)

		SET @username = '"""+ username +"""'
		SET @userid = (select userid from [user] where username=@username)


		IF (@userid != '') 
			BEGIN
				-- case 01: user just sign up and did not share any files yet
				DELETE FROM WizardUser WHERE UserID = @userid
				DELETE FROM RegisteredDevice WHERE DeviceOwnerID = @userid
				DELETE FROM ServicePreference WHERE UserID = @userid
				DELETE FROM NotificationDeviceToken WHERE DeviceOwnerID = @userid
				DELETE FROM UserEmailAddress WHERE UserID = @userid
				DELETE FROM [User] WHERE UserID = @userid
				
				
				-- case 02: user has share many files or first time recipients
				-- case 02 - a: recipient is a non-user and owner is a user

				-- + find all relation ship between non-user and exist user
				DECLARE @tbl_nonUser as table(FileID nvarchar(255));
				INSERT INTO @tbl_nonUser (FileID) SELECT FileID FROM ShareToEmailAddress WHERE SenderID = @userid or ReceiverEmailAddress = @username


				DECLARE @FileID NVARCHAR (255)
				DECLARE _cursor CURSOR FOR 
					SELECT FileID FROM  @tbl_nonUser
				OPEN _cursor

				FETCH NEXT FROM _cursor into @FileID
				WHILE @@FETCH_STATUS = 0
				BEGIN
					
					SET @tempuserid = (SELECT ownerid FROM [file] where FileID = @FileID)
					-- co 02 cases cho nay:
					-- 1. neu user la owner thi phai delete het tat ca cac files lien quan toi owner + cac quan he share + reshare 2 cap
					-- 2. Neu user ko phai la owner thi chi can delete quan he giua thang user hien tai vs thang cha + con no la dc
					
					IF (@tempuserid = @userid)
						EXEC fsauto_deleteAccountIsOwner @fsauto_FileID = @FileID
					ELSE
						EXEC fsauto_deleteAccountISNotOwner @fsauto_UserName = @username, @fsauto_userid = @userid, @fsauto_fileid = @FileID
				
				FETCH NEXT FROM _cursor into @FileID
				END

				CLOSE _cursor
				DEALLOCATE _cursor


				-- case 02 - b: recipient and owner are users

				-- + find all relation ship between non-user and exist user
				DECLARE @tbl_User as table(FileID nvarchar(255));
				INSERT INTO @tbl_User (FileID) SELECT FileID FROM FileSharing WHERE SenderID = @userid or ReceiverID = @userid


				SET @FileID = ''
				SET @tempuserid = ''
				DECLARE _cursor CURSOR FOR 
					SELECT FileID FROM  @tbl_User
				OPEN _cursor

				FETCH NEXT FROM _cursor into @FileID
				WHILE @@FETCH_STATUS = 0
				BEGIN

					SET @tempuserid = (SELECT ownerid FROM [file] where FileID = @FileID)
					-- co 02 cases cho nay:
					-- 1. neu user la owner thi phai delete het tat ca cac files lien quan toi owner + cac quan he share + reshare 2 cap
					-- 2. Neu user ko phai la owner thi chi can delete quan he giua thang user hien tai vs thang cha + con no la dc
					
					IF (@tempuserid = @userid)
						EXEC fsauto_deleteAccountIsOwner @fsauto_FileID = @FileID
					ELSE
						EXEC fsauto_deleteAccountISNotOwner @fsauto_UserName = @username, @fsauto_userid = @userid, @fsauto_fileid = @FileID
				

				FETCH NEXT FROM _cursor into @FileID
				END

				CLOSE _cursor
				DEALLOCATE _cursor

				-- delete all information in ShareToEmailAddress table
				DELETE FROM FileSharing WHERE SenderID = @userid or ReceiverID = @userid
				DELETE FROM [File] WHERE OwnerID = @userid
			END

		ELSE
			BEGIN

				-- + find all relation ship between non-user and exist user
				DECLARE @tbl_nonUser1 as table(SharingSettingID nvarchar (255));
				INSERT INTO @tbl_nonUser1 (SharingSettingID) SELECT SharingSettingID FROM ShareToEmailAddress WHERE ReceiverEmailAddress = @username


				DECLARE @SharingSettingID1 NVARCHAR(255)
				DECLARE _cursor CURSOR FOR 
					SELECT SharingSettingID FROM  @tbl_nonUser1
				OPEN _cursor

				FETCH NEXT FROM _cursor into @SharingSettingID1
				WHILE @@FETCH_STATUS = 0
				BEGIN
					DELETE FROM SharingSetting WHERE SharingSettingID = @SharingSettingID1
				FETCH NEXT FROM _cursor into @SharingSettingID1
				END

				CLOSE _cursor
				DEALLOCATE _cursor

				-- delete all information in ShareToEmailAddress table
				DELETE FROM ShareToEmailAddress WHERE ReceiverEmailAddress = @username


			END

		"""

		self._execute_sql_string(sql_string)



	def clear_firstname_and_lastname(self, email_address):
		"""This keyword will clear firstname & lastname
		"""
		self._verify_emailaddress(email_address)

		sql_string = "UPDATE [user] SET firstname='', lastname='' WHERE username=\'" + email_address + "\'"
		self._execute_sql_string(sql_string)




	def _verify_emailaddress(self, email_address):
		if email_address=='':
			raise AssertionError("Please input your email address")



	def _execute_sql_string(self, sql_query):

		query = Query()
		try:
			self._connect_to_db()
			query._dbconnection = self.conn._dbconnection
			query.execute_sql_string(sql_query)

		except:
			print "Unexpected error:", sys.exc_info()[0]
		
		finally:
			self._disconnect_db()



	def _connect_to_db(self):
		self.conn.connect_to_database_using_custom_params('adodbapi', self.db_connection_string)

	def _disconnect_db(self):
		self.conn.disconnect_from_database()




