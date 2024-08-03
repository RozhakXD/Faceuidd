# Faceuidd - Facebook ID Retriever

![Faceuidd Logo](https://github.com/user-attachments/assets/00626f43-fb6e-49ec-b275-34631d86cc42)

Faceuidd is an easy-to-use online tool designed to quickly retrieve Facebook IDs from profiles, groups, or posts. By simply entering the appropriate Facebook link, users can obtain the ID in seconds. This tool is ideal for developers, researchers, and digital marketers who need to extract unique Facebook IDs for API integrations, data analysis, and activity tracking.

## Features
- Retrieve Facebook IDs from profiles, groups, or posts.
- Simple and user-friendly interface.
- Fast and accurate processing.

## Installation

Follow these steps to run Faceuidd on localhost using Termux:

1. **Install Termux**: Download and install the Termux app from the [F-Droid](https://f-droid.org/repo/com.termux_1020.apk).
2. **Update Packages and Install Python**:
    ```sh
    pkg update && pkg upgrade
    pkg install python
    ```
3. **Clone the Repository**:
    ```sh
    pkg install git
    git clone https://github.com/RozhakXD/Faceuidd.git
    cd Faceuidd
    ```
4. **Create a Virtual Environment and Install Dependencies**:
    ```sh
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
5. **Run the Application**:
    ```sh
    export FLASK_APP=app.py
    flask run
    ```
6. **Access the Application**:
    Open your browser and go to `http://127.0.0.1:5000`.

## Troubleshooting

If you encounter issues while running Faceuidd, try the following steps:

- **Check Internet Connection**: Ensure you have a stable internet connection.
- **Verify Dependencies**: Make sure all dependencies are installed correctly using `pip install -r requirements.txt`.
- **Check Error Messages**: Look at the terminal error messages for more information about the problem.
- **Read Documentation**: Refer to the [Flask documentation](https://flask.palletsprojects.com/) for more information on running a Flask application.
- **Contact Us**: If the issue persists, you can open an [issue on GitHub](https://github.com/RozhakXD/Faceuidd/issues) or contact the developer.

## Support

If you would like to support this project, you can donate via:
- [Trakteer](https://trakteer.id/rozhak_official/tip)
- [PayPal](https://paypal.me/rozhak9)

## Screenshot


## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/RozhakXD/Faceuidd?tab=GPL-3.0-1-ov-file) file for details.

---

Developed by [Rozhak](https://github.com/RozhakXD).
