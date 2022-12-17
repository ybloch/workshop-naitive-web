$(document).ready(function () {
  $("#login-btn").click(function () {
    const username = $("#username").val();
    const password = $("#password").val();
    fetch("/login", {
      method: "POST",
      body: JSON.stringify({ username: username, password: password }),
    }).then((response) => {
      console.log(response);
      if (response.status === 200) {
        window.location.href = "/static/home.html";
      }
    });
  });
});
