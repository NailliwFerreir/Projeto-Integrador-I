//menu
let optInsert = document.getElementById("option-insert");
let optAlter = document.getElementById("option-alter");
let optDelete = document.getElementById("option-delete");
let optInsertView = document.querySelector(".option-insert");
let optDeleteView = document.querySelector(".option-delete");
let optAlterView = document.querySelector(".option-alter");
optInsert.addEventListener("click", () => {
  optInsert.attributes.style.value = "background-color:#4B9B5C";
  optAlter.attributes.style.value = "";
  optDelete.attributes.style.value = "";
  optInsertView.style.display = "block";
  optAlterView.style.display = "none";
  optDeleteView.style.display = "none";
});
optAlter.addEventListener("click", () => {
  optAlter.attributes.style.value = "background-color:#4B9B5C";
  optInsert.attributes.style.value = "";
  optDelete.attributes.style.value = "";
  optInsertView.style.display = "none";
  optAlterView.style.display = "block";
  optDeleteView.style.display = "none";
});
optDelete.addEventListener("click", () => {
  optInsert.attributes.style.value = "";
  optAlter.attributes.style.value = "";
  optDelete.attributes.style.value = "background-color:#4B9B5C";
  optInsertView.style.display = "none";
  optAlterView.style.display = "none";
  optDeleteView.style.display = "block";
});
//select custom
document.addEventListener("DOMContentLoaded", function () {
  document.addEventListener("click", function (event) {
    closeAllSelects(event.target);
  });

  var selects = document.getElementsByClassName("custom-select");
  for (var i = 0; i < selects.length; i++) {
    var select = selects[i].querySelector(".select-selected");
    select.addEventListener("click", function (event) {
      event.stopPropagation();
      closeAllSelects(this);
      this.nextElementSibling.style.display = "block";
    });
  }

  function closeAllSelects(element) {
    var selects = document.getElementsByClassName("custom-select");
    for (var i = 0; i < selects.length; i++) {
      var select = selects[i].querySelector(".select-selected");
      var selectItems = selects[i].querySelector(".select-items");
      if (element !== select && element !== selectItems) {
        selectItems.style.display = "none";
      }
    }
  }
});
// inputs filter
window.onload = function () {
  document.querySelectorAll(".option-inputs input").forEach((inputs) =>
    inputs.addEventListener("keyup", function () {
      if (this.value.length === 1 && (this.value === ',' || this.value === '.')) {
        this.value = this.value.replace("");
      }
      this.value = this.value.replace(/[^0-9.,]+/g, "");
    })
  );
};
