"""
Setup script for AI Code Learning Assistant
"""
import os
import subprocess
import sys

def install_requirements():
    """Install required packages"""
    print("Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Requirements installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing requirements: {e}")
        return False

def create_directories():
    """Create necessary directories"""
    directories = [
        "data/programming_docs",
        "data/sample_code",
        "chroma_db"
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"✅ Created directory: {directory}")

def check_env_file():
    """Check if .env file exists and guide user"""
    if not os.path.exists(".env"):
        print("\n⚠️  .env file not found!")
        print("Please create a .env file with your Google Gemini API key:")
        print("1. Copy .env.example to .env")
        print("2. Add your Google Gemini API key (get it from https://makersuite.google.com/app/apikey)")
        print("3. Optionally add LangChain API key for tracing")
        return False
    else:
        print("✅ .env file found!")
        return True

def main():
    """Main setup function"""
    print("🚀 Setting up AI Code Learning Assistant...")
    print("=" * 50)
    
    # Create directories
    create_directories()
    
    # Install requirements
    if not install_requirements():
        return
    
    # Check environment file
    env_exists = check_env_file()
    
    print("\n" + "=" * 50)
    print("🎉 Setup complete!")
    
    if env_exists:
        print("\nTo run the application:")
        print("streamlit run streamlit_app.py")
    else:
        print("\nNext steps:")
        print("1. Set up your .env file with API keys")
        print("2. Run: streamlit run streamlit_app.py")
    
    print("\nFor testing the core functionality:")
    print("python src/main.py")

if __name__ == "__main__":
    main()