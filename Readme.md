# Portfolio – ETL de Dados da Lei Rouanet com Airflow & Arquitetura Medalhão  

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)  
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)  
[![Airflow](https://img.shields.io/badge/Airflow-2.x-orange.svg)](https://airflow.apache.org/)  
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-+-blue.svg)](https://www.postgresql.org/)  

---

## ✨ Visão Geral  
Este projeto implementa um pipeline completo de **engenharia de dados** para a extração, tratamento, padronização e carga dos dados públicos da Lei Rouanet (via API VERSALIC) em um banco PostgreSQL, orquestrado pelo Airflow em ambiente Docker.  
É um exemplo de trabalho para portfólio, demonstrando o fluxo de ETL com arquitetura de medalhão:  
- Extração de dados via API REST  
- Arquitetura **bronze → silver → gold** (medalhão)  
- Orquestração via Airflow com observabilidade (logs, retries, alertas)  
- Containerização (Docker-Compose) e modularização em código (`extract`, `transform`, `load`)  
- Uso de banco relacional como destino e preparo para consumo analítico

---

## 🏗 Arquitetura da Solução  
### Fluxo geral  
1. **Fonte**: API pública VERSALIC (dados de projetos incentivados pela Lei Rouanet)  
2. **Camada Bronze**: Dados brutos extraídos e armazenados (ex: JSON)  
3. **Camada Silver**: Dados limpos, tipados e padronizados em tabelas intermediárias no PostgreSQL  
4. **Camada Gold**: Tabelas analíticas agregadas, prontas para consumo BI  
5. **Orquestração**: DAGs do Airflow com TaskFlow API, agendadas e operacionalizadas  
6. **Infraestrutura**: Containers Docker (Airflow, Postgres), versão controlada, reprodutível  

```mermaid
flowchart LR
   A[Fonte: VERSALIC API] --> B[Bronze Layer (raw JSON)]
   B --> C[Silver Layer (tabelas limpas)]
   C --> D[Gold Layer (indicadores/analíticos)]
   C -->|Carga para| ← E[PostgreSQL]
   F[Airflow DAGs] -.-> A
   F -.-> B
   F -.-> C
   F -.-> D
   G[Docker Compose] -. containers .-> F
   G -.-> E
