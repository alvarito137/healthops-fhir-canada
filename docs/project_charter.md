# HealthOps FHIR Canada — Project Charter

## 1. Project Overview

**Project name:** HealthOps FHIR Canada

**Product description:**  
HealthOps FHIR Canada is an educational healthcare data quality and implementation platform. It will ingest synthetic HL7 FHIR R4 records, validate healthcare data, transform selected clinical resources into a relational PostgreSQL model, expose operational information through a FastAPI service, and present data-quality and implementation indicators in Power BI.

**Project type:**  
Professional portfolio and technical learning project.

**Project owner:**  
Álvaro Portilla

**Current phase:**  
Planning and environment setup.

---

## 2. Business Problem

A simulated Canadian health technology company receives healthcare data from multiple client organizations.

The submitted files may contain incomplete records, duplicate identifiers, invalid dates, unsupported values, missing units, repeated files, and broken references between clinical resources.

Without an organized ingestion and validation process, implementation and support teams may have difficulty determining:

- Which files were received and processed.
- Which records were accepted or rejected.
- Which organizations produce recurring data-quality problems.
- Which clinical resources require attention.
- Which issues remain unresolved.
- Whether a file has already been processed.
- How transformed records relate to the original source file.
- How long each import takes to complete.

The company needs a traceable and testable workflow for importing, validating, investigating, and reporting synthetic healthcare data.

---

## 3. Project Purpose

The purpose of HealthOps FHIR Canada is to demonstrate how a technical implementation team could manage healthcare data imports from multiple simulated client organizations.

The project will provide evidence of skills in:

- Python application development.
- Healthcare data ingestion.
- Data-quality validation.
- PostgreSQL database design.
- SQL analysis.
- REST API development.
- Software testing and quality assurance.
- Power BI reporting.
- Client implementation documentation.
- Technical support and incident investigation.
- Git and GitHub collaboration workflows.

---

## 4. Intended Users

### Implementation analysts

Use import results, mapping documentation, validation issues, and UAT evidence to support client onboarding.

### Data quality analysts

Review rejected records, broken references, recurring validation failures, and quality trends.

### Application support analysts

Investigate failed imports, review logs, reproduce errors, and follow troubleshooting procedures.

### Operations managers

Monitor processing volume, import status, open issues, critical incidents, and processing duration.

### Client data contacts

Receive understandable explanations of data problems and the corrections required before resubmission.

### Hiring managers and recruiters

Review the project as evidence of technical, analytical, implementation, testing, and documentation skills.

---

## 5. Simulated Client Organizations

The MVP will represent three fictional Canadian healthcare organizations:

1. NorthCare Clinic.
2. Maple Community Health.
3. Ottawa Digital Health Centre.

All organizations, patients, practitioners, and healthcare events represented in the project are fictional or synthetically generated.

---

## 6. MVP Scope

The minimum viable product will include the following capabilities.

### Data ingestion

- Read synthetic FHIR R4 JSON files.
- Process FHIR Bundles.
- Record the source organization.
- Assign an import batch identifier.
- Record the source filename and processing timestamp.
- Detect invalid JSON.
- Detect empty Bundles.
- Detect repeated files.

### Supported FHIR resources

- Patient.
- Encounter.
- Observation.
- Condition.
- Organization when required for source attribution.

### Data validation

- Validate required identifiers.
- Validate required dates.
- Detect future birth dates.
- Detect duplicate patient and encounter identifiers.
- Detect missing patient references.
- Detect references to nonexistent records.
- Detect invalid encounter date ranges.
- Detect missing observation codes and units.
- Record issue severity and status.

### Data storage

- Store normalized data in PostgreSQL.
- Preserve source identifiers.
- Preserve organization and import-batch traceability.
- Record validation issues.
- Record processing results and logs.

### REST API

- Provide a health-check endpoint.
- List and inspect imports.
- Create an import request.
- Return data-quality summaries.
- Return quality results by organization and resource type.
- List and inspect validation issues.
- Update issue status and resolution notes.
- Return a patient timeline.

### Testing

- Unit tests.
- Integration tests.
- API tests.
- Positive and negative test cases.
- Basic regression testing.
- Data reconciliation evidence.

### Reporting

- Power BI executive overview.
- Data-quality analysis.
- Operations and support indicators.
- Documented KPI definitions.

### Implementation and support documentation

- Project requirements.
- Architecture documentation.
- Data mapping.
- Test plan.
- UAT checklist.
- Implementation checklist.
- Support runbook.
- Troubleshooting guide.
- Incident report.
- Release notes.

---

## 7. Out of Scope for the MVP

The following capabilities will not be part of the initial MVP:

- Processing real patient information.
- Production deployment for clinical use.
- Complex user authentication.
- Role-based access control.
- Complete FHIR specification support.
- MedicationRequest transformation.
- Practitioner transformation.
- Bulk FHIR processing.
- Integration with a production FHIR server.
- Azure deployment.
- Machine learning.
- Automated anomaly detection.
- AI-generated clinical recommendations.
- Clinical decision support.
- Automated diagnosis.
- Real-time hospital integrations.
- Bilingual user interface.
- Geographic healthcare analysis.

These capabilities may be evaluated only after the MVP has been completed and documented.

---

## 8. Main Deliverables

The project will produce:

1. A public GitHub repository.
2. Reproducible local installation instructions.
3. Synthetic FHIR sample data.
4. A Python ingestion and validation pipeline.
5. A normalized PostgreSQL database.
6. SQL scripts and analytical queries.
7. A documented FastAPI service.
8. A Postman collection.
9. Automated tests.
10. A GitHub Actions workflow.
11. A Power BI dashboard.
12. Implementation documentation.
13. QA and UAT evidence.
14. A support and troubleshooting package.
15. A simulated incident and blameless postmortem.
16. A demonstration video.
17. A versioned `v1.0.0` release.
18. Verified résumé and LinkedIn project statements.

---

## 9. Success Criteria

The MVP will be considered successful when:

- A new developer can follow the README and run the project locally.
- The system can ingest a valid synthetic FHIR Bundle.
- Invalid JSON and empty Bundles are rejected with understandable errors.
- Every import receives a traceable batch identifier.
- Supported FHIR resources can be transformed and stored in PostgreSQL.
- Duplicate identifiers and broken references can be detected.
- Validation issues include resource, rule, severity, status, and source information.
- The API returns documented operational and data-quality information.
- Automated tests run successfully in GitHub Actions.
- The Postman collection includes successful and negative test scenarios.
- The Power BI dashboard displays documented operational and quality KPIs.
- Implementation and support documentation describes how to investigate common failures.
- No real protected health information is included.
- All résumé metrics are derived from actual project results.
- The project can be explained during a technical or behavioural interview.

---

## 10. Constraints

- The project must use synthetic healthcare data only.
- The project owner has limited financial resources.
- Free and open-source tools will be preferred.
- Power BI Desktop will be used for local dashboard development.
- Development will normally occur during morning study sessions.
- The project must remain achievable by one developer.
- The MVP must not depend on paid cloud infrastructure.
- New technologies will be introduced only when they solve a defined project problem.
- Machine learning will not be added before the MVP is complete.
- Public documentation, source code, tickets, and portfolio materials will be written in professional English.

---

## 11. Assumptions

- Synthea can provide suitable synthetic FHIR R4 records.
- PostgreSQL can run locally or through Docker.
- The project will initially process small batches of synthetic records.
- The first implementation will prioritize correctness and traceability over performance optimization.
- Supported FHIR resources will be limited to those required by the MVP.
- Client organizations and implementation scenarios are fictional.
- The project owner will verify each major stage before proceeding.

---

## 12. Initial Risks and Mitigations

| Risk | Potential impact | Initial mitigation |
|---|---|---|
| FHIR structures are more complex than expected | Development delays | Start with a limited set of resources and small Bundles |
| Project scope becomes too large | MVP is not completed | Maintain a documented out-of-scope section |
| Tooling issues on Windows | Lost development time | Use a dedicated Conda environment and documented commands |
| Database configuration problems | Pipeline cannot be tested | Validate PostgreSQL independently before integration |
| Synthetic data lacks required error cases | Validation rules cannot be demonstrated | Create controlled synthetic negative-test fixtures |
| Dashboard metrics are inconsistent with database results | Reduced credibility | Perform data reconciliation between SQL, API, and Power BI |
| Sensitive information is committed accidentally | Privacy and security risk | Use `.gitignore`, `.env`, synthetic data, and repository reviews |
| Metrics are claimed before measurement | Misleading portfolio statements | Record only results produced by repeatable tests |
| Too many technologies are added | Increased maintenance and incomplete features | Require a business or technical justification for each tool |
| Documentation becomes outdated | Instructions stop working | Update documentation within the same pull request as the code change |

---

## 13. Privacy and Safety Statement

> This portfolio project uses synthetic patient data generated for educational and demonstration purposes. It does not contain real protected health information.

HealthOps FHIR Canada is not a clinical system, medical device, diagnostic application, or production-ready healthcare platform.

It must not be used to store, process, diagnose, or make decisions about real patients.

---

## 14. Project Governance

Development will follow a lightweight remote-team workflow:

- Changes will be developed in focused branches.
- Commits will describe one meaningful change.
- Issues will document planned work.
- Pull requests will document the reason for each change.
- Tests and documentation will be updated with the related functionality.
- Large features will be divided into smaller tasks.
- MVP work will be prioritized over future enhancements.
- Results will be verified before they are published.

---

## 15. Approval Status

**Status:** Draft

The project charter will remain a living document and may be updated when requirements are clarified. Changes that affect the MVP scope must be documented through an issue and pull request.