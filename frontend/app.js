const API_BASE_URL = window.__MARKET_INTELLIGENCE_API__ || 'http://127.0.0.1:8000';

const metrics = {
  activeCompanies: 128,
  responsesCount: '4.8k',
  npsValue: '+42',
  agreementValue: '87%'
};

async function loadDashboard() {
  try {
    const response = await fetch(`${API_BASE_URL}/analytics/dashboard`);
    if (!response.ok) {
      throw new Error('Backend indisponível');
    }

    const data = await response.json();
    metrics.activeCompanies = data.total_usuarios ?? metrics.activeCompanies;
    metrics.responsesCount = `${Math.round((data.taxa_resposta ?? 0.74) * 100)}%`;
    metrics.npsValue = `${Math.round((data.taxa_resposta ?? 0.74) * 100)} pts`;
    metrics.agreementValue = `${Math.round((data.taxa_resposta ?? 0.74) * 100)}%`;
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
}

window.addEventListener('DOMContentLoaded', loadDashboard);
