# Faceuidd - Facebook ID Retriever

![Faceuidd Logo](https://github.com/user-attachments/assets/00626f43-fb6e-49ec-b275-34631d86cc42)

Faceuidd is a simple online tool to quickly get Facebook IDs from profiles, groups, or posts. Just enter a Facebook link to get the ID in seconds. Perfect for developers, researchers, and marketers needing Facebook IDs for API integration, data analysis, and tracking.

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
![FunPic_20240803_091304861](https://github.com/user-attachments/assets/22df319d-b3bc-448c-9c9a-131ba18d2204)

![FunPic_20240803_091237802](https://github.com/user-attachments/assets/a4c1f2f1-a494-4736-a382-1897fe912ba1)

## API Usage

You can also use Faceuidd via its API. Here is an example of how to use the API with Python:

```python
import requests
import json

headers = {
    "Content-Type": "application/json"
}

data = json.dumps({
    "link": "https://www.facebook.com/share/p/...?"
})

response = requests.post('https://www.faceuidd.rozhakxd.my.id/api/v1/facebook-id-retriever/', headers=headers, data=data)
print(response.json())
```

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/RozhakXD/Faceuidd?tab=GPL-3.0-1-ov-file) file for details.

---

Developed by [Rozhak](https://github.com/RozhakXD).
