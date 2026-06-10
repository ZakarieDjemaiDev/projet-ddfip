/* ============================================
   DASHBOARD RH - JAVASCRIPT
   Gestion des interactions et API
   ============================================ */

// ==================== VARIABLES GLOBALES ====================
let agents = [];
let currentPage = 1;
const itemsPerPage = 10;
let editingIndex = null;
let deleteConfirmIndex = null;

// ==================== INITIALISATION ====================
function init() {
    loadAgents();
    setupEventListeners();
}

function setupEventListeners() {
    // Recherche en temps reel
    const searchInput = document.getElementById("searchInput");
    if (searchInput) {
        searchInput.addEventListener("input", filterTable);
    }

    // Filtre par service
    const serviceFilter = document.getElementById("serviceFilter");
    if (serviceFilter) {
        serviceFilter.addEventListener("change", filterTable);
    }

    // Filtre alertes uniquement
    const alertesFilter = document.getElementById("alertesOnlyFilter");
    if (alertesFilter) {
        alertesFilter.addEventListener("change", filterTable);
    }

    // Formulaire d''ajout/modification
    const agentForm = document.getElementById("agentForm");
    if (agentForm) {
        agentForm.addEventListener("submit", handleFormSubmit);
    }

    // Fermer modal si clic en dehors
    const modal = document.getElementById("agentModal");
    if (modal) {
        window.addEventListener("click", function(event) {
            if (event.target === modal) {
                closeModal();
            }
        });
    }
}

// ==================== CHARGEMENT DES DONNEES ====================
function loadAgents() {
    fetch("/api/agents")
        .then(response => response.json())
        .then(data => {
            agents = data;
            displayAgents();
            updateStats();
        })
        .catch(error => {
            console.error("Erreur:", error);
            showNotification("Erreur lors du chargement des donnees", "error");
        });
}

// ==================== AFFICHAGE DU TABLEAU ====================
function displayAgents() {
    const filteredAgents = getFilteredAgents();
    const tableBody = document.getElementById("tableBody");

    if (!tableBody) return;

    tableBody.innerHTML = "";

    const start = (currentPage - 1) * itemsPerPage;
    const paginatedAgents = filteredAgents.slice(start, start + itemsPerPage);

    paginatedAgents.forEach((agent, index) => {
        const row = createTableRow(agent, start + index);
        tableBody.appendChild(row);
    });

    updatePagination(filteredAgents.length);
    updateStats(filteredAgents.length);
}

function createTableRow(agent, originalIndex) {
    const row = document.createElement("tr");
    if (agent.a_alerte) {
        row.classList.add("alert-row");
    }

    const soldeClass = agent.alerte_solde ? "alert-solde" : "";
    const habClass = agent.alerte_habilitation ? "alert-hab" : "";

    const serviceBadgeClass = agent.service
        .toLowerCase()
        .replace(/\s/g, "-")
        .replace(/é/g, "e")
        .replace(/ç/g, "c");

    row.innerHTML = `
        <td><strong>${agent.nom}</strong></td>
        <td>${agent.prénom}</td>
        <td><span class="badge badge-${serviceBadgeClass}">${agent.service}</span></td>
        <td>${agent.grade}</td>
        <td class="text-center">${agent.jours_congés_pris}</td>
        <td class="text-center ${soldeClass}">
            ${agent.solde_congés}
            ${agent.alerte_solde ? '<span class="alert"> !</span>' : ''}
        </td>
        <td><small>${agent.habilitations}</small></td>
        <td class="text-center ${habClass}">
            <small>${agent.date_dernière_habilitation}</small>
        </td>
        <td class="text-center">
            <div class="actions">
                <button class="btn-icon" onclick="openModalEdit(${originalIndex})" title="Modifier">
                    ✏️
                </button>
                <button class="btn-icon delete" onclick="openConfirmDelete(${originalIndex})" title="Supprimer">
                    🗑️
                </button>
            </div>
        </td>
    `;

    return row;
}

// ==================== FILTRAGE ====================
function getFilteredAgents() {
    const searchTerm = document.getElementById("searchInput")?.value.toLowerCase() || "";
    const serviceFilter = document.getElementById("serviceFilter")?.value || "";
    const alertesOnly = document.getElementById("alertesOnlyFilter")?.checked || false;

    return agents.filter(agent => {
        // Recherche par nom/prenom
        const searchMatch = !searchTerm ||
            agent.nom.toLowerCase().includes(searchTerm) ||
            agent.prénom.toLowerCase().includes(searchTerm);

        // Filtre service
        const serviceMatch = !serviceFilter || agent.service === serviceFilter;

        // Filtre alertes
        const alerteMatch = !alertesOnly || agent.a_alerte;

        return searchMatch && serviceMatch && alerteMatch;
    });
}

function filterTable() {
    currentPage = 1;
    displayAgents();
}

// ==================== PAGINATION ====================
function updatePagination(totalItems) {
    const totalPages = Math.ceil(totalItems / itemsPerPage);

    const pageInfo = document.getElementById("pageInfo");
    if (pageInfo) {
        pageInfo.textContent = `Page ${currentPage} / ${totalPages}`;
    }

    const prevBtn = document.getElementById("prevBtn");
    if (prevBtn) {
        prevBtn.disabled = currentPage <= 1;
    }

    const nextBtn = document.getElementById("nextBtn");
    if (nextBtn) {
        nextBtn.disabled = currentPage >= totalPages;
    }
}

function previousPage() {
    if (currentPage > 1) {
        currentPage--;
        displayAgents();
    }
}

function nextPage() {
    const filteredAgents = getFilteredAgents();
    const totalPages = Math.ceil(filteredAgents.length / itemsPerPage);
    if (currentPage < totalPages) {
        currentPage++;
        displayAgents();
    }
}

// ==================== MODALES ====================
function openModalAdd(event) {
    if (event) event.preventDefault();
    editingIndex = null;
    document.getElementById("modalTitle").textContent = "Ajouter un agent";
    document.getElementById("agentForm").reset();
    showModal();
}

function openModalEdit(index) {
    editingIndex = index;
    const agent = agents[index];

    document.getElementById("modalTitle").textContent = "Modifier un agent";
    document.getElementById("formNom").value = agent.nom;
    document.getElementById("formPrenom").value = agent.prénom;
    document.getElementById("formService").value = agent.service;
    document.getElementById("formGrade").value = agent.grade;
    document.getElementById("formJoursConges").value = agent.jours_congés_pris;
    document.getElementById("formSolde").value = agent.solde_congés;
    document.getElementById("formHabilitations").value = agent.habilitations;
    document.getElementById("formDateHab").value = agent.date_dernière_habilitation;

    showModal();
}

function showModal() {
    const modal = document.getElementById("agentModal");
    if (modal) {
        modal.classList.add("show");
    }
}

function closeModal() {
    const modal = document.getElementById("agentModal");
    if (modal) {
        modal.classList.remove("show");
    }
    editingIndex = null;
}

function showConfirmModal(message) {
    const confirmModal = document.getElementById("confirmModal");
    const confirmMessage = document.getElementById("confirmMessage");
    if (confirmMessage) {
        confirmMessage.textContent = message;
    }
    if (confirmModal) {
        confirmModal.classList.add("show");
    }
}

function closeConfirmModal() {
    const confirmModal = document.getElementById("confirmModal");
    if (confirmModal) {
        confirmModal.classList.remove("show");
    }
    deleteConfirmIndex = null;
}

// ==================== FORMULAIRE ====================
function handleFormSubmit(event) {
    event.preventDefault();

    const donnees = {
        nom: document.getElementById("formNom").value.trim(),
        prénom: document.getElementById("formPrenom").value.trim(),
        service: document.getElementById("formService").value,
        grade: document.getElementById("formGrade").value,
        jours_congés_pris: document.getElementById("formJoursConges").value || "0",
        solde_congés: document.getElementById("formSolde").value || "0",
        habilitations: document.getElementById("formHabilitations").value.trim(),
        date_dernière_habilitation: document.getElementById("formDateHab").value.trim()
    };

    // Validation
    if (!donnees.nom || !donnees.prénom || !donnees.service || !donnees.grade) {
        showNotification("Veuillez remplir tous les champs obligatoires", "warning");
        return;
    }

    if (editingIndex !== null) {
        updateAgent(editingIndex, donnees);
    } else {
        addAgent(donnees);
    }
}

function addAgent(donnees) {
    fetch("/api/agent/add", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(donnees)
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            agents = data.agents;
            closeModal();
            displayAgents();
            showNotification(data.message, "success");
        } else {
            showNotification(data.message, "error");
        }
    })
    .catch(error => {
        console.error("Erreur:", error);
        showNotification("Erreur lors de l''ajout", "error");
    });
}

function updateAgent(index, donnees) {
    fetch(`/api/agent/update/${index}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(donnees)
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            agents = data.agents;
            closeModal();
            displayAgents();
            showNotification(data.message, "success");
        } else {
            showNotification(data.message, "error");
        }
    })
    .catch(error => {
        console.error("Erreur:", error);
        showNotification("Erreur lors de la modification", "error");
    });
}

// ==================== SUPPRESSION ====================
function openConfirmDelete(index) {
    deleteConfirmIndex = index;
    const agent = agents[index];
    showConfirmModal(`Voulez-vous supprimer ${agent.prénom} ${agent.nom} ?`);
}

function confirmDelete() {
    if (deleteConfirmIndex === null) return;

    fetch(`/api/agent/delete/${deleteConfirmIndex}`, { method: "DELETE" })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                agents = data.agents;
                closeConfirmModal();
                currentPage = 1;
                displayAgents();
                showNotification(data.message, "success");
            } else {
                showNotification(data.message, "error");
            }
        })
        .catch(error => {
            console.error("Erreur:", error);
            showNotification("Erreur lors de la suppression", "error");
        });
}

// ==================== EXPORT ====================
function exportCSV() {
    const filteredAgents = getFilteredAgents();

    if (filteredAgents.length === 0) {
        showNotification("Aucun donnee a exporter", "warning");
        return;
    }

    const entetes = ["nom", "prénom", "service", "grade", "jours_congés_pris", "solde_congés", "habilitations", "date_dernière_habilitation"];
    let csv = entetes.join(",") + "\n";

    filteredAgents.forEach(agent => {
        const row = [
            agent.nom,
            agent.prénom,
            agent.service,
            agent.grade,
            agent.jours_congés_pris,
            agent.solde_congés,
            `"${agent.habilitations}"`,
            agent.date_dernière_habilitation
        ];
        csv += row.join(",") + "\n";
    });

    const blob = new Blob([csv], { type: "text/csv;charset=utf-8;" });
    const link = document.createElement("a");
    const url = URL.createObjectURL(blob);

    link.setAttribute("href", url);
    link.setAttribute("download", `agents_${new Date().toISOString().split("T")[0]}.csv`);
    link.style.visibility = "hidden";
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);

    showNotification("Export CSV reussi", "success");
}

// ==================== STATISTIQUES ====================
function updateStats(totalVisible) {
    const agentCount = document.getElementById("agentCount");
    if (agentCount) {
        agentCount.textContent = `${totalVisible || agents.length} agent${totalVisible !== 1 ? "s" : ""}`;
    }
}

// ==================== GRAPHIQUES ====================
function initCharts() {
    console.log("[initCharts] Starting...");

    if (typeof Chart === "undefined") {
        console.error("[initCharts] Chart.js not loaded!");
        return;
    }

    // Utiliser les variables globales statsServices et repartitionServices
    console.log("[initCharts] statsServices:", statsServices);
    console.log("[initCharts] repartitionServices:", repartitionServices);

    // Graphique barres : Congés par service
    const canvasConges = document.getElementById("chartConges");
    console.log("[initCharts] Canvas Conges found:", !!canvasConges);

    if (canvasConges && statsServices && Object.keys(statsServices).length > 0) {
        try {
            const ctxConges = canvasConges.getContext("2d");
            const labelsConges = Object.keys(statsServices);
            const dataConges = Object.values(statsServices);

            console.log("[initCharts] Creating bar chart - Labels:", labelsConges, "Data:", dataConges);

            new Chart(ctxConges, {
                type: "bar",
                data: {
                    labels: labelsConges,
                    datasets: [{
                        label: "Moyenne de conges pris (jours)",
                        data: dataConges,
                        backgroundColor: "#2563eb",
                        borderColor: "#1d4ed8",
                        borderWidth: 2,
                        borderRadius: 6,
                        borderSkipped: false
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    indexAxis: undefined,
                    plugins: {
                        legend: {
                            display: true,
                            position: "top"
                        },
                        title: {
                            display: false
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: true,
                            max: 30,
                            ticks: {
                                callback: function(value) {
                                    return value + " j";
                                }
                            }
                        }
                    }
                }
            });
            console.log("[initCharts] Bar chart created successfully!");
        } catch(e) {
            console.error("[initCharts] Error creating bar chart:", e);
        }
    } else {
        console.warn("[initCharts] Missing canvas or data for bar chart");
    }

    // Graphique donut : Répartition par service
    const canvasRepartition = document.getElementById("chartRepartition");
    console.log("[initCharts] Canvas Repartition found:", !!canvasRepartition);

    if (canvasRepartition && repartitionServices && Object.keys(repartitionServices).length > 0) {
        try {
            const ctxRepartition = canvasRepartition.getContext("2d");
            const labelsRepartition = Object.keys(repartitionServices);
            const dataRepartition = Object.values(repartitionServices);

            console.log("[initCharts] Creating donut chart - Labels:", labelsRepartition, "Data:", dataRepartition);

            new Chart(ctxRepartition, {
                type: "doughnut",
                data: {
                    labels: labelsRepartition,
                    datasets: [{
                        data: dataRepartition,
                        backgroundColor: [
                            "#1e40af",
                            "#15803d",
                            "#be185d",
                            "#92400e",
                            "#5b21b6",
                            "#0369a1",
                            "#7c2d12"
                        ],
                        borderColor: "white",
                        borderWidth: 2
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            position: "right",
                            labels: {
                                padding: 15
                            }
                        }
                    }
                }
            });
            console.log("[initCharts] Donut chart created successfully!");
        } catch(e) {
            console.error("[initCharts] Error creating donut chart:", e);
        }
    } else {
        console.warn("[initCharts] Missing canvas or data for donut chart");
    }

    console.log("[initCharts] Completed!");
}

// ==================== NAVIGATION ====================
function switchTab(event, tabName) {
    event.preventDefault();

    // Cacher tous les onglets
    document.querySelectorAll(".tab-content").forEach(tab => {
        tab.classList.remove("active");
    });

    // Masquer les nav items actifs
    document.querySelectorAll(".nav-item").forEach(item => {
        item.classList.remove("active");
    });

    // Afficher le nouvel onglet
    const tab = document.getElementById(tabName + "-tab");
    if (tab) {
        tab.classList.add("active");
    }

    // Activer le nav item
    event.target.closest(".nav-item").classList.add("active");
}

// ==================== NOTIFICATIONS ====================
function showNotification(message, type = "success") {
    const notification = document.getElementById("notification");
    if (!notification) return;

    notification.textContent = message;
    notification.className = "notification show " + type;

    setTimeout(() => {
        notification.classList.remove("show");
    }, 3000);
}

// ==================== DEMARRAGE ====================
document.addEventListener("DOMContentLoaded", init);
