const target = document.getElementById("target");

const first = document.createElement("li");
first.textContent = "First item";

const second = document.createElement("li");
second.textContent = "Second item";

const third = document.createElement("li");
third.textContent = "Third item";
second.classList.add("my-item");
target.appendChild(first);
target.appendChild(second);
target.appendChild(third);