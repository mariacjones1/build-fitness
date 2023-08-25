const addFormBtn = document.getElementById('add-form')
const totalNewForms = document.getElementById('id_exercises-TOTAL_FORMS')
const currentExerciseForms = document.getElementsByClassName('exercise-form')

addFormBtn.addEventListener('click', add_new_form)

function add_new_form(event) {
    if (event) {
        event.preventDefault()
    }
    
    let currentFormCount = currentExerciseForms.length
    if (currentFormCount < 10) {
        const exercisesList = document.getElementById('exercises')
        const copyEmptyForm = document.getElementById('empty-form').cloneNode(true)
        copyEmptyForm.setAttribute('class', 'exercise-form')
        copyEmptyForm.setAttribute('id', `form-${currentFormCount}`)
        const regex = new RegExp('__prefix__', 'g')
        const exerciseNum = document.createElement("p")
        exerciseNum.innerHTML = `<strong>Exercise ${currentFormCount+1}</strong>`
        exerciseNum.setAttribute('class', 'mt-3')
        copyEmptyForm.innerHTML = copyEmptyForm.innerHTML.replace(`${regex, currentFormCount}`)
        totalNewForms.setAttribute('value', currentFormCount + 1)
        exercisesList.append(exerciseNum)
        exercisesList.append(copyEmptyForm)
    }
}