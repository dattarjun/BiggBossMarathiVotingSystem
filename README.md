# BiggBossMarathiVotingSystem
SUBMITTED FOR THE PARTIAL FULFILLMENT OF THE DEGREE Bachelor of Computer Application Group Project
# Bigg Boss Marathi Voting System

### A Project Report Submitted for the Partial Fulfillment of the Degree
**Bachelor of Computer Application, Part-III, Semester - V**

---

### Project by
- **Mr. Sushant Bhanudas Shekhar**
- **Miss. Dipali Kumar Gaikwad**
- **Miss. Aishwarya Bharat Shinde**

**Under the Guidance of**  
**Dr. Kabir G. Kharade**  
Department of Computer Science,  
Shivaji University, Kolhapur

#### Year 2024-25

---

## Project Overview

This project, *Bigg Boss Marathi Voting System*, is designed to create a web-based platform for the popular reality show *Bigg Boss Marathi*. It allows viewers to participate in voting for contestants in a fair, secure, and user-friendly environment. This system addresses the need for a dedicated platform where users can:
1. Register and securely log in.
2. View the list of contestants.
3. Vote for their favorite contestant.
4. Access real-time voting statistics.

The project serves as a hands-on application of web development and database management skills learned during the Bachelor of Computer Application program at Shivaji University.

---

## Project Features

1. **User Registration and Login**:
   - Secure user authentication with encrypted passwords (bcrypt).
   - Registration and login functionality using Flask and MySQL.

2. **Voting System**:
   - Users can vote for their preferred contestant once per voting cycle.
   - Real-time vote counts displayed on the admin dashboard.

3. **Contestant Profiles**:
   - Each contestant has a dedicated profile with relevant information and a vote button.
   - Profiles display the current vote status, creating transparency.

4. **Admin Dashboard**:
   - Access for administrators to manage contestants and monitor voting progress.
   - Dashboard shows live voting data and contest standings.

---

## Technology Stack

- **FrontEnd**: HTML, CSS, JavaScript for responsive and interactive user experience.
- **BackEnd**: Flask framework in Python for handling server-side logic.
- **Database**: MySQL for storing user details, contestant information, and vote data.
- **Encryption**: Bcrypt library for secure password storage.
  
---

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/BiggBossMarathiVotingSystem.git
2. **Install Required Libraries**: pip install flask mysql-connector-python bcrypt

3. **Database Setup** : Import the database.sql file into MySQL to create the necessary tables.
Update database credentials in the Flask configuration file (config.py).
4. **Run the Application**: python app.py

5. **Access the Application** : Open your browser and navigate to http://localhost:5000.

## System Requirements
Hardware: Minimum Intel i3 or AMD equivalent, 4GB RAM, 20GB storage.
Software: Python 3.x, MySQL, Flask, and a modern web browser.
## Future Enhancements
Integration with mobile applications for expanded accessibility.
Improved contestant profiles with multimedia content.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
MIT License

Copyright (c) 2024 Sushant Bhanudas Shekhar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


Shivaji University, Kolhapur
Department of Computer Science
Bachelor of Computer Application, Part-III, Semester - V
Year 2024-25

