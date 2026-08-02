const metrics = {
  activeCompanies: 128,
  responsesCount: '4.8k',
  npsValue: '+42',
  agreementValue: '87%'
};

function renderDashboard() {
  document.getElementById('activeCompanies').textContent = metrics.activeCompanies;
  document.getElementById('responsesCount').textContent = metrics.responsesCount;
  document.getElementById('npsValue').textContent = metrics.npsValue;
  document.getElementById('agreementValue').textContent = metrics.agreementValue;
}

window.addEventListener('DOMContentLoaded', renderDashboard);
