function redirectToStudentPage(event) {
    event.preventDefault(); 
    var button = event.target;
    var studentId = button.value;
    var url = '/student-details-editor/' + studentId; 
    window.location.href = url;
}
