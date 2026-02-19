"""
AI Engineering Standalone Application
Use this to work with AI models independently from the main AKIRA system
"""
from ai_engineering_module import AIEngineeringModule
import numpy as np


def main_menu():
    """Display main menu"""
    print("\n" + "="*70)
    print("🤖 AI ENGINEERING MODULE - Standalone Mode")
    print("="*70)
    print("\nOptions:")
    print("1. Train New Model")
    print("2. Load Existing Model")
    print("3. Make Predictions")
    print("4. Evaluate Model")
    print("5. List All Models")
    print("6. Feature Importance")
    print("7. Deploy Model")
    print("8. Training History")
    print("9. Export Model Report")
    print("10. Run Demo")
    print("0. Exit")
    print("="*70)


def train_model_menu(ai_eng):
    """Train a new model"""
    print("\n--- Train New Model ---")
    print("1. Classification Model")
    print("2. Regression Model")
    print("3. Clustering Model")
    print("4. Use Synthetic Data (for testing)")
    
    choice = input("\nSelect option: ").strip()
    
    if choice == "4":
        # Create synthetic data
        n_samples = int(input("Number of samples (default 1000): ") or "1000")
        n_features = int(input("Number of features (default 10): ") or "10")
        n_classes = int(input("Number of classes (default 3): ") or "3")
        
        data = ai_eng.create_synthetic_data(n_samples, n_features, n_classes)
        X, y = data['X'], data['y']
        
        model_name = input("Model name: ").strip()
        
        print("\nModel types:")
        print("1. Random Forest")
        print("2. Gradient Boosting")
        print("3. Neural Network")
        
        model_type_choice = input("Select model type: ").strip()
        model_types = {
            '1': 'random_forest',
            '2': 'gradient_boosting',
            '3': 'neural_network'
        }
        
        model_type = model_types.get(model_type_choice, 'random_forest')
        
        # Train
        result = ai_eng.train_classification_model(X, y, model_name, model_type)
        
        # Ask to save
        save = input("\nSave model? (yes/no): ").strip().lower()
        if save in ['yes', 'y']:
            ai_eng.save_model(model_name)
    
    else:
        print("Feature coming soon. Use option 4 for now.")


def load_model_menu(ai_eng):
    """Load an existing model"""
    print("\n--- Load Existing Model ---")
    model_name = input("Model name: ").strip()
    filename = input("Filename (press Enter for default): ").strip() or None
    
    result = ai_eng.load_model(model_name, filename)
    
    if 'success' in result:
        print(f"✅ Model loaded successfully!")
    else:
        print(f"❌ Error: {result.get('error', 'Unknown error')}")


def make_predictions_menu(ai_eng):
    """Make predictions with a model"""
    print("\n--- Make Predictions ---")
    
    # List available models
    if not ai_eng.models:
        print("No models loaded. Please train or load a model first.")
        return
    
    print("\nAvailable models:")
    for i, name in enumerate(ai_eng.models.keys(), 1):
        print(f"{i}. {name}")
    
    model_name = input("\nEnter model name: ").strip()
    
    if model_name not in ai_eng.models:
        print(f"Model {model_name} not found.")
        return
    
    print("\nEnter features (comma-separated):")
    print("Example: 1.5, 2.3, 0.8, 1.2, ...")
    
    features_str = input("Features: ").strip()
    
    try:
        features = [float(x.strip()) for x in features_str.split(',')]
        
        result = ai_eng.predict_single(model_name, features)
        
        print(f"\n✅ Prediction: {result['prediction']}")
        if result.get('probability'):
            print(f"   Probabilities: {result['probability']}")
    
    except Exception as e:
        print(f"❌ Error: {e}")


def evaluate_model_menu(ai_eng):
    """Evaluate a model"""
    print("\n--- Evaluate Model ---")
    
    if not ai_eng.models:
        print("No models loaded.")
        return
    
    print("\nAvailable models:")
    for i, name in enumerate(ai_eng.models.keys(), 1):
        print(f"{i}. {name}")
    
    model_name = input("\nEnter model name: ").strip()
    
    if model_name not in ai_eng.models:
        print(f"Model {model_name} not found.")
        return
    
    print("\nCreate test data? (yes/no)")
    create_test = input(": ").strip().lower()
    
    if create_test in ['yes', 'y']:
        data = ai_eng.create_synthetic_data(n_samples=200, n_features=10, n_classes=3)
        X_test, y_test = data['X'], data['y']
        
        ai_eng.evaluate_model(model_name, X_test, y_test)
    else:
        print("Please provide test data.")


def deploy_model_menu(ai_eng):
    """Deploy a model"""
    print("\n--- Deploy Model ---")
    
    if not ai_eng.models:
        print("No models loaded.")
        return
    
    print("\nAvailable models:")
    for i, name in enumerate(ai_eng.models.keys(), 1):
        print(f"{i}. {name}")
    
    model_name = input("\nEnter model name to deploy: ").strip()
    
    if model_name not in ai_eng.models:
        print(f"Model {model_name} not found.")
        return
    
    deployment_name = input("Deployment name (press Enter for default): ").strip() or None
    
    result = ai_eng.deploy_model(model_name, deployment_name)
    
    if 'success' in result:
        print(f"✅ Model deployed: {result['deployment_name']}")


def main():
    """Main application loop"""
    ai_eng = AIEngineeringModule()
    
    while True:
        main_menu()
        choice = input("\nSelect option: ").strip()
        
        if choice == "1":
            train_model_menu(ai_eng)
        
        elif choice == "2":
            load_model_menu(ai_eng)
        
        elif choice == "3":
            make_predictions_menu(ai_eng)
        
        elif choice == "4":
            evaluate_model_menu(ai_eng)
        
        elif choice == "5":
            ai_eng.list_models()
        
        elif choice == "6":
            model_name = input("\nEnter model name: ").strip()
            ai_eng.feature_importance(model_name)
        
        elif choice == "7":
            deploy_model_menu(ai_eng)
        
        elif choice == "8":
            ai_eng.get_training_history()
        
        elif choice == "9":
            model_name = input("\nEnter model name: ").strip()
            ai_eng.export_model_report(model_name)
        
        elif choice == "10":
            from ai_engineering_module import demo_ai_engineering
            demo_ai_engineering()
        
        elif choice == "0":
            print("\n👋 Goodbye!")
            break
        
        else:
            print("\n❌ Invalid option. Please try again.")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    print("""
    ╔═══════════════════════════════════════════════════════════════╗
    ║                                                               ║
    ║          AI ENGINEERING MODULE - Standalone Mode              ║
    ║                                                               ║
    ║  Train, evaluate, and deploy machine learning models         ║
    ║  independently from the main AKIRA system                     ║
    ║                                                               ║
    ╚═══════════════════════════════════════════════════════════════╝
    """)
    
    main()
