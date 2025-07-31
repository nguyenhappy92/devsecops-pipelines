# Terraform Infrastructure for DevSecOps
# Multi-environment infrastructure with security and compliance

terraform {
  required_version = ">= 1.5.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.0"
    }
  }
}

# Provider configuration
provider "aws" {
  region = var.aws_region
  
  default_tags {
    tags = {
      Environment = var.environment
      Project     = var.project_name
      ManagedBy   = "Terraform"
      Owner       = "DevSecOps"
    }
  }
}

# VPC and Networking
module "vpc" {
  source = "./modules/vpc"
  
  environment    = var.environment
  vpc_cidr      = var.vpc_cidr
  azs           = var.availability_zones
  public_subnets  = var.public_subnet_cidrs
  private_subnets = var.private_subnet_cidrs
}

# EKS Cluster
module "eks" {
  source = "./modules/eks"
  
  cluster_name    = "${var.project_name}-${var.environment}"
  cluster_version = "1.27"
  vpc_id          = module.vpc.vpc_id
  subnet_ids      = module.vpc.private_subnet_ids
  
  node_groups = {
    main = {
      desired_capacity = var.environment == "production" ? 3 : 2
      max_capacity     = var.environment == "production" ? 5 : 3
      min_capacity     = var.environment == "production" ? 2 : 1
      
      instance_types = ["t3.medium"]
      capacity_type  = "ON_DEMAND"
    }
  }
}

# Container Registry (ECR)
module "ecr" {
  source = "./modules/ecr"
  
  repository_name = "${var.project_name}-app"
  environment     = var.environment
}

# Security Groups
module "security_groups" {
  source = "./modules/security_groups"
  
  vpc_id      = module.vpc.vpc_id
  environment = var.environment
}

# Load Balancer
module "alb" {
  source = "./modules/alb"
  
  vpc_id         = module.vpc.vpc_id
  subnets        = module.vpc.public_subnet_ids
  security_groups = [module.security_groups.alb_sg_id]
  environment    = var.environment
}

# Database (RDS)
module "rds" {
  source = "./modules/rds"
  
  vpc_id         = module.vpc.vpc_id
  subnets        = module.vpc.private_subnet_ids
  security_groups = [module.security_groups.rds_sg_id]
  environment    = var.environment
  
  # Security: Enable encryption and monitoring
  storage_encrypted = true
  monitoring_interval = 60
  monitoring_role_arn = module.iam.rds_monitoring_role_arn
}

# IAM Roles and Policies
module "iam" {
  source = "./modules/iam"
  
  cluster_name = module.eks.cluster_name
  environment  = var.environment
}

# CloudWatch Logging
module "cloudwatch" {
  source = "./modules/cloudwatch"
  
  environment = var.environment
  cluster_name = module.eks.cluster_name
}

# WAF for Application Load Balancer
module "waf" {
  source = "./modules/waf"
  
  alb_arn     = module.alb.alb_arn
  environment = var.environment
}

# Backup and Recovery
module "backup" {
  source = "./modules/backup"
  
  environment = var.environment
  resources = [
    module.rds.db_instance_arn,
    module.ecr.repository_arn
  ]
}

# Monitoring and Alerting
module "monitoring" {
  source = "./modules/monitoring"
  
  environment = var.environment
  cluster_name = module.eks.cluster_name
  alb_arn = module.alb.alb_arn
  rds_arn = module.rds.db_instance_arn
}

# Outputs
output "cluster_endpoint" {
  description = "EKS cluster endpoint"
  value       = module.eks.cluster_endpoint
}

output "cluster_name" {
  description = "EKS cluster name"
  value       = module.eks.cluster_name
}

output "repository_url" {
  description = "ECR repository URL"
  value       = module.ecr.repository_url
}

output "alb_dns_name" {
  description = "Application Load Balancer DNS name"
  value       = module.alb.alb_dns_name
}

output "database_endpoint" {
  description = "RDS database endpoint"
  value       = module.rds.db_endpoint
  sensitive   = true
} 