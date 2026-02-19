"""
AI Engineering Module - Advanced ML Model Training and Deployment
Standalone module that doesn't interfere with existing AKIRA system
"""
import json
import pickle
import os
from datetime import datetime
from collections import defaultdict

try:
    import numpy as np
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
    from sklearn.neural_network import MLPClassifier
    from sklearn.preprocessing import StandardScaler
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
    ML_AVAILABLE = True
except ImportError:
    ML_AVAILABLE = False
    print("⚠️  ML libraries not available. Install scikit-learn for AI Engineering features.")


class AIEngineeringModule:
    """
    Standalone AI Engineering Module for Model Development and Deployment
    Can be used independently or integrated with AKIRA system
    """
    
    def __init__(self, models_dir='ai_models'):
        self.models_dir = models_dir
        self.models = {}
        self.scalers = {}
        self.training_history = []
        self.model_registry = {}
        
        # Create models directory
        if not os.path.exists(models_dir):
            os.makedirs(models_dir)
        
        print("🤖 AI Engineering Module initialized")
    
    # ==================== MODEL TRAINING ====================
    
    def train_classification_model(self, X, y, model_name, model_type='random_forest'):
        """
        Train a classification model
        
        Args:
            X: Feature matrix
            y: Target labels
            model_name: Name to save the model
            model_type: 'random_forest', 'gradient_boosting', or 'neural_network'
        """
        if not ML_AVAILABLE:
            return {"error": "ML libraries not available"}
        
        print(f"\n🔧 Training {model_type} model: {model_name}")
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Scale features
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        # Select and train model
        if model_type == 'random_forest':
            model = RandomForestClassifier(n_estimators=100, random_state=42)
        elif model_type == 'gradient_boosting':
            model = GradientBoostingClassifier(n_estimators=100, random_state=42)
        elif model_type == 'neural_network':
            model = MLPClassifier(hidden_layer_sizes=(100, 50), max_iter=500, random_state=42)
        else:
            return {"error": f"Unknown model type: {model_type}"}
        
        # Train
        start_time = datetime.now()
        model.fit(X_train_scaled, y_train)
        training_time = (datetime.now() - start_time).total_seconds()
        
        # Evaluate
        y_pred = model.predict(X_test_scaled)
        metrics = {
            'accuracy': accuracy_score(y_test, y_pred),
            'precision': precision_score(y_test, y_pred, average='weighted', zero_division=0),
            'recall': recall_score(y_test, y_pred, average='weighted', zero_division=0),
            'f1_score': f1_score(y_test, y_pred, average='weighted', zero_division=0)
        }
        
        # Store model and scaler
        self.models[model_name] = model
        self.scalers[model_name] = scaler
        
        # Log training
        training_log = {
            'model_name': model_name,
            'model_type': model_type,
            'training_time': training_time,
            'metrics': metrics,
            'timestamp': datetime.now(),
            'train_size': len(X_train),
            'test_size': len(X_test)
        }
        self.training_history.append(training_log)
        
        # Register model
        self.model_registry[model_name] = {
            'type': model_type,
            'version': '1.0',
            'created': datetime.now(),
            'status': 'trained',
            'metrics': metrics
        }
        
        print(f"✅ Model trained successfully!")
        print(f"   Accuracy: {metrics['accuracy']:.4f}")
        print(f"   Precision: {metrics['precision']:.4f}")
        print(f"   Recall: {metrics['recall']:.4f}")
        print(f"   F1 Score: {metrics['f1_score']:.4f}")
        print(f"   Training time: {training_time:.2f}s")
        
        return training_log
    
    def train_regression_model(self, X, y, model_name):
        """Train a regression model"""
        if not ML_AVAILABLE:
            return {"error": "ML libraries not available"}
        
        from sklearn.ensemble import RandomForestRegressor
        from sklearn.metrics import mean_squared_error, r2_score
        
        print(f"\n🔧 Training regression model: {model_name}")
        
        # Split and scale
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        # Train
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        start_time = datetime.now()
        model.fit(X_train_scaled, y_train)
        training_time = (datetime.now() - start_time).total_seconds()
        
        # Evaluate
        y_pred = model.predict(X_test_scaled)
        metrics = {
            'mse': mean_squared_error(y_test, y_pred),
            'rmse': np.sqrt(mean_squared_error(y_test, y_pred)),
            'r2_score': r2_score(y_test, y_pred)
        }
        
        # Store
        self.models[model_name] = model
        self.scalers[model_name] = scaler
        
        print(f"✅ Regression model trained!")
        print(f"   RMSE: {metrics['rmse']:.4f}")
        print(f"   R² Score: {metrics['r2_score']:.4f}")
        
        return metrics
    
    def train_clustering_model(self, X, model_name, n_clusters=3):
        """Train a clustering model"""
        if not ML_AVAILABLE:
            return {"error": "ML libraries not available"}
        
        from sklearn.cluster import KMeans
        
        print(f"\n🔧 Training clustering model: {model_name}")
        
        # Scale
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        
        # Train
        model = KMeans(n_clusters=n_clusters, random_state=42)
        start_time = datetime.now()
        model.fit(X_scaled)
        training_time = (datetime.now() - start_time).total_seconds()
        
        # Store
        self.models[model_name] = model
        self.scalers[model_name] = scaler
        
        print(f"✅ Clustering model trained!")
        print(f"   Clusters: {n_clusters}")
        print(f"   Inertia: {model.inertia_:.4f}")
        
        return {'n_clusters': n_clusters, 'inertia': model.inertia_}
    
    # ==================== MODEL PREDICTION ====================
    
    def predict(self, model_name, X):
        """Make predictions using a trained model"""
        if model_name not in self.models:
            return {"error": f"Model {model_name} not found"}
        
        model = self.models[model_name]
        scaler = self.scalers.get(model_name)
        
        # Scale if scaler exists
        if scaler:
            X_scaled = scaler.transform(X)
        else:
            X_scaled = X
        
        # Predict
        predictions = model.predict(X_scaled)
        
        # Get probabilities if available
        if hasattr(model, 'predict_proba'):
            probabilities = model.predict_proba(X_scaled)
            return {
                'predictions': predictions.tolist(),
                'probabilities': probabilities.tolist()
            }
        
        return {'predictions': predictions.tolist()}
    
    def predict_single(self, model_name, features):
        """Predict for a single sample"""
        if not ML_AVAILABLE:
            return {"error": "ML libraries not available"}
        
        X = np.array([features])
        result = self.predict(model_name, X)
        
        if 'predictions' in result:
            return {
                'prediction': result['predictions'][0],
                'probability': result.get('probabilities', [[]])[0] if 'probabilities' in result else None
            }
        
        return result
    
    # ==================== MODEL MANAGEMENT ====================
    
    def save_model(self, model_name, filename=None):
        """Save a trained model to disk"""
        if model_name not in self.models:
            return {"error": f"Model {model_name} not found"}
        
        if not filename:
            filename = f"{model_name}.pkl"
        
        filepath = os.path.join(self.models_dir, filename)
        
        model_data = {
            'model': self.models[model_name],
            'scaler': self.scalers.get(model_name),
            'metadata': self.model_registry.get(model_name, {}),
            'saved_at': datetime.now()
        }
        
        try:
            with open(filepath, 'wb') as f:
                pickle.dump(model_data, f)
            print(f"✅ Model saved: {filepath}")
            return {'success': True, 'filepath': filepath}
        except Exception as e:
            print(f"❌ Error saving model: {e}")
            return {'error': str(e)}
    
    def load_model(self, model_name, filename=None):
        """Load a trained model from disk"""
        if not filename:
            filename = f"{model_name}.pkl"
        
        filepath = os.path.join(self.models_dir, filename)
        
        if not os.path.exists(filepath):
            return {"error": f"Model file not found: {filepath}"}
        
        try:
            with open(filepath, 'rb') as f:
                model_data = pickle.load(f)
            
            self.models[model_name] = model_data['model']
            self.scalers[model_name] = model_data.get('scaler')
            self.model_registry[model_name] = model_data.get('metadata', {})
            
            print(f"✅ Model loaded: {filepath}")
            return {'success': True, 'model_name': model_name}
        except Exception as e:
            print(f"❌ Error loading model: {e}")
            return {'error': str(e)}
    
    def list_models(self):
        """List all available models"""
        print("\n📋 Available Models:")
        
        if not self.models:
            print("   No models loaded")
            return []
        
        model_list = []
        for name, info in self.model_registry.items():
            print(f"\n   {name}:")
            print(f"      Type: {info.get('type', 'unknown')}")
            print(f"      Version: {info.get('version', 'unknown')}")
            print(f"      Status: {info.get('status', 'unknown')}")
            if 'metrics' in info:
                print(f"      Metrics: {info['metrics']}")
            
            model_list.append({
                'name': name,
                'info': info
            })
        
        return model_list
    
    def delete_model(self, model_name):
        """Delete a model from memory"""
        if model_name in self.models:
            del self.models[model_name]
        if model_name in self.scalers:
            del self.scalers[model_name]
        if model_name in self.model_registry:
            del self.model_registry[model_name]
        
        print(f"✅ Model {model_name} deleted from memory")
        return {'success': True}
    
    # ==================== MODEL EVALUATION ====================
    
    def evaluate_model(self, model_name, X_test, y_test):
        """Evaluate a model on test data"""
        if model_name not in self.models:
            return {"error": f"Model {model_name} not found"}
        
        if not ML_AVAILABLE:
            return {"error": "ML libraries not available"}
        
        model = self.models[model_name]
        scaler = self.scalers.get(model_name)
        
        # Scale
        if scaler:
            X_test_scaled = scaler.transform(X_test)
        else:
            X_test_scaled = X_test
        
        # Predict
        y_pred = model.predict(X_test_scaled)
        
        # Calculate metrics
        metrics = {
            'accuracy': accuracy_score(y_test, y_pred),
            'precision': precision_score(y_test, y_pred, average='weighted', zero_division=0),
            'recall': recall_score(y_test, y_pred, average='weighted', zero_division=0),
            'f1_score': f1_score(y_test, y_pred, average='weighted', zero_division=0)
        }
        
        print(f"\n📊 Evaluation Results for {model_name}:")
        for metric, value in metrics.items():
            print(f"   {metric}: {value:.4f}")
        
        return metrics
    
    def compare_models(self, model_names, X_test, y_test):
        """Compare multiple models"""
        print("\n🔍 Model Comparison:")
        
        results = {}
        for name in model_names:
            if name in self.models:
                metrics = self.evaluate_model(name, X_test, y_test)
                results[name] = metrics
        
        # Find best model
        if results:
            best_model = max(results.items(), key=lambda x: x[1].get('accuracy', 0))
            print(f"\n🏆 Best Model: {best_model[0]}")
            print(f"   Accuracy: {best_model[1]['accuracy']:.4f}")
        
        return results
    
    # ==================== FEATURE ENGINEERING ====================
    
    def feature_importance(self, model_name):
        """Get feature importance from tree-based models"""
        if model_name not in self.models:
            return {"error": f"Model {model_name} not found"}
        
        model = self.models[model_name]
        
        if hasattr(model, 'feature_importances_'):
            importances = model.feature_importances_
            
            print(f"\n📊 Feature Importance for {model_name}:")
            for i, importance in enumerate(importances):
                print(f"   Feature {i}: {importance:.4f}")
            
            return importances.tolist()
        else:
            return {"error": "Model doesn't support feature importance"}
    
    def create_synthetic_data(self, n_samples=1000, n_features=10, n_classes=2):
        """Create synthetic data for testing"""
        if not ML_AVAILABLE:
            return {"error": "ML libraries not available"}
        
        from sklearn.datasets import make_classification
        
        X, y = make_classification(
            n_samples=n_samples,
            n_features=n_features,
            n_classes=n_classes,
            random_state=42
        )
        
        print(f"✅ Created synthetic dataset:")
        print(f"   Samples: {n_samples}")
        print(f"   Features: {n_features}")
        print(f"   Classes: {n_classes}")
        
        return {'X': X, 'y': y}
    
    # ==================== MODEL DEPLOYMENT ====================
    
    def deploy_model(self, model_name, deployment_name=None):
        """Mark a model as deployed"""
        if model_name not in self.models:
            return {"error": f"Model {model_name} not found"}
        
        if not deployment_name:
            deployment_name = f"{model_name}_production"
        
        # Update registry
        if model_name in self.model_registry:
            self.model_registry[model_name]['status'] = 'deployed'
            self.model_registry[model_name]['deployment_name'] = deployment_name
            self.model_registry[model_name]['deployed_at'] = datetime.now()
        
        # Save deployed model
        self.save_model(model_name, f"{deployment_name}.pkl")
        
        print(f"✅ Model deployed: {deployment_name}")
        return {
            'success': True,
            'deployment_name': deployment_name,
            'model_name': model_name
        }
    
    def rollback_model(self, model_name):
        """Rollback a deployed model"""
        if model_name in self.model_registry:
            self.model_registry[model_name]['status'] = 'trained'
            if 'deployment_name' in self.model_registry[model_name]:
                del self.model_registry[model_name]['deployment_name']
        
        print(f"✅ Model rolled back: {model_name}")
        return {'success': True}
    
    # ==================== MONITORING ====================
    
    def get_training_history(self):
        """Get training history"""
        print("\n📜 Training History:")
        
        for i, log in enumerate(self.training_history, 1):
            print(f"\n{i}. {log['model_name']} ({log['model_type']})")
            print(f"   Trained: {log['timestamp']}")
            print(f"   Accuracy: {log['metrics']['accuracy']:.4f}")
            print(f"   Training time: {log['training_time']:.2f}s")
        
        return self.training_history
    
    def get_model_info(self, model_name):
        """Get detailed model information"""
        if model_name not in self.model_registry:
            return {"error": f"Model {model_name} not found in registry"}
        
        info = self.model_registry[model_name]
        
        print(f"\n📋 Model Information: {model_name}")
        for key, value in info.items():
            print(f"   {key}: {value}")
        
        return info
    
    def export_model_report(self, model_name, filename=None):
        """Export model report to JSON"""
        if model_name not in self.model_registry:
            return {"error": f"Model {model_name} not found"}
        
        if not filename:
            filename = f"{model_name}_report.json"
        
        filepath = os.path.join(self.models_dir, filename)
        
        report = {
            'model_name': model_name,
            'registry_info': self.model_registry[model_name],
            'training_logs': [
                log for log in self.training_history 
                if log['model_name'] == model_name
            ],
            'generated_at': datetime.now().isoformat()
        }
        
        try:
            with open(filepath, 'w') as f:
                json.dump(report, f, indent=2, default=str)
            
            print(f"✅ Report exported: {filepath}")
            return {'success': True, 'filepath': filepath}
        except Exception as e:
            print(f"❌ Error exporting report: {e}")
            return {'error': str(e)}


# ==================== DEMO FUNCTION ====================

def demo_ai_engineering():
    """Demonstrate AI Engineering Module capabilities"""
    print("\n" + "="*70)
    print("🤖 AI ENGINEERING MODULE DEMO")
    print("="*70)
    
    ai_eng = AIEngineeringModule()
    
    # Create synthetic data
    print("\n--- Creating Synthetic Dataset ---")
    data = ai_eng.create_synthetic_data(n_samples=1000, n_features=10, n_classes=3)
    X, y = data['X'], data['y']
    
    # Train multiple models
    print("\n--- Training Multiple Models ---")
    
    # Random Forest
    ai_eng.train_classification_model(X, y, 'user_behavior_rf', 'random_forest')
    
    # Gradient Boosting
    ai_eng.train_classification_model(X, y, 'user_behavior_gb', 'gradient_boosting')
    
    # Neural Network
    ai_eng.train_classification_model(X, y, 'user_behavior_nn', 'neural_network')
    
    # List models
    print("\n--- Listing All Models ---")
    ai_eng.list_models()
    
    # Make predictions
    print("\n--- Making Predictions ---")
    test_sample = X[0:5]
    predictions = ai_eng.predict('user_behavior_rf', test_sample)
    print(f"Predictions: {predictions['predictions']}")
    
    # Feature importance
    print("\n--- Feature Importance ---")
    ai_eng.feature_importance('user_behavior_rf')
    
    # Save models
    print("\n--- Saving Models ---")
    ai_eng.save_model('user_behavior_rf')
    ai_eng.save_model('user_behavior_gb')
    
    # Deploy model
    print("\n--- Deploying Best Model ---")
    ai_eng.deploy_model('user_behavior_rf', 'production_v1')
    
    # Training history
    print("\n--- Training History ---")
    ai_eng.get_training_history()
    
    # Export report
    print("\n--- Exporting Model Report ---")
    ai_eng.export_model_report('user_behavior_rf')
    
    print("\n" + "="*70)
    print("✨ AI Engineering Module Demo Complete!")
    print("="*70)


if __name__ == "__main__":
    demo_ai_engineering()
