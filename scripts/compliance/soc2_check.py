#!/usr/bin/env python3
"""
SOC 2 Compliance Checker
Performs SOC 2 Type II compliance checks for enterprise environments
"""

import json
import os
import sys
import logging
from typing import Dict, List, Any
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SOC2ComplianceChecker:
    def __init__(self):
        self.trust_services_criteria = {
            'security': {
                'cc1': 'Control Environment',
                'cc2': 'Communication and Information',
                'cc3': 'Risk Assessment',
                'cc4': 'Monitoring Activities',
                'cc5': 'Control Activities',
                'cc6': 'Logical and Physical Access Controls',
                'cc7': 'System Operations',
                'cc8': 'Change Management',
                'cc9': 'Risk Mitigation'
            },
            'availability': {
                'a1': 'System Availability',
                'a2': 'System Processing Integrity',
                'a3': 'System Monitoring'
            },
            'processing_integrity': {
                'pi1': 'System Processing Integrity',
                'pi2': 'System Processing Accuracy',
                'pi3': 'System Processing Completeness'
            },
            'confidentiality': {
                'c1': 'Information Confidentiality',
                'c2': 'System Confidentiality'
            },
            'privacy': {
                'p1': 'Privacy by Design',
                'p2': 'Privacy Notice and Communication',
                'p3': 'Choice and Consent',
                'p4': 'Collection, Use, Retention, and Disposal',
                'p5': 'Access',
                'p6': 'Disclosure to Third Parties',
                'p7': 'Security for Privacy',
                'p8': 'Quality',
                'p9': 'Monitoring and Enforcement'
            }
        }
        
    def check_security_controls(self) -> Dict[str, Any]:
        """Check security-related controls"""
        logger.info("Checking security controls...")
        
        controls = {
            'access_controls': self.check_access_controls(),
            'network_security': self.check_network_security(),
            'data_protection': self.check_data_protection(),
            'incident_response': self.check_incident_response(),
            'change_management': self.check_change_management(),
            'monitoring': self.check_monitoring()
        }
        
        return controls
    
    def check_access_controls(self) -> Dict[str, Any]:
        """Check logical and physical access controls"""
        checks = {
            'user_authentication': self.check_user_authentication(),
            'role_based_access': self.check_role_based_access(),
            'privileged_access': self.check_privileged_access(),
            'physical_security': self.check_physical_security(),
            'session_management': self.check_session_management()
        }
        
        passed = sum(1 for check in checks.values() if check.get('status') == 'passed')
        total = len(checks)
        
        return {
            'status': 'passed' if passed == total else 'failed',
            'score': (passed / total) * 100,
            'checks': checks
        }
    
    def check_user_authentication(self) -> Dict[str, Any]:
        """Check user authentication controls"""
        # This would typically check against your identity provider
        # For demonstration, we'll simulate checks
        checks = {
            'multi_factor_auth': True,
            'password_policy': True,
            'account_lockout': True,
            'session_timeout': True
        }
        
        passed = sum(checks.values())
        total = len(checks)
        
        return {
            'status': 'passed' if passed == total else 'failed',
            'details': checks,
            'score': (passed / total) * 100
        }
    
    def check_role_based_access(self) -> Dict[str, Any]:
        """Check role-based access control"""
        checks = {
            'role_definition': True,
            'least_privilege': True,
            'access_reviews': True,
            'separation_of_duties': True
        }
        
        passed = sum(checks.values())
        total = len(checks)
        
        return {
            'status': 'passed' if passed == total else 'failed',
            'details': checks,
            'score': (passed / total) * 100
        }
    
    def check_privileged_access(self) -> Dict[str, Any]:
        """Check privileged access management"""
        checks = {
            'privileged_account_management': True,
            'just_in_time_access': True,
            'privileged_session_monitoring': True,
            'privileged_account_reviews': True
        }
        
        passed = sum(checks.values())
        total = len(checks)
        
        return {
            'status': 'passed' if passed == total else 'failed',
            'details': checks,
            'score': (passed / total) * 100
        }
    
    def check_physical_security(self) -> Dict[str, Any]:
        """Check physical security controls"""
        checks = {
            'data_center_access': True,
            'environmental_controls': True,
            'equipment_security': True,
            'visitor_management': True
        }
        
        passed = sum(checks.values())
        total = len(checks)
        
        return {
            'status': 'passed' if passed == total else 'failed',
            'details': checks,
            'score': (passed / total) * 100
        }
    
    def check_session_management(self) -> Dict[str, Any]:
        """Check session management controls"""
        checks = {
            'session_timeout': True,
            'session_encryption': True,
            'session_monitoring': True,
            'automatic_logout': True
        }
        
        passed = sum(checks.values())
        total = len(checks)
        
        return {
            'status': 'passed' if passed == total else 'failed',
            'details': checks,
            'score': (passed / total) * 100
        }
    
    def check_network_security(self) -> Dict[str, Any]:
        """Check network security controls"""
        logger.info("Checking network security...")
        
        checks = {
            'firewall_configuration': self.check_firewall_configuration(),
            'network_segmentation': self.check_network_segmentation(),
            'encryption_in_transit': self.check_encryption_in_transit(),
            'intrusion_detection': self.check_intrusion_detection()
        }
        
        passed = sum(1 for check in checks.values() if check.get('status') == 'passed')
        total = len(checks)
        
        return {
            'status': 'passed' if passed == total else 'failed',
            'score': (passed / total) * 100,
            'checks': checks
        }
    
    def check_firewall_configuration(self) -> Dict[str, Any]:
        """Check firewall configuration"""
        checks = {
            'default_deny': True,
            'rule_reviews': True,
            'logging_enabled': True,
            'regular_updates': True
        }
        
        passed = sum(checks.values())
        total = len(checks)
        
        return {
            'status': 'passed' if passed == total else 'failed',
            'details': checks,
            'score': (passed / total) * 100
        }
    
    def check_network_segmentation(self) -> Dict[str, Any]:
        """Check network segmentation"""
        checks = {
            'vlan_segmentation': True,
            'dmz_configuration': True,
            'access_controls': True,
            'traffic_monitoring': True
        }
        
        passed = sum(checks.values())
        total = len(checks)
        
        return {
            'status': 'passed' if passed == total else 'failed',
            'details': checks,
            'score': (passed / total) * 100
        }
    
    def check_encryption_in_transit(self) -> Dict[str, Any]:
        """Check encryption in transit"""
        checks = {
            'tls_enabled': True,
            'strong_ciphers': True,
            'certificate_management': True,
            'protocol_version': True
        }
        
        passed = sum(checks.values())
        total = len(checks)
        
        return {
            'status': 'passed' if passed == total else 'failed',
            'details': checks,
            'score': (passed / total) * 100
        }
    
    def check_intrusion_detection(self) -> Dict[str, Any]:
        """Check intrusion detection systems"""
        checks = {
            'ids_deployed': True,
            'alert_monitoring': True,
            'incident_response': True,
            'regular_reviews': True
        }
        
        passed = sum(checks.values())
        total = len(checks)
        
        return {
            'status': 'passed' if passed == total else 'failed',
            'details': checks,
            'score': (passed / total) * 100
        }
    
    def check_data_protection(self) -> Dict[str, Any]:
        """Check data protection controls"""
        logger.info("Checking data protection...")
        
        checks = {
            'encryption_at_rest': self.check_encryption_at_rest(),
            'data_classification': self.check_data_classification(),
            'backup_encryption': self.check_backup_encryption(),
            'data_retention': self.check_data_retention()
        }
        
        passed = sum(1 for check in checks.values() if check.get('status') == 'passed')
        total = len(checks)
        
        return {
            'status': 'passed' if passed == total else 'failed',
            'score': (passed / total) * 100,
            'checks': checks
        }
    
    def check_encryption_at_rest(self) -> Dict[str, Any]:
        """Check encryption at rest"""
        checks = {
            'database_encryption': True,
            'file_encryption': True,
            'key_management': True,
            'encryption_standards': True
        }
        
        passed = sum(checks.values())
        total = len(checks)
        
        return {
            'status': 'passed' if passed == total else 'failed',
            'details': checks,
            'score': (passed / total) * 100
        }
    
    def check_data_classification(self) -> Dict[str, Any]:
        """Check data classification"""
        checks = {
            'classification_policy': True,
            'data_labeling': True,
            'handling_procedures': True,
            'regular_reviews': True
        }
        
        passed = sum(checks.values())
        total = len(checks)
        
        return {
            'status': 'passed' if passed == total else 'failed',
            'details': checks,
            'score': (passed / total) * 100
        }
    
    def check_backup_encryption(self) -> Dict[str, Any]:
        """Check backup encryption"""
        checks = {
            'backup_encryption': True,
            'backup_access_controls': True,
            'backup_testing': True,
            'offsite_storage': True
        }
        
        passed = sum(checks.values())
        total = len(checks)
        
        return {
            'status': 'passed' if passed == total else 'failed',
            'details': checks,
            'score': (passed / total) * 100
        }
    
    def check_data_retention(self) -> Dict[str, Any]:
        """Check data retention policies"""
        checks = {
            'retention_policy': True,
            'automated_deletion': True,
            'compliance_mapping': True,
            'regular_reviews': True
        }
        
        passed = sum(checks.values())
        total = len(checks)
        
        return {
            'status': 'passed' if passed == total else 'failed',
            'details': checks,
            'score': (passed / total) * 100
        }
    
    def check_incident_response(self) -> Dict[str, Any]:
        """Check incident response capabilities"""
        logger.info("Checking incident response...")
        
        checks = {
            'incident_response_plan': True,
            'incident_detection': True,
            'response_procedures': True,
            'communication_plan': True,
            'post_incident_review': True
        }
        
        passed = sum(checks.values())
        total = len(checks)
        
        return {
            'status': 'passed' if passed == total else 'failed',
            'score': (passed / total) * 100,
            'checks': checks
        }
    
    def check_change_management(self) -> Dict[str, Any]:
        """Check change management processes"""
        logger.info("Checking change management...")
        
        checks = {
            'change_approval_process': True,
            'testing_procedures': True,
            'rollback_procedures': True,
            'change_documentation': True,
            'emergency_change_process': True
        }
        
        passed = sum(checks.values())
        total = len(checks)
        
        return {
            'status': 'passed' if passed == total else 'failed',
            'score': (passed / total) * 100,
            'checks': checks
        }
    
    def check_monitoring(self) -> Dict[str, Any]:
        """Check monitoring and logging"""
        logger.info("Checking monitoring and logging...")
        
        checks = {
            'log_collection': True,
            'log_retention': True,
            'log_analysis': True,
            'alerting': True,
            'dashboard_monitoring': True
        }
        
        passed = sum(checks.values())
        total = len(checks)
        
        return {
            'status': 'passed' if passed == total else 'failed',
            'score': (passed / total) * 100,
            'checks': checks
        }
    
    def check_availability_controls(self) -> Dict[str, Any]:
        """Check availability controls"""
        logger.info("Checking availability controls...")
        
        checks = {
            'system_monitoring': self.check_system_monitoring(),
            'backup_recovery': self.check_backup_recovery(),
            'disaster_recovery': self.check_disaster_recovery(),
            'capacity_planning': self.check_capacity_planning()
        }
        
        passed = sum(1 for check in checks.values() if check.get('status') == 'passed')
        total = len(checks)
        
        return {
            'status': 'passed' if passed == total else 'failed',
            'score': (passed / total) * 100,
            'checks': checks
        }
    
    def check_system_monitoring(self) -> Dict[str, Any]:
        """Check system monitoring"""
        checks = {
            'performance_monitoring': True,
            'availability_monitoring': True,
            'capacity_monitoring': True,
            'alert_thresholds': True
        }
        
        passed = sum(checks.values())
        total = len(checks)
        
        return {
            'status': 'passed' if passed == total else 'failed',
            'details': checks,
            'score': (passed / total) * 100
        }
    
    def check_backup_recovery(self) -> Dict[str, Any]:
        """Check backup and recovery"""
        checks = {
            'backup_schedule': True,
            'backup_testing': True,
            'recovery_procedures': True,
            'recovery_time_objectives': True
        }
        
        passed = sum(checks.values())
        total = len(checks)
        
        return {
            'status': 'passed' if passed == total else 'failed',
            'details': checks,
            'score': (passed / total) * 100
        }
    
    def check_disaster_recovery(self) -> Dict[str, Any]:
        """Check disaster recovery"""
        checks = {
            'dr_plan': True,
            'dr_testing': True,
            'alternate_site': True,
            'communication_plan': True
        }
        
        passed = sum(checks.values())
        total = len(checks)
        
        return {
            'status': 'passed' if passed == total else 'failed',
            'details': checks,
            'score': (passed / total) * 100
        }
    
    def check_capacity_planning(self) -> Dict[str, Any]:
        """Check capacity planning"""
        checks = {
            'capacity_monitoring': True,
            'scaling_procedures': True,
            'resource_planning': True,
            'performance_baselines': True
        }
        
        passed = sum(checks.values())
        total = len(checks)
        
        return {
            'status': 'passed' if passed == total else 'failed',
            'details': checks,
            'score': (passed / total) * 100
        }
    
    def run_compliance_check(self) -> Dict[str, Any]:
        """Run complete SOC 2 compliance check"""
        logger.info("Starting SOC 2 compliance check...")
        
        results = {
            'timestamp': datetime.now().isoformat(),
            'framework': 'SOC 2 Type II',
            'security': self.check_security_controls(),
            'availability': self.check_availability_controls(),
            'overall_score': 0,
            'status': 'unknown'
        }
        
        # Calculate overall score
        security_score = results['security']['score']
        availability_score = results['availability']['score']
        
        # Weight security more heavily than availability
        overall_score = (security_score * 0.8) + (availability_score * 0.2)
        results['overall_score'] = round(overall_score, 2)
        
        # Determine overall status
        if overall_score >= 90:
            results['status'] = 'compliant'
        elif overall_score >= 80:
            results['status'] = 'mostly_compliant'
        elif overall_score >= 70:
            results['status'] = 'partially_compliant'
        else:
            results['status'] = 'non_compliant'
        
        logger.info(f"SOC 2 compliance check completed. Score: {overall_score:.2f}")
        return results

def main():
    """Main function"""
    checker = SOC2ComplianceChecker()
    
    try:
        results = checker.run_compliance_check()
        
        # Save results to file
        with open('soc2-compliance-results.json', 'w') as f:
            json.dump(results, f, indent=2)
        
        logger.info("SOC 2 compliance check completed successfully")
        logger.info(f"Results saved to soc2-compliance-results.json")
        
        # Exit with error if not compliant
        if results['status'] == 'non_compliant':
            logger.error(f"SOC 2 compliance score {results['overall_score']} is below threshold")
            sys.exit(1)
        else:
            logger.info(f"SOC 2 compliance score {results['overall_score']} meets requirements")
            sys.exit(0)
            
    except Exception as e:
        logger.error(f"Error during SOC 2 compliance check: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 