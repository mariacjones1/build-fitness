## Testing

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

#### CSS validator
[W3C](https://jigsaw.w3.org/css-validator/validator)

| File | Results |
| --- | --- |
| [style.css](/static/css/style.css) | No Error Found. |

#### JavaScript validator
[JSHint](https://jshint.com/)
| File | Results |
| --- | --- |
| [script.js](/static/js/script.js) | x2 unnecessary semi-colons (Removed and re-run to confirm.) <br> All other warnings ignored:<br>x7: 'const' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).<br>x1: 'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).<br>x3: 'template literal syntax' is only available in ES6 (use 'esversion: 6'). |

## Credits
Extending user model: https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
Multiselect: https://pypi.org/project/django-multiselectfield/
Register models: https://codinggear.blog/how-to-register-model-in-django-admin/?expand_article=1&expand_article=1
Multi-model view: https://www.youtube.com/watch?v=tP99aNINOGI&ab_channel=HarithaComputers%26Technology
Dynamic form: https://www.youtube.com/watch?v=s3T-w2jhDHE&ab_channel=CodingEntrepreneurs
Search: https://learndjango.com/tutorials/django-search-tutorial
Permissions: https://www.honeybadger.io/blog/django-permissions/