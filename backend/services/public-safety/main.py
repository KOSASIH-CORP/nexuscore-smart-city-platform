from emergency_response.services import EmergencyResponseService
from crime_reporting.services import CrimeReportingService
from safety_analytics.services import SafetyAnalyticsService

emergency_response_service = EmergencyResponseService()
crime_reporting_service = CrimeReportingService()
safety_analytics_service = SafetyAnalyticsService()

def handle_emergency_response(emergency_response: EmergencyResponse):
    emergency_response_service.create_emergency_response(emergency_response)

def handle_crime_report(crime_report: CrimeReport):
    crime_reporting_service.create_crime_report(crime_report)

def handle_safety_analytics(safety_analytics: SafetyAnalytics):
    safety_analytics_service.create_safety_analytics(safety_analytics)
