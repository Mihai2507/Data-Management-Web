function handleDropdownChange() {
    var dropdown = document.getElementById('dropdown');
    var cursantForm = document.getElementById('cursantForm');
    var companieForm = document.getElementById('companieForm');
    var comisieForm = document.getElementById('comisieForm');
    var cursForm = document.getElementById('cursForm');

    cursantForm.classList.add('hidden');
    companieForm.classList.add('hidden');
    comisieForm.classList.add('hidden');
    cursForm.classList.add('hidden');

    if (dropdown.value === 'option1') {
        cursantForm.classList.remove('hidden');
    }
    else if (dropdown.value === 'option2') {
        companieForm.classList.remove('hidden');
    }
    else if (dropdown.value === 'option3') {
        comisieForm.classList.remove('hidden');
    }
    else if (dropdown.value === 'option4') {
        cursForm.classList.remove('hidden');
    }
}