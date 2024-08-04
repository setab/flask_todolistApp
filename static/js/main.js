// document.addEventListener("DOMContentLoaded", () => {
//   const addTaskButton = document.getElementById("add-task");
//   const taskInput = document.getElementById("task-input");
//   const taskList = document.getElementById("task-list");

//   addTaskButton.addEventListener("click", () => {
//     const taskText = taskInput.value.trim();
//     if (taskText) {
//       const li = document.createElement("li");
//       li.textContent = taskText;

//       const removeButton = document.createElement("button");
//       removeButton.textContent = "Remove";
//       removeButton.className = "remove-task";
//       removeButton.addEventListener("click", () => {
//         taskList.removeChild(li);
//       });

//       li.appendChild(removeButton);
//       taskList.appendChild(li);
//       taskInput.value = "";
//     }
//   });

//   taskInput.addEventListener("keypress", (e) => {
//     if (e.key === "Enter") {
//       addTaskButton.click();
//     }
//   });
// });
