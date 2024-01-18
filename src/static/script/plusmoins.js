const buttons = document.querySelectorAll(".button");
const minValue = 0;
const maxValue = 99;

buttons.forEach((button) => {
  button.addEventListener("click", (event) => {
    const element = event.currentTarget;
    const parent = element.parentNode;
    const numberContainer = parent.querySelector(".number");
    const number = parseFloat(numberContainer.textContent);
    const increment = parent.querySelector(".plus");
    const decrement = parent.querySelector(".minus");
    const newNumber = element.classList.contains("plus")
      ? number + 1
      : number - 1;
    numberContainer.textContent = newNumber;
    console.log(newNumber);
    if (newNumber === minValue) {
      decrement.disabled = true;
      numberContainer.classList.add("dim");
      element.blur();
    } else if (newNumber > minValue && newNumber < maxValue) {
      decrement.disabled = false;
      increment.disabled = false;
      numberContainer.classList.remove("dim");
    } else if (newNumber === maxValue) {
      increment.disabled = true;
      numberContainer.textContent = `${newNumber}+`;
      element.blur();
    }
  });
});