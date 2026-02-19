# AI Engineering Module - Quick Reference

## 🚀 Quick Start

### Run Standalone App
```bash
python ai_engineering_standalone.py
```

### Run Demo
```bash
python ai_engineering_module.py
```

## 📝 Common Tasks

### 1. Train a Model
```python
from ai_engineering_module import AIEngineeringModule

ai_eng = AIEngineeringModule()

# Create test data
data = ai_eng.create_synthetic_data(1000, 10, 3)
X, y = data['X'], data['y']

# Train
ai_eng.train_classification_model(X, y, 'my_model', 'random_forest')
```

### 2. Save Model
```python
ai_eng.save_model('my_model')
```

### 3. Load Model
```python
ai_eng.load_model('my_model')
```

### 4. Make Prediction
```python
# Single prediction
result = ai_eng.predict_single('my_model', [1.5, 2.3, 0.8, ...])
print(result['prediction'])

# Multiple predictions
predictions = ai_eng.predict('my_model', X_test)
```

### 5. Evaluate Model
```python
metrics = ai_eng.evaluate_model('my_model', X_test, y_test)
print(f"Accuracy: {metrics['accuracy']:.4f}")
```

### 6. Deploy Model
```python
ai_eng.deploy_model('my_model', 'production_v1')
```

## 🎯 Model Types

| Type | Use Case | Command |
|------|----------|---------|
| Random Forest | General classification | `model_type='random_forest'` |
| Gradient Boosting | High accuracy | `model_type='gradient_boosting'` |
| Neural Network | Complex patterns | `model_type='neural_network'` |
| Regression | Continuous values | `train_regression_model()` |
| Clustering | Grouping | `train_clustering_model()` |

## 📊 Key Methods

### Training
- `train_classification_model(X, y, name, type)`
- `train_regression_model(X, y, name)`
- `train_clustering_model(X, name, n_clusters)`

### Prediction
- `predict(model_name, X)` - Multiple samples
- `predict_single(model_name, features)` - Single sample

### Management
- `save_model(name)` - Save to disk
- `load_model(name)` - Load from disk
- `list_models()` - Show all models
- `delete_model(name)` - Remove from memory

### Evaluation
- `evaluate_model(name, X_test, y_test)`
- `compare_models(names, X_test, y_test)`
- `feature_importance(name)`

### Deployment
- `deploy_model(name, deployment_name)`
- `rollback_model(name)`
- `export_model_report(name)`

### Utilities
- `create_synthetic_data(n_samples, n_features, n_classes)`
- `get_training_history()`
- `get_model_info(name)`

## 💡 Tips

1. **Always save models** after training
2. **Evaluate before deploying** to production
3. **Use synthetic data** for testing
4. **Compare multiple models** to find the best
5. **Check feature importance** to understand your model
6. **Export reports** for documentation

## 🔗 Integration with AKIRA

### Optional Integration
```python
# AI Engineering works independently
ai_eng = AIEngineeringModule()

# But can be used with AKIRA if needed
from akira_complete_system import AkiraCompleteSystem
akira = AkiraCompleteSystem()

# Train custom models for AKIRA features
# ... your code ...
```

## 📁 File Locations

- **Models**: `ai_models/*.pkl`
- **Reports**: `ai_models/*_report.json`
- **Module**: `ai_engineering_module.py`
- **Standalone App**: `ai_engineering_standalone.py`
- **Guide**: `AI_ENGINEERING_GUIDE.md`

## ⚡ Performance

| Dataset Size | Recommended Model | Training Time |
|--------------|-------------------|---------------|
| < 1,000 | Random Forest | < 1 second |
| 1,000 - 10,000 | Random Forest | 1-5 seconds |
| 10,000 - 100,000 | Gradient Boosting | 5-30 seconds |
| > 100,000 | Neural Network | 30+ seconds |

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Model not found | Check if model is loaded or saved |
| Low accuracy | Try different model type or more data |
| Slow training | Use Random Forest or reduce data size |
| Memory error | Process in batches or use smaller model |

## 📚 Learn More

- Full Guide: `AI_ENGINEERING_GUIDE.md`
- Feature List: `FEATURES.md`
- Main README: `README.md`

---

**AI Engineering Module - Train ML Models Independently** 🤖
