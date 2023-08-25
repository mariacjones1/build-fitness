const addFormBtn = document.getElementById('add-form')
const totalNewForms = document.getElementById('id_exercises-TOTAL_FORMS')
const currentExerciseForms = document.getElementsByClassName('exercise-form')

addFormBtn.addEventListener('click', add_new_form)

function add_new_form(event) {
    if (event) {
        event.preventDefault()
    }
    
    let currentFormCount = currentExerciseForms.length
    const exercisesList = document.getElementById('exercises')
    const copyEmptyForm = document.getElementById('empty-form').cloneNode(true)
    copyEmptyForm.setAttribute('class', 'exercise-form')
    copyEmptyForm.setAttribute('id', `form-${currentFormCount}`)
    const regex = new RegExp('__prefix__', 'g')
    copyEmptyForm.innerHTML = copyEmptyForm.innerHTML.replace(regex, currentFormCount)
    totalNewForms.setAttribute('value', currentFormCount + 1)
    exercisesList.append(copyEmptyForm)
}