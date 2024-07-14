from setuptools import setup, find_packages

setup(
    name="checkout_bot",
    version="1.0.0",
    description="A comprehensive, customizable, and scalable library for creating AI-enhanced checkout bots.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Farzin Shifat",
    author_email="farzinshifat@gmail.com",
    url="https://github.com/Farzin312/checkoutbot",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "beautifulsoup4==4.12.3",
        "requests==2.32.3",
        "selenium==4.22.0",
        "tensorflow==2.16.2",
        "flask==3.0.3",
        "jinja2==3.1.4",
        "psycopg2",
        "paypalrestsdk==1.13.3",
        "yagmail==0.15.293",
        "python-dotenv==1.0.1",
        "lxml==5.2.2",
        "pillow==10.4.0",
        "twilio==9.2.3",
        "premailer==3.10.0",
        "cryptography==42.0.8",
        "pysocks==1.7.1"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
