"""
Database Manager - Data Persistence and Storage
"""
import json
import sqlite3
from datetime import datetime
import os


class DatabaseManager:
    """Manage data persistence with SQLite"""
    
    def __init__(self, db_path='akira_data.db'):
        self.db_path = db_path
        self.conn = None
        self.initialize_database()
    
    def initialize_database(self):
        """Create database tables"""
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        cursor = self.conn.cursor()
        
        # Users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT,
                phone TEXT,
                face_encoding BLOB,
                preferences TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_seen TIMESTAMP
            )
        ''')
        
        # Interactions table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS interactions (
                interaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT,
                interaction_type TEXT,
                content TEXT,
                sentiment TEXT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            )
        ''')
        
        # Surveillance logs table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS surveillance_logs (
                log_id INTEGER PRIMARY KEY AUTOINCREMENT,
                event_type TEXT,
                person_id TEXT,
                location TEXT,
                confidence REAL,
                image_path TEXT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Marketing campaigns table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS campaigns (
                campaign_id TEXT PRIMARY KEY,
                name TEXT,
                segment TEXT,
                offer_type TEXT,
                discount TEXT,
                status TEXT,
                reach INTEGER DEFAULT 0,
                conversions INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Customer profiles table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                customer_id TEXT PRIMARY KEY,
                name TEXT,
                email TEXT,
                segment TEXT,
                lifetime_value REAL DEFAULT 0,
                engagement_score INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # IoT devices table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS iot_devices (
                device_id TEXT PRIMARY KEY,
                device_type TEXT,
                name TEXT,
                status TEXT,
                last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # System logs table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS system_logs (
                log_id INTEGER PRIMARY KEY AUTOINCREMENT,
                level TEXT,
                module TEXT,
                message TEXT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        self.conn.commit()
        print("✅ Database initialized")
    
    # User Management
    def add_user(self, user_id, name, email=None, phone=None, preferences=None):
        """Add a new user"""
        cursor = self.conn.cursor()
        prefs_json = json.dumps(preferences) if preferences else None
        
        cursor.execute('''
            INSERT OR REPLACE INTO users (user_id, name, email, phone, preferences)
            VALUES (?, ?, ?, ?, ?)
        ''', (user_id, name, email, phone, prefs_json))
        
        self.conn.commit()
        return True
    
    def get_user(self, user_id):
        """Get user information"""
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
        row = cursor.fetchone()
        
        if row:
            return {
                'user_id': row[0],
                'name': row[1],
                'email': row[2],
                'phone': row[3],
                'preferences': json.loads(row[5]) if row[5] else {},
                'created_at': row[6],
                'last_seen': row[7]
            }
        return None
    
    def update_user_last_seen(self, user_id):
        """Update user's last seen timestamp"""
        cursor = self.conn.cursor()
        cursor.execute('''
            UPDATE users SET last_seen = ? WHERE user_id = ?
        ''', (datetime.now(), user_id))
        self.conn.commit()
    
    # Interaction Logging
    def log_interaction(self, user_id, interaction_type, content, sentiment=None):
        """Log user interaction"""
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO interactions (user_id, interaction_type, content, sentiment)
            VALUES (?, ?, ?, ?)
        ''', (user_id, interaction_type, content, sentiment))
        self.conn.commit()
        return cursor.lastrowid
    
    def get_user_interactions(self, user_id, limit=50):
        """Get user's interaction history"""
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT * FROM interactions 
            WHERE user_id = ? 
            ORDER BY timestamp DESC 
            LIMIT ?
        ''', (user_id, limit))
        
        rows = cursor.fetchall()
        return [{
            'interaction_id': row[0],
            'user_id': row[1],
            'type': row[2],
            'content': row[3],
            'sentiment': row[4],
            'timestamp': row[5]
        } for row in rows]
    
    # Surveillance Logging
    def log_surveillance_event(self, event_type, person_id=None, location=None, confidence=None):
        """Log surveillance event"""
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO surveillance_logs (event_type, person_id, location, confidence)
            VALUES (?, ?, ?, ?)
        ''', (event_type, person_id, location, confidence))
        self.conn.commit()
        return cursor.lastrowid
    
    def get_surveillance_logs(self, hours=24, limit=100):
        """Get recent surveillance logs"""
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT * FROM surveillance_logs 
            WHERE timestamp > datetime('now', '-' || ? || ' hours')
            ORDER BY timestamp DESC 
            LIMIT ?
        ''', (hours, limit))
        
        rows = cursor.fetchall()
        return [{
            'log_id': row[0],
            'event_type': row[1],
            'person_id': row[2],
            'location': row[3],
            'confidence': row[4],
            'timestamp': row[6]
        } for row in rows]
    
    # Marketing Data
    def save_campaign(self, campaign_id, name, segment, offer_type, discount, status='active'):
        """Save marketing campaign"""
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO campaigns 
            (campaign_id, name, segment, offer_type, discount, status)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (campaign_id, name, segment, offer_type, discount, status))
        self.conn.commit()
        return True
    
    def update_campaign_metrics(self, campaign_id, reach=None, conversions=None):
        """Update campaign metrics"""
        cursor = self.conn.cursor()
        
        if reach is not None:
            cursor.execute('''
                UPDATE campaigns SET reach = reach + ? WHERE campaign_id = ?
            ''', (reach, campaign_id))
        
        if conversions is not None:
            cursor.execute('''
                UPDATE campaigns SET conversions = conversions + ? WHERE campaign_id = ?
            ''', (conversions, campaign_id))
        
        self.conn.commit()
        return True
    
    def get_campaign(self, campaign_id):
        """Get campaign details"""
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM campaigns WHERE campaign_id = ?', (campaign_id,))
        row = cursor.fetchone()
        
        if row:
            return {
                'campaign_id': row[0],
                'name': row[1],
                'segment': row[2],
                'offer_type': row[3],
                'discount': row[4],
                'status': row[5],
                'reach': row[6],
                'conversions': row[7],
                'created_at': row[8]
            }
        return None
    
    # Customer Management
    def save_customer(self, customer_id, name, email, segment, lifetime_value, engagement_score):
        """Save customer profile"""
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO customers 
            (customer_id, name, email, segment, lifetime_value, engagement_score)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (customer_id, name, email, segment, lifetime_value, engagement_score))
        self.conn.commit()
        return True
    
    def get_customer(self, customer_id):
        """Get customer profile"""
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM customers WHERE customer_id = ?', (customer_id,))
        row = cursor.fetchone()
        
        if row:
            return {
                'customer_id': row[0],
                'name': row[1],
                'email': row[2],
                'segment': row[3],
                'lifetime_value': row[4],
                'engagement_score': row[5],
                'created_at': row[6]
            }
        return None
    
    # IoT Device Management
    def register_iot_device(self, device_id, device_type, name, status='offline'):
        """Register IoT device"""
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO iot_devices (device_id, device_type, name, status)
            VALUES (?, ?, ?, ?)
        ''', (device_id, device_type, name, status))
        self.conn.commit()
        return True
    
    def update_device_status(self, device_id, status):
        """Update device status"""
        cursor = self.conn.cursor()
        cursor.execute('''
            UPDATE iot_devices SET status = ?, last_updated = ? WHERE device_id = ?
        ''', (status, datetime.now(), device_id))
        self.conn.commit()
        return True
    
    # System Logging
    def log_system_event(self, level, module, message):
        """Log system event"""
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO system_logs (level, module, message)
            VALUES (?, ?, ?)
        ''', (level, module, message))
        self.conn.commit()
        return cursor.lastrowid
    
    def get_system_logs(self, level=None, limit=100):
        """Get system logs"""
        cursor = self.conn.cursor()
        
        if level:
            cursor.execute('''
                SELECT * FROM system_logs 
                WHERE level = ?
                ORDER BY timestamp DESC 
                LIMIT ?
            ''', (level, limit))
        else:
            cursor.execute('''
                SELECT * FROM system_logs 
                ORDER BY timestamp DESC 
                LIMIT ?
            ''', (limit,))
        
        rows = cursor.fetchall()
        return [{
            'log_id': row[0],
            'level': row[1],
            'module': row[2],
            'message': row[3],
            'timestamp': row[4]
        } for row in rows]
    
    # Analytics
    def get_user_statistics(self):
        """Get user statistics"""
        cursor = self.conn.cursor()
        
        cursor.execute('SELECT COUNT(*) FROM users')
        total_users = cursor.fetchone()[0]
        
        cursor.execute('''
            SELECT COUNT(*) FROM users 
            WHERE last_seen > datetime('now', '-24 hours')
        ''')
        active_users = cursor.fetchone()[0]
        
        return {
            'total_users': total_users,
            'active_users_24h': active_users
        }
    
    def get_interaction_statistics(self):
        """Get interaction statistics"""
        cursor = self.conn.cursor()
        
        cursor.execute('SELECT COUNT(*) FROM interactions')
        total_interactions = cursor.fetchone()[0]
        
        cursor.execute('''
            SELECT sentiment, COUNT(*) 
            FROM interactions 
            WHERE sentiment IS NOT NULL 
            GROUP BY sentiment
        ''')
        sentiment_dist = dict(cursor.fetchall())
        
        return {
            'total_interactions': total_interactions,
            'sentiment_distribution': sentiment_dist
        }
    
    def close(self):
        """Close database connection"""
        if self.conn:
            self.conn.close()
            print("Database connection closed")
