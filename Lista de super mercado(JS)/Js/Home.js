function mascaraMoeda(event) {
  const onlyDigits = event.target.value
    .split("")
    .filter(s => /\d/.test(s))
    .join("")
    .padStart(3, "0")
  const digitsFloat = onlyDigits.slice(0, -2) + "." + onlyDigits.slice(-2)
  event.target.value = maskCurrency(digitsFloat)
}

function maskCurrency(valor, locale = 'pt-BR', currency = 'BRL') {
  return new Intl.NumberFormat(locale, {
    style: 'currency',
    currency
  }).format(valor)
}

var items = [];

document.querySelector('input[type=submit]')
  .addEventListener('click', () => {
    var nome = document.querySelector('input[name=nome]');
    var valore = document.querySelector('input[name=valor]');
    var valor = valore.value.replace('R$',' ').replace('.', '').replace(',', '.');
    if (valor.value == false || nome.value == false) {
      alert('É nessesario informar o nome e o valor do produto.')
    } else {
      items.push({
        nome: nome.value,
        valor: parseFloat(valor).toFixed(2),

      });
      
      let lista = document.querySelector('.lista')
      let somar = 0
      lista.innerHTML = '';
      items.map(function (val) {
        somar += parseFloat(val.valor);
        lista.innerHTML += `
                <div class="listados">
                    <h3>${val.nome}</h3>
                    <h3 class="preco"><span>R$ ${val.valor.replace('.', ',')}</span></h3>
                `
      })
      somar = somar.toFixed(2);
      nome.value = '';
      valore.value = '';
      

      let pegarSoma = document.querySelector('.soma h1')
      pegarSoma.innerHTML = '';
      pegarSoma.innerHTML += 'TOTAL: R$ ' + somar.replace('.',',');

    }

  });

  