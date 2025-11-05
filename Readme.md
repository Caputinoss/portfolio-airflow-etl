# 🧠 Portfolio – ETL de Dados da Lei Rouanet com Airflow & Arquitetura Medalhão  

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)  
[![Airflow](https://img.shields.io/badge/Airflow-3.x-orange.svg)](https://airflow.apache.org/)  
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16+-blue.svg)](https://www.postgresql.org/)  

---

## ✨ Visão Geral  

Este projeto implementa um pipeline completo de **engenharia de dados** para a extração, transformação e carga dos dados públicos da Lei Rouanet (via API **VERSALIC**) em um banco PostgreSQL, orquestrado pelo **Apache Airflow** em ambiente Docker.  

É um projeto voltado para portfólio profissional, demonstrando:  
- Extração de dados via API REST  
- Arquitetura **Medalhão (Bronze → Silver → Gold)**  
- Orquestração com Airflow (observabilidade, retries e logs)  
- Modularização (`extract`, `transform`, `load`)  
- Infraestrutura containerizada e reprodutível  

---

## 🏗 Arquitetura da Solução  

### Fluxo Geral  

```mermaid
flowchart LR
    A[Fonte: API VERSALIC]-->B[Camada Bronze -- dados brutos em JSON]
    B-->C[Camada Silver -- dados tratados e padronizados ]
    C-->D[Camada Gold -- tabelas analíticas e agregadas]
    C-->|Carga final|E[(PostgreSQL)]
    F[Airflow DAGs]-.->A
    F-.->B
    F-.->C
    F-.->D
    G[Docker Compose]-.->F
    G-.->E
