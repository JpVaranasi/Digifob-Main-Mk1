const formsByYear = {
    "11": ["DO", "YOU", "FRY"],
    "10": ["PEA", "IN", "PAN"],
    "9": ["FOR", "DRY", "SOUP"],
    "8": ["NAH", "NO", "WAY"],
    "7": ["LMAO", "LOL","XD"],
};
const studentsByForm = {

    "DO": ["John", "Jane", "Jim"],
    "YOU": ["Alice", "Bob", "Charlie"],
    "FRY": ["Eva", "David", "Emma"],
};
function updateFormDropdown() {
    const selectedYear = document.getElementById('select-year').value;
    const formDropdown = document.getElementById('select-form');
    formDropdown.innerHTML = '';
    formsByYear[selectedYear].forEach(form => {
        const formElement = document.createElement('option');
        formElement.value = form;
        formElement.text = form;
        formDropdown.appendChild(formElement);
    });

    updateStudentDropdown();
}
function updateStudentDropdown() {
    const selectedForm = document.getElementById('select-form').value;
    const studentOptions = document.getElementById('student-options');
    
    studentOptions.innerHTML = '';
    studentsByForm[selectedForm].forEach(student => {
        const studentOption = document.createElement('option');
        studentOption.value = student;
        studentOptions.appendChild(studentOption);
    });
}
function filterStudents() {
    const selectedForm = document.getElementById('select-form').value;
    const studentInput = document.getElementById('student-input').value.toLowerCase();
    const studentOptions = document.getElementById('student-options');
    studentOptions.innerHTML = '';
    studentsByForm[selectedForm]
        .filter(student => student.toLowerCase().includes(studentInput))
        .forEach(filteredStudent => {
            const studentOption = document.createElement('option');
            studentOption.value = filteredStudent;
            studentOptions.appendChild(studentOption);
        });
}
updateFormDropdown();



