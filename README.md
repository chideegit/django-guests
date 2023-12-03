# Django-Guests

Track Guests as they enter and leave your office premises. It's for improved security, and adding an extra hue of a welcome experience.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Description

No more endless sheets of paper to record guests information. Switch to a more efficient process. With Django-Guests, organizations can track guests in real time, as they enter and leave the office premises. Search for guests easily and see ther data and duration they spent within the premise. The welcome experience is improved as well as security because only defined users (based on access and authorization) can have access to Guests data. 

## Features

Here are what makes the project tick! Please go through the features to see why this project is awesome!

- Simple Dashboard
    - This is the landing page for all authenticated users. However, users would be directed to the login page when they are not authenticated. 
    - You can add customizations to change the looks of the dashboard to suit your taste. 
- Search Functionality
    - Want to checkout a particular guest? All you have to do is search for the guest with either firstname or surname and you get the result in real time. 
    - The search func also uses the Q algorithm and API that comes inbuilt in django. This improves speed and search results accuracy. 
- User Authentication
    - All users on the app would have to authenticated and authorized before adding, updating or retrieving guests records. 
- Default Message Framework Integration
    - This only improves the user's experience by letting them know the outcome of the operations that they've completed within the applicaition.
- .CSV file export
    - You can back up your data by exporting into a CSV file and storing locally or in the cloud 

## Installation

Setting up and installing this project is quite straightforward and easy. Below are detailed step on how to get this web app up and running. 

1. Install a virtual environment. 
```bash
pip intall virtualenv

```

2. Create and activate a virtual environment 
```bash
virtualenv generic_name

cd generic_name && Scripts\activate
```

3. Clone the project's github repo and cd into project
```bash
git clone https://github.com/chideegit/django-guests.git

cd django-guest
```

4. Install all the dependencies contained in the [requirements.txt](./requirements.txt) file. 
```bash
pip install -r requirements.txt
```

5. Make migrations, migrate and  then run local server 
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
## Usage
Navigating through the app is as easy as it look. You can follow through the steps below to have an idea of the experience before diving in yourself.

1. Navigate to http://127.0.0.1:8000/ 
2. If there's an existing account, then you would have to log in, if not, click on the 'Sign Up' link to create a new user account. 
3. After creating a new user account, you'd be required to log in. 
4. Once you're logged, then you're free to enjoy the simplistic UI architecture and think of customization ideas to the dashboard and also adding new features!

## Contributing
If you would like to contribute to the project, please follow the guidelines outlined in the [CONTRIBUTING.md](./CONTRIBUTING.md) file.

## License
This project is licensed under the MIT License - see the [LICENSE file](./LICENSE) for details.

## Acknowledgments
Special thanks to the Django community for providing a robust framework.

Feel free to reach out for any questions, issues, or feature requests!

Happy coding🚀