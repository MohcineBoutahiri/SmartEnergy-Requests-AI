-- =====================================================
-- BASE DE DONNÉES : Traitement intelligent des demandes
-- =====================================================

-- (Optionnel) Création de la base
-- CREATE DATABASE energie_ia;
-- \c energie_ia;

-- =====================================================
-- TABLE : ROLE
-- =====================================================
CREATE TABLE role (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(50) UNIQUE NOT NULL
);

-- =====================================================
-- TABLE : UTILISATEUR
-- =====================================================
CREATE TABLE utilisateur (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(100),
    email VARCHAR(100) UNIQUE NOT NULL,
    mot_de_passe VARCHAR(255) NOT NULL,
    actif BOOLEAN DEFAULT TRUE,
    role_id INT NOT NULL,
    CONSTRAINT fk_role
        FOREIGN KEY (role_id)
        REFERENCES role(id)
        ON DELETE RESTRICT
);

-- =====================================================
-- TABLE : CLIENT
-- =====================================================
CREATE TABLE client (
    id SERIAL PRIMARY KEY,
    utilisateur_id INT UNIQUE NOT NULL,
    telephone VARCHAR(20),
    adresse TEXT,
    CONSTRAINT fk_client_utilisateur
        FOREIGN KEY (utilisateur_id)
        REFERENCES utilisateur(id)
        ON DELETE CASCADE
);

-- =====================================================
-- TABLE : DEMANDE
-- =====================================================
CREATE TABLE demande (
    id SERIAL PRIMARY KEY,
    client_id INT NOT NULL,
    message TEXT NOT NULL,
    type_demande VARCHAR(50),
    statut VARCHAR(50) DEFAULT 'EN_ATTENTE',
    date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_demande_client
        FOREIGN KEY (client_id)
        REFERENCES client(id)
        ON DELETE CASCADE
);

-- =====================================================
-- TABLE : ANALYSE IA
-- =====================================================
CREATE TABLE analyse_ia (
    id SERIAL PRIMARY KEY,
    demande_id INT UNIQUE NOT NULL,
    intention VARCHAR(50),
    energie VARCHAR(50),
    score_confiance FLOAT CHECK (score_confiance BETWEEN 0 AND 1),
    date_analyse TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_analyse_demande
        FOREIGN KEY (demande_id)
        REFERENCES demande(id)
        ON DELETE CASCADE
);

-- =====================================================
-- TABLE : CONSENTEMENT (RGPD)
-- =====================================================
CREATE TABLE consentement (
    id SERIAL PRIMARY KEY,
    client_id INT UNIQUE NOT NULL,
    accepte BOOLEAN NOT NULL,
    date_consentement TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ip_client VARCHAR(50),
    CONSTRAINT fk_consentement_client
        FOREIGN KEY (client_id)
        REFERENCES client(id)
        ON DELETE CASCADE
);

-- =====================================================
-- TABLE : OFFRE
-- =====================================================
CREATE TABLE offre (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    type_energie VARCHAR(50) NOT NULL,
    prix_kwh NUMERIC(10,4) NOT NULL,
    duree_mois INT NOT NULL,
    actif BOOLEAN DEFAULT TRUE
);

-- =====================================================
-- TABLE : CONTRAT
-- =====================================================
CREATE TABLE contrat (
    id SERIAL PRIMARY KEY,
    reference VARCHAR(50) UNIQUE NOT NULL,
    client_id INT NOT NULL,
    offre_id INT NOT NULL,
    date_debut DATE NOT NULL,
    date_fin DATE NOT NULL,
    statut VARCHAR(50) DEFAULT 'GENERE',
    date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_contrat_client
        FOREIGN KEY (client_id)
        REFERENCES client(id)
        ON DELETE CASCADE,
    CONSTRAINT fk_contrat_offre
        FOREIGN KEY (offre_id)
        REFERENCES offre(id)
        ON DELETE RESTRICT
);

-- =====================================================
-- TABLE : SIGNATURE
-- =====================================================
CREATE TABLE signature (
    id SERIAL PRIMARY KEY,
    contrat_id INT UNIQUE NOT NULL,
    statut VARCHAR(50) DEFAULT 'EN_ATTENTE',
    date_signature TIMESTAMP,
    prestataire VARCHAR(50),
    CONSTRAINT fk_signature_contrat
        FOREIGN KEY (contrat_id)
        REFERENCES contrat(id)
        ON DELETE CASCADE
);

-- =====================================================
-- TABLE : LOG (AUDIT & TRAÇABILITÉ)
-- =====================================================
CREATE TABLE log (
    id SERIAL PRIMARY KEY,
    utilisateur_id INT NOT NULL,
    action TEXT NOT NULL,
    date_action TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_log_utilisateur
        FOREIGN KEY (utilisateur_id)
        REFERENCES utilisateur(id)
        ON DELETE CASCADE
);

-- =====================================================
-- DONNÉES INITIALES (SEED)
-- =====================================================

-- Rôles
INSERT INTO role (nom) VALUES
('CLIENT'),
('AGENT'),
('ADMIN');

-- Offres
INSERT INTO offre (nom, type_energie, prix_kwh, duree_mois) VALUES
('Offre Électricité Standard', 'Electricité', 0.95, 12),
('Offre Gaz Standard', 'Gaz', 0.75, 12),
('Offre Duo Premium', 'Gaz + Electricité', 0.85, 24);

