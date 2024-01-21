const buttons = document.querySelectorAll(".button");
const minValue = 0;
const maxValue = 99;
const totalAmountElement = document.getElementById("totalAmount");

buttons.forEach((button) => {
  button.addEventListener("click", async (event) => {
    const element = event.currentTarget;
    const parent = element.parentNode;
    const numberContainer = parent.querySelector(".number");
    const number = parseFloat(numberContainer.textContent);
    const increment = parent.querySelector(".plus");
    const decrement = parent.querySelector(".minus");
    const billetId = element.closest('.item-left').querySelector('.billet-item').dataset.id;
    const newNumber = element.classList.contains("plus")
      ? number + 1
      : number - 1;
    numberContainer.textContent = newNumber;
    try {
      const response = await fetch(`/modifier_quantite/${billetId}/${newNumber}`, {
          method: 'GET',
      });
      if (!response.ok) {
          throw new Error('La requête a échoué');
      }
      const data = await response.json();
      console.log(data);
      updateTotalPrice();
      }
    catch (error) {
      console.error('Erreur de la requête:', error);
    }
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

const deleteButtons = document.querySelectorAll(".delete-button");

deleteButtons.forEach((deleteButton) => {
    deleteButton.addEventListener("click", async (event) => {
        const element = event.currentTarget;
        const parent = element.closest('.item');
        const billetId = parent.querySelector('.billet-item').dataset.id;

        try {
            const numberContainer = parent.querySelector(".number");
            numberContainer.textContent = '0';

            const response = await fetch(`/modifier_quantite/${billetId}/0`, {
                method: 'GET',
            });

            if (!response.ok) {
                throw new Error('La requête a échoué');
            }

            const data = await response.json();
            console.log(data);
            updateTotalPrice();
        } catch (error) {
            console.error('Erreur de la requête:', error);
        }
    });
});

function updateTotalPrice() {
  let totalAmount = 0;
  const quantityElements = document.querySelectorAll(".number");

  quantityElements.forEach((quantityElement) => {
      const parent = quantityElement.closest('.item');
      const prixElement = parent.querySelector('.valprice');
      const prixUnitaire = parseFloat(prixElement.dataset.prix);
      const quantite = parseFloat(quantityElement.textContent);
      totalAmount += prixUnitaire * quantite;
  });
  totalAmountElement.textContent = "TOTAL : " + totalAmount.toFixed(2) + "€";
}

document.querySelector('.payer-button').addEventListener('click', async () => {
  // Récupérer les données nécessaires
  const billets = document.querySelectorAll('.billet-item');
  const totalAmountElement = document.getElementById('totalAmount');
  
  try {
    const numberContainer = document.querySelector(".number");
    numberContainer.textContent = '0';

    const response = await fetch(`/valider_panier`, {
        method: 'GET',
    });

    if (!response.ok) {
        throw new Error('La requête a échoué');
    }

    const data = await response.json();
    console.log(data);
    } catch (error) {
        console.error('Erreur de la requête:', error);
    }

  // Réinitialise les quantités à zéro et appele la route modifier_quantite
  const billetsArray = [...billets];
  for (const billet of billetsArray) {
    const idBillet = billet.dataset.id;
    const quantite = 0;
    
    try {
      const response = await fetch(`/modifier_quantite/${idBillet}/${quantite}`, {
        method: 'GET',
      });

      if (!response.ok) {
        throw new Error('La requête a échoué');
      }
    } catch (error) {
      console.error('Erreur de la requête:', error);
    }
  }
  // Mettre à jour le prix total dans l'interface
  totalAmountElement.textContent = `TOTAL : 0€`;
  window.location.href = '/panier';
});