var game = document.querySelectorAll('.jogada div > img');
var playJs = document.querySelectorAll('.joga-java div > img')
var jogador = 0
var js = 0
var impates = 0
var total = 0

function resetAdiver() {
  for (var i = 0; i < playJs.length; i++) {
    playJs[i].style.opacity = 0.2;
  }
}

function Inimigo() {
  let rand = Math.floor(Math.random() * 3);

  for (var i = 0; i < playJs.length; i++) {
    if (i == rand) {
      resetAdiver();
      playJs[i].style.opacity = 1;
      inimi = playJs[i].getAttribute('opt');
      ;
    }
  }
}

function reset() {
  for (var i = 0; i < game.length; i++) {
    game[i].style.opacity = 0.2;
  }
}

function definir() {
  if (play == 'papel' && inimi == 'pedra' || play == 'pedra' && inimi == 'tesoura' || play == 'tesoura' && inimi == 'papel') {
    jogador += 1
    total += 1
    var informar = document.querySelector('.resultado')
    informar.innerHTML = `
    <h1>!!!PARABENS!!!</h1>
    <h1>VOCÊ GANHOU!!!</h1>
    <h2>Você = ${jogador}</h2>
        <h2>Adiversario = ${js}</h2>
        <h2>Impates = ${impates}</h2>
        <h2>Total de jogadas = ${total}</h2>
    `
    
  } if (inimi == 'papel' && play == 'pedra' || inimi == 'pedra' && play == 'tesoura' || inimi == 'tesoura' && play == 'papel') {
    js += 1
    total += 1
    var informar = document.querySelector('.resultado')
    informar.innerHTML = `
    <h1>AHH QUE PENA </h1>
    <h1>VOCÊ PERDEU =( </h1>
    <h2>Você = ${jogador}</h2>
    <h2>Adiversario = ${js}</h2>
    <h2>Impates = ${impates}</h2>
    <h2>Total de jogadas = ${total}</h2>
    `
  } if (inimi == play) {
    impates += 1
    total += 1
    var informar = document.querySelector('.resultado')
    informar.innerHTML = `
    <h1>!!!IMPATE!!!</h1>
    <h2>Você = ${jogador}</h2>
    <h2>Adiversario = ${js}</h2>
    <h2>Impates = ${impates}</h2>
    <h2>Total de jogadas = ${total}</h2>
    `
    
  }
}

for (var i = 0; i < game.length; i++) {
  game[i].addEventListener('click', function (t) {
    reset();
    t.target.style.opacity = 1;
    play = t.target.getAttribute('opt');
    Inimigo();
    definir();
    numeros();
  })
}

