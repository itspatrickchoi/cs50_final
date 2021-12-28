let itemCount = document.querySelector(".foci").childElementCount;
let focusFoci = document.querySelector(".focus-foci");
let taskCount = document.querySelector(".task-count");
if (itemCount != 0) {
    taskCount.innerHTML = itemCount;
}
if (itemCount > 1 || itemCount == 0) {
    focusFoci.innerHTML = "FOCI";
}
else {
    focusFoci.innerHTML = "FOCUS";
}