<script>
    var ctx = document.getElementById('vibracionesChart').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'doughnut', // Tipo de gráfico circular
        data: {
            labels: ['Vibraciones Normales', 'Vibraciones Anormales'],
            datasets: [{
                data: [50, 50], // Porcentaje de cada categoría (ajusta según tus datos)
                backgroundColor: ['#36A2EB', '#FFCE56'], // Colores de las categorías
            }],
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
        }
    });
</script>