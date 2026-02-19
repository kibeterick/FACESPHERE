"""
IoT Integration Module - Smart Home Control
"""
from datetime import datetime
import json


class IoTController:
    """Control IoT devices and smart home systems"""
    
    def __init__(self):
        self.devices = {}
        self.scenes = {}
        self.automations = []
        self.device_status = {}
        
    def register_device(self, device_id, device_type, name, capabilities):
        """Register an IoT device"""
        self.devices[device_id] = {
            'type': device_type,
            'name': name,
            'capabilities': capabilities,
            'status': 'offline',
            'last_updated': datetime.now()
        }
        
        # Initialize device status
        self.device_status[device_id] = {
            'power': 'off',
            'value': 0
        }
        
        print(f"✅ Registered device: {name} ({device_type})")
        return True
    
    def control_light(self, device_id, action, brightness=100):
        """Control smart lights"""
        if device_id not in self.devices:
            return "Device not found"
        
        device = self.devices[device_id]
        if device['type'] != 'light':
            return "Device is not a light"
        
        if action == 'on':
            self.device_status[device_id]['power'] = 'on'
            self.device_status[device_id]['brightness'] = brightness
            return f"💡 {device['name']} turned ON (brightness: {brightness}%)"
        elif action == 'off':
            self.device_status[device_id]['power'] = 'off'
            return f"💡 {device['name']} turned OFF"
        elif action == 'dim':
            self.device_status[device_id]['brightness'] = brightness
            return f"💡 {device['name']} dimmed to {brightness}%"
        
        return "Invalid action"
    
    def control_thermostat(self, device_id, temperature):
        """Control smart thermostat"""
        if device_id not in self.devices:
            return "Device not found"
        
        device = self.devices[device_id]
        if device['type'] != 'thermostat':
            return "Device is not a thermostat"
        
        self.device_status[device_id]['temperature'] = temperature
        return f"🌡️  {device['name']} set to {temperature}°F"
    
    def control_lock(self, device_id, action):
        """Control smart locks"""
        if device_id not in self.devices:
            return "Device not found"
        
        device = self.devices[device_id]
        if device['type'] != 'lock':
            return "Device is not a lock"
        
        if action == 'lock':
            self.device_status[device_id]['status'] = 'locked'
            return f"🔒 {device['name']} LOCKED"
        elif action == 'unlock':
            self.device_status[device_id]['status'] = 'unlocked'
            return f"🔓 {device['name']} UNLOCKED"
        
        return "Invalid action"
    
    def control_camera(self, device_id, action):
        """Control security cameras"""
        if device_id not in self.devices:
            return "Device not found"
        
        device = self.devices[device_id]
        if device['type'] != 'camera':
            return "Device is not a camera"
        
        if action == 'start':
            self.device_status[device_id]['recording'] = True
            return f"📹 {device['name']} started recording"
        elif action == 'stop':
            self.device_status[device_id]['recording'] = False
            return f"📹 {device['name']} stopped recording"
        
        return "Invalid action"
    
    def control_speaker(self, device_id, action, volume=50):
        """Control smart speakers"""
        if device_id not in self.devices:
            return "Device not found"
        
        device = self.devices[device_id]
        if device['type'] != 'speaker':
            return "Device is not a speaker"
        
        if action == 'play':
            self.device_status[device_id]['playing'] = True
            self.device_status[device_id]['volume'] = volume
            return f"🔊 {device['name']} playing (volume: {volume}%)"
        elif action == 'pause':
            self.device_status[device_id]['playing'] = False
            return f"⏸️  {device['name']} paused"
        elif action == 'volume':
            self.device_status[device_id]['volume'] = volume
            return f"🔊 {device['name']} volume set to {volume}%"
        
        return "Invalid action"
    
    def create_scene(self, scene_name, device_actions):
        """Create a scene with multiple device actions"""
        self.scenes[scene_name] = {
            'actions': device_actions,
            'created': datetime.now()
        }
        
        print(f"✅ Scene created: {scene_name}")
        return True
    
    def activate_scene(self, scene_name):
        """Activate a predefined scene"""
        if scene_name not in self.scenes:
            return "Scene not found"
        
        scene = self.scenes[scene_name]
        results = []
        
        for action in scene['actions']:
            device_id = action['device_id']
            command = action['command']
            params = action.get('params', {})
            
            # Execute command based on device type
            device = self.devices.get(device_id)
            if not device:
                continue
            
            if device['type'] == 'light':
                result = self.control_light(device_id, command, params.get('brightness', 100))
            elif device['type'] == 'thermostat':
                result = self.control_thermostat(device_id, params.get('temperature', 72))
            elif device['type'] == 'lock':
                result = self.control_lock(device_id, command)
            elif device['type'] == 'speaker':
                result = self.control_speaker(device_id, command, params.get('volume', 50))
            else:
                result = "Unknown device type"
            
            results.append(result)
        
        return f"🎬 Scene '{scene_name}' activated:\n" + "\n".join(results)
    
    def add_automation(self, name, trigger, actions):
        """Add automation rule"""
        automation = {
            'name': name,
            'trigger': trigger,
            'actions': actions,
            'enabled': True,
            'created': datetime.now()
        }
        
        self.automations.append(automation)
        print(f"✅ Automation added: {name}")
        return True
    
    def check_automations(self, current_context):
        """Check and execute automations based on triggers"""
        executed = []
        
        for automation in self.automations:
            if not automation['enabled']:
                continue
            
            trigger = automation['trigger']
            
            # Check trigger conditions
            triggered = False
            if trigger['type'] == 'time':
                current_hour = datetime.now().hour
                if current_hour == trigger['hour']:
                    triggered = True
            elif trigger['type'] == 'presence':
                if current_context.get('person_detected') == trigger['condition']:
                    triggered = True
            elif trigger['type'] == 'temperature':
                if current_context.get('temperature', 0) > trigger['threshold']:
                    triggered = True
            
            if triggered:
                # Execute actions
                for action in automation['actions']:
                    # Execute device control
                    pass
                executed.append(automation['name'])
        
        return executed
    
    def get_device_status(self, device_id=None):
        """Get status of devices"""
        if device_id:
            if device_id in self.devices:
                return {
                    'device': self.devices[device_id],
                    'status': self.device_status.get(device_id, {})
                }
            return "Device not found"
        
        # Return all devices
        all_status = {}
        for dev_id, device in self.devices.items():
            all_status[dev_id] = {
                'name': device['name'],
                'type': device['type'],
                'status': self.device_status.get(dev_id, {})
            }
        
        return all_status
    
    def voice_control(self, command):
        """Process voice commands for IoT control"""
        command_lower = command.lower()
        
        # Light controls
        if 'turn on' in command_lower and 'light' in command_lower:
            # Find light devices
            lights = [d for d, info in self.devices.items() if info['type'] == 'light']
            if lights:
                return self.control_light(lights[0], 'on')
        
        elif 'turn off' in command_lower and 'light' in command_lower:
            lights = [d for d, info in self.devices.items() if info['type'] == 'light']
            if lights:
                return self.control_light(lights[0], 'off')
        
        # Temperature controls
        elif 'set temperature' in command_lower or 'thermostat' in command_lower:
            import re
            temp_match = re.search(r'\d+', command)
            if temp_match:
                temp = int(temp_match.group())
                thermostats = [d for d, info in self.devices.items() if info['type'] == 'thermostat']
                if thermostats:
                    return self.control_thermostat(thermostats[0], temp)
        
        # Lock controls
        elif 'lock' in command_lower and 'door' in command_lower:
            locks = [d for d, info in self.devices.items() if info['type'] == 'lock']
            if locks:
                action = 'lock' if 'lock' in command_lower else 'unlock'
                return self.control_lock(locks[0], action)
        
        # Scene activation
        elif 'activate' in command_lower or 'scene' in command_lower:
            for scene_name in self.scenes.keys():
                if scene_name.lower() in command_lower:
                    return self.activate_scene(scene_name)
        
        return "Command not recognized. Try: 'turn on lights', 'set temperature to 72', 'lock door'"
    
    def energy_monitoring(self):
        """Monitor energy usage of devices"""
        total_usage = 0
        device_usage = {}
        
        for device_id, status in self.device_status.items():
            device = self.devices[device_id]
            usage = 0
            
            if status.get('power') == 'on':
                if device['type'] == 'light':
                    usage = 10 * (status.get('brightness', 100) / 100)
                elif device['type'] == 'thermostat':
                    usage = 50
                elif device['type'] == 'speaker':
                    usage = 5
            
            device_usage[device['name']] = usage
            total_usage += usage
        
        return {
            'total_usage': f"{total_usage:.1f}W",
            'device_breakdown': device_usage,
            'estimated_cost': f"${total_usage * 0.12 / 1000:.2f}/hour"
        }
