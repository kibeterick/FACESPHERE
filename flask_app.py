"""
AKIRA Flask Web Application
Web interface and REST API for the AKIRA AI System
"""
from flask import Flask, render_template, request, jsonify, send_file
from datetime import datetime
import json
import os
import sys

# Force reload of modules in debug mode
if '--reload' in sys.argv or os.environ.get('FLASK_DEBUG') == '1':
    import importlib
    
# Import AKIRA modules
try:
    # Try to import enhanced assistant first
    try:
        from ai_assistant_enhanced import EnhancedAkira as Akira
        print("✅ Using Enhanced AI Assistant")
    except ImportError:
        from akira_assistant import Akira
        print("ℹ️  Using Standard Assistant")
    
    from smart_surveillance import SmartSurveillance
    from personalized_marketing import PersonalizedMarketing
    from advanced_ai_engine import AdvancedAIEngine
    from iot_integration import IoTController
    from database_manager import DatabaseManager
    from notification_system import NotificationSystem
    from web_dashboard import WebDashboard
    from interactive_assistant import InteractiveAssistant
    from user_profile import user_profile_manager
    from weather_service import weather_service
    from calendar_scheduler import calendar
    from email_service import email_service
    from video_call_system import video_call_system
    from payment_system import payment_system
    MODULES_AVAILABLE = True
except ImportError as e:
    print(f"⚠️  Some modules not available: {e}")
    MODULES_AVAILABLE = False

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'akira-secret-key-change-in-production'

# Initialize AKIRA modules
if MODULES_AVAILABLE:
    akira = Akira()
    surveillance = SmartSurveillance()
    marketing = PersonalizedMarketing()
    ai_engine = AdvancedAIEngine()
    iot = IoTController()
    database = DatabaseManager()
    notifications = NotificationSystem()
    dashboard = WebDashboard()
    interactive = InteractiveAssistant("Erick Too")  # Initialize with user name
    
    # Setup demo IoT devices
    iot.register_device('light_001', 'light', 'Living Room Light', ['on', 'off', 'dim'])
    iot.register_device('thermo_001', 'thermostat', 'Main Thermostat', ['temperature'])
    iot.register_device('lock_001', 'lock', 'Front Door Lock', ['lock', 'unlock'])
    
    print("✅ All AKIRA modules initialized successfully")


# ==================== WEB ROUTES ====================

@app.route('/')
def index():
    """Main dashboard page"""
    return render_template('index.html')

@app.route('/dashboard')
def dashboard_page():
    """Dashboard page"""
    if not MODULES_AVAILABLE:
        return "Modules not available", 500
    
    metrics = dashboard.get_system_metrics()
    module_status = dashboard.get_module_status()
    
    return render_template('dashboard.html', 
                         metrics=metrics, 
                         module_status=module_status)

@app.route('/assistant')
def assistant_page():
    """Virtual assistant page"""
    return render_template('assistant.html')

@app.route('/iot')
def iot_page():
    """IoT control page"""
    if not MODULES_AVAILABLE:
        return "Modules not available", 500
    
    devices = iot.get_device_status()
    return render_template('iot.html', devices=devices)

@app.route('/surveillance')
def surveillance_page():
    """Surveillance page"""
    return render_template('surveillance.html')

@app.route('/marketing')
def marketing_page():
    """Marketing page"""
    return render_template('marketing.html')

@app.route('/notifications')
def notifications_page():
    """Notifications page"""
    return render_template('notifications.html')

@app.route('/calendar')
def calendar_page():
    """Calendar & Scheduling page"""
    return render_template('calendar.html')

@app.route('/email')
def email_page():
    """Email Management page"""
    return render_template('email.html')

@app.route('/email/diagnostics')
def email_diagnostics_page():
    """Email Diagnostics page"""
    return render_template('email_diagnostics.html')

@app.route('/video-calls')
def video_calls_page():
    """Video Calls page"""
    return render_template('video_calls.html')

@app.route('/payments')
def payments_page():
    """Payment Processing page"""
    return render_template('payments.html')

@app.route('/interactive')
def interactive_page():
    """Interactive Assistant page - Voice, Music, Detection & Alerts"""
    return render_template('interactive.html')


# ==================== API ROUTES ====================

@app.route('/api/status')
def api_status():
    """Get system status"""
    return jsonify({
        'status': 'online',
        'timestamp': datetime.now().isoformat(),
        'modules_available': MODULES_AVAILABLE
    })

@app.route('/api/assistant/command', methods=['POST'])
def api_assistant_command():
    """Process assistant command"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    data = request.get_json()
    command = data.get('command', '')
    
    if not command:
        return jsonify({'error': 'No command provided'}), 400
    
    response = akira.process_command(command)
    
    return jsonify({
        'command': command,
        'response': response,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/assistant/tasks')
def api_assistant_tasks():
    """Get assistant tasks"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    tasks = akira.get_tasks()
    
    return jsonify({
        'tasks': tasks,
        'count': len(akira.tasks)
    })

@app.route('/api/iot/devices')
def api_iot_devices():
    """Get all IoT devices"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    devices = iot.get_device_status()
    
    return jsonify({
        'devices': devices,
        'count': len(devices)
    })

@app.route('/api/iot/control', methods=['POST'])
def api_iot_control():
    """Control IoT device"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    data = request.get_json()
    device_id = data.get('device_id')
    action = data.get('action')
    params = data.get('params', {})
    
    if not device_id or not action:
        return jsonify({'error': 'Missing device_id or action'}), 400
    
    # Get device type
    device = iot.devices.get(device_id)
    if not device:
        return jsonify({'error': 'Device not found'}), 404
    
    # Control based on device type
    if device['type'] == 'light':
        result = iot.control_light(device_id, action, params.get('brightness', 100))
    elif device['type'] == 'thermostat':
        result = iot.control_thermostat(device_id, params.get('temperature', 72))
    elif device['type'] == 'lock':
        result = iot.control_lock(device_id, action)
    else:
        result = "Device type not supported"
    
    return jsonify({
        'device_id': device_id,
        'action': action,
        'result': result,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/iot/voice', methods=['POST'])
def api_iot_voice():
    """Voice control for IoT"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    data = request.get_json()
    command = data.get('command', '')
    
    if not command:
        return jsonify({'error': 'No command provided'}), 400
    
    result = iot.voice_control(command)
    
    return jsonify({
        'command': command,
        'result': result,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/iot/energy')
def api_iot_energy():
    """Get energy monitoring data"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    energy = iot.energy_monitoring()
    
    return jsonify(energy)

@app.route('/api/surveillance/status')
def api_surveillance_status():
    """Get surveillance status"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    return jsonify({
        'monitoring': surveillance.is_monitoring,
        'authorized_persons': surveillance.authorized_persons,
        'alerts_count': len(surveillance.alerts)
    })

@app.route('/api/surveillance/alerts')
def api_surveillance_alerts():
    """Get surveillance alerts"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    alerts = surveillance.get_alerts()
    
    return jsonify({
        'alerts': alerts,
        'count': len(surveillance.alerts)
    })

@app.route('/api/marketing/customers')
def api_marketing_customers():
    """Get customer insights"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    insights = marketing.get_customer_insights()
    
    return jsonify(insights)

@app.route('/api/marketing/campaign', methods=['POST'])
def api_marketing_campaign():
    """Create marketing campaign"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    data = request.get_json()
    segment = data.get('segment')
    offer_type = data.get('offer_type')
    
    if not segment or not offer_type:
        return jsonify({'error': 'Missing segment or offer_type'}), 400
    
    campaign = marketing.create_targeted_campaign(segment, offer_type)
    
    return jsonify(campaign)

@app.route('/api/ai/predict', methods=['POST'])
def api_ai_predict():
    """Get AI predictions"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    data = request.get_json()
    user_id = data.get('user_id', 'default_user')
    
    predictions = ai_engine.predict_user_behavior(user_id)
    recommendations = ai_engine.generate_recommendations(user_id)
    
    return jsonify({
        'predictions': predictions,
        'recommendations': recommendations,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/notifications/send', methods=['POST'])
def api_send_notification():
    """Send notification"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    data = request.get_json()
    notification_type = data.get('type', 'system')
    recipient = data.get('recipient')
    message = data.get('message')
    
    if not recipient or not message:
        return jsonify({'error': 'Missing recipient or message'}), 400
    
    if notification_type == 'email':
        result = notifications.send_email(recipient, 'AKIRA Notification', message)
    elif notification_type == 'sms':
        result = notifications.send_sms(recipient, message)
    else:
        result = notifications.send_system_notification(recipient, 'info', message)
    
    return jsonify({
        'success': result,
        'type': notification_type,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/dashboard/metrics')
def api_dashboard_metrics():
    """Get dashboard metrics"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    metrics = dashboard.get_system_metrics()
    module_status = dashboard.get_module_status()
    
    return jsonify({
        'metrics': metrics,
        'module_status': module_status
    })

@app.route('/api/dashboard/report')
def api_dashboard_report():
    """Generate system report"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    report_type = request.args.get('type', 'daily')
    format_type = request.args.get('format', 'html')  # html or json
    
    report = dashboard.generate_report(report_type)
    
    # Return JSON if requested
    if format_type == 'json':
        return jsonify(report)
    
    # Format the generated_at timestamp
    from datetime import datetime
    try:
        dt = datetime.fromisoformat(report['generated_at'])
        formatted_date = dt.strftime('%B %d, %Y at %I:%M %p')
    except:
        formatted_date = report['generated_at']
    
    # Render beautiful HTML report
    return render_template('report.html',
        report_type=report['report_type'],
        generated_at=formatted_date,
        summary=report['summary'],
        highlights=report['highlights'],
        recommendations=report['recommendations']
    )


# ==================== INTERACTIVE ASSISTANT API ====================

@app.route('/api/interactive/speak', methods=['POST'])
def api_interactive_speak():
    """Text-to-speech"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    data = request.get_json()
    text = data.get('text', '')
    
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    interactive.speak(text)
    
    return jsonify({
        'status': 'spoken',
        'text': text
    })

@app.route('/api/interactive/music', methods=['POST'])
def api_interactive_music():
    """Play music"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    data = request.get_json()
    mood = data.get('mood', 'relaxing')
    
    result = interactive.handle_music_request(f"play {mood} music")
    
    return jsonify(result)

@app.route('/api/interactive/detect-person', methods=['POST'])
def api_interactive_detect():
    """Detect person around you (360-degree scan)"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    result = interactive.check_for_person()
    
    return jsonify(result)

@app.route('/api/interactive/emergency', methods=['POST'])
def api_interactive_emergency():
    """Trigger emergency alert"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    result = interactive.trigger_emergency_alert()
    
    return jsonify(result)

@app.route('/api/interactive/tired-mode', methods=['POST'])
def api_interactive_tired():
    """Activate tired/relaxation mode"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    result = interactive.handle_tired_mood()
    
    return jsonify(result)

@app.route('/api/interactive/status')
def api_interactive_status():
    """Get interactive assistant status"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    status = interactive.get_status()
    
    return jsonify(status)

@app.route('/api/user/profile/<user_name>')
def api_user_profile(user_name):
    """Get user profile"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    profile = user_profile_manager.get_profile(user_name)
    
    return jsonify(profile)

@app.route('/api/user/greeting/<user_name>')
def api_user_greeting(user_name):
    """Get personalized greeting"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    greeting = user_profile_manager.get_personalized_greeting(user_name)
    
    return jsonify({'greeting': greeting})

@app.route('/api/user/summary/<user_name>')
def api_user_summary(user_name):
    """Get user summary"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    summary = user_profile_manager.get_user_summary(user_name)
    
    return jsonify(summary)

@app.route('/api/user/note', methods=['POST'])
def api_user_add_note():
    """Add note about user"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    data = request.get_json()
    user_name = data.get('user_name')
    note = data.get('note')
    
    user_profile_manager.add_note(user_name, note)
    
    return jsonify({'status': 'note_added'})

@app.route('/api/user/activity', methods=['POST'])
def api_user_add_activity():
    """Record user activity"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    data = request.get_json()
    user_name = data.get('user_name')
    activity = data.get('activity')
    
    user_profile_manager.add_activity(user_name, activity)
    user_profile_manager.add_interaction(user_name, 'total_conversations')
    
    return jsonify({'status': 'activity_recorded'})


# ==================== WEATHER API ====================

@app.route('/api/weather/current')
def api_weather_current():
    """Get current weather"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    location = request.args.get('location', None)
    weather = weather_service.get_current_weather(location)
    
    return jsonify(weather)

@app.route('/api/weather/forecast')
def api_weather_forecast():
    """Get weather forecast"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    location = request.args.get('location', None)
    days = int(request.args.get('days', 5))
    
    forecast = weather_service.get_forecast(location, days)
    
    return jsonify(forecast)

@app.route('/api/weather/summary')
def api_weather_summary():
    """Get weather summary"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    location = request.args.get('location', None)
    summary = weather_service.get_weather_summary(location)
    
    return jsonify({
        'summary': summary,
        'timestamp': datetime.now().isoformat()
    })


# ==================== NOTIFICATIONS API ====================

@app.route('/api/notifications/send', methods=['POST'])
def api_notifications_send():
    """Send notification"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    data = request.get_json()
    notif_type = data.get('type', 'info')
    recipient = data.get('recipient')
    message = data.get('message')
    channels = data.get('channels', ['push'])
    
    if not recipient or not message:
        return jsonify({'error': 'Missing recipient or message'}), 400
    
    results = []
    
    # Send via requested channels
    if 'email' in channels:
        notifications.send_email(recipient, f"AKIRA Notification", message)
        results.append('email')
    
    if 'sms' in channels:
        notifications.send_sms(recipient, message)
        results.append('sms')
    
    if 'push' in channels:
        notifications.send_push_notification(recipient, notif_type.title(), message)
        results.append('push')
    
    return jsonify({
        'success': True,
        'channels': results,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/notifications/history')
def api_notifications_history():
    """Get notification history"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    user_id = request.args.get('user_id', None)
    limit = int(request.args.get('limit', 50))
    
    history = notifications.get_notification_history(user_id, limit)
    
    # Convert datetime objects to strings
    history_json = []
    for notif in history:
        notif_copy = notif.copy()
        if 'timestamp' in notif_copy and hasattr(notif_copy['timestamp'], 'isoformat'):
            notif_copy['timestamp'] = notif_copy['timestamp'].isoformat()
        history_json.append(notif_copy)
    
    return jsonify({
        'notifications': history_json,
        'count': len(history_json)
    })

@app.route('/api/notifications/statistics')
def api_notifications_statistics():
    """Get notification statistics"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    stats = notifications.get_notification_statistics()
    
    # Calculate success rate
    total = stats['total_notifications']
    sent = stats['by_status'].get('sent', 0)
    success_rate = f"{int((sent/total)*100)}%" if total > 0 else "100%"
    
    # Count today's notifications
    today_count = 0
    for notif in notifications.notification_history:
        if hasattr(notif['timestamp'], 'date'):
            if notif['timestamp'].date() == datetime.now().date():
                today_count += 1
    
    return jsonify({
        'total_notifications': total,
        'by_type': stats['by_type'],
        'by_status': stats['by_status'],
        'success_rate': success_rate,
        'today_count': today_count
    })

@app.route('/api/notifications/preferences', methods=['POST'])
def api_notifications_preferences():
    """Save notification preferences"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    data = request.get_json()
    user_id = data.get('user_id', 'default_user')
    
    notifications.set_notification_preferences(user_id, data)
    
    return jsonify({
        'success': True,
        'message': 'Preferences saved'
    })


# ==================== CALENDAR API ====================

@app.route('/api/calendar/meetings', methods=['GET', 'POST'])
def api_calendar_meetings():
    """Get or create meetings"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    if request.method == 'POST':
        data = request.get_json()
        meeting = calendar.schedule_meeting(
            title=data.get('title'),
            date=data.get('date'),
            time=data.get('time'),
            duration=data.get('duration', 60),
            attendees=data.get('attendees', []),
            location=data.get('location', ''),
            notes=data.get('notes', '')
        )
        return jsonify(meeting)
    else:
        return jsonify({'meetings': calendar.meetings})

@app.route('/api/calendar/appointments', methods=['GET', 'POST'])
def api_calendar_appointments():
    """Get or create appointments"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    if request.method == 'POST':
        data = request.get_json()
        appointment = calendar.schedule_appointment(
            title=data.get('title'),
            date=data.get('date'),
            time=data.get('time'),
            duration=data.get('duration', 60),
            with_person=data.get('with_person', ''),
            location=data.get('location', ''),
            notes=data.get('notes', '')
        )
        return jsonify(appointment)
    else:
        return jsonify({'appointments': calendar.appointments})

@app.route('/api/calendar/events', methods=['GET', 'POST'])
def api_calendar_events():
    """Get or create events"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    if request.method == 'POST':
        data = request.get_json()
        event = calendar.create_event(
            title=data.get('title'),
            date=data.get('date'),
            time=data.get('time', ''),
            all_day=data.get('all_day', False),
            location=data.get('location', ''),
            description=data.get('description', ''),
            category=data.get('category', 'general')
        )
        return jsonify(event)
    else:
        return jsonify({'events': calendar.events})

@app.route('/api/calendar/today')
def api_calendar_today():
    """Get today's schedule"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    schedule = calendar.get_today_schedule()
    return jsonify(schedule)

@app.route('/api/calendar/week')
def api_calendar_week():
    """Get this week's schedule"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    schedule = calendar.get_week_schedule()
    return jsonify(schedule)

@app.route('/api/calendar/reminders')
def api_calendar_reminders():
    """Get upcoming reminders"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    hours = int(request.args.get('hours', 24))
    reminders = calendar.get_upcoming_reminders(hours)
    return jsonify({'reminders': reminders})

@app.route('/api/calendar/search')
def api_calendar_search():
    """Search calendar"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    query = request.args.get('q', '')
    results = calendar.search_schedule(query)
    return jsonify(results)

@app.route('/api/calendar/statistics')
def api_calendar_statistics():
    """Get calendar statistics"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    stats = calendar.get_statistics()
    return jsonify(stats)

@app.route('/api/calendar/meeting/<int:meeting_id>/cancel', methods=['POST'])
def api_calendar_cancel_meeting(meeting_id):
    """Cancel a meeting"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    success = calendar.cancel_meeting(meeting_id)
    return jsonify({'success': success})

@app.route('/api/calendar/meeting/<int:meeting_id>/reschedule', methods=['POST'])
def api_calendar_reschedule_meeting(meeting_id):
    """Reschedule a meeting"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    data = request.get_json()
    success = calendar.reschedule_meeting(
        meeting_id,
        data.get('date'),
        data.get('time')
    )
    return jsonify({'success': success})


# ==================== EMAIL API ====================

@app.route('/api/email/send', methods=['POST'])
def api_email_send():
    """Send email"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    data = request.get_json()
    result = email_service.send_email(
        to_email=data.get('to_email'),
        subject=data.get('subject'),
        body=data.get('body'),
        html=data.get('html', False),
        attachments=data.get('attachments', None)
    )
    
    return jsonify(result)

@app.route('/api/email/inbox')
def api_email_inbox():
    """Get inbox emails"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    unread_only = request.args.get('unread_only', 'false').lower() == 'true'
    emails = email_service.get_inbox(unread_only)
    
    return jsonify({'emails': emails})

@app.route('/api/email/sent')
def api_email_sent():
    """Get sent emails"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    limit = int(request.args.get('limit', 50))
    emails = email_service.get_sent_emails(limit)
    
    return jsonify({'emails': emails})

@app.route('/api/email/drafts', methods=['GET', 'POST'])
def api_email_drafts():
    """Get or create drafts"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    if request.method == 'POST':
        data = request.get_json()
        draft = email_service.create_draft(
            to_email=data.get('to_email'),
            subject=data.get('subject'),
            body=data.get('body')
        )
        return jsonify(draft)
    else:
        drafts = email_service.get_drafts()
        return jsonify({'drafts': drafts})

@app.route('/api/email/templates')
def api_email_templates():
    """Get email templates"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    templates = email_service.get_templates()
    return jsonify({'templates': templates})

@app.route('/api/email/template', methods=['POST'])
def api_email_send_template():
    """Send email from template"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    data = request.get_json()
    result = email_service.send_from_template(
        template_name=data.get('template_name'),
        to_email=data.get('to_email'),
        variables=data.get('variables', {})
    )
    
    return jsonify(result)

@app.route('/api/email/statistics')
def api_email_statistics():
    """Get email statistics"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    stats = email_service.get_email_statistics()
    return jsonify(stats)

@app.route('/api/email/search')
def api_email_search():
    """Search emails"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    query = request.args.get('q', '')
    folder = request.args.get('folder', 'all')
    results = email_service.search_emails(query, folder)
    
    return jsonify({'results': results})


# ==================== VIDEO CALLS API ====================

@app.route('/api/video/create', methods=['POST'])
def api_video_create_call():
    """Create video call"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    data = request.get_json()
    call = video_call_system.create_call(
        host_id=data.get('host_id'),
        title=data.get('title'),
        participants=data.get('participants', []),
        scheduled_time=data.get('scheduled_time')
    )
    
    return jsonify(call)

@app.route('/api/video/start', methods=['POST'])
def api_video_start_call():
    """Start video call"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    data = request.get_json()
    call = video_call_system.start_call(
        call_id=data.get('call_id'),
        host_id=data.get('host_id')
    )
    
    return jsonify(call)

@app.route('/api/video/join', methods=['POST'])
def api_video_join_call():
    """Join video call"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    data = request.get_json()
    result = video_call_system.join_call(
        call_id=data.get('call_id'),
        participant_id=data.get('participant_id'),
        participant_name=data.get('participant_name')
    )
    
    return jsonify(result)

@app.route('/api/video/end', methods=['POST'])
def api_video_end_call():
    """End video call"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    data = request.get_json()
    result = video_call_system.end_call(
        call_id=data.get('call_id'),
        host_id=data.get('host_id')
    )
    
    return jsonify(result)

@app.route('/api/video/active')
def api_video_active_calls():
    """Get active calls"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    calls = video_call_system.get_active_calls()
    return jsonify({'calls': calls})

@app.route('/api/video/history')
def api_video_call_history():
    """Get call history"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    user_id = request.args.get('user_id')
    limit = int(request.args.get('limit', 50))
    history = video_call_system.get_call_history(user_id, limit)
    
    return jsonify({'history': history})

@app.route('/api/video/statistics')
def api_video_statistics():
    """Get video call statistics"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    stats = video_call_system.get_statistics()
    return jsonify(stats)

@app.route('/api/video/recording/start', methods=['POST'])
def api_video_start_recording():
    """Start recording"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    data = request.get_json()
    recording = video_call_system.start_recording(
        call_id=data.get('call_id'),
        host_id=data.get('host_id')
    )
    
    return jsonify(recording)

@app.route('/api/video/recording/stop', methods=['POST'])
def api_video_stop_recording():
    """Stop recording"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    data = request.get_json()
    recording = video_call_system.stop_recording(
        call_id=data.get('call_id'),
        recording_id=data.get('recording_id')
    )
    
    return jsonify(recording)


# ==================== PAYMENTS API ====================

@app.route('/api/payment/process', methods=['POST'])
def api_payment_process():
    """Process payment"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    data = request.get_json()
    transaction = payment_system.process_payment(
        customer_id=data.get('customer_id'),
        amount=float(data.get('amount')),
        currency=data.get('currency', 'USD'),
        payment_method=data.get('payment_method', 'card'),
        description=data.get('description', ''),
        metadata=data.get('metadata', {})
    )
    
    return jsonify(transaction)

@app.route('/api/payment/invoice/create', methods=['POST'])
def api_payment_create_invoice():
    """Create invoice"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    data = request.get_json()
    invoice = payment_system.create_invoice(
        customer_id=data.get('customer_id'),
        items=data.get('items', []),
        due_date=data.get('due_date'),
        notes=data.get('notes', '')
    )
    
    return jsonify(invoice)

@app.route('/api/payment/invoice/pay', methods=['POST'])
def api_payment_pay_invoice():
    """Pay invoice"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    data = request.get_json()
    result = payment_system.pay_invoice(
        invoice_id=data.get('invoice_id'),
        payment_method=data.get('payment_method', 'card')
    )
    
    return jsonify(result)

@app.route('/api/payment/refund', methods=['POST'])
def api_payment_refund():
    """Refund payment"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    data = request.get_json()
    refund = payment_system.refund_payment(
        transaction_id=data.get('transaction_id'),
        amount=data.get('amount'),
        reason=data.get('reason', '')
    )
    
    return jsonify(refund)

@app.route('/api/payment/transactions')
def api_payment_transactions():
    """Get transactions"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    customer_id = request.args.get('customer_id')
    status = request.args.get('status')
    limit = int(request.args.get('limit', 50))
    
    transactions = payment_system.get_transactions(customer_id, status, limit)
    return jsonify({'transactions': transactions})

@app.route('/api/payment/invoices')
def api_payment_invoices():
    """Get invoices"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    customer_id = request.args.get('customer_id')
    status = request.args.get('status')
    
    invoices = payment_system.get_invoices(customer_id, status)
    return jsonify({'invoices': invoices})

@app.route('/api/payment/report')
def api_payment_report():
    """Get financial report"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    period = request.args.get('period', 'month')
    report = payment_system.get_financial_report(period)
    
    return jsonify(report)

@app.route('/api/payment/statistics')
def api_payment_statistics():
    """Get payment statistics"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    stats = payment_system.get_statistics()
    return jsonify(stats)

@app.route('/api/payment/customer/add', methods=['POST'])
def api_payment_add_customer():
    """Add customer"""
    if not MODULES_AVAILABLE:
        return jsonify({'error': 'Modules not available'}), 500
    
    data = request.get_json()
    customer = payment_system.add_customer(
        customer_id=data.get('customer_id'),
        name=data.get('name'),
        email=data.get('email'),
        phone=data.get('phone', ''),
        address=data.get('address', {})
    )
    
    return jsonify(customer)


# ==================== ERROR HANDLERS ====================

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500


# ==================== MAIN ====================

if __name__ == '__main__':
    print("\n" + "="*70)
    print("🌐 AKIRA Flask Web Application")
    print("="*70)
    print("\nStarting web server...")
    print("\n📍 Access the application at:")
    print("   http://localhost:5000")
    print("\n📊 Available pages:")
    print("   - Dashboard: http://localhost:5000/dashboard")
    print("   - Assistant: http://localhost:5000/assistant")
    print("   - IoT Control: http://localhost:5000/iot")
    print("   - Surveillance: http://localhost:5000/surveillance")
    print("   - Marketing: http://localhost:5000/marketing")
    print("\n🔌 API Endpoints:")
    print("   - GET  /api/status")
    print("   - POST /api/assistant/command")
    print("   - GET  /api/iot/devices")
    print("   - POST /api/iot/control")
    print("   - GET  /api/dashboard/metrics")
    print("\nPress Ctrl+C to stop the server")
    print("="*70 + "\n")
    
    # Create templates directory if it doesn't exist
    if not os.path.exists('templates'):
        os.makedirs('templates')
        print("✅ Created templates directory")
    
    # Run Flask app with auto-reload enabled
    app.run(debug=True, host='0.0.0.0', port=5000, use_reloader=True)
