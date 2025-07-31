# Node.js Application DevSecOps Example

This example demonstrates how to implement DevSecOps pipelines for a Node.js application with comprehensive security scanning, testing, and deployment.

## 📁 Project Structure

```
nodejs-application/
├── README.md
├── package.json
├── package-lock.json
├── .gitignore
├── .eslintrc.js
├── jest.config.js
├── Dockerfile
├── docker-compose.yml
├── k8s/
│   ├── dev/
│   │   ├── deployment.yml
│   │   ├── service.yml
│   │   └── ingress.yml
│   ├── staging/
│   │   ├── deployment.yml
│   │   ├── service.yml
│   │   └── ingress.yml
│   └── production/
│       ├── deployment.yml
│       ├── service.yml
│       └── ingress.yml
├── src/
│   ├── app.js
│   ├── routes/
│   │   ├── health.js
│   │   ├── users.js
│   │   └── api.js
│   ├── middleware/
│   │   ├── auth.js
│   │   ├── validation.js
│   │   └── security.js
│   ├── services/
│   │   ├── database.js
│   │   └── external-api.js
│   └── utils/
│       ├── logger.js
│       └── helpers.js
├── tests/
│   ├── unit/
│   │   ├── routes.test.js
│   │   ├── services.test.js
│   │   └── utils.test.js
│   ├── integration/
│   │   ├── api.test.js
│   │   └── database.test.js
│   └── e2e/
│       └── app.test.js
├── scripts/
│   ├── security/
│   │   ├── scan-dependencies.js
│   │   └── check-vulnerabilities.js
│   └── deployment/
│       ├── health-check.js
│       └── rollback.js
└── docs/
    ├── API.md
    ├── DEPLOYMENT.md
    └── SECURITY.md
```

## 🚀 Quick Start

### Prerequisites

1. **Node.js Environment**
   ```bash
   # Install Node.js 18.x
   curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
   sudo apt-get install -y nodejs
   
   # Verify installation
   node --version
   npm --version
   ```

2. **Docker Environment**
   ```bash
   # Install Docker
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   
   # Verify installation
   docker --version
   ```

3. **Kubernetes Environment**
   ```bash
   # Install kubectl
   curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
   sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
   
   # Verify installation
   kubectl version --client
   ```

### Installation

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd nodejs-application
   ```

2. **Install Dependencies**
   ```bash
   npm install
   ```

3. **Set Up Environment Variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. **Run Security Scans**
   ```bash
   npm run security:scan
   ```

5. **Run Tests**
   ```bash
   npm run test
   npm run test:coverage
   ```

6. **Build and Run**
   ```bash
   npm run build
   npm start
   ```

## 🔧 Configuration

### Package.json Scripts

```json
{
  "scripts": {
    "start": "node src/app.js",
    "dev": "nodemon src/app.js",
    "build": "npm run lint && npm run test",
    "test": "jest",
    "test:watch": "jest --watch",
    "test:coverage": "jest --coverage",
    "test:e2e": "jest --config jest.e2e.config.js",
    "lint": "eslint src/ tests/",
    "lint:fix": "eslint src/ tests/ --fix",
    "security:scan": "npm audit && npm run security:check-dependencies",
    "security:check-dependencies": "node scripts/security/check-vulnerabilities.js",
    "docker:build": "docker build -t nodejs-app .",
    "docker:run": "docker run -p 3000:3000 nodejs-app",
    "k8s:deploy": "kubectl apply -f k8s/",
    "k8s:deploy-dev": "kubectl apply -f k8s/dev/",
    "k8s:deploy-staging": "kubectl apply -f k8s/staging/",
    "k8s:deploy-prod": "kubectl apply -f k8s/production/"
  }
}
```

### Environment Configuration

```bash
# .env
NODE_ENV=development
PORT=3000
DATABASE_URL=mongodb://localhost:27017/nodejs-app
JWT_SECRET=your-jwt-secret
API_KEY=your-api-key
LOG_LEVEL=info
CORS_ORIGIN=http://localhost:3000
RATE_LIMIT_WINDOW=15
RATE_LIMIT_MAX=100
```

## 🔒 Security Implementation

### Security Middleware

```javascript
// src/middleware/security.js
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const cors = require('cors');

const securityMiddleware = (app) => {
  // Security headers
  app.use(helmet({
    contentSecurityPolicy: {
      directives: {
        defaultSrc: ["'self'"],
        styleSrc: ["'self'", "'unsafe-inline'"],
        scriptSrc: ["'self'"],
        imgSrc: ["'self'", "data:", "https:"],
      },
    },
    hsts: {
      maxAge: 31536000,
      includeSubDomains: true,
      preload: true
    }
  }));

  // Rate limiting
  const limiter = rateLimit({
    windowMs: 15 * 60 * 1000, // 15 minutes
    max: 100, // limit each IP to 100 requests per windowMs
    message: 'Too many requests from this IP'
  });
  app.use('/api/', limiter);

  // CORS configuration
  app.use(cors({
    origin: process.env.CORS_ORIGIN,
    credentials: true
  }));

  // Input validation
  app.use(express.json({ limit: '10mb' }));
  app.use(express.urlencoded({ extended: true, limit: '10mb' }));
};

module.exports = securityMiddleware;
```

### Authentication Middleware

```javascript
// src/middleware/auth.js
const jwt = require('jsonwebtoken');

const authenticateToken = (req, res, next) => {
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1];

  if (!token) {
    return res.status(401).json({ error: 'Access token required' });
  }

  jwt.verify(token, process.env.JWT_SECRET, (err, user) => {
    if (err) {
      return res.status(403).json({ error: 'Invalid token' });
    }
    req.user = user;
    next();
  });
};

const authorizeRole = (roles) => {
  return (req, res, next) => {
    if (!req.user) {
      return res.status(401).json({ error: 'Authentication required' });
    }

    if (!roles.includes(req.user.role)) {
      return res.status(403).json({ error: 'Insufficient permissions' });
    }

    next();
  };
};

module.exports = { authenticateToken, authorizeRole };
```

### Input Validation

```javascript
// src/middleware/validation.js
const Joi = require('joi');

const validateUser = (req, res, next) => {
  const schema = Joi.object({
    email: Joi.string().email().required(),
    password: Joi.string().min(8).pattern(new RegExp('^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])')).required(),
    name: Joi.string().min(2).max(50).required()
  });

  const { error } = schema.validate(req.body);
  if (error) {
    return res.status(400).json({ error: error.details[0].message });
  }

  next();
};

module.exports = { validateUser };
```

## 🐳 Docker Configuration

### Dockerfile

```dockerfile
# Multi-stage build for security and optimization
FROM node:18-alpine AS base

# Install security updates
RUN apk update && apk upgrade

# Create non-root user
RUN addgroup -g 1001 -S nodejs
RUN adduser -S nodejs -u 1001

# Set working directory
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci --only=production && npm cache clean --force

# Copy source code
COPY . .

# Security: Remove unnecessary files
RUN rm -rf tests/ docs/ scripts/ examples/

# Security: Set proper permissions
RUN chown -R nodejs:nodejs /app
USER nodejs

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:3000/health || exit 1

# Expose port
EXPOSE 3000

# Start application
CMD ["npm", "start"]
```

### Docker Compose

```yaml
# docker-compose.yml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=development
      - DATABASE_URL=mongodb://mongo:27017/nodejs-app
    depends_on:
      - mongo
    networks:
      - app-network

  mongo:
    image: mongo:6.0
    ports:
      - "27017:27017"
    volumes:
      - mongo-data:/data/db
    networks:
      - app-network

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    networks:
      - app-network

volumes:
  mongo-data:

networks:
  app-network:
    driver: bridge
```

## ☸️ Kubernetes Configuration

### Development Environment

```yaml
# k8s/dev/deployment.yml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nodejs-app-dev
  namespace: dev
spec:
  replicas: 2
  selector:
    matchLabels:
      app: nodejs-app
      environment: dev
  template:
    metadata:
      labels:
        app: nodejs-app
        environment: dev
    spec:
      containers:
      - name: nodejs-app
        image: nodejs-app:dev
        ports:
        - containerPort: 3000
        env:
        - name: NODE_ENV
          value: "development"
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: app-secrets
              key: database-url
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /health
            port: 3000
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /ready
            port: 3000
          initialDelaySeconds: 5
          periodSeconds: 5
```

### Production Environment

```yaml
# k8s/production/deployment.yml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nodejs-app-prod
  namespace: production
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nodejs-app
      environment: production
  template:
    metadata:
      labels:
        app: nodejs-app
        environment: production
    spec:
      containers:
      - name: nodejs-app
        image: nodejs-app:production
        ports:
        - containerPort: 3000
        env:
        - name: NODE_ENV
          value: "production"
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: app-secrets
              key: database-url
        resources:
          requests:
            memory: "512Mi"
            cpu: "500m"
          limits:
            memory: "1Gi"
            cpu: "1000m"
        securityContext:
          runAsNonRoot: true
          runAsUser: 1001
          readOnlyRootFilesystem: true
          capabilities:
            drop:
            - ALL
        livenessProbe:
          httpGet:
            path: /health
            port: 3000
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /ready
            port: 3000
          initialDelaySeconds: 5
          periodSeconds: 5
```

## 🧪 Testing Strategy

### Unit Tests

```javascript
// tests/unit/routes.test.js
const request = require('supertest');
const app = require('../../src/app');

describe('Health Route', () => {
  test('GET /health should return 200', async () => {
    const response = await request(app).get('/health');
    expect(response.status).toBe(200);
    expect(response.body).toHaveProperty('status', 'healthy');
  });
});

describe('User Routes', () => {
  test('POST /api/users should create user', async () => {
    const userData = {
      email: 'test@example.com',
      password: 'SecurePass123!',
      name: 'Test User'
    };

    const response = await request(app)
      .post('/api/users')
      .send(userData);

    expect(response.status).toBe(201);
    expect(response.body).toHaveProperty('id');
    expect(response.body.email).toBe(userData.email);
  });
});
```

### Integration Tests

```javascript
// tests/integration/api.test.js
const request = require('supertest');
const app = require('../../src/app');
const mongoose = require('mongoose');

describe('API Integration Tests', () => {
  beforeAll(async () => {
    // Connect to test database
    await mongoose.connect(process.env.TEST_DATABASE_URL);
  });

  afterAll(async () => {
    // Clean up
    await mongoose.connection.close();
  });

  test('Complete user workflow', async () => {
    // 1. Create user
    const userData = {
      email: 'integration@example.com',
      password: 'SecurePass123!',
      name: 'Integration User'
    };

    const createResponse = await request(app)
      .post('/api/users')
      .send(userData);

    expect(createResponse.status).toBe(201);
    const userId = createResponse.body.id;

    // 2. Login user
    const loginResponse = await request(app)
      .post('/api/auth/login')
      .send({
        email: userData.email,
        password: userData.password
      });

    expect(loginResponse.status).toBe(200);
    const token = loginResponse.body.token;

    // 3. Access protected route
    const protectedResponse = await request(app)
      .get('/api/users/profile')
      .set('Authorization', `Bearer ${token}`);

    expect(protectedResponse.status).toBe(200);
  });
});
```

### E2E Tests

```javascript
// tests/e2e/app.test.js
const puppeteer = require('puppeteer');

describe('End-to-End Tests', () => {
  let browser;
  let page;

  beforeAll(async () => {
    browser = await puppeteer.launch({
      headless: true,
      args: ['--no-sandbox', '--disable-setuid-sandbox']
    });
    page = await browser.newPage();
  });

  afterAll(async () => {
    await browser.close();
  });

  test('User registration and login flow', async () => {
    // Navigate to application
    await page.goto('http://localhost:3000');

    // Check if page loads
    await expect(page.title()).resolves.toMatch(/Node.js App/);

    // Navigate to registration
    await page.click('a[href="/register"]');

    // Fill registration form
    await page.type('#email', 'e2e@example.com');
    await page.type('#password', 'SecurePass123!');
    await page.type('#name', 'E2E User');

    // Submit form
    await page.click('button[type="submit"]');

    // Wait for redirect
    await page.waitForNavigation();

    // Verify successful registration
    const url = page.url();
    expect(url).toContain('/dashboard');
  });
});
```

## 🔒 Security Scripts

### Dependency Vulnerability Check

```javascript
// scripts/security/check-vulnerabilities.js
const { execSync } = require('child_process');
const fs = require('fs');

async function checkVulnerabilities() {
  try {
    console.log('🔍 Checking for vulnerabilities...');

    // Run npm audit
    const auditResult = execSync('npm audit --json', { encoding: 'utf8' });
    const auditData = JSON.parse(auditResult);

    // Check for critical and high vulnerabilities
    const criticalVulns = auditData.metadata.vulnerabilities.critical || 0;
    const highVulns = auditData.metadata.vulnerabilities.high || 0;

    if (criticalVulns > 0) {
      console.error(`❌ Critical vulnerabilities found: ${criticalVulns}`);
      process.exit(1);
    }

    if (highVulns > 5) {
      console.error(`❌ High vulnerabilities exceed threshold: ${highVulns}`);
      process.exit(1);
    }

    console.log(`✅ Security check passed. Critical: ${criticalVulns}, High: ${highVulns}`);

    // Generate security report
    const report = {
      timestamp: new Date().toISOString(),
      vulnerabilities: auditData.metadata.vulnerabilities,
      advisories: auditData.advisories
    };

    fs.writeFileSync('security-report.json', JSON.stringify(report, null, 2));
    console.log('📄 Security report generated: security-report.json');

  } catch (error) {
    console.error('❌ Security check failed:', error.message);
    process.exit(1);
  }
}

checkVulnerabilities();
```

### Health Check Script

```javascript
// scripts/deployment/health-check.js
const axios = require('axios');

async function healthCheck(url, timeout = 30000) {
  const startTime = Date.now();
  const maxAttempts = 30;
  let attempts = 0;

  while (attempts < maxAttempts) {
    try {
      console.log(`🔍 Health check attempt ${attempts + 1}/${maxAttempts}`);
      
      const response = await axios.get(`${url}/health`, {
        timeout: 5000,
        headers: {
          'User-Agent': 'Health-Check-Script'
        }
      });

      if (response.status === 200 && response.data.status === 'healthy') {
        const duration = Date.now() - startTime;
        console.log(`✅ Health check passed in ${duration}ms`);
        return true;
      }
    } catch (error) {
      console.log(`⚠️ Health check failed: ${error.message}`);
    }

    attempts++;
    await new Promise(resolve => setTimeout(resolve, 10000)); // Wait 10 seconds
  }

  console.error('❌ Health check failed after maximum attempts');
  return false;
}

// Usage
if (require.main === module) {
  const url = process.argv[2] || 'http://localhost:3000';
  healthCheck(url).then(success => {
    process.exit(success ? 0 : 1);
  });
}

module.exports = healthCheck;
```

## 📊 Monitoring and Logging

### Application Logging

```javascript
// src/utils/logger.js
const winston = require('winston');

const logger = winston.createLogger({
  level: process.env.LOG_LEVEL || 'info',
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.errors({ stack: true }),
    winston.format.json()
  ),
  defaultMeta: { service: 'nodejs-app' },
  transports: [
    new winston.transports.File({ filename: 'logs/error.log', level: 'error' }),
    new winston.transports.File({ filename: 'logs/combined.log' })
  ]
});

if (process.env.NODE_ENV !== 'production') {
  logger.add(new winston.transports.Console({
    format: winston.format.simple()
  }));
}

module.exports = logger;
```

### Metrics Collection

```javascript
// src/utils/metrics.js
const prometheus = require('prom-client');

// Create metrics
const httpRequestDuration = new prometheus.Histogram({
  name: 'http_request_duration_seconds',
  help: 'Duration of HTTP requests in seconds',
  labelNames: ['method', 'route', 'status_code']
});

const httpRequestTotal = new prometheus.Counter({
  name: 'http_requests_total',
  help: 'Total number of HTTP requests',
  labelNames: ['method', 'route', 'status_code']
});

const activeConnections = new prometheus.Gauge({
  name: 'active_connections',
  help: 'Number of active connections'
});

// Metrics middleware
const metricsMiddleware = (req, res, next) => {
  const start = Date.now();
  
  res.on('finish', () => {
    const duration = (Date.now() - start) / 1000;
    
    httpRequestDuration
      .labels(req.method, req.route?.path || req.path, res.statusCode)
      .observe(duration);
    
    httpRequestTotal
      .labels(req.method, req.route?.path || req.path, res.statusCode)
      .inc();
  });
  
  next();
};

module.exports = { metricsMiddleware, prometheus };
```

## 🚀 Deployment Pipeline

### GitLab CI/CD Pipeline

```yaml
# .gitlab-ci.yml
stages:
  - validate
  - security
  - test
  - build
  - scan
  - deploy-staging
  - deploy-production
  - monitor

variables:
  DOCKER_REGISTRY: $CI_REGISTRY
  DOCKER_IMAGE: $DOCKER_REGISTRY/$CI_PROJECT_PATH:$CI_COMMIT_SHORT_SHA

validate:
  stage: validate
  image: node:18-alpine
  script:
    - npm ci
    - npm run lint
    - npm run security:scan
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"

security:
  stage: security
  image: node:18-alpine
  script:
    - npm ci
    - npm audit --audit-level=high
    - npm run security:check-dependencies
  artifacts:
    reports:
      security: security-report.json
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"

test:
  stage: test
  image: node:18-alpine
  script:
    - npm ci
    - npm run test:coverage
  artifacts:
    reports:
      coverage_report:
        coverage_format: cobertura
        path: coverage/cobertura-coverage.xml
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"

build:
  stage: build
  image: docker:latest
  services:
    - docker:dind
  script:
    - docker build -t $DOCKER_IMAGE .
    - docker push $DOCKER_IMAGE
  rules:
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH

scan:
  stage: scan
  image: docker:latest
  services:
    - docker:dind
  script:
    - docker pull $DOCKER_IMAGE
    - docker run --rm -v /var/run/docker.sock:/var/run/docker.sock aquasec/trivy image $DOCKER_IMAGE
  rules:
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH

deploy-staging:
  stage: deploy-staging
  image: alpine:latest
  script:
    - kubectl config use-context staging-cluster
    - kubectl set image deployment/nodejs-app-dev nodejs-app=$DOCKER_IMAGE
    - kubectl rollout status deployment/nodejs-app-dev
  environment:
    name: staging
  rules:
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH
      when: manual

deploy-production:
  stage: deploy-production
  image: alpine:latest
  script:
    - kubectl config use-context production-cluster
    - kubectl set image deployment/nodejs-app-prod nodejs-app=$DOCKER_IMAGE
    - kubectl rollout status deployment/nodejs-app-prod
  environment:
    name: production
  rules:
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH
      when: manual

monitor:
  stage: monitor
  image: alpine:latest
  script:
    - node scripts/deployment/health-check.js https://app.example.com
  rules:
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH
```

## 📈 Performance Optimization

### Application Optimization

```javascript
// src/app.js
const express = require('express');
const compression = require('compression');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');

const app = express();

// Performance optimizations
app.use(compression()); // Enable gzip compression
app.use(express.static('public', { maxAge: '1d' })); // Static file caching

// Security middleware
app.use(helmet());
app.use(rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100 // limit each IP to 100 requests per windowMs
}));

// Routes
app.use('/api', require('./routes/api'));
app.use('/health', require('./routes/health'));

module.exports = app;
```

### Database Optimization

```javascript
// src/services/database.js
const mongoose = require('mongoose');

// Connection optimization
mongoose.connect(process.env.DATABASE_URL, {
  maxPoolSize: 10,
  serverSelectionTimeoutMS: 5000,
  socketTimeoutMS: 45000,
  bufferMaxEntries: 0,
  useNewUrlParser: true,
  useUnifiedTopology: true
});

// Schema optimization
const userSchema = new mongoose.Schema({
  email: {
    type: String,
    required: true,
    unique: true,
    index: true // Add index for faster queries
  },
  name: String,
  createdAt: {
    type: Date,
    default: Date.now,
    index: true // Add index for date-based queries
  }
}, {
  timestamps: true,
  toJSON: { virtuals: true },
  toObject: { virtuals: true }
});

module.exports = mongoose.model('User', userSchema);
```

## 🔧 Troubleshooting

### Common Issues

1. **Build Failures**
   ```bash
   # Check Node.js version
   node --version
   
   # Clear npm cache
   npm cache clean --force
   
   # Reinstall dependencies
   rm -rf node_modules package-lock.json
   npm install
   ```

2. **Security Scan Failures**
   ```bash
   # Update dependencies
   npm update
   
   # Check for vulnerabilities
   npm audit
   
   # Fix vulnerabilities
   npm audit fix
   ```

3. **Docker Build Issues**
   ```bash
   # Clean Docker cache
   docker system prune -a
   
   # Rebuild without cache
   docker build --no-cache -t nodejs-app .
   ```

4. **Kubernetes Deployment Issues**
   ```bash
   # Check pod status
   kubectl get pods -n <namespace>
   
   # Check pod logs
   kubectl logs <pod-name> -n <namespace>
   
   # Describe pod for details
   kubectl describe pod <pod-name> -n <namespace>
   ```

### Debug Mode

```javascript
// Enable debug logging
process.env.DEBUG = 'app:*';
process.env.LOG_LEVEL = 'debug';

// Add debug middleware
app.use((req, res, next) => {
  console.log(`${req.method} ${req.path}`);
  next();
});
```

## 📚 Best Practices

### Security Best Practices

1. **Dependency Management**
   - Regular security updates
   - Automated vulnerability scanning
   - Lock file versioning

2. **Input Validation**
   - Validate all user inputs
   - Sanitize data before processing
   - Use parameterized queries

3. **Authentication & Authorization**
   - JWT token validation
   - Role-based access control
   - Session management

4. **Data Protection**
   - Encrypt sensitive data
   - Use HTTPS in production
   - Implement rate limiting

### Performance Best Practices

1. **Caching Strategy**
   - Redis for session storage
   - CDN for static assets
   - Database query optimization

2. **Monitoring**
   - Application metrics
   - Error tracking
   - Performance monitoring

3. **Scaling**
   - Horizontal scaling with Kubernetes
   - Load balancing
   - Auto-scaling policies

---

This Node.js application example demonstrates a complete DevSecOps implementation with security scanning, testing, containerization, and deployment automation. The example includes all necessary configurations for enterprise-grade security and compliance. 