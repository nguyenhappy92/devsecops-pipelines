#!/usr/bin/env python3
"""
Security Score Calculator
Calculates overall security score based on various security metrics
"""

import json
import os
import sys
from typing import Dict, List, Any
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SecurityScoreCalculator:
    def __init__(self):
        self.weights = {
            'sast': 0.25,
            'dast': 0.20,
            'sca': 0.20,
            'container_security': 0.15,
            'compliance': 0.20
        }
        
    def load_scan_results(self, file_path: str) -> Dict[str, Any]:
        """Load scan results from JSON file"""
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.warning(f"File not found: {file_path}")
            return {}
        except json.JSONDecodeError:
            logger.error(f"Invalid JSON in file: {file_path}")
            return {}

    def calculate_sast_score(self, sast_results: Dict[str, Any]) -> float:
        """Calculate SAST security score"""
        if not sast_results:
            return 0.0
            
        total_issues = 0
        critical_issues = 0
        high_issues = 0
        medium_issues = 0
        
        # Parse SAST results (adjust based on your SAST tool output format)
        if 'results' in sast_results:
            for result in sast_results['results']:
                severity = result.get('level', 'medium').lower()
                if severity == 'critical':
                    critical_issues += 1
                elif severity == 'high':
                    high_issues += 1
                elif severity == 'medium':
                    medium_issues += 1
                total_issues += 1
        
        # Calculate score based on issues
        if total_issues == 0:
            return 100.0
            
        # Penalize based on severity
        score = 100.0
        score -= critical_issues * 20  # -20 points per critical
        score -= high_issues * 10      # -10 points per high
        score -= medium_issues * 5     # -5 points per medium
        
        return max(0.0, score)

    def calculate_dast_score(self, dast_results: Dict[str, Any]) -> float:
        """Calculate DAST security score"""
        if not dast_results:
            return 0.0
            
        total_vulnerabilities = 0
        critical_vulnerabilities = 0
        high_vulnerabilities = 0
        
        # Parse DAST results (adjust based on your DAST tool output format)
        if 'vulnerabilities' in dast_results:
            for vuln in dast_results['vulnerabilities']:
                severity = vuln.get('risk', 'medium').lower()
                if severity == 'critical':
                    critical_vulnerabilities += 1
                elif severity == 'high':
                    high_vulnerabilities += 1
                total_vulnerabilities += 1
        
        # Calculate score
        if total_vulnerabilities == 0:
            return 100.0
            
        score = 100.0
        score -= critical_vulnerabilities * 25  # -25 points per critical
        score -= high_vulnerabilities * 15      # -15 points per high
        
        return max(0.0, score)

    def calculate_sca_score(self, sca_results: Dict[str, Any]) -> float:
        """Calculate Software Composition Analysis score"""
        if not sca_results:
            return 0.0
            
        total_dependencies = 0
        vulnerable_dependencies = 0
        critical_vulnerabilities = 0
        
        # Parse SCA results
        if 'dependencies' in sca_results:
            for dep in sca_results['dependencies']:
                total_dependencies += 1
                if dep.get('vulnerabilities'):
                    vulnerable_dependencies += 1
                    for vuln in dep['vulnerabilities']:
                        if vuln.get('severity') == 'critical':
                            critical_vulnerabilities += 1
        
        # Calculate score
        if total_dependencies == 0:
            return 100.0
            
        vulnerability_rate = vulnerable_dependencies / total_dependencies
        score = 100.0 - (vulnerability_rate * 50)  # -50 points for 100% vulnerable
        score -= critical_vulnerabilities * 10      # -10 points per critical vuln
        
        return max(0.0, score)

    def calculate_container_security_score(self, container_results: Dict[str, Any]) -> float:
        """Calculate container security score"""
        if not container_results:
            return 0.0
            
        total_vulnerabilities = 0
        critical_vulnerabilities = 0
        high_vulnerabilities = 0
        
        # Parse container scan results
        if 'vulnerabilities' in container_results:
            for vuln in container_results['vulnerabilities']:
                severity = vuln.get('severity', 'medium').lower()
                if severity == 'critical':
                    critical_vulnerabilities += 1
                elif severity == 'high':
                    high_vulnerabilities += 1
                total_vulnerabilities += 1
        
        # Calculate score
        if total_vulnerabilities == 0:
            return 100.0
            
        score = 100.0
        score -= critical_vulnerabilities * 20  # -20 points per critical
        score -= high_vulnerabilities * 10      # -10 points per high
        
        return max(0.0, score)

    def calculate_compliance_score(self, compliance_results: Dict[str, Any]) -> float:
        """Calculate compliance score"""
        if not compliance_results:
            return 0.0
            
        total_checks = 0
        passed_checks = 0
        
        # Parse compliance results
        if 'checks' in compliance_results:
            for check in compliance_results['checks']:
                total_checks += 1
                if check.get('status') == 'passed':
                    passed_checks += 1
        
        # Calculate score
        if total_checks == 0:
            return 100.0
            
        return (passed_checks / total_checks) * 100.0

    def calculate_overall_score(self) -> Dict[str, Any]:
        """Calculate overall security score"""
        logger.info("Calculating security scores...")
        
        # Load scan results
        sast_results = self.load_scan_results('sast-results.json')
        dast_results = self.load_scan_results('dast-results.json')
        sca_results = self.load_scan_results('sca-results.json')
        container_results = self.load_scan_results('container-results.json')
        compliance_results = self.load_scan_results('compliance-results.json')
        
        # Calculate individual scores
        sast_score = self.calculate_sast_score(sast_results)
        dast_score = self.calculate_dast_score(dast_results)
        sca_score = self.calculate_sca_score(sca_results)
        container_score = self.calculate_container_security_score(container_results)
        compliance_score = self.calculate_compliance_score(compliance_results)
        
        # Calculate weighted overall score
        overall_score = (
            sast_score * self.weights['sast'] +
            dast_score * self.weights['dast'] +
            sca_score * self.weights['sca'] +
            container_score * self.weights['container_security'] +
            compliance_score * self.weights['compliance']
        )
        
        # Determine security grade
        if overall_score >= 90:
            grade = 'A'
        elif overall_score >= 80:
            grade = 'B'
        elif overall_score >= 70:
            grade = 'C'
        elif overall_score >= 60:
            grade = 'D'
        else:
            grade = 'F'
        
        # Prepare results
        results = {
            'overall_score': round(overall_score, 2),
            'grade': grade,
            'component_scores': {
                'sast': round(sast_score, 2),
                'dast': round(dast_score, 2),
                'sca': round(sca_score, 2),
                'container_security': round(container_score, 2),
                'compliance': round(compliance_score, 2)
            },
            'weights': self.weights,
            'recommendations': self.generate_recommendations({
                'sast': sast_score,
                'dast': dast_score,
                'sca': sca_score,
                'container_security': container_score,
                'compliance': compliance_score
            })
        }
        
        logger.info(f"Overall security score: {overall_score:.2f} ({grade})")
        return results

    def generate_recommendations(self, scores: Dict[str, float]) -> List[str]:
        """Generate security recommendations based on scores"""
        recommendations = []
        
        if scores['sast'] < 80:
            recommendations.append("Improve SAST coverage and fix critical/high severity issues")
        
        if scores['dast'] < 80:
            recommendations.append("Enhance DAST testing and address web application vulnerabilities")
        
        if scores['sca'] < 80:
            recommendations.append("Update vulnerable dependencies and implement dependency scanning")
        
        if scores['container_security'] < 80:
            recommendations.append("Harden container images and fix container vulnerabilities")
        
        if scores['compliance'] < 80:
            recommendations.append("Address compliance gaps and implement security controls")
        
        if not recommendations:
            recommendations.append("Maintain current security practices and continue monitoring")
        
        return recommendations

def main():
    """Main function"""
    calculator = SecurityScoreCalculator()
    
    try:
        results = calculator.calculate_overall_score()
        
        # Save results to file
        with open('security-score.json', 'w') as f:
            json.dump(results, f, indent=2)
        
        logger.info("Security score calculation completed successfully")
        logger.info(f"Results saved to security-score.json")
        
        # Exit with error if score is too low
        if results['overall_score'] < 70:
            logger.error(f"Security score {results['overall_score']} is below threshold")
            sys.exit(1)
        else:
            logger.info(f"Security score {results['overall_score']} meets requirements")
            sys.exit(0)
            
    except Exception as e:
        logger.error(f"Error calculating security score: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 