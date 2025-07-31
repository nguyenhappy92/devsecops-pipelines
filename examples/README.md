# DevSecOps Pipeline Examples

This directory contains practical examples of DevSecOps pipeline implementations for different application types and infrastructure configurations.

## 📁 Available Examples

### 1. Node.js Application (`nodejs-application/`)
**Complete Node.js application with DevSecOps pipeline implementation**

**Features:**
- ✅ Express.js REST API with security middleware
- ✅ Comprehensive testing (unit, integration, E2E)
- ✅ Security scanning and vulnerability management
- ✅ Docker containerization with security best practices
- ✅ Kubernetes deployment configurations
- ✅ GitLab CI/CD pipeline with security gates

**Key Components:**
- `package.json` - Dependencies and scripts
- `Dockerfile` - Secure container configuration
- `.gitlab-ci.yml` - Complete CI/CD pipeline
- `k8s/` - Kubernetes manifests for multiple environments
- `src/` - Application source code with security features
- `tests/` - Comprehensive test suite
- `scripts/` - Security and deployment scripts

**Security Features:**
- Helmet.js for security headers
- Rate limiting and CORS protection
- JWT authentication and authorization
- Input validation and sanitization
- Dependency vulnerability scanning
- Container security scanning

### 2. Python Application (`python-application/`)
**Flask-based Python application with DevSecOps practices**

**Features:**
- ✅ Flask REST API with security extensions
- ✅ Comprehensive dependency management
- ✅ Security scanning with Bandit and Safety
- ✅ Docker containerization
- ✅ Testing with pytest and coverage
- ✅ Code quality with Black and Flake8

**Key Components:**
- `requirements.txt` - Python dependencies with security tools
- `Dockerfile` - Secure Python container
- `app.py` - Flask application with security middleware
- `tests/` - pytest test suite
- `scripts/` - Security and deployment scripts

**Security Features:**
- Flask-Security for authentication
- Input validation with Cerberus
- Rate limiting with Flask-Limiter
- CORS protection
- Dependency vulnerability scanning
- Code quality and security linting

### 3. Terraform Infrastructure (`terraform-infrastructure/`)
**Infrastructure as Code with security and compliance**

**Features:**
- ✅ Multi-environment AWS infrastructure
- ✅ EKS cluster with security configurations
- ✅ VPC with network segmentation
- ✅ RDS with encryption and monitoring
- ✅ WAF and security groups
- ✅ CloudWatch logging and monitoring

**Key Components:**
- `main.tf` - Main infrastructure configuration
- `modules/` - Reusable Terraform modules
- `variables.tf` - Environment-specific variables
- `outputs.tf` - Infrastructure outputs
- `security/` - Security and compliance configurations

**Security Features:**
- Network segmentation with private subnets
- Security groups with least privilege
- RDS encryption at rest and in transit
- WAF for web application protection
- CloudTrail for audit logging
- IAM roles with minimal permissions

## 🚀 Getting Started

### Prerequisites

1. **Development Environment**
   ```bash
   # Install Node.js (for Node.js example)
   curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
   sudo apt-get install -y nodejs
   
   # Install Python (for Python example)
   sudo apt-get install python3.11 python3-pip
   
   # Install Docker
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   
   # Install kubectl
   curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
   sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
   ```

2. **Cloud Environment**
   ```bash
   # Install AWS CLI
   curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
   unzip awscliv2.zip
   sudo ./aws/install
   
   # Install Terraform
   curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -
   sudo apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"
   sudo apt-get update && sudo apt-get install terraform
   ```

### Running Examples

#### Node.js Application

```bash
# Clone and setup
cd examples/nodejs-application
npm install

# Run security scan
npm run security:scan

# Run tests
npm run test:coverage

# Build Docker image
npm run docker:build

# Deploy to Kubernetes
npm run k8s:deploy-dev
```

#### Python Application

```bash
# Clone and setup
cd examples/python-application
pip install -r requirements.txt

# Run security scan
safety check
bandit -r .

# Run tests
pytest --cov=app tests/

# Build Docker image
docker build -t python-app .

# Run application
docker run -p 5000:5000 python-app
```

#### Terraform Infrastructure

```bash
# Clone and setup
cd examples/terraform-infrastructure

# Initialize Terraform
terraform init

# Plan deployment
terraform plan -var-file=environments/dev.tfvars

# Apply infrastructure
terraform apply -var-file=environments/dev.tfvars
```

## 🔒 Security Features

### Application Security

1. **Input Validation**
   - Joi (Node.js) and Cerberus (Python) for validation
   - SQL injection prevention
   - XSS protection

2. **Authentication & Authorization**
   - JWT token-based authentication
   - Role-based access control
   - Session management

3. **API Security**
   - Rate limiting
   - CORS configuration
   - Security headers (Helmet)

4. **Dependency Security**
   - Automated vulnerability scanning
   - Regular dependency updates
   - License compliance checking

### Infrastructure Security

1. **Network Security**
   - VPC with public/private subnets
   - Security groups with least privilege
   - Network ACLs

2. **Data Security**
   - Encryption at rest and in transit
   - Key management with AWS KMS
   - Backup encryption

3. **Access Control**
   - IAM roles with minimal permissions
   - Multi-factor authentication
   - Audit logging

4. **Monitoring & Alerting**
   - CloudWatch monitoring
   - Security event logging
   - Automated alerting

## 📊 Monitoring and Observability

### Application Monitoring

1. **Health Checks**
   - `/health` endpoint for liveness
   - `/ready` endpoint for readiness
   - `/metrics` endpoint for Prometheus

2. **Logging**
   - Structured logging with Winston/Structlog
   - Log aggregation and analysis
   - Error tracking with Sentry

3. **Metrics**
   - Prometheus metrics collection
   - Custom business metrics
   - Performance monitoring

### Infrastructure Monitoring

1. **CloudWatch**
   - Application metrics
   - Infrastructure metrics
   - Custom dashboards

2. **Logging**
   - CloudTrail for API calls
   - VPC Flow Logs
   - RDS audit logs

3. **Alerting**
   - SNS notifications
   - Slack/Teams integration
   - PagerDuty escalation

## 🧪 Testing Strategy

### Application Testing

1. **Unit Tests**
   - Jest (Node.js) and pytest (Python)
   - Mock external dependencies
   - High code coverage

2. **Integration Tests**
   - API endpoint testing
   - Database integration
   - External service mocking

3. **E2E Tests**
   - Puppeteer for browser testing
   - Complete user workflows
   - Performance testing

### Infrastructure Testing

1. **Terraform Testing**
   - `terraform plan` validation
   - Security policy checking
   - Cost estimation

2. **Security Testing**
   - Infrastructure vulnerability scanning
   - Compliance checking
   - Penetration testing

## 🚀 Deployment Pipeline

### CI/CD Pipeline Stages

1. **Validate**
   - Code linting and formatting
   - Security policy checking
   - Infrastructure validation

2. **Security**
   - SAST/DAST scanning
   - Dependency vulnerability scanning
   - Container security scanning

3. **Test**
   - Unit and integration tests
   - Code coverage reporting
   - Performance testing

4. **Build**
   - Container image building
   - Security scanning
   - Artifact publishing

5. **Deploy**
   - Staging deployment
   - Production deployment
   - Rollback procedures

6. **Monitor**
   - Health checks
   - Performance monitoring
   - Alert management

### Environment Strategy

1. **Development**
   - Local development environment
   - Automated testing
   - Code quality gates

2. **Staging**
   - Production-like environment
   - Integration testing
   - Performance testing

3. **Production**
   - Blue-green deployment
   - Automated rollback
   - Monitoring and alerting

## 📈 Performance Optimization

### Application Optimization

1. **Code Optimization**
   - Efficient algorithms
   - Memory management
   - Caching strategies

2. **Database Optimization**
   - Query optimization
   - Index management
   - Connection pooling

3. **Infrastructure Optimization**
   - Auto-scaling
   - Load balancing
   - CDN integration

### Cost Optimization

1. **Resource Management**
   - Right-sizing instances
   - Reserved instances
   - Spot instances for non-critical workloads

2. **Monitoring**
   - Cost tracking
   - Resource utilization
   - Optimization recommendations

## 🔧 Troubleshooting

### Common Issues

1. **Build Failures**
   - Check dependency versions
   - Verify environment setup
   - Review build logs

2. **Security Scan Failures**
   - Update vulnerable dependencies
   - Review security policies
   - Fix code security issues

3. **Deployment Failures**
   - Check Kubernetes resources
   - Verify configuration
   - Review deployment logs

### Debug Tools

1. **Application Debugging**
   - Node.js debugger
   - Python debugger
   - Log analysis

2. **Infrastructure Debugging**
   - Terraform logs
   - AWS CloudWatch logs
   - Kubernetes logs

## 📚 Best Practices

### Security Best Practices

1. **Code Security**
   - Regular security reviews
   - Automated security scanning
   - Secure coding practices

2. **Infrastructure Security**
   - Least privilege access
   - Network segmentation
   - Encryption everywhere

3. **Compliance**
   - Regular compliance audits
   - Automated compliance checking
   - Documentation maintenance

### Performance Best Practices

1. **Application Performance**
   - Efficient algorithms
   - Caching strategies
   - Database optimization

2. **Infrastructure Performance**
   - Auto-scaling
   - Load balancing
   - CDN usage

### Operational Best Practices

1. **Monitoring**
   - Comprehensive monitoring
   - Proactive alerting
   - Performance tracking

2. **Documentation**
   - API documentation
   - Infrastructure documentation
   - Runbooks and procedures

---

These examples provide comprehensive DevSecOps implementations that can be used as templates for real-world projects. Each example includes security scanning, testing, containerization, and deployment automation with enterprise-grade features. 