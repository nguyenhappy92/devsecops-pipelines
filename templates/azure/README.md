# Azure DevOps Pipeline Templates

This directory contains enterprise-grade Azure DevOps pipeline templates designed for DevSecOps implementations in enterprise environments.

## 📋 Available Templates

### 1. Application Pipeline (`application-pipeline.yml`)
**Comprehensive CI/CD pipeline with integrated security and compliance**

**Features:**
- ✅ Multi-stage validation and testing
- ✅ Security scanning (SAST, DAST, SCA)
- ✅ Container security scanning
- ✅ Blue-green deployment strategy
- ✅ Quality gates and monitoring
- ✅ Multi-environment deployment (Dev, Staging, Production)

**Stages:**
1. **Validate** - Project structure and configuration validation
2. **Security** - Security scanning and vulnerability assessment
3. **Test** - Unit, integration, and E2E testing
4. **Build** - Container image building and registry push
5. **Scan** - Container security scanning
6. **Deploy Staging** - Staging environment deployment
7. **Deploy Production** - Production environment deployment
8. **Monitor** - Deployment health monitoring
9. **Quality Gates** - Security and compliance quality gates

### 2. Security Pipeline (`security-pipeline.yml`)
**Dedicated security scanning and compliance pipeline**

**Features:**
- ✅ SAST (Static Application Security Testing)
- ✅ DAST (Dynamic Application Security Testing)
- ✅ SCA (Software Composition Analysis)
- ✅ Secret Detection
- ✅ Container Security
- ✅ Infrastructure Security
- ✅ Compliance Scanning (SOC 2, PCI DSS, GDPR)
- ✅ Security Score Calculation
- ✅ Vulnerability Management

**Stages:**
1. **SAST** - Static code analysis with SonarQube and Semgrep
2. **DAST** - Dynamic application testing with OWASP ZAP
3. **SCA** - Dependency vulnerability scanning
4. **Secret Detection** - Credential and secret scanning
5. **Container Security** - Container image security scanning
6. **Infrastructure Security** - IaC security validation
7. **Compliance Scan** - Regulatory compliance checking
8. **Security Score** - Overall security score calculation
9. **Vulnerability Management** - Vulnerability aggregation and reporting
10. **Security Notifications** - Alert and dashboard updates
11. **Security Quality Gates** - Security threshold enforcement

## 🚀 Quick Start

### Prerequisites

1. **Azure DevOps Organization**
   - Active Azure DevOps organization
   - Project with repository access
   - Service connections configured

2. **Required Service Connections**
   ```yaml
   # Azure Container Registry
   - Name: Azure Container Registry
   - Type: Docker Registry
   - Registry: your-registry.azurecr.io
   
   # SonarQube
   - Name: SonarQube
   - Type: SonarQube
   - URL: https://your-sonarqube-instance.com
   
   # Snyk
   - Name: Snyk
   - Type: Generic
   - URL: https://api.snyk.io
   ```

3. **Environment Setup**
   ```yaml
   # Staging Environment
   - Name: staging
   - Protection: Manual approval
   - Resource: Kubernetes cluster
   
   # Production Environment
   - Name: production
   - Protection: Manual approval
   - Resource: Kubernetes cluster
   ```

### Installation

1. **Copy Pipeline Template**
   ```bash
   # Copy the application pipeline
   cp templates/azure/application-pipeline.yml azure-pipelines.yml
   
   # Or copy the security pipeline
   cp templates/azure/security-pipeline.yml azure-pipelines-security.yml
   ```

2. **Configure Variables**
   ```yaml
   # In Azure DevOps Project Settings > Variables
   variables:
     ACR_NAME: your-registry-name
     GITGUARDIAN_API_KEY: your-gitguardian-key
     SLACK_WEBHOOK_URL: your-slack-webhook
     TEAMS_WEBHOOK_URL: your-teams-webhook
   ```

3. **Set Up Environments**
   - Go to Project Settings > Environments
   - Create `staging` and `production` environments
   - Configure approval gates and security

## ⚙️ Configuration

### Application Pipeline Configuration

```yaml
variables:
  # Application Configuration
  appName: '$(Build.Repository.Name)'
  appVersion: '$(Build.BuildId)'
  dockerRegistry: '$(ACR_NAME).azurecr.io'
  
  # Security Configuration
  sastEnabled: 'true'
  dastEnabled: 'true'
  scaEnabled: 'true'
  
  # Quality Gates
  testCoverageThreshold: '80'
  vulnerabilityThreshold: 'medium'
  securityScoreThreshold: '80'
```

### Security Pipeline Configuration

```yaml
variables:
  # Security Thresholds
  criticalVulnerabilitiesThreshold: '0'
  highVulnerabilitiesThreshold: '5'
  mediumVulnerabilitiesThreshold: '20'
  
  # Compliance Standards
  soc2Enabled: 'true'
  pciDssEnabled: 'true'
  gdprEnabled: 'true'
  iso27001Enabled: 'true'
```

## 🔧 Customization

### Adding Custom Security Tools

```yaml
# Add custom SAST tool
- script: |
    echo "Running custom SAST tool..."
    # Your custom SAST implementation
  displayName: 'Custom SAST Tool'
```

### Modifying Quality Gates

```yaml
# Custom quality gate thresholds
variables:
  customTestCoverageThreshold: '85'
  customSecurityScoreThreshold: '90'
  customVulnerabilityThreshold: 'low'
```

### Environment-Specific Configuration

```yaml
# Environment-specific variables
- stage: DeployStaging
  variables:
    environment: 'staging'
    clusterName: 'staging-cluster'
    namespace: 'staging'
    
- stage: DeployProduction
  variables:
    environment: 'production'
    clusterName: 'production-cluster'
    namespace: 'production'
```

## 🔒 Security Features

### Built-in Security Scanning

1. **SAST (Static Analysis)**
   - SonarQube integration
   - Semgrep security rules
   - CodeQL analysis
   - Custom security rules

2. **DAST (Dynamic Analysis)**
   - OWASP ZAP baseline scan
   - OWASP ZAP full scan
   - Custom web application testing

3. **SCA (Software Composition Analysis)**
   - Trivy vulnerability scanning
   - Snyk dependency scanning
   - License compliance checking

4. **Container Security**
   - Trivy container scanning
   - Snyk container analysis
   - Image vulnerability assessment

5. **Secret Detection**
   - TruffleHog scanning
   - GitGuardian integration
   - Credential detection

### Compliance Frameworks

1. **SOC 2 Type II**
   - Security controls validation
   - Availability controls checking
   - Automated compliance reporting

2. **PCI DSS**
   - Payment card security controls
   - Data protection validation
   - Network security assessment

3. **GDPR**
   - Data protection principles
   - Privacy controls validation
   - Rights management checking

4. **ISO 27001**
   - Information security controls
   - Risk management validation
   - Security governance checking

## 📊 Monitoring and Reporting

### Built-in Dashboards

1. **Security Dashboard**
   - Vulnerability trends
   - Security score tracking
   - Compliance status

2. **Pipeline Dashboard**
   - Build success rates
   - Deployment metrics
   - Performance indicators

3. **Cost Dashboard**
   - Resource utilization
   - Cost optimization
   - Budget tracking

### Notifications

```yaml
# Slack notifications
- task: Slack@1
  inputs:
    channel: '#deployments'
    message: 'Deployment completed successfully'

# Email notifications
- task: EmailReport@1
  inputs:
    to: 'devsecops@company.com'
    subject: 'Security Scan Results'
    body: 'Security scan completed'
```

## 🛠️ Troubleshooting

### Common Issues

1. **Build Failures**
   ```bash
   # Check build logs
   az pipelines runs list --project YourProject
   az pipelines runs show --id <run-id>
   ```

2. **Security Scan Failures**
   ```bash
   # Check security tool logs
   docker logs <container-id>
   ```

3. **Deployment Failures**
   ```bash
   # Check Kubernetes deployment
   kubectl get pods -n <namespace>
   kubectl describe pod <pod-name>
   ```

### Debug Mode

```yaml
# Enable debug logging
variables:
  system.debug: 'true'
  agent.diagnostic: 'true'
```

## 📚 Best Practices

### Security Best Practices

1. **Pipeline Security**
   - Use service connections with minimal permissions
   - Enable branch protection policies
   - Implement approval gates for production

2. **Code Security**
   - Scan all code changes
   - Block deployments with critical vulnerabilities
   - Regular dependency updates

3. **Infrastructure Security**
   - Scan all infrastructure code
   - Validate security configurations
   - Monitor resource access

### Performance Best Practices

1. **Pipeline Optimization**
   - Use parallel job execution
   - Implement build caching
   - Optimize resource allocation

2. **Security Scanning**
   - Run security scans in parallel
   - Use incremental scanning
   - Cache scan results

### Compliance Best Practices

1. **Automated Compliance**
   - Continuous compliance monitoring
   - Automated policy enforcement
   - Regular compliance reporting

2. **Audit Preparation**
   - Comprehensive logging
   - Evidence collection
   - Automated reporting

## 🔄 Integration

### Azure Services Integration

1. **Azure Container Registry**
   ```yaml
   - task: Docker@2
     inputs:
       containerRegistry: 'Azure Container Registry'
       repository: '$(appName)'
       command: 'buildAndPush'
   ```

2. **Azure Kubernetes Service**
   ```yaml
   - script: |
       az aks get-credentials --resource-group $(resourceGroup) --name $(clusterName)
       kubectl apply -f k8s/
   ```

3. **Azure Key Vault**
   ```yaml
   - task: AzureKeyVault@2
     inputs:
       azureSubscription: 'Azure Subscription'
       KeyVaultName: 'your-keyvault'
       SecretsFilter: '*'
   ```

### Third-Party Integrations

1. **Slack Integration**
   ```yaml
   - task: Slack@1
     inputs:
       channel: '#deployments'
       message: 'Deployment status'
   ```

2. **Email Integration**
   ```yaml
   - task: EmailReport@1
     inputs:
       to: 'team@company.com'
       subject: 'Pipeline Report'
   ```

## 📈 Metrics and KPIs

### Security Metrics

- **Vulnerability Count**: Track critical/high vulnerabilities
- **Security Score**: Overall security assessment score
- **Compliance Status**: Regulatory compliance percentage
- **Scan Coverage**: Percentage of code scanned

### Pipeline Metrics

- **Build Success Rate**: Percentage of successful builds
- **Deployment Success Rate**: Percentage of successful deployments
- **Mean Time to Recovery**: Time to fix and deploy
- **Lead Time**: Time from commit to production

### Cost Metrics

- **Resource Utilization**: CPU and memory usage
- **Build Time**: Average build duration
- **Infrastructure Cost**: Monthly infrastructure spend
- **Optimization Opportunities**: Cost reduction potential

## 🆘 Support

### Documentation

- [Azure DevOps Documentation](https://docs.microsoft.com/en-us/azure/devops/)
- [Pipeline YAML Reference](https://docs.microsoft.com/en-us/azure/devops/pipelines/yaml-schema/)
- [Security Best Practices](https://docs.microsoft.com/en-us/azure/devops/pipelines/security/)

### Community Resources

- [Azure DevOps Community](https://developercommunity.visualstudio.com/spaces/21/index.html)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/azure-devops)
- [GitHub Issues](https://github.com/microsoft/azure-pipelines-tasks/issues)

### Enterprise Support

For enterprise support and customization:
- Contact your Azure DevOps administrator
- Engage with Microsoft Premier Support
- Work with certified Azure DevOps consultants

---

**Built for Enterprise Security and Compliance** 🔐 