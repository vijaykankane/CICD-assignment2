# Flask CI/CD Pipeline - Beginner Guide

This is a simple Flask application with a complete CI/CD pipeline using GitHub Actions. Perfect for learning DevOps basics!

## 📋 What This Project Includes

- **Simple Flask App**: A basic web application with 3 pages
- **Tests**: Automated tests to check if everything works
- **CI/CD Pipeline**: Automatically tests and deploys your code
- **Complete Documentation**: Step-by-step instructions

## 🚀 Getting Started

### Prerequisites
- Python 3.9 or higher
- Git
- GitHub account

### Local Setup

1. **Clone this repository**
```bash
git clone https://github.com/your-username/flask-cicd-demo.git
cd flask-cicd-demo
```

2. **Create a virtual environment**
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
python app.py
```

5. **Visit your app**
Open your browser and go to: http://localhost:5000

### Test the Application

Run tests to make sure everything works:
```bash
pytest -v
```

## 📁 Project Structure

```
flask-cicd-demo/
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # GitHub Actions workflow
│
├── app.py                     # Main Flask application
├── test_app.py               # Tests for the application
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## 🔄 CI/CD Pipeline Explanation

Our GitHub Actions workflow automatically:

### 1. **Runs Tests** (on every push and pull request)
- Sets up Python environment
- Installs dependencies
- Runs all tests
- Only continues if tests pass ✅

### 2. **Deploy to Staging** (when you push to `staging` branch)
- Waits for tests to pass
- Simulates deployment to staging environment
- Runs health checks

### 3. **Deploy to Production** (when you create a release)
- Waits for tests to pass
- Simulates deployment to production
- Runs health checks
- Sends success notification

## 🌟 How to Use the Pipeline

### For Regular Development:
1. Make changes to your code
2. Push to `main` branch
3. GitHub Actions will automatically run tests

### For Staging Deployment:
1. Create a `staging` branch: `git checkout -b staging`
2. Push changes to staging: `git push origin staging`
3. GitHub Actions will test and deploy to staging

### For Production Deployment:
1. Go to your GitHub repository
2. Click "Releases" → "Create a new release"
3. Tag version (e.g., `v1.0.0`) and publish
4. GitHub Actions will automatically deploy to production

## 🔧 Setting Up GitHub Secrets (For Real Deployments)

When you're ready for real deployments, you'll need to add secrets:

1. Go to your GitHub repository
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Add these secrets:

| Secret Name | Description | Example Value |
|------------|-------------|---------------|
| `STAGING_SERVER_HOST` | Staging server address | `staging.yourapp.com` |
| `PRODUCTION_SERVER_HOST` | Production server address | `yourapp.com` |
| `DEPLOY_KEY` | SSH key for deployment | `-----BEGIN PRIVATE KEY-----...` |
| `API_TOKEN` | Deployment service token | `abc123xyz789` |

## 📊 Workflow Status Badges

Add this to your README to show build status:

```markdown
![CI/CD Pipeline](https://github.com/your-username/flask-cicd-demo/workflows/CI/CD%20Pipeline/badge.svg)
```

## 🧪 Testing Your Setup

### Test the Flask App:
```bash
# Run the app
python app.py

# In another terminal, test the endpoints:
curl http://localhost:5000/
curl http://localhost:5000/health
curl http://localhost:5000/about
```

### Test the CI/CD Pipeline:
1. Make a small change to `app.py`
2. Commit and push: `git add . && git commit -m "Test pipeline" && git push`
3. Go to GitHub → Your Repository → Actions tab
4. Watch your pipeline run! 🎉

## 🔍 Understanding the Workflow File

The `.github/workflows/ci-cd.yml` file contains our pipeline. Here's what each part does:

```yaml
# Trigger conditions
on:
  push:
    branches: [ main, staging ]  # Run on pushes to these branches
  pull_request:
    branches: [ main ]           # Run on PRs to main
  release:
    types: [published]           # Run on new releases
```

```yaml
# Jobs run in parallel unless specified otherwise
jobs:
  test:           # Always runs first
  deploy-staging: # Runs after tests, only on staging branch
  deploy-production: # Runs after tests, only on releases
```

## 🚨 Troubleshooting

### Common Issues:

**Tests failing?**
- Check if all dependencies are in `requirements.txt`
- Make sure your test functions start with `test_`
- Verify Python version compatibility

**Pipeline not running?**
- Check if `.github/workflows/ci-cd.yml` is in the right location
- Verify YAML syntax (indentation matters!)
- Check GitHub Actions tab for error messages

**Deployment not working?**
- Verify branch names match exactly (`main`, `staging`)
- Check if secrets are properly configured
- Review workflow logs in GitHub Actions

## 🎯 Next Steps

Once you master this basic setup, you can enhance it with:

- Real deployment to cloud services (Heroku, AWS, etc.)
- Database integration
- Code quality checks (linting, formatting)
- Security scanning
- Performance testing
- Slack/email notifications

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and test them
4. Push to your fork and submit a pull request

## 📚 Learning Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [pytest Documentation](https://docs.pytest.org/)
- [CI/CD Best Practices](https://www.atlassian.com/continuous-delivery/principles/continuous-integration-vs-delivery-vs-deployment)
