# **Testings**

## Validation

Pressented underneath are the validation test that have been made for the website. The images should the test that is made on the homepage but there is a link to all the other tests that have been made.

### PEP8

### W3C

#### HTML

#### CSS

### JSHint

### Ligthhouse

## Manuell Testing

### Home page


| **Test Case ID** | **Description**                  | **Steps to Execute**                                                        | **Expected Result**                          | **Actual Result**       | **Status** |
|------------------|----------------------------------|-----------------------------------------------------------------------------|----------------------------------------------|-------------------------|------------|
| HTC01             | Verify homepage loads            | 1. Open browser<br>2. Navigate to homepage                                  | Homepage displays correctly                  | Homepage displays correctly | Passed     |
| HTC02             | Verify gym list displays         | 1. Click on "View all" under "Climbing gyms"                                | List of gyms is displayed                    | List of gyms is displayed | Passed     |
| HTC03             | Verify gym details page          | 1. Click on a gym name<br>2. Check the gym details page                     | Gym details page shows correct information   | Gym details page shows correct information | Passed     |
| HTC04             | Verify signup functionality      | 1. Click "Sign up"<br>2. Enter details<br>3. Submit                         | User account created                         | User account created     | Passed     |
| HTC05             | Verify login functionality       | 1. Click "Log in"<br>2. Enter credentials<br>3. Submit                      | User is logged in                            | User is logged in        | Passed     |
| HTC06             | Verify contact form submission   | 1. Navigate to "Contact"<br>2. Fill in the form<br>3. Submit                | Form submission successful                   | Form submission successful | Passed     |

### Search Climbing gym

| **Test Case ID** | **Description**                      | **Steps to Execute**                                                       | **Expected Result**                               | **Actual Result**       | **Status** |
|------------------|--------------------------------------|----------------------------------------------------------------------------|---------------------------------------------------|-------------------------|------------|
| STC01             | Verify search page loads             | 1. Open browser<br>2. Navigate to search page                              | Search page displays correctly                    | Search page displays correctly | Passed     |
| STC02             | Verify search functionality          | 1. Enter "Stockholm" in search box <br> 2. Click "Search"                    | Gyms in Stockholm are displayed                   | Gyms in Stockholm are displayed | Passed     |
| STC03             | Verify filter by rating              | 1. Click on "Rating" filter                                                | Gyms are sorted by rating                         | Gyms are sorted by rating | Passed     |
| STC04             | Verify filter by A-Z                 | 1. Click on "A-Z" filter                                                   | Gyms are sorted alphabetically (A-Z)              | Gyms are sorted alphabetically (A-Z) | Passed     |
| STC05             | Verify filter by Z-A                 | 1. Click on "Z-A" filter                                                   | Gyms are sorted alphabetically (Z-A)              | Gyms are sorted alphabetically (Z-A) | Passed     |
| STC06             | Verify gym details link              | 1. Click on a gym name                                                     | Gym details page is displayed                     | Gym details page is displayed | Passed     |

### Climbing gym detail

| **Test Case ID** | **Description**                      | **Steps to Execute**                                                       | **Expected Result**                               | **Actual Result**       | **Status** |
|------------------|--------------------------------------|----------------------------------------------------------------------------|---------------------------------------------------|-------------------------|------------|
| CTC01             | Verify Karbin Klätterhall page loads | 1. Open browser<br>2. Navigate to Karbin Klätterhall page                  | Page displays correctly                           | Page displays correctly | Passed     |
| CTC02             | Verify gym name displays             | 1. Open Karbin Klätterhall page                                            | Gym name "Karbin Klätterhall" is displayed        | Gym name is displayed | Passed     |
| CTC03             | Verify gym address displays          | 1. Open Karbin Klätterhall page                                            | Address "Stockholm" is displayed                  | Address is displayed | Passed     |
| CTC04             | Verify gym description displays      | 1. Open Karbin Klätterhall page                                            | Gym description is displayed                      | Gym description is displayed | Passed     |
| CTC05             | Verify contact information           | 1. Open Karbin Klätterhall page                                            | Contact information is displayed                  | Contact information is displayed | Passed     |
| CTC06             | Verify socialmedia linke           | 1. Open Karbin Klätterhall page<br>2.Click on socialmedia link                                            | SocialMedia site Opens in new tap                  | SocialMedia site Opens in new tap | Passed     |
| CTC07             | Verify reviews section               | 1. Open Karbin Klätterhall page<br>2. Scroll to reviews section            | Reviews are displayed                             | Reviews are displayed | Passed     |
| CTC08             | Verify review submission             | 1. Open Karbin Klätterhall page<br>2. Submit a review                      | Review is submitted and displayed                 | Review is submitted and displayed | Passed     |
| CTC09             | Verify image gallery displays        | 1. Open Karbin Klätterhall page<br>2. View image gallery                   | Image gallery is displayed                        | Image gallery is displayed | Passed     |

### Profile 

### Test Cases

| **Test Case ID** | **Description**                      | **Steps to Execute**                                                       | **Expected Result**                               | **Actual Result**       | **Status** |
|------------------|--------------------------------------|----------------------------------------------------------------------------|---------------------------------------------------|-------------------------|------------|
| PTC01             | Verify User Profile page loads       | 1. Open browser<br>2. Navigate to User Profile page                        | User Profile page displays correctly              | User Profile page displays correctly | Passed     |
| PTC02             | Verify user information displays     | 1. Open User Profile page                                                  | User information (name, email, etc.) is displayed | User information is displayed | Passed     |
| PTC03             | Verify user can edit profile         | 1. Open User Profile page<br>2. Click "Edit Profile"<br>3. Make changes<br>4. Submit | User information is updated                      | User information is updated | Passed     |
| PTC04             | Verify profile picture upload        | 1. Open User Profile page<br>2. Click "Edit Profile"<br>3. Upload new picture<br>4. Submit | Profile picture is updated                       | Profile picture is updated | Passed     |
| PTC05             | Verify changes persist after refresh | 1. Open User Profile page<br>2. Edit profile<br>3. Submit<br>4. Refresh page | Updated information is still displayed           | Updated information is still displayed | Passed     |
| PTC06             | Verify form validation               | 1. Open User Profile page<br>2. Click "Edit Profile"<br>3. Enter invalid data (e.g., invalid email)<br>4. Submit | Validation errors are displayed                   | Validation errors are displayed | Passed     |
| PTC07             | Verify cancel button functionality   | 1. Open User Profile page<br>2. Click "Edit Profile"<br>3. Make changes<br>4. Click cancel | Changes are not saved, user is redirected         | Changes are not saved, user is redirected | Passed     |
| PTC08             | Verify user activity logs display    | 1. Open User Profile page<br>2. Scroll to activity logs                    | User activity logs are displayed                  | User activity logs are displayed | Passed     |
| PTC09             | Verify navigation to other pages     | 1. Open User Profile page<br>2. Click on links to other sections (e.g., "My Gyms") | User is navigated to the respective section      | User is navigated to the respective section | Passed     |

## Edit Views

#### Reviews/Comments

| **Test Case ID** | **Description**                      | **Steps to Execute**                                                       | **Expected Result**                               | **Actual Result**       | **Status** |
|------------------|--------------------------------------|----------------------------------------------------------------------------|---------------------------------------------------|-------------------------|------------|
| RETC01             | Verify Edit Comment page loads       | 1. Open browser<br>2. Navigate to Edit Comment page                        | Edit Comment page displays correctly              | Edit Comment page displays correctly | Passed     |
| TC02             | Verify existing comment displays     | 1. Open Edit Comment page                                                  | Existing comment text is displayed                | Existing comment text is displayed | Passed     |
| RETC03             | Verify comment text can be edited    | 1. Open Edit Comment page<br>2. Edit comment text<br>3. Submit             | Comment text is updated                           | Comment text is updated | Passed     |
| RETC04             | Verify comment update persists       | 1. Open Edit Comment page<br>2. Edit comment text<br>3. Submit<br>4. Refresh page | Updated comment text is still displayed         | Updated comment text is still displayed | Passed     |
| RETC05             | Verify form validation               | 1. Open Edit Comment page<br>2. Enter invalid data (e.g., empty comment)<br>3. Submit | Validation errors are displayed                   | Validation errors are displayed | Passed     |
| RETC06             | Verify cancel button functionality   | 1. Open Edit Comment page<br>2. Make edits<br>3. Click cancel              | Changes are not saved, user is redirected         | Changes are not saved, user is redirected | Passed     |

#### Climbing Gyms

| **Test Case ID** | **Description**                      | **Steps to Execute**                                                       | **Expected Result**                               | **Actual Result**       | **Status** |
|------------------|--------------------------------------|----------------------------------------------------------------------------|---------------------------------------------------|-------------------------|------------|
| ECTC01             | Verify Edit Gym page loads           | 1. Open browser<br>2. Navigate to Edit Gym page                            | Edit Gym page displays correctly                  | Edit Gym page displays correctly | Passed     |
| ECTC02             | Verify gym name can be edited        | 1. Open Edit Gym page<br>2. Edit gym name<br>3. Submit                     | Gym name is updated                               | Gym name is updated | Passed     |
| ECTC03             | Verify gym address can be edited     | 1. Open Edit Gym page<br>2. Edit gym address<br>3. Submit                  | Gym address is updated                            | Gym address is updated | Passed     |
| ECTC04             | Verify gym description can be edited | 1. Open Edit Gym page<br>2. Edit gym description<br>3. Submit              | Gym description is updated                        | Gym description is updated | Passed     |
| ECTC05             | Verify Map-location can be edited | 1. Open Edit Gym page<br>2. Edit Map location<br>3. Submit         | Map location is updated                    |  is updated | Passed     |
| ECTC06             | Socialmedia link can be edited   | 1. Open Edit Gym page<br>2. Edit Socialmedia link<br>3. Submit                | Socialmedia link are updated                         | Socialmedia link are updated | Passed     |
| ETC07             | Verify image upload functionality    | 1. Open Edit Gym page<br>2. Upload a new image<br>3. Submit                | Image is uploaded and displayed                   | Image is uploaded and displayed | Passed     |
| ECTC08             | Verify changes are saved             | 1. Open Edit Gym page<br>2. Make multiple edits<br>3. Submit               | All changes are saved                             | All changes are saved | Passed     |
| ECTC09             | Verify form validation               | 1. Open Edit Gym page<br>2. Enter invalid data<br>3. Submit                | Validation errors are displayed                   | Validation errors are displayed | Passed     |
| ECTC10             | Verify cancel button functionality   | 1. Open Edit Gym page<br>2. Make edits<br>3. Click cancel                  | Changes are not saved, user is redirected         | Changes are not saved, user is redirected | Passed     |

## Delete Views


| **Test Case ID** | **Description**                      | **Steps to Execute**                                                       | **Expected Result**                               | **Actual Result**       | **Status** |
|------------------|--------------------------------------|----------------------------------------------------------------------------|---------------------------------------------------|-------------------------|------------|
| DTC01             | Verify Delete Confirmation page loads| 1. Open browser<br>2. Navigate to Delete Confirmation page                 | Delete Confirmation page displays correctly       | Delete Confirmation page displays correctly | Passed     |
| DTC02             | Verify user information displays     | 1. Open Delete Confirmation page                                           | User information (name, email, etc.) is displayed | User information is displayed | Passed     |
| DTC02             | Verify delete action                 | 1. Open Delete Confirmation page<br>2. Click "Delete"                      | User profile is deleted                           | User profile is deleted | Passed     |
| DTC03             | Verify cancel button functionality   | 1. Open Delete Confirmation page<br>2. Click "Cancel"                      | User is redirected back to the profile page       | User is redirected back to the profile page | Passed     |
| DTC04             | Verify post-delete redirection       | 1. Open Delete Confirmation page<br>2. Click "Delete"                      | User is redirected to the homepage after deletion | User is redirected to the homepage | Passed     |
| DTC05             | Verify deletion persistence          | 1. Open Delete Confirmation page<br>2. Click "Delete"<br>3. Try to log in with deleted account | Login should fail                                 | Login fails as expected | Passed     |
| DTC06             | Verify deletion persistence          | 1. Open Delete Confirmation page<br>2. Click "Delete"<br>3. Try to find the deleted object | The object can not be found                                 | The object can not be found | Passed     |


## Bugs

### Fixed buges

- Could not find the form to edit the profile
    - spelling error from insted of form
- Multipul time when creating a new veiws the template could not be found
    - spelling error, miss places - or _ 

- Error 500 when submiting All View 
    - 

### Ofixed buges
