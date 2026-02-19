# AI Engineering Module Guide

## Overview

The AI Engineering Module is a **standalone** component that provides advanced machine learning capabilities without interfering with your existing AKIRA system. You can use it independently or integrate it when needed.

## Key Features

### 🎯 Model Training
- **Classification Models**: Random Forest, Gradient Boosting, Neural Networks
- **Regression Models**: Random Forest Regressor
- **Clustering Models**: K-Means clustering
- **Automatic train/test splitting**
- **Feature scaling**
- **Performance metrics**

### 📊 Model Evaluation
- Accuracy, Precision, Recall, F1 Score
- Model comparison
- Feature importance analysis
- Cross-validation ready

### 💾 Model Management
- Save/Load models to disk
- Model registry and versioning
- Training history tracking
- Model deployment tracking

### 🚀 Model Deployment
- Deploy models to production
- Rollback capabilities
- Model status tracking
- Export model reports

## Installation

The AI Engineering Module uses the same dependencies as AKIRA:

```bash
pip install numpy scikit-learn
```

## Usage

### Option 1: Standalone Mode (Recommended for AI Engineering)

Run the interactive application:

```bash
python ai_engineering_standalone.py
```

This gives you a menu-driven interface to:
- Train new models
- Load existing models
- Make predictions
- Evaluate models
- Deploy models
- View training history

### Option 2: Python API

Use the module in your own code:

```python
from ai_engineering_module import AIEngineeringModule

# Initialize
ai_eng = AIEngineeringModule()

# Create synthetic data for testing
data = ai_eng.create_synthetic_data(n_samples=1000, n_features=10, n_classes=3)
X, y = data['X'], data['y']

# Train a model
ai_eng.train_classification_model(
    X, y, 
    model_name='my_model',
    model_type='random_forest'
)

# Make predictions
predictions = ai_eng.predict('my_model', X_test)

# Save model
ai_eng.save_model('my_model')

# Deploy model
ai_eng.deploy_model('my_model', 'production_v1')
```

### Option 3: Integration with AKIRA (Optional)

If you want to integrate with the main AKIRA system:

```python
from akira_complete_system import AkiraCompleteSystem
from ai_engineering_module import AIEngineeringModule

# Initialize both systems
akira = AkiraCompleteSystem()
ai_eng = AIEngineeringModule()

# Train a model for user behavior prediction
# ... your training code ...

# Use predictions in AKIRA
predictions = ai_eng.predict('user_behavior_model', user_features)
# Feed predictions to AKIRA modules
```

## Examples

### Example 1: Train a Classification Model

```python
from ai_engineering_module import AIEngineeringModule
import numpy as np

ai_eng = AIEngineeringModule()

# Create sample data
data = ai_eng.create_synthetic_data(
    n_samples=1000,
    n_features=10,
    n_classes=3
)

X, y = data['X'], data['y']

# Train Random Forest
result = ai_eng.train_classification_model(
    X, y,
    model_name='user_classifier',
    model_type='random_forest'
)

print(f"Accuracy: {result['metrics']['accuracy']:.4f}")

# Save the model
ai_eng.save_model('user_classifier')
```

### Example 2: Make Predictions

```python
# Load a saved model
ai_eng.load_model('user_classifier')

# Prepare new data
new_user_features = [1.5, 2.3, 0.8, 1.2, 3.4, 0.5, 2.1, 1.8, 0.9, 2.7]

# Predict
result = ai_eng.predict_single('user_classifier', new_user_features)

print(f"Prediction: {result['prediction']}")
print(f"Probability: {result['probability']}")
```

### Example 3: Compare Multiple Models

```python
# Train multiple models
ai_eng.train_classification_model(X, y, 'model_rf', 'random_forest')
ai_eng.train_classification_model(X, y, 'model_gb', 'gradient_boosting')
ai_eng.train_classification_model(X, y, 'model_nn', 'neural_network')

# Compare on test data
results = ai_eng.compare_models(
    ['model_rf', 'model_gb', 'model_nn'],
    X_test,
    y_test
)

# Best model is automatically identified
```

### Example 4: Feature Importance

```python
# Get feature importance from tree-based models
importances = ai_eng.feature_importance('model_rf')

# Use this to understand which features matter most
for i, importance in enumerate(importances):
    print(f"Feature {i}: {importance:.4f}")
```

### Example 5: Model Deployment

```python
# Deploy a model to production
ai_eng.deploy_model('user_classifier', 'production_v1')

# Later, if needed, rollback
ai_eng.rollback_model('user_classifier')

# Export model report
ai_eng.export_model_report('user_classifier')
```

## Model Types

### Classification Models

**Random Forest**
- Best for: General purpose classification
- Pros: Robust, handles non-linear data well
- Cons: Can be slow on very large datasets

**Gradient Boosting**
- Best for: High accuracy requirements
- Pros: Often highest accuracy
- Cons: Slower training, prone to overfitting

**Neural Network**
- Best for: Complex patterns
- Pros: Can learn complex relationships
- Cons: Requires more data, longer training

### Regression Models

**Random Forest Regressor**
- Best for: Predicting continuous values
- Use cases: Price prediction, score prediction

### Clustering Models

**K-Means**
- Best for: Grouping similar items
- Use cases: Customer segmentation, pattern discovery

## File Structure

```
.
├── ai_engineering_module.py        # Core AI Engineering module
├── ai_engineering_standalone.py    # Standalone interactive app
├── ai_models/                      # Saved models directory
│   ├── model_name.pkl             # Saved model files
│   └── model_name_report.json     # Model reports
└── AI_ENGINEERING_GUIDE.md        # This guide
```

## API Reference

### AIEngineeringModule Class

#### Training Methods

**`train_classification_model(X, y, model_name, model_type='random_forest')`**
- Train a classification model
- Returns: Training log with metrics

**`train_regression_model(X, y, model_name)`**
- Train a regression model
- Returns: Metrics (MSE, RMSE, R²)

**`train_clustering_model(X, model_name, n_clusters=3)`**
- Train a clustering model
- Returns: Cluster info

#### Prediction Methods

**`predict(model_name, X)`**
- Make predictions for multiple samples
- Returns: Predictions and probabilities

**`predict_single(model_name, features)`**
- Predict for a single sample
- Returns: Single prediction and probability

#### Model Management

**`save_model(model_name, filename=None)`**
- Save model to disk
- Returns: Success status and filepath

**`load_model(model_name, filename=None)`**
- Load model from disk
- Returns: Success status

**`list_models()`**
- List all loaded models
- Returns: List of model info

**`delete_model(model_name)`**
- Remove model from memory
- Returns: Success status

#### Evaluation Methods

**`evaluate_model(model_name, X_test, y_test)`**
- Evaluate model performance
- Returns: Metrics dictionary

**`compare_models(model_names, X_test, y_test)`**
- Compare multiple models
- Returns: Comparison results

**`feature_importance(model_name)`**
- Get feature importance
- Returns: Importance scores

#### Deployment Methods

**`deploy_model(model_name, deployment_name=None)`**
- Deploy model to production
- Returns: Deployment info

**`rollback_model(model_name)`**
- Rollback deployed model
- Returns: Success status

#### Utility Methods

**`create_synthetic_data(n_samples, n_features, n_classes)`**
- Create test data
- Returns: X and y arrays

**`get_training_history()`**
- View all training history
- Returns: List of training logs

**`export_model_report(model_name, filename=None)`**
- Export model report to JSON
- Returns: Success status and filepath

## Best Practices

### 1. Data Preparation
```python
# Always split your data
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

### 2. Model Selection
- Start with Random Forest (good baseline)
- Try Gradient Boosting for better accuracy
- Use Neural Networks for complex patterns

### 3. Model Evaluation
- Always evaluate on test data
- Compare multiple models
- Check feature importance

### 4. Model Deployment
- Save models before deploying
- Export model reports
- Track deployment versions

### 5. Model Monitoring
- Keep training history
- Monitor prediction accuracy
- Retrain when performance drops

## Integration with AKIRA

The AI Engineering Module is designed to work independently, but you can integrate it:

### Use Case 1: User Behavior Prediction

```python
# Train a model to predict user behavior
ai_eng.train_classification_model(
    user_behavior_data,
    user_labels,
    'user_behavior_predictor',
    'random_forest'
)

# Use in AKIRA's AI engine
from advanced_ai_engine import AdvancedAIEngine

ai_engine = AdvancedAIEngine()
# Feed predictions to AI engine for better recommendations
```

### Use Case 2: Marketing Segmentation

```python
# Train clustering model for customer segmentation
ai_eng.train_clustering_model(
    customer_features,
    'customer_segments',
    n_clusters=5
)

# Use in AKIRA's marketing module
from personalized_marketing import PersonalizedMarketing

marketing = PersonalizedMarketing()
# Use cluster predictions for targeted campaigns
```

### Use Case 3: Anomaly Detection

```python
# Train model to detect anomalies
ai_eng.train_classification_model(
    normal_vs_anomaly_data,
    labels,
    'anomaly_detector',
    'gradient_boosting'
)

# Use in AKIRA's surveillance
from smart_surveillance import SmartSurveillance

surveillance = SmartSurveillance()
# Use predictions to enhance anomaly detection
```

## Troubleshooting

### Issue: Model not loading
**Solution**: Check if the model file exists in `ai_models/` directory

### Issue: Low accuracy
**Solution**: 
- Try different model types
- Increase training data
- Check feature quality
- Tune hyperparameters

### Issue: Slow training
**Solution**:
- Reduce dataset size
- Use Random Forest instead of Neural Network
- Use fewer features

### Issue: Memory errors
**Solution**:
- Process data in batches
- Use smaller models
- Reduce feature dimensions

## Performance Tips

1. **Use appropriate model types**
   - Small datasets (<1000): Random Forest
   - Large datasets (>10000): Gradient Boosting
   - Complex patterns: Neural Network

2. **Feature engineering**
   - Remove irrelevant features
   - Scale features properly
   - Create meaningful features

3. **Model optimization**
   - Save trained models
   - Load models instead of retraining
   - Use model registry

## Support

For issues or questions:
1. Check this guide
2. Run the demo: `python ai_engineering_module.py`
3. Use standalone mode for interactive help

## License

Part of the AKIRA AI System. Use independently or integrate as needed.

---

**AI Engineering Module - Build, Train, Deploy ML Models** 🤖🔧
