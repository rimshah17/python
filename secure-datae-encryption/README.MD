# 🔒 Secure Data Encryption System

A Streamlit-based secure data storage and retrieval system that allows users to encrypt and decrypt data using unique passkeys. This system provides enterprise-grade security features with a user-friendly interface, making it perfect for storing sensitive information securely.

## ✨ Features

- 🔐 Secure data encryption using Fernet symmetric encryption
- 👤 User authentication with PBKDF2-SHA256 password hashing
- 💾 Secure data persistence using Streamlit's secrets management
- 🔑 Environment-aware secure key management
- 🛡️ Protection against brute force attacks (3 attempts limit)
- ⏱️ 30-second lockout after failed attempts
- 🎨 Clean, modern Streamlit interface
- 📝 Title-based data organization
- 🗑️ Secure data deletion capability

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- 2GB free RAM (for secure in-memory operations)
- Modern web browser
- Streamlit account (for cloud deployment)

### Installation & Configuration

#### Local Development Setup

1. Clone the repository or download the source code
2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
.\venv\Scripts\Activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Set up local secrets:
   - Create a `.streamlit` directory in your project root
   - Create `secrets.toml` inside `.streamlit` directory with the following template:
   ```toml
   encryption_key = "your-secure-encryption-key"
   jwt_secret = "your-secure-jwt-secret"
   cookie_name = "secure_data_cookie"
   session_expiry_days = 30
   ```
   - Replace the placeholder values with secure random keys
   - Never commit `secrets.toml` to version control

### Running the Application

#### Local Development
1. Start the Streamlit application:
```bash
streamlit run main.py
```
2. Your default web browser will automatically open to `http://localhost:8501`
3. The application uses your local secrets configuration

#### Streamlit Cloud Deployment
1. Push your code to GitHub (excluding secrets.toml)
2. Go to https://streamlit.io and connect your repository
3. In the Streamlit Cloud dashboard:
   - Navigate to your app settings
   - Under "Secrets", add your production configuration:
   ```toml
   encryption_key = "your-production-encryption-key"
   jwt_secret = "your-production-jwt-secret"
   cookie_name = "secure_data_cookie"
   session_expiry_days = 30
   ```
4. Deploy your application
5. Your app will now run with secure, environment-specific secrets

## 🔑 Usage

1. **Navigation**:
   - Use the sidebar menu to navigate between different sections
   - The available options change based on your login status

2. **Sign Up**:
   - Click "Sign Up" in the sidebar
   - Choose a unique username
   - Create a strong password
   - Confirm your password
   - Your password will be securely hashed using PBKDF2-SHA256

3. **Login**:
   - Select "Login" from the sidebar
   - Enter your username and password
   - You have 3 attempts before a 30-second lockout
   - Failed attempts are tracked per username

4. **Store Data**:
   - Navigate to "Store Data" in the sidebar
   - Enter a descriptive title for your data
   - Input the data you want to encrypt
   - Create a unique encryption passkey
   - Save this passkey securely - it's required for decryption!
   - Click "Encrypt & Save"

5. **Retrieve Data**:
   - Go to "Retrieve Data" in the sidebar
   - Select the data entry from the dropdown menu
   - Enter the encryption passkey you used when storing
   - Click "Decrypt" to view your data
   - Use the delete button (🗑️) to permanently remove entries

6. **Logout**:
   - Click "Logout" in the sidebar to end your session
   - All session data is cleared for security

## 🔒 Security Features

- **Authentication Security**:
  - PBKDF2-SHA256 password hashing with salting
  - Rate limiting with 3 attempts maximum
  - 30-second account lockouts after failed attempts
  - Secure session management with Streamlit
  - Environment-specific JWT secrets

- **Data Security**:
  - Fernet symmetric encryption (AES-128 in CBC mode)
  - Two-layer encryption key system:
    - System-level encryption key from Streamlit secrets
    - User-provided encryption passkeys
  - Zero plaintext storage - all data encrypted at rest
  - Secure key derivation from combined keys
  - Memory-safe data handling

- **Secrets Management**:
  - Streamlit's built-in secrets management
  - Environment-specific configurations
  - Secure storage of system-level keys
  - Separate development and production secrets
  - No sensitive data in version control

## 💡 Important Notes

- **Secrets Management**:
  - Never commit `.streamlit/secrets.toml` to version control
  - Use different secrets for development and production
  - Generate strong random keys for production deployment
  - Regularly rotate production secrets

- **Passkey Security**:
  - Store your encryption passkeys securely
  - Different passkeys for different data entries recommended
  - Lost passkeys CANNOT be recovered (by design)
  - Use a password manager for passkey storage

- **Environment Management**:
  - Keep development and production environments separate
  - Use secure random keys in production
  - Test with development secrets locally
  - Backup your production secrets securely

- **Best Practices**:
  - Use strong, unique passwords
  - Change encryption passkeys periodically
  - Don't share passkeys or system secrets
  - Log out after each session
  - Regularly verify your stored data
  - Monitor Streamlit Cloud logs for security events

## 🤝 Contributing

Feel free to contribute to this project:
- Submit issues for bug reports
- Propose security enhancements
- Suggest new features
- Create pull requests

## 📜 License

This project is licensed under the MIT License - making it free for both personal and commercial use.
