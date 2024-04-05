function movimentar() {
    var x;
    var y;
    var z; 

    while (true) {
        x = prompt("Digite o valor de x: ");
        y = prompt("Digite o valor de y: ");
        z = prompt("Digite o valor de z: ");

        if (x === null || y === null || z === null) {
            return; 
        }

        if (x === "" || y === "" || z === "") {
            alert("Você não preencheu todos os campos!");
            continue;
        }

        if (isNaN(x) || isNaN(y) || isNaN(z)) {
            alert("Você não digitou um número!");
            return;
        }        

        break;
    }

    var dados = {
        x: x,
        y: y,
        z: z
    };

    fetch('/movimentar', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(dados),
    })
    .then(response => response.text())
    .then(data => {
        console.log(data);
        alert("movimentado com sucesso!")
    })
    .catch(error => {
        console.error('Erro:', error);
    });
}

function ligarAtuador() {
    var data = {
        ligar: 1
    }

    fetch('/ligar-ferramenta', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.text())
    .then(data => {
        console.log(data);
        alert("atuador ligado com sucesso!")
    })
    .catch(error => {
        console.error('Erro:', error);
    });
}

function desligarAtuador() {
    var data = {
        desligar: 1
    }

    fetch('/desligar-ferramenta', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.text())
    .then(data => {
        console.log(data);
        alert("atuador desligado com sucesso!")
    })
    .catch(error => {
        console.error('Erro:', error);
    });
}

function home(){
    var data = {
        voltar: 1
    }

    fetch('/home', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.text())
    .then(data => {
        console.log(data);
        alert("voltando para home!")
    })
    .catch(error => {
        console.error('Erro:', error);
    });
}

function logs () {
    console.log("Logs");
}