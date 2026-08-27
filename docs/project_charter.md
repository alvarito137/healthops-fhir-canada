# HealthOps FHIR Canada — Project Charter

## 1. Project Overview

**Project name:** HealthOps FHIR Canada

**Portfolio focus:** Application Support & Troubleshooting

**Product description:**
HealthOps FHIR Canada is a small simulated healthcare SaaS application and technical support lab designed to demonstrate practical Application Support skills.

The application will use synthetic healthcare and HL7 FHIR data as a realistic technical context while focusing primarily on diagnosing, investigating, resolving, validating, documenting, and escalating application incidents.

The project will demonstrate troubleshooting across REST APIs, application logs, PostgreSQL databases, JSON payloads, authentication, local services, and basic connectivity.

**Project type:**
Professional portfolio and technical learning project.

**Project owner:**
Álvaro Portilla

**Current phase:**
Application Support MVP planning.

---

## 2. Business Problem

A simulated Canadian health technology company operates a SaaS application that receives and displays synthetic healthcare information.

Customers may contact the support team when they experience problems such as:

* Unable to sign in.
* API requests returning errors.
* Patient records not appearing.
* Invalid JSON or FHIR payloads being rejected.
* Application services becoming unavailable.
* Database records not matching what users expect to see.

Support analysts need to determine whether an issue originates from:

* User input.
* Authentication or authorization.
* Application logic.
* REST API behaviour.
* Database records.
* Application configuration.
* Service availability.
* Local connectivity.

The support team must be able to reproduce reported problems, gather evidence, review logs, query the database, form and test hypotheses, identify root causes, apply or recommend resolutions, validate recovery, and document the incident.

---

## 3. Project Purpose

The purpose of HealthOps FHIR Canada is to demonstrate an end-to-end Application Support troubleshooting workflow using a small but realistic SaaS application.

The project will provide practical evidence of skills in:

* Application troubleshooting.
* REST API investigation.
* HTTP status-code interpretation.
* PostgreSQL and SQL troubleshooting.
* Application log analysis.
* JSON and FHIR payload investigation.
* Authentication troubleshooting.
* Basic Windows and Linux diagnostics.
* Service and port investigation.
* Incident management.
* Root cause analysis.
* Resolution validation.
* Technical escalation.
* Knowledge-base and runbook documentation.
* Python scripting for simple support automation.
* Postman API testing.
* Git and GitHub workflows.

FHIR is used as the application's healthcare data format and business context. The project is not intended to implement the complete FHIR specification or function as a production clinical platform.

---

## 4. Intended Users

### Application Support Analysts

Investigate reported application problems using API responses, logs, SQL queries, configuration information, and operating-system diagnostics.

### Technical Support Specialists

Reproduce customer issues, collect evidence, identify probable causes, apply documented resolutions, and escalate unresolved problems with sufficient technical information.

### Product Support Specialists

Help customers understand application behaviour, investigate data and API problems, document known issues, and provide clear customer-facing explanations.

### Junior Support Engineers

Investigate incidents that require deeper technical analysis across application code, databases, REST APIs, logs, and local services.

### Support Leads and Engineering Teams

Receive structured escalation information including impact, reproduction steps, evidence, investigation already completed, and suspected root cause.

### Hiring Managers and Recruiters`

Review the project as evidence of practical troubleshooting, technical communication, incident management, API support, SQL investigation, and support documentation skills.

---

## 5. Application Support MVP Scope

The MVP will remain intentionally small. Its purpose is to provide a realistic application that can be monitored, broken, investigated, restored, and documented.

### 5.1 Core Application

HealthOps will provide a small FastAPI application with enough functionality to support realistic troubleshooting scenarios.

The MVP will include:

* A health-check endpoint.
* A basic authentication scenario.
* A patient lookup endpoint.
* A FHIR/JSON submission endpoint.
* PostgreSQL-backed patient data.
* Synthetic healthcare data only.
* Application logging.
* Appropriate HTTP status codes and error responses.

The MVP does not require a complete healthcare platform.

---

### 5.2 Support Investigation Capabilities

The application must allow a support analyst to investigate problems using:

* REST API responses.
* HTTP status codes.
* Postman or `curl`.
* Application logs.
* Python exception information.
* PostgreSQL queries.
* Basic operating-system commands.
* Service status.
* Port availability.
* Basic local connectivity checks.

The purpose of these capabilities is troubleshooting rather than application feature development.

---

### 5.3 Incident Scenarios

The MVP will include five controlled support incidents.

#### INC-001 — Authentication Failure

A user cannot access the application.

Investigation will demonstrate:

* HTTP 401 and/or 403 responses.
* Authentication troubleshooting.
* Log investigation.
* User or credential validation.
* Root cause identification.
* Resolution and validation.

#### INC-002 — API HTTP 500

An API endpoint returns an internal server error.

Investigation will demonstrate:

* Issue reproduction.
* API-response investigation.
* Log review.
* Python exception analysis.
* Root cause analysis.
* Fix or remediation.
* Regression validation.

#### INC-003 — Missing Patient Record

A user reports that a patient record is missing.

Investigation will demonstrate:

* API lookup.
* SQL querying.
* PostgreSQL troubleshooting.
* Comparison between application behaviour and stored data.
* Root cause identification.
* Customer-facing explanation.

#### INC-004 — Invalid JSON/FHIR Payload

A malformed or invalid request is submitted to the application.

Investigation will demonstrate:

* HTTP 400 and/or 422 responses.
* JSON troubleshooting.
* Basic FHIR validation.
* Request-body investigation.
* Error-log analysis.
* Identification and correction of invalid input.

#### INC-005 — Application Unavailable

The HealthOps API cannot be reached.

Investigation will demonstrate:

* Application process checks.
* Localhost connectivity.
* Port investigation.
* Service availability.
* Basic network troubleshooting.
* Configuration investigation.
* Distinguishing application, service, database, and connectivity failures.

---

### 5.4 Incident Management

Each incident will be documented using a consistent support-ticket structure containing:

* Incident ID.
* Title.
* Customer or user impact.
* Priority.
* Status.
* Description.
* Steps to reproduce.
* Investigation performed.
* Evidence collected.
* Hypotheses tested.
* Root cause.
* Resolution or workaround.
* Validation.
* Escalation information when applicable.
* Prevention or knowledge-base update.

At least one incident will demonstrate a realistic technical escalation to another team.

---

### 5.5 Support Documentation

The MVP will include:

* A troubleshooting guide.
* A support runbook.
* A small knowledge base.
* Incident records.
* Escalation notes.
* Reproduction steps.
* Resolution evidence.

Documentation will focus on actions that an Application Support Analyst could realistically perform.

---

### 5.6 Diagnostic Automation

A small Python script named `healthops_diagnostics.py` will perform basic checks such as:

* Operating system.
* Hostname.
* API availability.
* Database connectivity.
* API port availability.
* Available disk space.
* Basic memory status.

The script will provide a simple overall health assessment and possible cause when a major check fails.

The diagnostic tool must remain understandable enough to explain during a technical interview.

---

### 5.7 Postman

A small Postman collection will be created for:

* Health checks.
* Authentication testing.
* Patient lookup.
* FHIR/JSON submissions.
* Successful requests.
* Authentication failures.
* Invalid payloads.
* Not-found scenarios.
* Server-error investigation.

Postman will be used as both a testing tool and troubleshooting evidence.

---

### 5.8 Support Dashboard

A simple support-focused dashboard may be included after the five incidents are operational.

It should display only useful support indicators such as:

* Total incidents.
* Open incidents.
* Resolved incidents.
* Incidents by priority.
* Incidents by category.
* Average resolution time, if sufficient incident data exists.
* Current API status.
* Current database status.

The dashboard must remain secondary to the troubleshooting workflow.

---

## 6. Out of Scope for the MVP

The following capabilities are deliberately excluded from the initial Application Support MVP:

* Machine learning.
* Predictive analytics.
* Advanced healthcare analytics.
* Large Power BI dashboards.
* Complete HL7 FHIR implementation.
* Complex healthcare workflows.
* Kubernetes.
* Microservices architecture.
* Complex cloud infrastructure.
* Advanced CI/CD pipelines.
* Production-grade identity management.
* Role-based access-control systems.
* Real patient information.
* Production clinical use.
* Dozens of API endpoints.
* Performance optimization before a demonstrated need exists.

Future features will be evaluated only after the support scenarios are complete and the project is recruiter-ready.

---

## 7. MVP Success Criteria

The Application Support MVP will be considered complete when:

* The HealthOps API runs locally.
* PostgreSQL contains synthetic patient records.
* Application logs can be inspected during troubleshooting.
* The five defined incidents can be reproduced deliberately.
* Each incident has documented investigation evidence.
* Each incident has an identified root cause or documented escalation.
* Resolutions or workarounds are validated.
* SQL is used for at least one database investigation.
* Postman is used to reproduce and validate API incidents.
* Basic operating-system or connectivity commands are used during the application-unavailable investigation.
* The diagnostic Python script can identify at least basic API and database health conditions.
* A support runbook and troubleshooting guide exist.
* Incident documentation follows a consistent structure.
* No real patient or protected health information is used.
* The README explains the project's support focus in less than one minute.
* Any résumé claims are supported by functionality that exists in the repository.

---

## 8. Main Deliverables

The Application Support MVP will produce:

1. A small FastAPI application.
2. A PostgreSQL database containing synthetic patient records.
3. Application logging for troubleshooting.
4. A Postman collection for API investigation.
5. Five reproducible support incidents.
6. Incident investigation and root cause analysis documentation.
7. At least one technical escalation example.
8. A support runbook.
9. A troubleshooting guide.
10. A small knowledge base.
11. A Python diagnostic utility.
12. GitHub Issues and Pull Requests demonstrating traceable work.
13. A recruiter-focused README.
14. Screenshots or evidence from troubleshooting scenarios.
15. Verified résumé statements based only on implemented functionality.

---

## 9. Constraints

* The project must use synthetic healthcare data only.
* The project must remain achievable by one developer.
* Free or low-cost tools will be preferred.
* The MVP must not require paid cloud infrastructure.
* New technologies will be added only when they solve a defined support problem.
* The project will prioritize troubleshooting scenarios over feature development.
* Machine learning will not be added before the support MVP is complete.
* Complex cloud infrastructure and microservices are outside the MVP.
* Public documentation and portfolio materials will be written in professional English.
* Results must be verified before being used in résumé or portfolio statements.

---

## 10. Assumptions

* HealthOps will run locally during the MVP.
* PostgreSQL will be available locally.
* FastAPI will provide enough functionality to reproduce the planned support incidents.
* Synthetic patient and FHIR data will be sufficient for troubleshooting scenarios.
* The application will intentionally include controlled failure scenarios for educational purposes.
* Support incidents will be reproduced in a safe local environment.
* The first version will prioritize clarity and troubleshooting value over performance or feature completeness.
* The project owner will verify each major stage before proceeding.

---

## 11. Initial Risks and Mitigations

| Risk | Potential Impact | Mitigation |
| --- | --- | --- |
| Project scope becomes too large | MVP is delayed or never completed | Keep features limited to those required for the five incidents |
| Application is too simple to troubleshoot realistically | Weak portfolio evidence | Ensure each incident produces observable API, log, database, or OS evidence |
| Failure scenarios feel artificial | Reduced credibility | Base incidents on realistic support situations and document reproduction clearly |
| PostgreSQL configuration problems | Database scenarios cannot be tested | Validate database connectivity independently before application integration |
| Logs do not provide enough evidence | Troubleshooting becomes guesswork | Add useful timestamps, severity levels, endpoint context, and exceptions |
| Incident documentation becomes inconsistent | Difficult to compare investigations | Use one standard incident template |
| Sensitive information is committed accidentally | Privacy and security risk | Use synthetic data, `.gitignore`, `.env`, and repository reviews |
| Fixes introduce new problems | Regression risk | Validate each resolution and add a test when appropriate |
| Too many technologies are added | Increased complexity and unfinished features | Require a support-related reason before introducing another tool |
| Portfolio claims exceed implemented work | Reduced credibility with employers | Use only evidence and results that exist in the repository |

---

## 12. Privacy and Safety Statement

> This portfolio project uses synthetic patient data generated for educational and demonstration purposes. It does not contain real protected health information.

HealthOps FHIR Canada is not a clinical system, medical device, diagnostic application, or production-ready healthcare platform.

It must not be used to store, process, diagnose, or make decisions about real patients.

---

## 13. Project Governance

Development will follow a lightweight remote-team workflow:

* Changes will be developed in focused branches.
* Commits will describe one meaningful change.
* Issues will document planned work.
* Pull requests will document the reason for each change.
* Tests and documentation will be updated with the related functionality.
* Large features will be divided into smaller tasks.
* MVP work will be prioritized over future enhancements.
* Results will be verified before they are published.

---

## 14. Approval Status

**Status:** Draft

The project charter will remain a living document and may be updated when requirements are clarified. Changes that affect the MVP scope must be documented through an issue and pull request.
