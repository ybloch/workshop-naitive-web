$(document).ready(function () {
  fetch("/api/v1/tasks", {
    method: "GET",
  }).then((response) => {
    console.log(response);
    if (response.status === 200) {
      response.json().then((data) => {
        console.log(data);
        data.forEach((task) => {
          $("#tasks-container").append(
            `<div class="task-item">${task.title} - ${task.description}</div>`
          );
        });
      });
    }
  });
});
