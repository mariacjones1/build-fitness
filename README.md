# Build Fitness workout planner
Build Fitness workout planner is a website that allows users to browse workouts. Users can either browse all workouts, browse by category or search for a specific workout, and authenticated users can browse by workouts they have either saved or completed. Authorised users can create new workouts, or edit or delete existing ones.

Final website: [https://build-fitness-66f794a76bbb.herokuapp.com/](https://build-fitness-66f794a76bbb.herokuapp.com/)

![Responsive mock-up](/documentation/screenshots/responsive_mock_up.png)

<hr>

## Table of contents

- [Design and planning](#design-and-planning)
    - [User stories](#user-stories)
    - [Flowcharts](#flowcharts)
    - [Models diagram](#models-diagram)
    - [Wireframes](#wireframes)
- [Technology](#technology)
    - [Languages used](#languages-used)
    - [Frameworks and libraries used](#frameworks-and-libraries-used)
- [Testing](#testing)
    - [Testing user stories](#testing-user-stories)
    - [Automated testing](#automated-testing)
    - [Validator testing](#validator-testing)
- [Credits](#credits)

## Design and planning

### User stories

1. View workouts: As a user I can view a selection of workouts so that I can choose one to complete.
2. Filter workouts: As a user I can filter workouts so that I can easily find one that I want to do.
3. Save workouts: As a user I can mark workouts I like so that I can come back to them later.
4. Complete workouts: As a user I can mark off workouts I have completed so that I can see a record of what I have done.
5. Comment on workouts: As a user I can comment on workouts so that I can leave my feedback.
6. Workout categories: As a user I can browse different categories of workouts so that I can easily find the type of workout I want to do.
7. Create account: As a user I can create an account so that I can come back to saved workouts and comment on workouts.
8. View saves: As an admin I can see how many people have saved a workout so that I can see what is popular.
9. View comments: As an admin I can see comments on workouts so that I can understand user feedback.
10. Approve comments: As an admin I can approve comments so that I can make sure they are appropriate.
11. Create workouts: As an admin I can create new workouts so that there is regular new content for users.
12. Update workouts: As an admin I can update existing workouts so that they can be changed based on user feedback.
13. Delete workouts: As an admin I can delete workouts so that unpopular workouts can be removed.

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
![Create workout scrolled down (screenshot)](/documentation/screenshots/create_workout.png)
![Edit workout (screenshot)](/documentation/screenshots/edit_workout.png)

Changes made from design to final project:
- All fields span the entire section (automatically formatted using crispy forms).
- Additional information field not included - potential future feature.
- Edit workout uses a similar template, but current workout information is pre-populated and the user has the option to delete exercises.

#### Delete workout
![Confirm workout delete (screenshot)](/documentation/screenshots/delete_workout.png)

Changes made from design to final project:
- No wireframe created for deletion confirmation page.

### Design choices

- Colours:
    - The main colours used are white, black and blue (dark blue for buttons, logo and links, light blue for container backgrounds). Other colours are used for workout category overlays to make them more visually different and interesting.
- Fonts:
    - Default Bootstrap fonts are used as they work well and there was no need to change them.
- Images:
    - Each workout has an image to keep the pages visually interesting. Placeholder images are provided if the user doesn't upload a specific image when creating a workout; these differ by category to keep the homepage and 'Browse all workouts' pages varied.

## Technology

### Languages used

- HTML5
- CSS3
- JavaScript
- Python

### Frameworks and libraries used

- Django 3.2.20
    - Web framework
- Bootstrap 5.3.1
    - To assist with styling and responsiveness
- Font Awesome
    - To provide icons
- Git
    - Used for version control by pushing commits to GitHub
- GitHub
    - For project storage
- GIMP
    - To edit images used

## Testing

### Testing user stories

1. View workouts: As a user I can view a selection of workouts so that I can choose one to complete.
    - Upon entering the site, users can see the three most recent workouts, as well as the options to see all workouts or to select a workout category by scrolling down.

2. Filter workouts: As a user I can filter workouts so that I can easily find one that I want to do.
    - Users are able to use the search bar to search for a workout whose name contains the search term.

3. Save workouts: As a user I can mark workouts I like so that I can come back to them later.
    - Users who have signed in are able to save workouts from the workout detail page. Saved workouts will be shown when the user goes to My workouts > Saved in the navbar.

4. Complete workouts: As a user I can mark off workouts I have completed so that I can see a record of what I have done.
    - Users who have signed in are able to mark workouts as completed from the workout detail page. Completed workouts will be shown when the user goes to My workouts > Completed in the navbar.

5. Comment on workouts: As a user I can comment on workouts so that I can leave my feedback.
    - Users who have signed in are able to comment on workout from the workout detail page. Comments must be approved by admin before they appear for other users to see. Users who have not signed in are still able to see other users' comments.

6. Workout categories: As a user I can browse different categories of workouts so that I can easily find the type of workout I want to do.
    - Users are able to select a workout category from the homepage, which will show them all the workouts within that category.

7. Create account: As a user I can create an account so that I can come back to saved workouts and comment on workouts.
    - Users can either sign up or sign in using the respective navbar links. Authenticated users have access to additional website features, such as saving, completing and commenting on workouts.

8. View saves: As an admin I can see how many people have saved a workout so that I can see what is popular.
    - The number of saves and completes is visible on all workouts, both the cards on browsing pages and on the workout detail pages themselves. All users are able to see these numbers.

9. View comments: As an admin I can see comments on workouts so that I can understand user feedback.
    - Comments are visible on all workout detail pages to all users.

10. Approve comments: As an admin I can approve comments so that I can make sure they are appropriate.
    - Submitted comments are not approved by default; an admin user must approve them before they are visible to other users.

11. Create workouts: As an admin I can create new workouts so that there is regular new content for users.
    - Users assigned to the admin group on Django admin are able to create new workouts by clicking 'New workout' in the navbar and filling in the new workout form. The workout slug is populated from the workout title. Users without admin permissions will not see the 'New workout' option in the navbar, and will be directed to a 403 page if they try to access it via the address bar.

12. Update workouts: As an admin I can update existing workouts so that they can be changed based on user feedback.
    - Users assigned to the admin group on Django admin are able to edit workouts by clicking the 'Edit workout' button on the workout detail page and making changes in the workout form. The workout slug will be updated if the title is changed. Users are able to delete and add new exercises. Users without admin permissions will not see the 'Edit workout' button, and will be directed to a 403 page if they try to access it via the address bar.

13. Delete workouts: As an admin I can delete workouts so that unpopular workouts can be removed.
    - Users assigned to the admin group on Django admin are able to delete workouts by clicking the 'Delete workout' button on the workout detail page. They will be directed to a page asking them to confirm the deletion, at which point they can either cancel or confirm delete. Users without admin permissions will not see the 'Delete workout' button, and will be directed to a 403 page if they try to access it via the address bar.

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
[W3C](https://jigsaw.w3.org/css-validator/validator)

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