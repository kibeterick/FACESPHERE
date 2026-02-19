"""
Web Dashboard for AKIRA System - Real-time Monitoring
"""
from datetime import datetime
import json


class WebDashboard:
    """Web-based dashboard for system monitoring and control"""
    
    def __init__(self):
        self.dashboard_data = {
            'system_status': 'online',
            'uptime': datetime.now(),
            'active_users': 0,
            'alerts': [],
            'metrics': {}
        }
    
    def generate_dashboard_html(self):
        """Generate HTML dashboard"""
        html = """
<!DOCTYPE html>
<html>
<head>
    <title>AKIRA AI System Dashboard</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #333;
            padding: 20px;
        }
        .container {
            max-width: 1400px;
            margin: 0 auto;
        }
        .header {
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            margin-bottom: 30px;
        }
        .header h1 {
            color: #667eea;
            font-size: 2.5em;
            margin-bottom: 10px;
        }
        .status-badge {
            display: inline-block;
            padding: 8px 20px;
            background: #10b981;
            color: white;
            border-radius: 20px;
            font-weight: bold;
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        .card {
            background: white;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        .card h2 {
            color: #667eea;
            margin-bottom: 15px;
            font-size: 1.3em;
        }
        .metric {
            display: flex;
            justify-content: space-between;
            padding: 10px 0;
            border-bottom: 1px solid #eee;
        }
        .metric:last-child { border-bottom: none; }
        .metric-value {
            font-weight: bold;
            color: #667eea;
            font-size: 1.2em;
        }
        .alert {
            padding: 15px;
            background: #fef3c7;
            border-left: 4px solid #f59e0b;
            margin-bottom: 10px;
            border-radius: 5px;
        }
        .alert.critical {
            background: #fee2e2;
            border-left-color: #ef4444;
        }
        .button {
            display: inline-block;
            padding: 12px 24px;
            background: #667eea;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 1em;
            margin: 5px;
            text-decoration: none;
        }
        .button:hover {
            background: #5568d3;
        }
        .chart-placeholder {
            height: 200px;
            background: linear-gradient(to right, #667eea, #764ba2);
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 1.2em;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🤖 AKIRA AI System Dashboard</h1>
            <p>Real-time monitoring and control</p>
            <span class="status-badge">● SYSTEM ONLINE</span>
        </div>
        
        <div class="grid">
            <div class="card">
                <h2>📊 System Overview</h2>
                <div class="metric">
                    <span>Status</span>
                    <span class="metric-value">Online</span>
                </div>
                <div class="metric">
                    <span>Active Users</span>
                    <span class="metric-value">5</span>
                </div>
                <div class="metric">
                    <span>Total Interactions</span>
                    <span class="metric-value">1,247</span>
                </div>
                <div class="metric">
                    <span>Uptime</span>
                    <span class="metric-value">99.9%</span>
                </div>
            </div>
            
            <div class="card">
                <h2>🤖 Virtual Assistant</h2>
                <div class="metric">
                    <span>Tasks Completed</span>
                    <span class="metric-value">342</span>
                </div>
                <div class="metric">
                    <span>Avg Response Time</span>
                    <span class="metric-value">0.8s</span>
                </div>
                <div class="metric">
                    <span>Satisfaction Score</span>
                    <span class="metric-value">4.8/5</span>
                </div>
            </div>
            
            <div class="card">
                <h2>🎥 Surveillance</h2>
                <div class="metric">
                    <span>Active Cameras</span>
                    <span class="metric-value">4</span>
                </div>
                <div class="metric">
                    <span>Detections Today</span>
                    <span class="metric-value">127</span>
                </div>
                <div class="metric">
                    <span>Security Alerts</span>
                    <span class="metric-value">2</span>
                </div>
            </div>
            
            <div class="card">
                <h2>📊 Marketing</h2>
                <div class="metric">
                    <span>Active Campaigns</span>
                    <span class="metric-value">3</span>
                </div>
                <div class="metric">
                    <span>Total Customers</span>
                    <span class="metric-value">1,523</span>
                </div>
                <div class="metric">
                    <span>Conversion Rate</span>
                    <span class="metric-value">12.4%</span>
                </div>
            </div>
        </div>
        
        <div class="grid">
            <div class="card">
                <h2>🚨 Recent Alerts</h2>
                <div class="alert">
                    <strong>⚠️ High CPU Usage</strong><br>
                    CPU usage at 85% - Consider optimization
                </div>
                <div class="alert critical">
                    <strong>🚨 Unauthorized Access Attempt</strong><br>
                    Unknown person detected at front door
                </div>
            </div>
            
            <div class="card">
                <h2>📈 Activity Chart</h2>
                <div class="chart-placeholder">
                    📊 Real-time Activity Graph
                </div>
            </div>
        </div>
        
        <div class="card">
            <h2>⚙️ Quick Actions</h2>
            <button class="button">🔄 Refresh Data</button>
            <button class="button">📊 View Reports</button>
            <button class="button">⚙️ System Settings</button>
            <button class="button">👥 User Management</button>
            <button class="button">🎥 View Cameras</button>
            <button class="button">📧 Send Notification</button>
        </div>
    </div>
</body>
</html>
        """
        return html
    
    def save_dashboard(self, filename='dashboard.html'):
        """Save dashboard to HTML file"""
        html = self.generate_dashboard_html()
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"✅ Dashboard saved to {filename}")
            print(f"   Open in browser: file://{filename}")
            return True
        except Exception as e:
            print(f"❌ Error saving dashboard: {e}")
            return False
    
    def get_system_metrics(self):
        """Get current system metrics"""
        return {
            'timestamp': datetime.now().isoformat(),
            'system_status': 'online',
            'cpu_usage': 45.2,
            'memory_usage': 62.8,
            'disk_usage': 58.3,
            'active_users': 5,
            'total_interactions': 1247,
            'uptime_percentage': 99.9
        }
    
    def get_module_status(self):
        """Get status of all modules"""
        return {
            'virtual_assistant': {
                'status': 'online',
                'tasks_completed': 342,
                'avg_response_time': 0.8,
                'satisfaction_score': 4.8
            },
            'surveillance': {
                'status': 'online',
                'active_cameras': 4,
                'detections_today': 127,
                'security_alerts': 2
            },
            'marketing': {
                'status': 'online',
                'active_campaigns': 3,
                'total_customers': 1523,
                'conversion_rate': 12.4
            },
            'iot': {
                'status': 'online',
                'connected_devices': 12,
                'energy_usage': '2.4 kWh'
            }
        }
    
    def generate_report(self, report_type='daily'):
        """Generate system report"""
        report = {
            'report_type': report_type,
            'generated_at': datetime.now().isoformat(),
            'summary': {
                'total_interactions': 1247,
                'unique_users': 45,
                'tasks_completed': 342,
                'alerts_triggered': 8,
                'system_uptime': '99.9%'
            },
            'highlights': [
                'Peak usage at 2:00 PM with 156 interactions',
                'Customer satisfaction increased by 12%',
                'Zero critical security incidents',
                'Energy consumption reduced by 8%'
            ],
            'recommendations': [
                'Consider scaling up during peak hours',
                'Update surveillance camera firmware',
                'Launch new marketing campaign for segment A'
            ]
        }
        
        return report
    
    def export_data(self, format='json'):
        """Export dashboard data"""
        data = {
            'metrics': self.get_system_metrics(),
            'module_status': self.get_module_status(),
            'timestamp': datetime.now().isoformat()
        }
        
        if format == 'json':
            return json.dumps(data, indent=2)
        else:
            return str(data)
