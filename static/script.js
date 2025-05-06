document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("calcForm").addEventListener("submit", function (e) {
        e.preventDefault();

        const formData = new FormData(this);

        fetch("/calculate", {
            method: "POST",
            body: formData
        })
        .then(response => response.text())
        .then(result => {
            document.getElementById("result").innerText = "Result: " + result;
        });
    });
});
