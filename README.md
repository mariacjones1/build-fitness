# Build Fitness workout planner
Build Fitness workout planner is a website that allows users to browse workouts. Users can either browse all workouts, browse by category or search for a specific workout, and authenticated users can browse by workouts they have either saved or completed. Authorised users can create new workouts, or edit or delete existing ones.

Final website: [https://build-fitness-66f794a76bbb.herokuapp.com/](https://build-fitness-66f794a76bbb.herokuapp.com/)

![Responsive mock-up](/documentation/screenshots/responsive_mock_up.png)

<hr>

## Table of contents

- [Design and planning](#design-and-planning)
    - [Site owner goals](#site-owner-goals)
    - [User stories](#user-stories)
    - [Flowcharts](#flowcharts)
    - [Models diagram](#models-diagram)
    - [Wireframes](#wireframes)
- [Features](#features)
    - [Responsive layouts](#responsive-layouts)
    - [Favicon and title](#favicon-and-title)
    - [Navigation](#navigation)
    - [Create, edit and delete workouts](#create-edit-and-delete-workouts)
    - [Custom 403 and 404 pages](#custom-403-and-404-pages)
- [Technology](#technology)
    - [Languages used](#languages-used)
    - [Frameworks, libraries and programs used](#frameworks-libraries-and-programs-used)
- [Testing](#testing)
    - [Testing user stories](#testing-user-stories)
    - [Automated testing](#automated-testing)
    - [Validator testing](#validator-testing)
- [Credits](#credits)

## Design and planning

### Site owner goals

As the site owner, I want to provide a resource for users to find new workouts to try, and to have the option to save workouts, mark them as complete or leave comments. The website should be easy to navigate, with multiple options for users to find what they are looking for. It should be easy to register for an account, which will gain the user additional functionality to enhance their experience.
Admin users should be able to create, edit and delete workouts without difficulty, but non-admin users should not be able to access this functionality.
The site should be responsive and easy to use on any common device.
The end goal is to gain as much user traffic as possible, and have many people regularly interacting with the site as repeat visitors.

### User stories

#### As an anonymous user...
1. View workouts: As a user I can view a selection of workouts so that I can choose one to complete.
2. Filter workouts: As a user I can filter workouts so that I can easily find one that I want to do.
3. Workout categories: As a user I can browse different categories of workouts so that I can easily find the type of workout I want to do.
4. Create account: As a user I can create an account so that I can come back to saved workouts and comment on workouts (become an authenticated user).
5. View saves: As a user I can see how many people have saved a workout so that I can see what is popular.
6. View comments: As user I can see comments on workouts so that I can see what other people think.

#### As an authenitacted user...
1. Save workouts: As an authenticated user I can mark workouts I like so that I can come back to them later.
2. Complete workouts: As a user I can mark off workouts I have completed so that I can see a record of what I have done.
3. Comment on workouts: As a user I can comment on workouts and see those left by others so that I can leave my feedback and interact with other users.

#### As an admin user...
1. View saves: As an admin I can see how many people have saved a workout so that I can see what is popular.
2. View comments: As an admin I can see comments on workouts so that I can understand user feedback.
3. Approve comments: As an admin I can approve comments so that I can make sure they are appropriate.
4. Create workouts: As an admin I can create new workouts so that there is regular new content for users.
5. Update workouts: As an admin I can update existing workouts so that they can be changed based on user feedback.
6. Delete workouts: As an admin I can delete workouts so that unpopular workouts can be removed.

User stories were added and tracked using [GitHub projects](https://github.com/users/mariacjones1/projects/2/views/1).

### Flowcharts

1. Find a workout
![Find workout](/documentation/planning/flowchart_find-workout.png)

Changes made from plan to final project:
- User can also select the option 'See all workouts >>' from the homepage.

2. Sign in
![Sign in](/documentation/planning/flowchart_sign-in.png)

Changes made from plan to final project:
- Sign in and sign up are accessed via separate links (although one can be access via the other).

3. Create a new workout
![Create workout](/documentation/planning/flowchart_create-new-workout.png)

Changes made from plan to final project:
- User is redirected to homepage instead of the new workout page - potential future change.

### Models diagram

Created using [dbdiagram.io](https://dbdiagram.io/)
![Models diagram](/documentation/planning/models-diagram.png)

### Wireframes

Created using [Balsamiq](https://balsamiq.com/)

#### Homepage (not signed in)
![Homepage - not signed in (wireframe)](/documentation/wireframes/homepage_not_signed_in.png)
![Homepage - not signed in (screenshot)](/documentation/screenshots/homepage_not_signed_in.png)
![Homepage scrolled down (screenshot)](/documentation/screenshots/homepage_2.png)

Changes made from design to final project:
- The homepage first shows the three most recently added workouts, with the option to click 'See all workouts >>' which will show the user a page showing all workouts, not filtered by category. Below this, the user can select a category is they wish to browse a specific category. Each category card shows the placeholder image for that category with a coloured overlay to make it visually different to the workout cards.
- The main navbar components don't stretch across the width of the screen but are all to the left, next to the site logo. The search bar is included on the navbar but aligned right on the screen. On smaller screens, the entire navbar collapses and a burger icon is used.

#### Sign up, sign in and sign out
![Sign up (wireframe)](/documentation/wireframes/sign_up.png)
![Sign up (screenshot)](/documentation/screenshots/sign_up.png)
![Sign in (wireframe)](/documentation/wireframes/sign_in.png)
![Sign in (screenshot)](/documentation//screenshots/sign_in.png)
![Sign out (screenshot)](/documentation/screenshots/sign_out.png)

Changes made from design to final project:
- Final sign up, sign in and sign out pages use Django AllAuth templates which were edited to extend base.html and match the rest of the site.

#### Homepage (signed in)
![Homepage - signed in (wireframe)](/documentation/wireframes/homepage_signed_in.png)
![Homepage - signed in (screenshot)](/documentation/screenshots/homepage_signed_in.png)

Changes made from design to final project:
- The option to create a new workout (authorised users only) is in the navbar instead of being above it, and saved and completed workouts can be accessed via the 'My workouts' dropdown. These two choices make the site cleaner and easier to navigate.

#### Browse workouts
![Browse workouts (wireframe)](/documentation/wireframes/workout_category.png)
![Browse workouts (screenshot)](/documentation/screenshots/browse_workouts.png)
![Browse workouts scrolled down (screenshot)](/documentation/screenshots/browse_workouts_2.png)

Changes made from design to final project:
- Workout cards span three columns instead of four, and are six to a page.
- Workout cards include workout author, category, creation date, number of saves and number of completes.

#### Selected workout
![Selected workout (wireframe)](/documentation/wireframes/selected_workout.png)
![Selected workout (screenshot)](/documentation/screenshots/selected_workout.png)

Changes made from design to final project:
- The workout author, creation date and number of saves and completes are added below the workout title. Number of saves and completes is separate from the buttons below the workout image allowing the user to save or mark a workout as complete (authenticated users only) as having them together looked messy.
- Edit and delete workout buttons (visible to authorised users only) appear to the right of the workout.

#### Create (or edit) workout
![Create workout (wireframe)](/documentation/wireframes/create_new_workout.png)
![Create workout (screenshot)](/documentation/screenshots/create_workout.png)
![Edit workout (screenshot)](/documentation/screenshots/edit_workout.png)

Changes made from design to final project:
- All fields span the entire section (automatically formatted using crispy forms).
- Additional information field not included - potential future feature.
- Edit workout uses a similar template, but current workout information is pre-populated and the user has the option to delete exercises.

#### Delete workout
![Confirm workout delete (screenshot)](/documentation/screenshots/delete_workout.png)

Changes made from design to final project:
- No wireframe created for deletion confirmation page.

#### Responsiveness
- No wireframes were made for additional devices as the primary method of ensuring responsiveness was to use Bootstrap classes before testing and updating as needed for smaller screens.

### Design choices

- Colours:
    - The main colours used are white, black and blue (dark blue for buttons, logo and links, light blue for container backgrounds). Other colours are used for workout category overlays to make them more visually different and interesting.
- Fonts:
    - Default Bootstrap fonts are used as they work well and there was no need to change them.
- Images:
    - Each workout has an image to keep the pages visually interesting. Placeholder images are provided if the user doesn't upload a specific image when creating a workout; these differ by category to keep the homepage and 'Browse all workouts' pages varied.

## Features

### Responsive layouts
- Bootstrap styles have been used to make the website responsive (see mock-up).

### Favicon and title
- UX is enhanced by featuring a relevant icon and title, making the tab easy to identify in the browser.

![Favicon and title](/documentation/screenshots/favicon_and_title.png)

### Navigation
- All users will be able to navigate to the homepage by clicking on either the site logo or 'Home' in the navbar.
- All users can navigate to 'Browse all workouts' by clicking either 'All workouts' in the navbar or 'See all workouts >>' on the homepage.
- All users can navigate to browse workouts filtered by a chosen category by either clicking 'Workout categories' in the navbar or navigating to the homepage and then choosing a workout category.
- All users can search for workouts by name by typing all or part of it in the search bar in the navbar and either clicking 'Search' or hitting the Enter key.
- All users can view a specific workout by selecting it from any of the browse pages.
- Non-authenticated users with existing accounts can navigate to the sign in page by clicking 'Sign in' in the navbar.
- Non-authenticated users without existing accounts can navigate to the sign up page by clicking 'Sign up' in the navbar.
- Authenticated users can navigate to the sign out page by clicking 'Sign out' in the navbar.
- Authenticated users can navigate to their saved or completed workouts by clicking 'My workouts' in the navbar and selecting either 'Saved' or 'Completed'.
- Authorised users can navigate to the 'Create workout' page by clicking 'New workout' in the navbar.
- Authorised pages can navigate to either 'Edit workout' or 'Delete workout' pages by clicking the respective button on the page of the workout they wish to edit or delete.

![Navbar - non-authenticated user](/documentation/screenshots/navbar_non-authenticated_user.png)
![Navbar - authenticated user](/documentation/screenshots/navbar_authenticated_user.png)
![Navbar - authorised user](/documentation/screenshots/navbar_authorised_user.png)

### Create, edit and delete workouts
- Only authorised users are able to create, update and delete workouts (permissions must be granted in Django admin). Non-authorised users will not see the 'New workout' link in the navbar, or the 'Edit workout' and 'Delete workout' buttons on the workout pages, and they will be receive a 403 error if they try to access the pages via the address bar.
- The create and edit workout pages are almost identical, with the exceptions that existing workout details will be pre-populated on the edit workout page, and users will also be able to delete existing exercises by selecting the 'Delete' checkbox which is below each one.
- New workouts will have space for three exercises, with the ability to add exercises one at a time by clicking 'Add exercise' at the bottom of the form, up to a maximum of ten exercises total. This feature is also present on the 'Edit workout' page, again up to a maximum total of ten (not taking into account any exercises marked for deletion, as they could be unchecked resulting in an error of too many exercises being added).
- Sets and reps use integer fields with a minimum value of 1 and a maximum value of 10 (sets) and 30 (reps), to prevent users from entering negative, decimal or too-high numbers.
- Users who select the 'Delete workout' button will be directed to a page asking them to confirm the deletion, giving them the option to cancel if they change their mind or selected the option by mistake.
- After creating a new workout, users will be redirected to the homepage, where they should see their new workout as the first card under 'Recently added workouts'. After editing a workout, users will be redirected back to that workout page where they can see the changes they have made. After deleting a workout, users will be redirected to the homepage.
- Any admin can edit or delete any existing workout, as only a limited number of users will have the necessary permissions.

![Create workout](/documentation/screenshots/create_workout.png)
![Create workout - add exercise and submit](/documentation/screenshots/create_workout_2.png)
![Edit workout](/documentation/screenshots/edit_workout.png)
![Delete workout](/documentation/screenshots/delete_workout.png)

### Custom 403 and 404 pages
- Users who are directed to either 403 (access forbidden) or 404 (page not found) pages will see custom pages instead of default Django pages. Although basic, this is less jarring as it uses the same formatting as the rest of the site, and both feature a link to the homepage so that the user doesn't have to rely on browser buttons to get back.

![403 page](/documentation/screenshots/403_page.png)
![404 page](/documentation/screenshots/404_page.png)

## Technology

### Languages used

- HTML5
- CSS3
- JavaScript
- Python

### Frameworks, libraries and programs used

- [Django 3.2.20](https://www.djangoproject.com/)
    - Web framework
- [Bootstrap 5.3.1](https://getbootstrap.com/)
    - To assist with styling and responsiveness
- [ElephantSQL](https://www.elephantsql.com/)
    - For database storage
- [Cloudinary](https://cloudinary.com/)
    - For media storage
- [Git](https://git-scm.com/)
    - Used for version control by pushing commits to GitHub
- [GitHub](https://github.com/)
    - For project storage
- [Font Awesome](https://fontawesome.com/)
    - To provide icons
- [favicon.io](https://favicon.io/)
    - To generate the favicon
- [GIMP](https://www.gimp.org/)
    - To edit images used
- [Balsamiq](https://balsamiq.com/)
    - For creating wireframes
- [dbdiagram.io](https://dbdiagram.io/)
    - For creating the models diagram
- [Pexels](https://www.pexels.com/)
    - For sourcing images

## Testing

### Testing user stories

1. View workouts: As a user I can view a selection of workouts so that I can choose one to complete.
    - Upon entering the site, users can see the three most recent workouts, as well as the options to see all workouts or to select a workout category by scrolling down.
    - Test: enter the site
    ![Homepage](/documentation/screenshots/homepage_not_signed_in.png)

2. Filter workouts: As a user I can filter workouts so that I can easily find one that I want to do.
    - Users are able to use the search bar to search for a workout whose name contains the search term.
    - Test: search term 'lower' entered into search bar
    ![Search results](/documentation/screenshots/search_results_lower.png)

3. Save workouts: As a user I can mark workouts I like so that I can come back to them later.
    - Users who have signed in are able to save workouts from the workout detail page. Saved workouts will be shown when the user goes to My workouts > Saved in the navbar.
    - Test: Sign in as any user, select a workout and click 'Save for later'. This should change to 'Saved'. Navigate to My workouts > Saved and see the workout.
    ![Save a workout](/documentation/screenshots/save_a_workout.png)
    ![Saved workouts](/documentation/screenshots/saved_workouts.png)

4. Complete workouts: As a user I can mark off workouts I have completed so that I can see a record of what I have done.
    - Users who have signed in are able to mark workouts as completed from the workout detail page. Completed workouts will be shown when the user goes to My workouts > Completed in the navbar.
    - Test: Sign in as any user, select a workout and click 'Mark as completed'. This should change to 'Completed'. Navigate to My workouts > Completed and see the workout.
    ![Complete a workout](/documentation/screenshots/complete_a_workout.png)
    ![Completed workouts](/documentation/screenshots/completed_workouts.png)

5. Comment on workouts: As a user I can comment on workouts so that I can leave my feedback.
    - Users who have signed in are able to comment on workout from the workout detail page. Comments must be approved by admin before they appear for other users to see. Users who have not signed in are still able to see other users' comments.
    - Test: Sign in as any user, select a workout and submit a comment. Sign in as admin, go to the Django admin panel and approve the comment. Go back to the site, select the same workout, and see the comment.
    ![Submit a comment](/documentation/screenshots/submit_comment.png)
    ![Comment awaiting approval](/documentation/screenshots/comment_awaiting_approval.png)
    ![Approve comment as admin](/documentation/screenshots/approve_comments.png)
    ![Comment is visible](/documentation/screenshots/comment_visible.png)

6. Workout categories: As a user I can browse different categories of workouts so that I can easily find the type of workout I want to do.
    - Users are able to select a workout category from the homepage or by selecting 'Workout categories' in the navbar and choosing a category from the rendered page, which will show them all the workouts within that category.
    - Test 1: Select a workout category from the homepage and view workouts for that category.
    - Test 2: Go to 'Workout categories' in the navbar, choose a category from the rendered page and view workouts for the chosen category.
    ![Select category](/documentation/screenshots/browse_by_category.png)
    ![Browse selected category](/documentation/screenshots/browse_selected_category.png)

7. Create account: As a user I can create an account so that I can come back to saved workouts and comment on workouts.
    - Users can either sign up or sign in using the respective navbar links. Authenticated users have access to additional website features, such as saving, completing and commenting on workouts.
    - Test: Sign up as a new user. Sign out and sign back in with new credentials. See the additional options in the navbar.
    ![New user sign-up](/documentation/screenshots/sign_up_new.png)
    ![New user sign-in](/documentation/screenshots/sign_in_new.png)
    ![Autheticated user navbar](/documentation/screenshots/navbar_authenticated_user.png)

8. View saves: As an admin I can see how many people have saved a workout so that I can see what is popular.
    - The number of saves and completes is visible on all workouts, both the cards on browsing pages and on the workout detail pages themselves. All users are able to see these numbers.
    - Test: Sign in as any user and check the saved and completed icons next to any workout.
    ![Saves and completes](/documentation/screenshots/saves_and_completes.png)


9. View comments: As an admin I can see comments on workouts so that I can understand user feedback.
    - Comments are visible on all workout detail pages to all users.
    - Test: Sign in as any user, select any workout and view the comments underneath the workout details.
    ![View comments](/documentation/screenshots/comment_visible.png)

10. Approve comments: As an admin I can approve comments so that I can make sure they are appropriate.
    - Submitted comments are not approved by default; an admin user must approve them before they are visible to other users. In the Django admin panel, the most recent comments will appear first, and comments can be filtered by whether or not they have been approved.
    - Test: Sign in as any user, navigate to any workout and submit a comment. A message will appear saying that the comment is pending approval. Sign in as an admin user and go to the Django admin panel, go to comments and see the comments which haven't been approved. Select and approve the comment, then navigate back to the workout on the main site and see the comment there.
    ![Approve comments](/documentation/screenshots/approve_comments.png)

11. Create workouts: As an admin I can create new workouts so that there is regular new content for users.
    - Users assigned to the admin group on Django admin are able to create new workouts by clicking 'New workout' in the navbar and filling in the new workout form. The workout slug is populated from the workout title. Users without admin permissions will not see the 'New workout' option in the navbar, and will be directed to a 403 page if they try to access it via the address bar.
    - Test 1: Sign in as an admin user, click 'New workout' in the navbar and fill in the new workout details. Click 'Add exercises' if additional exercises are needed beyond the forms for the first three initially provided. Submit the workout, and be navigated back to the homepage where the new workout will appear as the first workout under 'Recently added workouts'.
    ![Create new workout](/documentation/screenshots/create_workout_filled_in.png)
    ![Add exercise](/documentation/screenshots/add_exercise.png)
    ![Recently added workouts](/documentation/screenshots/new_workout_added.png)
    - Test 2: Sign in as a non-admin user and see that there is no 'New workout' link in the navbar. Add '/new_workout/' to the end of the URL in the address bar and be directed to a 403 page.
    ![Navbar for non-admin user](/documentation/screenshots/navbar_authenticated_user.png)
    ![403 page](/documentation/screenshots/new_workout_403.png)
    - Test 3: Sign out and add '/new_workout/' to the end of the URL in the address bar. Non-authenticated users are directed to the login page.
    ![Sign in page](/documentation/screenshots/new_workout_sign_in.png)

12. Update workouts: As an admin I can update existing workouts so that they can be changed based on user feedback.
    - Users assigned to the admin group on Django admin are able to edit workouts by clicking the 'Edit workout' button on the workout detail page and making changes in the workout form. The workout slug will be updated if the title is changed. Users are able to delete and add new exercises. Users without admin permissions will not see the 'Edit workout' button, and will be directed to a 403 page if they try to access it via the address bar.
    - Test 1: Sign in as an admin user, navigate to any workout page and click the 'Edit workout' button. Make the required changes, including clicking 'Add exercises' if additional exercises are needed beyond what has already been added, and deleting any existing exercises. Submit the workout, and be navigated back to the workout page which will show the new changes (including an updated slug if the workout name was changed).
    ![Workout page with edit button](/documentation/screenshots/workout_edit_button.png)
    ![Edit workout name and image](/documentation/screenshots/edit_workout_name_image.png)
    ![Add and delete exercises](/documentation/screenshots/edit_workout_add_delete.png)
    ![View updated workout](/documentation/screenshots/updated_workout.png)
    - Test 2: Sign in as a non-admin user and see that there is no 'Edit workout' button on the workout pages. Add '/edit_workout/' before the selected workout slug in the address bar and be directed to a 403 page.
    ![workout page with no edit button](/documentation/screenshots/selected_workout.png)
    ![403 page](/documentation/screenshots/edit_workout_403.png)
    - Test 3: Sign out and add '/edit_workout/' before the selected workout slug in the address bar. Non-authenticated users are directed to the login page.
    ![Sign in page](/documentation/screenshots/edit_workout_sign_in.png)

13. Delete workouts: As an admin I can delete workouts so that unpopular workouts can be removed.
    - Users assigned to the admin group on Django admin are able to delete workouts by clicking the 'Delete workout' button on the workout detail page. They will be directed to a page asking them to confirm the deletion, at which point they can either cancel or confirm delete. Users without admin permissions will not see the 'Delete workout' button, and will be directed to a 403 page if they try to access it via the address bar.
    - Test 1: Sign in as an admin user, navigate to any workout page and click the 'Delete workout' button. On the confirm delete page, click 'Delete' to confirm that the workout will be deleted. Search for the workout and see that it does not appear in the results. Enter the workout URL in the address bar and be redirected to a 404 page.
    ![Workout page with delete button](/documentation/screenshots/workout_delete_button.png)
    ![Confirm delete](/documentation/screenshots/confirm_delete.png)
    ![Workout search no results](/documentation/screenshots/deleted_workout_no_results.png)
    ![Enter URL 404](/documentation/screenshots/deleted_workout_404.png)
    - Test 2: Sign in as a non-admin user and see that there is no 'Delete workout' button on the workout pages. Add '/delete_workout/' before the selected workout slug in the address bar and be directed to a 403 page.
    ![workout page with no delete button](/documentation/screenshots/selected_workout.png)
    ![403 page](/documentation/screenshots/delete_workout_403.png)
    - Test 3: Sign out and add '/edit_workout/' before the selected workout slug in the address bar. Non-authenticated users are directed to the login page.
    ![Sign in page](/documentation/screenshots/delete_workout_sign_in.png)

### Automated testing

#### Python
Automated testing was done using the following files:
[test_forms.py](/planner/test_forms.py)
[test_views.py](/planner/test_views.py)
[test_models.py](/planner/test_models.py)

In order to run these tests, I had to change the database being used via [settings.py](/build/settings.py):
![settings.py databases](/documentation/testing/database_for_testing.png)

Total coverage was 91%, with the uncovered code being in [views.py](/planner/views.py) and [admin.py](/planner/admin.py). This code has been manually tested. All automated tests pass.
![Code coverage](/documentation/testing/coverage.png)

### Validator testing
#### HTML validator
[W3C](https://validator.w3.org/)

N.B. Django variables and tags removed before running as these were flagging as errors.

| File | Results |
| --- | --- |
| [base.html](/templates/base.html) | No errors or warnings to show. |
| [confirm_delete.html](/templates/confirm_delete.html) | Missing elements found in base.html. <br> The element button must not appear as a descendant of the a element. (Fixed in file and re-run to confirm issue is solved). |
| [edit_workout.html](/templates/edit_workout.html) | Missing elements found in base.html. <br> No other errors or warnings. |
| [index.html](/templates/index.html) | Missing elements found in base.html. <br> An img element must have an alt attribute. (Alt attributes added and file re-run to confirm issue is solved). |
| [new_workout.html](/templates/new_workout.html) | Missing elements found in base.html. <br> No other errors or warnings. |
| [workout_detail.html](/templates/workout_detail.html) | Missing elements found in base.html. <br> An img element must have an alt attribute. (Alt attributes added and file re-run to confirm issue is solved). <br> The element button must not appear as a descendant of the a element. (Fixed in file and re-run to confirm issue is solved). |
| [workouts.html](/templates/workouts.html) | Missing elements found in base.html. <br> An img element must have an alt attribute. (Alt attributes added and file re-run to confirm issue is solved). |
| [403/html](/templates/403.html) | No errors or warnings to show. |
| [404.html](/templates/404.html) | No errors or warnings to show. |

#### CSS validator
[W3C Jigsaw](https://jigsaw.w3.org/css-validator/validator)

| File | Results |
| --- | --- |
| [style.css](/static/css/style.css) | No Error Found. |

#### JavaScript validator
[JSHint](https://jshint.com/)

| File | Results |
| --- | --- |
| [script.js](/static/js/script.js) | x2 unnecessary semi-colons (Removed and re-run to confirm.) <br> All other warnings ignored:<br>x7: 'const' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).<br>x3: 'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).<br>x3: 'template literal syntax' is only available in ES6 (use 'esversion: 6').<br>One undefinred variable: bootstrap. |

#### Python validator
[PEP8](https://pep8ci.herokuapp.com/)

| File | Results |
| --- | --- |
| [admin.py](/planner/admin.py) | 18: E231 missing whitespace after ',' -> Fixed and re-run, all clear, no errors found. |
| [forms.py](/planner/forms.py) | 8, 17, 26: E231 missing whitespace after ',' -> Fixed and re-run, all clear, no errors found. |
| [models.py](/planner/models.py) | All clear, no errors found. |
| [planner urls.py](/planner/urls.py) | 10, 11, 12, 16: E501 line too long -> Fixed and re-run, all clear, no errors found. (N.B. only lines with errors split where needed - the decision was made not to put each parameter on a new line for consistency as this would result in the need for a lot of scrolling to edit or add new paths.) |
| [views.py](/planner/views.py) | All clear, no errors found. |
| [test_forms.py](/planner/test_forms.py) | 19, 30, 41: E231 missing whitespace after ','<br>44, 48, 52, 56: E501 line too long<br>-> All issues fixed and file re-run, all clear, no errors found. |
| [test_models.py](/planner/test_models.py) | All clear, no errors found. |
| [test_views.py](/planner/test_views.py) | All clear, no errors found. |
| [settings.py](/build/settings.py) | 129, 132, 135, 138, 161: E501 line too long -> Fixed using '\\' and re-run, all clear, no errors found. |
| [build urls.py](/build/urls.py) | All clear, no errors found. |


## Credits
Extending user model: https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
Multiselect: https://pypi.org/project/django-multiselectfield/
Register models: https://codinggear.blog/how-to-register-model-in-django-admin/?expand_article=1&expand_article=1
Multi-model view: https://www.youtube.com/watch?v=tP99aNINOGI&ab_channel=HarithaComputers%26Technology
Dynamic form: https://www.youtube.com/watch?v=s3T-w2jhDHE&ab_channel=CodingEntrepreneurs
Search: https://learndjango.com/tutorials/django-search-tutorial
Permissions: https://www.honeybadger.io/blog/django-permissions/