# Application Pipeline Templates

This directory contains comprehensive CI/CD pipeline templates for different application types, designed for enterprise DevSecOps implementations with security, compliance, and quality gates.

## 📁 Available Application Pipelines

### 1. Node.js Application Pipeline (`nodejs-pipeline.yml`)
**Complete CI/CD pipeline for Node.js applications with comprehensive security scanning**

**Features:**
- ✅ **Multi-stage Pipeline**: Validation → Security → Testing → Build → Container Security → Quality Gates → Deployment → Monitoring
- ✅ **Security Scanning**: SAST (Semgrep, CodeQL), SCA (npm audit, Snyk), Container Security (Trivy, Snyk)
- ✅ **Testing**: Unit, Integration, E2E tests with coverage reporting
- ✅ **Quality Gates**: Test coverage (80%+), security vulnerabilities (≤5), container vulnerabilities (0 critical)
- ✅ **Deployment**: Staging and Production with health checks
- ✅ **Monitoring**: Performance testing and metrics collection

**Pipeline Stages:**
1. **Validation**: Code linting, formatting, package validation
2. **Security**: SAST, SCA, dependency vulnerability scanning
3. **Testing**: Unit, integration, E2E tests with coverage
4. **Build**: Docker image building and registry push
5. **Container Security**: Container vulnerability scanning
6. **Quality Gates**: Automated quality checks and thresholds
7. **Deployment**: Staging and production deployments
8. **Monitoring**: Post-deployment monitoring and notifications

### 2. Python Application Pipeline (`python-pipeline.yml`)
**Flask-based Python application pipeline with security and compliance**

**Features:**
- ✅ **Code Quality**: Black, Flake8, isort for code formatting and linting
- ✅ **Security Scanning**: Bandit, Safety, Semgrep, CodeQL, Snyk
- ✅ **Testing**: pytest with unit, integration, E2E, and performance tests
- ✅ **Coverage**: XML and HTML coverage reports with Codecov integration
- ✅ **Container Security**: Trivy and Snyk container scanning
- ✅ **Quality Gates**: Automated thresholds for coverage and security

**Pipeline Stages:**
1. **Validation**: Code formatting, linting, dependency validation
2. **Security**: SAST, SCA, dependency vulnerability scanning
3. **Testing**: Comprehensive test suite with coverage reporting
4. **Build**: Docker image building and registry push
5. **Container Security**: Container vulnerability scanning
6. **Quality Gates**: Automated quality checks and thresholds
7. **Deployment**: Staging and production deployments
8. **Monitoring**: Performance testing and metrics collection

### 3. Java Application Pipeline (`java-pipeline.yml`)
**Enterprise Java application pipeline with Maven and comprehensive security**

**Features:**
- ✅ **Maven Integration**: Maven build system with caching
- ✅ **Code Quality**: Checkstyle, SpotBugs, PMD for static analysis
- ✅ **Security Scanning**: OWASP Dependency Check, Semgrep, CodeQL, Snyk
- ✅ **Testing**: Unit, integration, E2E tests with JaCoCo coverage
- ✅ **Container Security**: Trivy and Snyk container scanning
- ✅ **Quality Gates**: Automated thresholds for coverage and security

**Pipeline Stages:**
1. **Validation**: Maven validation, code quality checks
2. **Security**: SAST, SCA, dependency vulnerability scanning
3. **Testing**: Comprehensive test suite with coverage reporting
4. **Build**: Maven build and Docker image creation
5. **Container Security**: Container vulnerability scanning
6. **Quality Gates**: Automated quality checks and thresholds
7. **Deployment**: Staging and production deployments
8. **Monitoring**: Performance testing and metrics collection

## 🚀 Getting Started

### Prerequisites

1. **GitHub Repository Setup**
   ```bash
   # Clone the repository
   git clone <your-repo>
   cd <your-repo>
   
   # Copy the appropriate pipeline template
   cp pipelines/application/nodejs-pipeline.yml .github/workflows/
   ```

2. **Required Secrets**
   ```yaml
   # GitHub Secrets to configure:
   DOCKER_REGISTRY: "your-registry.com"
   DOCKER_USERNAME: "your-username"
   DOCKER_PASSWORD: "your-password"
   SNYK_TOKEN: "your-snyk-token"
   AWS_ACCESS_KEY_ID: "your-aws-access-key"
   AWS_SECRET_ACCESS_KEY: "your-aws-secret-key"
   AWS_REGION: "us-west-2"
   TEST_DATABASE_URL: "your-test-database-url"
   SLACK_WEBHOOK_URL: "your-slack-webhook"
   ```

3. **Environment Setup**
   ```bash
   # For Node.js applications
   npm install
   npm run lint
   npm run test
   
   # For Python applications
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   black --check .
   pytest tests/
   
   # For Java applications
   mvn clean install
   mvn test
   mvn checkstyle:check
   ```

### Usage Examples

#### Node.js Application
```yaml
# .github/workflows/ci-cd.yml
name: Node.js CI/CD

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  # Include the pipeline template
  include: .github/workflows/nodejs-pipeline.yml
```

#### Python Application
```yaml
# .github/workflows/ci-cd.yml
name: Python CI/CD

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  # Include the pipeline template
  include: .github/workflows/python-pipeline.yml
```

#### Java Application
```yaml
# .github/workflows/ci-cd.yml
name: Java CI/CD

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  # Include the pipeline template
  include: .github/workflows/java-pipeline.yml
```

## 🔒 Security Features

### Static Application Security Testing (SAST)
- **Semgrep**: Pattern-based security scanning
- **CodeQL**: Semantic code analysis
- **Language-specific tools**: Bandit (Python), SpotBugs (Java), ESLint (Node.js)

### Software Composition Analysis (SCA)
- **Dependency scanning**: npm audit, Safety, OWASP Dependency Check
- **Vulnerability databases**: NVD, Snyk vulnerability database
- **License compliance**: Automated license checking

### Container Security
- **Trivy**: Comprehensive container vulnerability scanning
- **Snyk Container**: Container security analysis
- **Base image scanning**: Vulnerability assessment of base images

### Dynamic Application Security Testing (DAST)
- **OWASP ZAP**: Web application security testing
- **Automated scanning**: Scheduled security scans
- **Vulnerability reporting**: Detailed security reports

## 🧪 Testing Strategy

### Test Types
1. **Unit Tests**: Fast, isolated tests for individual components
2. **Integration Tests**: Tests for component interactions
3. **E2E Tests**: Full application workflow testing
4. **Performance Tests**: Load and stress testing

### Coverage Requirements
- **Minimum Coverage**: 80% line coverage
- **Coverage Reporting**: XML and HTML reports
- **Codecov Integration**: Automated coverage tracking

### Test Automation
- **Parallel Execution**: Tests run in parallel for speed
- **Caching**: Dependency and build caching
- **Artifact Management**: Test results and reports storage

## 📊 Quality Gates

### Code Quality Gates
- **Test Coverage**: Minimum 80% line coverage
- **Security Vulnerabilities**: Maximum 5 high/critical vulnerabilities
- **Container Vulnerabilities**: Zero critical container vulnerabilities
- **Code Quality**: Linting and formatting compliance

### Security Quality Gates
- **SAST Results**: Automated security scan analysis
- **SCA Results**: Dependency vulnerability assessment
- **Container Security**: Container vulnerability scanning
- **Compliance**: Automated compliance checking

### Performance Quality Gates
- **Build Time**: Maximum build duration thresholds
- **Test Execution**: Test suite execution time limits
- **Deployment Time**: Deployment duration monitoring

## 🚀 Deployment Strategy

### Environment Strategy
1. **Development**: Local development and testing
2. **Staging**: Pre-production environment for validation
3. **Production**: Live production environment

### Deployment Methods
- **Blue-Green Deployment**: Zero-downtime deployments
- **Rolling Updates**: Gradual deployment with health checks
- **Canary Deployments**: Gradual rollout with monitoring

### Health Checks
- **Application Health**: `/health` endpoint monitoring
- **Readiness Checks**: `/ready` endpoint validation
- **Liveness Checks**: Application responsiveness monitoring

## 📈 Monitoring and Observability

### Application Monitoring
- **Health Endpoints**: Standardized health check endpoints
- **Metrics Collection**: Prometheus metrics integration
- **Logging**: Structured logging with correlation IDs
- **Error Tracking**: Sentry integration for error monitoring

### Infrastructure Monitoring
- **Kubernetes Monitoring**: Pod and service monitoring
- **Resource Monitoring**: CPU, memory, and network monitoring
- **Database Monitoring**: Database performance and health
- **Network Monitoring**: Network connectivity and performance

### Alerting
- **Slack Notifications**: Deployment and security alerts
- **Email Notifications**: Critical security and deployment alerts
- **PagerDuty Integration**: Incident escalation
- **Custom Webhooks**: Integration with existing systems

## 🔧 Customization

### Pipeline Customization
```yaml
# Customize pipeline stages
jobs:
  validate:
    # Custom validation steps
    steps:
      - name: Custom validation
        run: echo "Custom validation logic"
  
  security:
    # Custom security scanning
    steps:
      - name: Custom security scan
        run: echo "Custom security scanning"
```

### Environment-Specific Configuration
```yaml
# Environment-specific variables
env:
  STAGING_URL: "https://staging.example.com"
  PRODUCTION_URL: "https://app.example.com"
  TEST_DATABASE_URL: "${{ secrets.TEST_DATABASE_URL }}"
```

### Quality Gate Customization
```yaml
# Custom quality gate thresholds
quality-gates:
  test-coverage: 85  # Custom coverage threshold
  security-vulnerabilities: 3  # Custom vulnerability threshold
  container-vulnerabilities: 0  # Zero tolerance for critical
```

## 📚 Best Practices

### Security Best Practices
1. **Regular Scanning**: Daily security scans
2. **Vulnerability Management**: Automated vulnerability assessment
3. **Dependency Updates**: Regular dependency updates
4. **Container Security**: Base image security scanning

### Quality Best Practices
1. **Code Reviews**: Mandatory code reviews
2. **Automated Testing**: Comprehensive test automation
3. **Coverage Tracking**: Continuous coverage monitoring
4. **Performance Monitoring**: Continuous performance tracking

### Deployment Best Practices
1. **Blue-Green Deployments**: Zero-downtime deployments
2. **Health Checks**: Comprehensive health monitoring
3. **Rollback Procedures**: Automated rollback capabilities
4. **Monitoring**: Post-deployment monitoring

## 🔧 Troubleshooting

### Common Issues

1. **Build Failures**
   ```bash
   # Check build logs
   cat .github/workflows/build.log
   
   # Verify dependencies
   npm audit  # Node.js
   safety check  # Python
   mvn dependency:tree  # Java
   ```

2. **Security Scan Failures**
   ```bash
   # Update vulnerable dependencies
   npm audit fix  # Node.js
   pip install --upgrade package  # Python
   mvn versions:use-latest-versions  # Java
   ```

3. **Test Failures**
   ```bash
   # Run tests locally
   npm test  # Node.js
   pytest tests/  # Python
   mvn test  # Java
   ```

### Debug Tools

1. **Pipeline Debugging**
   ```bash
   # Enable debug logging
   echo "::debug::Debug information"
   
   # Check job status
   gh run list
   gh run view <run-id>
   ```

2. **Application Debugging**
   ```bash
   # Check application logs
   kubectl logs <pod-name>
   
   # Check application health
   curl -f https://app.example.com/health
   ```

## 📈 Performance Optimization

### Build Optimization
- **Dependency Caching**: Cache dependencies for faster builds
- **Parallel Execution**: Run jobs in parallel where possible
- **Build Caching**: Cache build artifacts for incremental builds

### Test Optimization
- **Test Parallelization**: Run tests in parallel
- **Test Caching**: Cache test results
- **Selective Testing**: Run only changed tests

### Deployment Optimization
- **Image Optimization**: Optimize Docker images
- **Registry Caching**: Cache container images
- **Deployment Strategies**: Use efficient deployment methods

---

These application pipeline templates provide enterprise-grade CI/CD implementations with comprehensive security, testing, and deployment automation. Each template is designed to be easily customizable for specific project requirements while maintaining security and quality standards. 