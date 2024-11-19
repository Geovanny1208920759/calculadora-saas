document.getElementById('calcular').addEventListener('click', () => {
    const num1 = parseFloat(document.getElementById('num1').value);
    const num2 = parseFloat(document.getElementById('num2').value);
    const operacion = document.getElementById('operacion').value;

    fetch('http://127.0.0.1:3000/calcular', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ num1, num2, operacion }),
    })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                document.getElementById('resultado').textContent = `Error: ${data.error}`;
            } else {
                document.getElementById('resultado').textContent = `Resultado: ${data.resultado}`;
            }
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('resultado').textContent = 'Error en la conexión con el servidor.';
        });
});
