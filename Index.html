<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ZafiroX - Recompensas y Juegos Reales</title>
    <style>
        :root {
            --bg-color: #0f172a;
            --card-bg: #1e293b;
            --accent: #8b5cf6;
            --accent-hover: #7c3aed;
            --text-color: #f8fafc;
            --text-muted: #94a3b8;
            --success: #10b981;
            --danger: #ef4444;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: var(--bg-color);
            color: var(--text-color);
            padding-bottom: 70px;
        }

        header {
            background: linear-gradient(135deg, #1e293b, #0f172a);
            padding: 20px;
            text-align: center;
            border-bottom: 2px solid var(--accent);
        }

        header h1 {
            font-size: 1.8rem;
            color: #c084fc;
        }

        .balance-container {
            display: flex;
            justify-content: space-around;
            background: var(--card-bg);
            margin: 15px;
            padding: 12px;
            border-radius: 12px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        }

        .balance-item {
            text-align: center;
        }

        .balance-item span {
            font-size: 0.85rem;
            color: var(--text-muted);
        }

        .balance-item h3 {
            font-size: 1.1rem;
            color: var(--success);
        }

        .container {
            padding: 15px;
            max-width: 600px;
            margin: 0 auto;
        }

        .section {
            display: none;
        }

        .section.active {
            display: block;
        }

        .card {
            background: var(--card-bg);
            padding: 20px;
            border-radius: 12px;
            margin-bottom: 15px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        }

        h2 {
            font-size: 1.3rem;
            margin-bottom: 10px;
        }

        p {
            color: var(--text-muted);
            font-size: 0.95rem;
            margin-bottom: 15px;
        }

        button {
            background: var(--accent);
            color: white;
            border: none;
            padding: 12px 20px;
            border-radius: 8px;
            font-size: 1rem;
            font-weight: bold;
            cursor: pointer;
            width: 100%;
            transition: background 0.3s;
        }

        button:hover {
            background: var(--accent-hover);
        }

        select, input {
            width: 100%;
            padding: 12px;
            background: #0f172a;
            border: 1px solid #334155;
            color: white;
            border-radius: 8px;
            margin-bottom: 15px;
            font-size: 1rem;
        }

        /* Barra de navegación inferior tipo App Nativa */
        nav {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background: #090d16;
            display: flex;
            justify-content: space-around;
            padding: 10px 0;
            border-top: 1px solid #1e293b;
            z-index: 1000;
        }

        nav button {
            background: transparent;
            color: var(--text-muted);
            font-size: 0.75rem;
            border: none;
            padding: 5px;
            cursor: pointer;
        }

        nav button.active {
            color: #c084fc;
        }

        .history-item {
            background: #0f172a;
            padding: 10px;
            border-radius: 6px;
            margin-bottom: 8px;
            font-size: 0.85rem;
            border-left: 4px solid var(--accent);
        }
    </style>
</head>
<body>

    <header>
        <h1>💎 ZafiroX Web Real</h1>
    </header>

    <!-- BARRA DE SALDO SUPERIOR -->
    <div class="balance-container">
        <div class="balance-item">
            <span>Monedas</span>
            <h3 id="lbl-coins">1,000</h3>
        </div>
        <div class="balance-item">
            <span>Gemas</span>
            <h3 id="lbl-gems" style="color: #c084fc;">50</h3>
        </div>
        <div class="balance-item">
            <span>Racha</span>
            <h3 id="lbl-streak" style="color: #f59e0b;">1 Día</h3>
        </div>
    </div>

    <div class="container">

        <!-- SECCIÓN 1: INICIO (MINIJUEGOS) -->
        <div id="sec-inicio" class="section active">
            <div class="card">
                <h2>🎮 Trivia Zafiro Interactiva</h2>
                <p>¿En qué lenguaje está programada la web moderna de ZafiroX?</p>
                <select id="trivia-resp">
                    <option value="python">Python</option>
                    <option value="javascript">JavaScript / HTML5</option>
                    <option value="cplusplus">C++</option>
                </select>
                <button onclick="jugarTrivia()">Enviar Respuesta (+200 Monedas)</button>
            </div>

            <div class="card">
                <h2>🎡 Ruleta de la Suerte Diaria</h2>
                <p>Gira la ruleta y prueba tu suerte de forma aleatoria.</p>
                <button onclick="girarRuleta()" style="background: #f59e0b;">Girar Ruleta (Costo: 50 Monedas)</button>
            </div>
        </div>

        <!-- SECCIÓN 2: DESAFÍOS -->
        <div id="sec-desafios" class="section">
            <div class="card">
                <h2>⚔️ Desafíos Activos</h2>
                <p>Completa 5 niveles en Merge Blast para reclamar recompensa.</p>
                <p>Progreso actual: <strong>3 / 5</strong></p>
                <button onclick="completarDesafio()">Simular Progreso de Nivel (+150 Monedas)</button>
            </div>
        </div>

        <!-- SECCIÓN 3: CARRUSEL -->
        <div id="sec-carrusel" class="section">
            <div class="card">
                <h2>🎠 Carrusel Sorpresa</h2>
                <p>Abre el cofre oculto disponible cada 24 horas.</p>
                <button onclick="abrirCofre()">Abrir Cofre Diario (+300 Monedas)</button>
            </div>
        </div>

        <!-- SECCIÓN 4: EVENTOS -->
        <div id="sec-eventos" class="section">
            <div class="card">
                <h2>🎒 Weekly Pot - $1,000 USD</h2>
                <p>Participa en el pozo semanal acumulando gemas.</p>
                <button onclick="reclamarGemas()">Reclamar Bono de Gemas (+50 Gemas)</button>
            </div>
        </div>

        <!-- SECCIÓN 5: RECOMPENSAS -->
        <div id="sec-recompensas" class="section">
            <div class="card">
                <h2>🔥 Bono de Racha Diaria</h2>
                <p>Mantén tu constancia diaria activa.</p>
                <button onclick="reclamarRacha()" style="background: var(--success);">Reclamar Bono Diario (+500 Monedas)</button>
            </div>
        </div>

        <!-- SECCIÓN 6: BILLETERA & RETIROS -->
        <div id="sec-billetera" class="section">
            <div class="card">
                <h2>💳 Billetera & Retiros Reales</h2>
                <p id="lbl-usd">Equivalente USD: $0.10 USD</p>
                
                <label>Método de Pago:</label>
                <select id="metodo-retiro">
                    <option value="Nequi">Nequi</option>
                    <option value="Daviplata">Daviplata</option>
                    <option value="PayPal">PayPal</option>
                </select>

                <label>Número / Cuenta / Correo:</label>
                <input type="text" id="input-cuenta" placeholder="Ej: 3185312231">

                <label>Monto a Retirar (USD):</label>
                <input type="number" id="input-monto" min="0.1" step="0.1" value="1.0">

                <button onclick="solicitarRetiro()">🚀 Confirmar Retiro</button>
            </div>

            <div class="card">
                <h2>📋 Historial de Transacciones</h2>
                <div id="historial-container">
                    <p>Aún no hay transacciones registradas.</p>
                </div>
            </div>
        </div>

    </div>

    <!-- MENÚ DE NAVEGACIÓN INFERIOR -->
    <nav>
        <button onclick="cambiarSeccion('inicio', this)" class="active">🏠<br>Inicio</button>
        <button onclick="cambiarSeccion('desafios', this)">⚔️<br>Desafíos</button>
        <button onclick="cambiarSeccion('carrusel', this)">🎠<br>Carrusel</button>
        <button onclick="cambiarSeccion('eventos', this)">🎯<br>Eventos</button>
        <button onclick="cambiarSeccion('recompensas', this)">🔥<br>Recompensas</button>
        <button onclick="cambiarSeccion('billetera', this)">💰<br>Billetera</button>
    </nav>

    <script>
        // ESTADO DE LA APLICACIÓN (Cargado desde LocalStorage)
        let usuario = JSON.parse(localStorage.getItem('zafirox_user')) || {
            coins: 1000,
            gems: 50,
            streak: 1,
            historial: []
        };

        function actualizarInterfaz() {
            document.getElementById('lbl-coins').innerText = usuario.coins.toLocaleString();
            document.getElementById('lbl-gems').innerText = usuario.gems;
            document.getElementById('lbl-streak').innerText = usuario.streak + ' Días';
            
            let usd = usuario.coins / 10000.0;
            document.getElementById('lbl-usd').innerText = `Equivalente USD: $${usd.toFixed(2)} USD`;

            // Guardar en persistencia local
            localStorage.setItem('zafirox_user', JSON.stringify(usuario));

            // Renderizar Historial
            let histContainer = document.getElementById('historial-container');
            if (usuario.historial.length > 0) {
                histContainer.innerHTML = usuario.historial.map(h => `
                    <div class="history-item">
                        📅 <strong>${h.fecha}</strong> | ${h.metodo} (${h.cuenta})<br>
                        Monto: <strong>$${h.monto} USD</strong> - Estado: <span style="color:var(--success)">${h.estado}</span>
                    </div>
                `).join('');
            }
        }

        function cambiarSeccion(secId, btn) {
            document.querySelectorAll('.section').forEach(s => s.classList.remove('active'));
            document.getElementById('sec-' + secId).classList.add('active');

            document.querySelectorAll('nav button').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
        }

        // LÓGICA DE MINIJUEGOS Y RECOMPENSAS
        function jugarTrivia() {
            let resp = document.getElementById('trivia-resp').value;
            if (resp === 'javascript') {
                usuario.coins += 200;
                usuario.gems += 5;
                alert('¡Correcto! Ganaste 200 monedas y 5 gemas.');
            } else {
                usuario.coins = Math.max(0, usuario.coins - 50);
                alert('Incorrecto. Perdiste 50 monedas.');
            }
            actualizarInterfaz();
        }

        function girarRuleta() {
            if (usuario.coins < 50) {
                alert('No tienes suficientes monedas para girar.');
                return;
            }
            usuario.coins -= 50;
            let premios = [100, 250, 500, 1000, 0];
            let premio = premios[Math.floor(Math.random() * premios.length)];
            usuario.coins += premio;
            alert(`¡La ruleta giró! Ganaste ${premio} monedas.`);
            actualizarInterfaz();
        }

        function completarDesafio() {
            usuario.coins += 150;
            usuario.gems += 10;
            alert('¡Progreso completado! +150 Monedas y +10 Gemas.');
            actualizarInterfaz();
        }

        function abrirCofre() {
            usuario.coins += 300;
            alert('¡Cofre abierto con éxito! +300 Monedas.');
            actualizarInterfaz();
        }

        function reclamarGemas() {
            usuario.gems += 50;
            alert('¡Gemas añadidas a tu cuenta semanal!');
            actualizarInterfaz();
        }

        function reclamarRacha() {
            usuario.coins += 500;
            usuario.streak += 1;
            alert('¡Bono de racha reclamado con éxito!');
            actualizarInterfaz();
        }

        function solicitarRetiro() {
            let metodo = document.getElementById('metodo-retiro').value;
            let cuenta = document.getElementById('input-cuenta').value;
            let monto = parseFloat(document.getElementById('input-monto').value);
            let monedasNecesarias = monto * 10000;

            if (!cuenta) {
                alert('Por favor ingresa una cuenta o número de destino válido.');
                return;
            }

            if (usuario.coins < monedasNecesarias) {
                alert('No tienes suficientes monedas para este monto de retiro.');
                return;
            }

            usuario.coins -= monedasNecesarias;
            usuario.historial.unshift({
                fecha: new Date().toLocaleDateString(),
                metodo: metodo,
                cuenta: cuenta,
                monto: monto,
                estado: 'Procesado'
            });

            alert(`¡Solicitud de retiro por $${monto} USD enviada a ${metodo}!`);
            actualizarInterfaz();
        }

        // Inicializar datos al cargar la página
        actualizarInterfaz();
    </script>
</body>
</html>
