const API_BASE_URL = window.__MARKET_INTELLIGENCE_API__ || 'http://127.0.0.1:8000';

const metrics = {
  activeCompanies: 128,
  responsesCount: '4.8k',
  npsValue: '+42',
  agreementValue: '87%'
};

const surveyRows = [
  ['Retail Pulse', 'Varejo', 'Ativa'],
  ['Fintech Score', 'Financeiro', 'Coletando'],
  ['Health Monitor', 'Saúde', 'Pendente']
];

async function loadDashboard() {
  try {
    const response = await fetch(`${API_BASE_URL}/analytics/dashboard`);
    if (!response.ok) throw new Error('Backend indisponível');

    const data = await response.json();
    metrics.activeCompanies = data.total_usuarios ?? metrics.activeCompanies;
    metrics.responsesCount = `${Math.round((data.taxa_resposta ?? 0.74) * 100)}%`;
    metrics.npsValue = `${Math.round((data.taxa_resposta ?? 0.74) * 100)} pts`;
    metrics.agreementValue = `${Math.round((data.taxa_resposta ?? 0.74) * 100)}%`;

    document.getElementById('segmentList').textContent = (data.segmentos ?? ['Tech', 'Financeiro', 'Varejo']).join(', ');
  } catch (error) {
    console.warn('Usando fallback local porque o backend ainda não está disponível:', error.message);
  }

  renderDashboard();
}

function renderDashboard() {
  document.getElementById('activeCompanies').textContent = metrics.activeCompanies;
  document.getElementById('responsesCount').textContent = metrics.responsesCount;
  document.getElementById('npsValue').textContent = metrics.npsValue;
  document.getElementById('agreementValue').textContent = metrics.agreementValue;

  const tbody = document.getElementById('surveyTableBody');
  tbody.innerHTML = surveyRows
    .map(([name, sector, status]) => {
      const pillClass = status === 'Ativa' ? 'ok' : status === 'Coletando' ? 'process' : 'warn';
      return `
        <tr>
          <td>${name}</td>
          <td>${sector}</td>
          <td><span class="pill ${pillClass}">${status}</span></td>
        </tr>
      `;
    })
    .join('');
}

function setView(viewName) {
  document.querySelectorAll('.nav-btn').forEach((button) => {
    button.classList.toggle('active', button.dataset.view === viewName);
  });

  document.querySelectorAll('.view').forEach((view) => {
    view.classList.toggle('active', view.id === `${viewName}View`);
  });

  const titles = {
    dashboard: 'Dashboard',
    companies: 'Empresas',
    surveys: 'Pesquisas',
    rewards: 'Recompensas',
    analytics: 'Analytics'
  };

  document.getElementById('viewTitle').textContent = titles[viewName] || 'Dashboard';
}

function bindActions() {
  document.querySelectorAll('.nav-btn').forEach((button) => {
    button.addEventListener('click', () => setView(button.dataset.view));
  });

  document.getElementById('newSurveyButton').addEventListener('click', () => {
    setView('surveys');
  });

  document.getElementById('companyForm').addEventListener('submit', (event) => {
    event.preventDefault();
    const formData = new FormData(event.currentTarget);
    const nome = formData.get('nome');
    document.getElementById('companyMessage').textContent = `Empresa ${nome} cadastrada com sucesso.`;
    event.currentTarget.reset();
  });

  document.getElementById('surveyForm').addEventListener('submit', (event) => {
    event.preventDefault();
    const formData = new FormData(event.currentTarget);
    const titulo = formData.get('titulo');
    surveyRows.unshift([titulo || 'Pesquisa nova', 'Canal digital', 'Ativa']);
    renderDashboard();
    document.getElementById('surveyMessage').textContent = `Pesquisa "${titulo}" criada.`;
    event.currentTarget.reset();
    setView('dashboard');
  });

  document.getElementById('rewardButton').addEventListener('click', () => {
    document.getElementById('rewardMessage').textContent = '20 pontos concedidos com sucesso.';
  });
}

window.addEventListener('DOMContentLoaded', () => {
  bindActions();
  loadDashboard();
});
