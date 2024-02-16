document.getElementById('money').addEventListener('input', function (event) {
    const maxLimit = 25; // Set your desired max limit
    let inputValue = event.target.value.replace(/\D/g, '');
    inputValue = (inputValue / 100).toFixed(2);
    if (parseFloat(inputValue) > maxLimit) {
        inputValue = (maxLimit).toFixed(2);
    }

    event.target.value = inputValue;
});
