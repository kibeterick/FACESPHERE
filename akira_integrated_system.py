"""
AKIRA - Complete AI System Integration
Combines Virtual Assistant, Smart Surveillance, and Personalized Marketing
"""
import time
from datetime import datetime
from akira_assistant import Akira
from smart_surveillance import SmartSurveillance
from personalized_marketing import PersonalizedMarketing
from face_recognition_module import FaceConnect


class AkiraIntegratedSystem:
    """Complete Akira AI System with all three modules"""
    
    def __init__(self):
        print("🚀 Initializing AKIRA AI System...")
        
        # Initialize all modules
        self.akira = Akira()
        self.surveillance = SmartSurveillance()
        self.marketing = PersonalizedMarketing()
        self.face_connect = FaceConnect()
        
        self.current_user = None
        print("✅ AKIRA System ready!")
    
    def demo_virtual_assistant(self):
        """Demo Akira Virtual Assistant features"""
        print("\n" + "="*60)
        print("🤖 AKIRA VIRTUAL ASSISTANT DEMO")
        print("="*60)
        
        # Greeting
        greeting = self.akira.greet_user("Erick")
        print(f"\n{greeting}")
        
        time.sleep(1)
        
        # Task management
        print("\n--- Task Management ---")
        print(self.akira.process_command("Schedule a meeting tomorrow at 3 PM"))
        print(self.akira.process_command("Remind me to call John"))
        print(self.akira.get_tasks())
        
        time.sleep(1)
        
        # Information queries
        print("\n--- Information Queries ---")
        print(self.akira.process_command("What's the weather like?"))
        print(self.akira.process_command("Show me the news"))
        
        time.sleep(1)
        
        # Calculations
        print("\n--- Smart Calculations ---")
        print(self.akira.process_command("Calculate 25 plus 17"))
        print(self.akira.process_command("What is 100 divided by 4"))
        
        time.sleep(1)
        
        # Learning preferences
        print("\n--- Learning User Preferences ---")
        print(self.akira.learn_preference("music_genre", "Jazz"))
        print(self.akira.learn_preference("work_hours", "9 AM - 5 PM"))
        
        time.sleep(1)
        
        # Task automation
        print("\n--- Task Automation ---")
        print(self.akira.automate_task("email"))
        print(self.akira.automate_task("backup"))
        
        time.sleep(1)
        
        # Sentiment analysis
        print("\n--- Sentiment Analysis ---")
        sentiment, score = self.akira.analyze_sentiment("This is an amazing product! I love it!")
        print(f"Sentiment: {sentiment} (Score: {score})")
        
        sentiment, score = self.akira.analyze_sentiment("This is terrible and disappointing.")
        print(f"Sentiment: {sentiment} (Score: {score})")
    
    def demo_smart_surveillance(self):
        """Demo Smart Surveillance features"""
        print("\n" + "="*60)
        print("🎥 SMART SURVEILLANCE DEMO")
        print("="*60)
        
        # Access control
        print("\n--- Access Control System ---")
        self.surveillance.add_authorized_person("Erick")
        self.surveillance.add_authorized_person("John")
        self.surveillance.add_authorized_person("Sarah")
        
        time.sleep(1)
        
        # Test access control
        print("\n--- Testing Access Control ---")
        print("Checking access for Erick...")
        if self.surveillance.check_access_control("Erick"):
            print("✅ Access granted to Erick")
        
        print("\nChecking access for Unknown Person...")
        if not self.surveillance.check_access_control("Unknown"):
            print("❌ Access denied to Unknown Person")
        
        time.sleep(1)
        
        # View logs
        print("\n--- Access Logs ---")
        print(self.surveillance.get_access_log())
        
        time.sleep(1)
        
        # View alerts
        print("\n--- Security Alerts ---")
        print(self.surveillance.get_alerts())
        
        time.sleep(1)
        
        # Pattern analysis
        print("\n--- Pattern Analysis ---")
        print(self.surveillance.analyze_patterns())
        
        print("\n💡 Tip: Run mode 5 to start live surveillance monitoring")
    
    def demo_personalized_marketing(self):
        """Demo Personalized Marketing features"""
        print("\n" + "="*60)
        print("📊 PERSONALIZED MARKETING DEMO")
        print("="*60)
        
        # Add customers
        print("\n--- Adding Customer Profiles ---")
        self.marketing.add_customer("CUST001", {
            'name': 'Alice Johnson',
            'age': 28,
            'location': 'New York'
        })
        self.marketing.customers['CUST001']['lifetime_value'] = 1200
        self.marketing.customers['CUST001']['engagement_score'] = 85
        
        self.marketing.add_customer("CUST002", {
            'name': 'Bob Smith',
            'age': 35,
            'location': 'Los Angeles'
        })
        self.marketing.customers['CUST002']['lifetime_value'] = 600
        self.marketing.customers['CUST002']['engagement_score'] = 55
        
        self.marketing.add_customer("CUST003", {
            'name': 'Carol White',
            'age': 42,
            'location': 'Chicago'
        })
        self.marketing.customers['CUST003']['lifetime_value'] = 300
        self.marketing.customers['CUST003']['engagement_score'] = 30
        
        time.sleep(1)
        
        # Customer profiling
        print("\n--- Customer Profiling ---")
        for cust_id in ['CUST001', 'CUST002', 'CUST003']:
            profile = self.marketing.profile_customer(cust_id)
            print(f"\n{cust_id}:")
            print(f"  Tier: {profile['tier']}")
            print(f"  Engagement: {profile['engagement_score']}")
            print(f"  Lifetime Value: ${profile['lifetime_value']}")
        
        time.sleep(1)
        
        # Customer segmentation
        print("\n--- Customer Segmentation (ML) ---")
        result = self.marketing.segment_customers()
        print(result)
        
        for cust_id in ['CUST001', 'CUST002', 'CUST003']:
            segment = self.marketing.customers[cust_id]['segment']
            print(f"{cust_id}: {segment}")
        
        time.sleep(1)
        
        # Create targeted campaigns
        print("\n--- Creating Targeted Campaigns ---")
        campaign1 = self.marketing.create_targeted_campaign('High-Value', 'VIP Offer')
        print(f"\nCampaign: {campaign1['id']}")
        print(f"  Target: {campaign1['segment']}")
        print(f"  Offer: {campaign1['discount']}")
        print(f"  Message: {campaign1['message']}")
        
        campaign2 = self.marketing.create_targeted_campaign('Medium-Value', 'Special Deal')
        print(f"\nCampaign: {campaign2['id']}")
        print(f"  Target: {campaign2['segment']}")
        print(f"  Offer: {campaign2['discount']}")
        
        time.sleep(1)
        
        # Send targeted ads
        print("\n--- Sending Targeted Advertisements ---")
        print(self.marketing.send_targeted_ad('CUST001', campaign1['id']))
        print(self.marketing.send_targeted_ad('CUST002', campaign2['id']))
        
        time.sleep(1)
        
        # Sentiment analysis
        print("\n--- Customer Feedback Sentiment Analysis ---")
        feedback1 = "This product is amazing! Best purchase ever!"
        result1 = self.marketing.analyze_sentiment('CUST001', feedback1)
        print(f"\nFeedback: '{feedback1}'")
        print(f"Sentiment: {result1['sentiment']} (Score: {result1['score']})")
        print(f"Recommendation: {result1['recommendation']}")
        
        feedback2 = "Very disappointed with the service. Not good at all."
        result2 = self.marketing.analyze_sentiment('CUST002', feedback2)
        print(f"\nFeedback: '{feedback2}'")
        print(f"Sentiment: {result2['sentiment']} (Score: {result2['score']})")
        print(f"Recommendation: {result2['recommendation']}")
        
        time.sleep(1)
        
        # Product recommendations
        print("\n--- AI Product Recommendations ---")
        for cust_id in ['CUST001', 'CUST002', 'CUST003']:
            rec = self.marketing.recommend_products(cust_id)
            print(f"\n{cust_id} ({rec['segment']}):")
            print(f"  Recommended: {', '.join(rec['recommended_products'])}")
        
        time.sleep(1)
        
        # Campaign optimization
        print("\n--- Campaign Optimization ---")
        campaign1['conversions'] = 3
        optimization = self.marketing.optimize_campaign(campaign1['id'])
        print(f"\nCampaign {optimization['campaign_id']}:")
        print(f"  Reach: {optimization['reach']}")
        print(f"  Conversions: {optimization['conversions']}")
        print(f"  Conversion Rate: {optimization['conversion_rate']}")
        print(f"  Recommendations:")
        for rec in optimization['recommendations']:
            print(f"    - {rec}")
        
        time.sleep(1)
        
        # Overall insights
        print("\n--- Customer Insights Dashboard ---")
        insights = self.marketing.get_customer_insights()
        print(f"\nTotal Customers: {insights['total_customers']}")
        print(f"Total Lifetime Value: ${insights['total_lifetime_value']}")
        print(f"Average Engagement: {insights['average_engagement']}")
        print(f"Active Campaigns: {insights['active_campaigns']}")
        print(f"Segment Distribution: {insights['segment_distribution']}")
    
    def run_complete_demo(self):
        """Run complete system demo"""
        print("\n" + "="*60)
        print("🚀 AKIRA COMPLETE AI SYSTEM DEMO")
        print("="*60)
        print("\nDemonstrating all three integrated modules:")
        print("1. Virtual Assistant (NLP + ML)")
        print("2. Smart Surveillance (Computer Vision + ML)")
        print("3. Personalized Marketing (ML + NLP)")
        
        input("\nPress Enter to start...")
        
        # Demo each module
        self.demo_virtual_assistant()
        input("\nPress Enter to continue to Smart Surveillance...")
        
        self.demo_smart_surveillance()
        input("\nPress Enter to continue to Personalized Marketing...")
        
        self.demo_personalized_marketing()
        
        print("\n" + "="*60)
        print("✨ COMPLETE DEMO FINISHED!")
        print("="*60)
        print("\nAKIRA AI System is ready for production use!")


def main():
    print("\n" + "="*60)
    print("🤖 AKIRA - Advanced AI System")
    print("="*60)
    print("\nIntegrated Modules:")
    print("  1. Virtual Assistant (Akira) - NLP & ML")
    print("  2. Smart Surveillance - Computer Vision & ML")
    print("  3. Personalized Marketing - ML & NLP")
    print("="*60)
    
    system = AkiraIntegratedSystem()
    
    print("\nSelect Mode:")
    print("1. Complete System Demo (All Modules)")
    print("2. Virtual Assistant Demo Only")
    print("3. Smart Surveillance Demo Only")
    print("4. Personalized Marketing Demo Only")
    print("5. Live Surveillance Monitoring")
    print("6. Interactive Marketing Console")
    
    try:
        choice = input("\nEnter choice (1-6): ").strip()
        
        if choice == "1":
            system.run_complete_demo()
        elif choice == "2":
            system.demo_virtual_assistant()
        elif choice == "3":
            system.demo_smart_surveillance()
        elif choice == "4":
            system.demo_personalized_marketing()
        elif choice == "5":
            print("\n🎥 Starting live surveillance...")
            print("Press 'q' in the camera window to quit")
            system.surveillance.start_monitoring()
        elif choice == "6":
            print("\n📊 Marketing Console")
            print("Feature coming soon - use mode 4 for demo")
        else:
            print("Invalid choice. Running complete demo...")
            system.run_complete_demo()
            
    except KeyboardInterrupt:
        print("\n\n👋 Shutting down AKIRA system...")


if __name__ == "__main__":
    main()
