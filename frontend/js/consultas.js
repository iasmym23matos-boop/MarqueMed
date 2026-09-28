// Dados das consultas (simulando a resposta do seu arquivo consultas.json)
const consultasDados = [
    { data: "2026-10-01", especialidade: "Cardiologia", medico: "Dr. Arnaldo Silva", unidade: "Centro" },
    { data: "2026-10-15", especialidade: "Pediatria", medico: "Dra. Beatriz Santos", unidade: "Zona Sul" },
    { data: "2026-11-03", especialidade: "Ortopedia", medico: "Dr. Carlos Oliveira", unidade: "Centro" },
    { data: "2026-11-20", especialidade: "Dermatologia", medico: "Dra. Daniela Lima", unidade: "Zona Norte" },
    { data: "2026-12-05", especialidade: "Ginecologia", medico: "Dra. Elaine Costa", unidade: "Zona Sul" },
    { data: "2026-12-18", especialidade: "Clínica Médica", medico: "Dr. Fernando Sousa", unidade: "Centro" },
    { data: "2027-01-10", especialidade: "Neurologia", medico: "Dra. Geovana Melo", unidade: "Zona Norte" },
    { data: "2027-01-25", especialidade: "Cardiologia", medico: "Dr. Arnaldo Silva", unidade: "Zona Sul" }
];

const nomesMeses = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
];

function formatarDataBR(dataString) {
    const [ano, mes, dia] = dataString.split('-');
    return `${dia}/${mes}/${ano}`;
}

function renderizarCalendario() {
    const container = document.getElementById("calendario-container");
    container.innerHTML = ""; // Limpa o container antes de renderizar

    // Agrupar as consultas por Ano e Mês
    const grupos = {};

    consultasDados.forEach(consulta => {
        const dataObj = new Date(consulta.data + 'T00:00:00');
        const ano = dataObj.getFullYear();
        const mesIndex = dataObj.getMonth();
        const chaveGrupo = `${ano}-${mesIndex}`;

        if (!grupos[chaveGrupo]) {
            grupos[chaveGrupo] = {
                ano: ano,
                mesNome: nomesMeses[mesIndex],
                mesIndex: mesIndex,
                consultas: []
            };
        }
        grupos[chaveGrupo].consultas.push(consulta);
    });

    // Ordenar as chaves de ano/mês de forma cronológica
    const chavesOrdenadas = Object.keys(grupos).sort();

    // Renderizar cada mês na tela
    chavesOrdenadas.forEach(chave => {
        const grupo = grupos[chave];

        // Criar o bloco do Mês
        const cardMes = document.createElement("div");
        cardMes.className = "card-mes";
        cardMes.style.cssText = "background: #fff; border-radius: 8px; padding: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.05); margin-bottom: 25px;";

        const tituloMes = document.createElement("h3");
        tituloMes.innerText = `${grupo.mesNome} ${grupo.ano}`;
        tituloMes.style.cssText = "margin-top: 0; color: #1a73e8; border-bottom: 2px solid #e8f0fe; padding-bottom: 8px; font-weight: 600;";
        cardMes.appendChild(tituloMes);

        // Criar a lista de consultas daquele mês
        const listaConsultas = document.createElement("div");
        listaConsultas.className = "lista-consultas-mes";

        grupo.consultas.forEach(c => {
            const item = document.createElement("div");
            item.style.cssText = "padding: 12px; border-bottom: 1px solid #f1f3f4; display: flex; justify-content: space-between; align-items: center; font-size: 14px;";
            
            item.innerHTML = `
                <div>
                    <span style="background: #e8f0fe; color: #1a73e8; padding: 4px 8px; border-radius: 4px; font-weight: bold; margin-right: 10px;">
                        ${formatarDataBR(c.data).substring(0, 5)}
                    </span>
                    <strong>${c.especialidade}</strong> - ${c.medico}
                </div>
                <span style="color: #5f6368; font-size: 12px;">📍 Unidade: ${c.unidade}</span>
            `;
            listaConsultas.appendChild(item);
        });

        cardMes.appendChild(listaConsultas);
        container.appendChild(cardMes);
    });
}

// Executa a função assim que a página terminar de carregar
document.addEventListener("DOMContentLoaded", renderizarCalendario);
