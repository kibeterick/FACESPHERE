"""
Personalized Marketing System with ML and NLP
"""
import random
from datetime import datetime
from collections import defaultdict

try:
    from sklearn.cluster import KMeans
    import numpy as np
    ML_AVAILABLE = True
except ImportError:
    ML_AVAILABLE = False
    print("⚠️  scikit-learn not available. Install for ML features.")


class PersonalizedMarketing:
    """AI-Powered Personalized Marketing System"""
    
    def __init__(self):
        self.customers = {}
        self.segments = {}
        self.campaigns = []
        self.interactions = []
        
    def add_customer(self, customer_id, profile):
        """Add customer profile"""
        self.customers[customer_id] = {
            'profile': profile,
            'interactions': [],
            'preferences': {},
            'segment': None,
            'lifetime_value': 0,
            'engagement_score': 0
        }
        print(f"✅ Customer {customer_id} added")
    
    def profile_customer(self, customer_id):
        """Create detailed customer profile"""
        if customer_id not in self.customers:
            return "Customer not found"
        
        customer = self.customers[customer_id]
        
        # Calculate engagement score
        interaction_count = len(customer['interactions'])
        customer['engagement_score'] = min(100, interaction_count * 10)
        
        # Determine customer tier
        if customer['lifetime_value'] > 1000:
            tier = "Premium"
        elif customer['lifetime_value'] > 500:
            tier = "Gold"
        else:
            tier = "Standard"
        
        return {
            'customer_id': customer_id,
            'tier': tier,
            'engagement_score': customer['engagement_score'],
            'lifetime_value': customer['lifetime_value'],
            'segment': customer['segment']
        }
    
    def segment_customers(self):
        """Segment customers using ML clustering"""
        if len(self.customers) < 3:
            return "Need at least 3 customers for segmentation"
        
        if not ML_AVAILABLE:
            # Simple rule-based segmentation
            return self._rule_based_segmentation()
        
        try:
            # Prepare data for clustering
            customer_ids = list(self.customers.keys())
            features = []
            
            for cid in customer_ids:
                customer = self.customers[cid]
                features.append([
                    customer['engagement_score'],
                    customer['lifetime_value'],
                    len(customer['interactions'])
                ])
            
            X = np.array(features)
            
            # K-means clustering
            n_clusters = min(3, len(customer_ids))
            kmeans = KMeans(n_clusters=n_clusters, random_state=42)
            labels = kmeans.fit_predict(X)
            
            # Assign segments
            segment_names = ['High-Value', 'Medium-Value', 'Low-Value']
            for i, cid in enumerate(customer_ids):
                self.customers[cid]['segment'] = segment_names[labels[i]]
            
            return f"✅ Customers segmented into {n_clusters} groups"
            
        except Exception as e:
            return f"Segmentation error: {e}"
    
    def _rule_based_segmentation(self):
        """Simple rule-based customer segmentation"""
        for cid, customer in self.customers.items():
            if customer['lifetime_value'] > 1000 and customer['engagement_score'] > 70:
                customer['segment'] = 'High-Value'
            elif customer['lifetime_value'] > 500 or customer['engagement_score'] > 50:
                customer['segment'] = 'Medium-Value'
            else:
                customer['segment'] = 'Low-Value'
        
        return "✅ Customers segmented using rule-based approach"
    
    def create_targeted_campaign(self, segment, offer_type):
        """Create targeted marketing campaign"""
        campaign = {
            'id': f"CAMP_{len(self.campaigns) + 1}",
            'segment': segment,
            'offer_type': offer_type,
            'created': datetime.now(),
            'status': 'active',
            'reach': 0,
            'conversions': 0
        }
        
        # Customize offer based on segment
        if segment == 'High-Value':
            campaign['discount'] = '20% VIP Discount'
            campaign['message'] = "Exclusive offer for our premium customers!"
        elif segment == 'Medium-Value':
            campaign['discount'] = '15% Special Offer'
            campaign['message'] = "Thank you for being a valued customer!"
        else:
            campaign['discount'] = '10% Welcome Discount'
            campaign['message'] = "Special offer just for you!"
        
        self.campaigns.append(campaign)
        return campaign
    
    def send_targeted_ad(self, customer_id, campaign_id):
        """Send targeted advertisement to customer"""
        if customer_id not in self.customers:
            return "Customer not found"
        
        customer = self.customers[customer_id]
        campaign = next((c for c in self.campaigns if c['id'] == campaign_id), None)
        
        if not campaign:
            return "Campaign not found"
        
        # Check if customer matches campaign segment
        if customer['segment'] != campaign['segment']:
            return "Customer not in target segment"
        
        # Record interaction
        interaction = {
            'type': 'ad_sent',
            'campaign_id': campaign_id,
            'timestamp': datetime.now()
        }
        customer['interactions'].append(interaction)
        campaign['reach'] += 1
        
        return f"📧 Sent {campaign['message']} with {campaign['discount']} to {customer_id}"
    
    def analyze_sentiment(self, customer_id, feedback):
        """Analyze customer feedback sentiment"""
        positive_words = ['great', 'excellent', 'love', 'amazing', 'wonderful', 'good', 'best']
        negative_words = ['bad', 'terrible', 'hate', 'awful', 'poor', 'worst', 'disappointed']
        
        feedback_lower = feedback.lower()
        
        pos_count = sum(1 for word in positive_words if word in feedback_lower)
        neg_count = sum(1 for word in negative_words if word in feedback_lower)
        
        if pos_count > neg_count:
            sentiment = "positive"
            score = min(100, pos_count * 20)
        elif neg_count > pos_count:
            sentiment = "negative"
            score = max(0, 100 - neg_count * 20)
        else:
            sentiment = "neutral"
            score = 50
        
        # Store sentiment
        if customer_id in self.customers:
            self.customers[customer_id]['interactions'].append({
                'type': 'feedback',
                'sentiment': sentiment,
                'score': score,
                'timestamp': datetime.now()
            })
        
        return {
            'sentiment': sentiment,
            'score': score,
            'recommendation': self._get_sentiment_recommendation(sentiment)
        }
    
    def _get_sentiment_recommendation(self, sentiment):
        """Get recommendation based on sentiment"""
        if sentiment == "positive":
            return "Customer is satisfied. Consider upselling or loyalty rewards."
        elif sentiment == "negative":
            return "Customer needs attention. Reach out with support or compensation."
        else:
            return "Monitor customer engagement and gather more feedback."
    
    def optimize_campaign(self, campaign_id):
        """Optimize campaign based on performance"""
        campaign = next((c for c in self.campaigns if c['id'] == campaign_id), None)
        
        if not campaign:
            return "Campaign not found"
        
        # Calculate conversion rate
        conversion_rate = (campaign['conversions'] / campaign['reach'] * 100) if campaign['reach'] > 0 else 0
        
        recommendations = []
        
        if conversion_rate < 5:
            recommendations.append("Low conversion rate. Consider improving offer or targeting.")
        elif conversion_rate < 15:
            recommendations.append("Moderate performance. Test different messaging.")
        else:
            recommendations.append("Good performance! Scale up this campaign.")
        
        if campaign['reach'] < 10:
            recommendations.append("Low reach. Expand target audience.")
        
        return {
            'campaign_id': campaign_id,
            'reach': campaign['reach'],
            'conversions': campaign['conversions'],
            'conversion_rate': f"{conversion_rate:.1f}%",
            'recommendations': recommendations
        }
    
    def get_customer_insights(self):
        """Get overall customer insights"""
        if not self.customers:
            return "No customer data available"
        
        total_customers = len(self.customers)
        total_value = sum(c['lifetime_value'] for c in self.customers.values())
        avg_engagement = sum(c['engagement_score'] for c in self.customers.values()) / total_customers
        
        # Segment distribution
        segment_dist = defaultdict(int)
        for customer in self.customers.values():
            if customer['segment']:
                segment_dist[customer['segment']] += 1
        
        insights = {
            'total_customers': total_customers,
            'total_lifetime_value': total_value,
            'average_engagement': f"{avg_engagement:.1f}",
            'segment_distribution': dict(segment_dist),
            'active_campaigns': len([c for c in self.campaigns if c['status'] == 'active'])
        }
        
        return insights
    
    def recommend_products(self, customer_id):
        """Recommend products based on customer profile"""
        if customer_id not in self.customers:
            return "Customer not found"
        
        customer = self.customers[customer_id]
        segment = customer['segment']
        
        # Product recommendations based on segment
        recommendations = {
            'High-Value': ['Premium Package', 'VIP Membership', 'Exclusive Products'],
            'Medium-Value': ['Popular Items', 'Bundle Deals', 'Seasonal Offers'],
            'Low-Value': ['Starter Pack', 'Trial Offers', 'Budget-Friendly Options']
        }
        
        products = recommendations.get(segment, ['General Products'])
        
        return {
            'customer_id': customer_id,
            'segment': segment,
            'recommended_products': products,
            'reason': f"Based on {segment} customer profile"
        }
