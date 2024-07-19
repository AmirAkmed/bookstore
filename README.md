
<img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/banner.png" />


# **Project overview**

## Introduction

Welcome to the **Exclusive Classics Bookstore App** repository. This project is designed for a small, specialist bookstore that prides itself on its collection of classical literature. The bookstore focuses on exclusive prints and antique editions with historical significance, curated from popular and famous authors over the centuries.

This app is intended to facilitate the management of this unique collection by providing a system for staff to maintain a comprehensive list of authors and the books they have published. The app is built with two primary tables: one for authors and another for their respective publications.

The live application can be viewed here :

https://amirbooks-d3222602a6af.herokuapp.com/

Key Features:

* **Author Management**: Easily add, edit, and delete author information.
* **Book Management**: Maintain detailed records of books, including titles, publication dates, and associated authors.
* **Staff-Only Access**: Secure login system ensuring that only authorized staff members can access and manage the information.

Please note that this system is exclusively for internal use. Customers will not have access to the site or its contents. This ensures that our treasured collection remains secure and meticulously documented.

We hope this tool enhances your experience in managing our esteemed collection of classical literature.


## **List of features**

****![](https://github.com/AmirAkmed/bookstore/blob/main/static/img/authors.png)****

**Authors**

Only authorized bookstore staff are able to view the list of authors and view a brief biography of them.
Staff members can add new authors and also edit or delete author information.


****![](https://github.com/AmirAkmed/bookstore/blob/main/static/img/books.png)****

**Books** 

Only authorized bookstore staff can view detailed information about the books, including titles, authors, and publication dates. 
Staff can also edit book information as needed and add new books.

![](https://github.com/AmirAkmed/bookstore/blob/main/static/img/login.png)

**Login**

Staff are required to login to be able to create, delete and edit records. 
They can simply register with an username and password.


## **UX/UI**


**Goals** 

To make the website simple and uncluttered in appearance. To aid in immediately identifying features such as authors and book listings and edit, create and delete features. 

**Design choices**

The schema should be basic and simple in design using primary and foreign keys. Minimising the number of tables (models) required. This will also simplify the design of templates but provide all the required functionality.

**User stories** 

- As a new user, I want to quickly and easily find the features. 

- As a new user, I want to quickly find a list of books.

- As a new user I want to quickly find a list of authors.

- As a new user I want to be able to quickly and easily create, edit and delete author records.

- As a new user I want to be able to create, edit and delete book records.

- As a new user I want feedback on actions I have performed on the website.

- As a new user I want confirmation before I delete any records.


### ***Planning and wireframe design***

**Database Schema for Author and Books**


<img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/schema.png " width="650" />


**Homepage**


<img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/homepage.png " width="650" />


**Login**


<img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/loginwf.png " width="650" />


**Author**



<img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/author.png " width="650" />



<img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/view%20author%20details.png " width="650" />



<img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/author%20list.png " width="650" />



**Book**


<img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/view%20book%20details.png " width="650" />


<img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/book%20title.png" width="650" />


## **Testing**


**HTML code Validation using W3C validator** 

| Page | Screenshot | Notes |
| ---- | ---------- | ----- |
| Home |         <img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/Home_HTML.png" alt="home w3c validation" width="650" />  | Pass: No Errors |
| Author List |  <img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/screenshots/validate%20html/Author_List_HTML.png" alt="author list w3c validation" width="750" /> | Pass: No Errors |
| Author Form |  <img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/screenshots/validate%20html/Author_Form_HTML.png" alt="author form w3c validation" width="750" />   | Pass: but there are extraneous newline characters (↩) these characters are not valid in HTML and can cause validation errors. |
| Author Detail |<img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/screenshots/validate%20html/Author_Detail_HTML.png" alt="author detail w3c validation" width="750" />   | Pass: but there are extraneous newline characters (↩) these characters are not valid in HTML and can cause validation errors. |
| Author Confirm Delete |<img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/screenshots/validate%20html/Author_Confirm_Delete_HTML.png" alt="author confirm delete w3c validation" width="750" />  | Pass: No Errors |
| Book List |    <img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/screenshots/validate%20html/Book_List_HTML.png" alt="book list w3c validation" width="750" />  | Pass: No Errors |
| Book Form |    <img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/screenshots/validate%20html/Book_Form_HTML.png" alt="book form w3c validation" width="750" />  | Pass: No Errors |
|Book Detail |          <img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/screenshots/validate%20html/Book_Detail_HTML.png" alt="book detail w3c validation" width="750" />  | Pass: No Errors |
|Book Confirm Delete |  <img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/screenshots/validate%20html/Book_Confirm_Delete_HTML.png" alt="book confirm delete w3c validation" width="750" />  | Pass: No Errors |

**CSS code Validation using W3C validator** 

| File | Screenshot | Notes |
| ---- | ---------- | ----- |
| style.css| <img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/screenshots/validate%20html/Style_Css_Validation.png" alt="style.css w3c validation" width="750" /> | Pass: No Errors|






### **Responsiveness**
Development tools were used to test responsiveness on varying devices including laptop, tablet and mobile.

Full testing was performed on the following devices:

#### Laptop:


* Lenovo Thinkpad Yoga 14" screen 

#### Mobile Devices:

* Samsung S21

Browser Compatibility:

I have tested the site using the following browsers:

* Google Chrome

<img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/screenshots/Responsiveness/Laptop/Laptop_Chrome.png" />


* Microsoft Edge

<img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/screenshots/Responsiveness/Laptop/Laptop_Edge.png" />

I can confirm that the site is responsive and looks as expected on different screen sizes.


#### **Tablet** 


**Homepage**

<img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/screenshots/Responsiveness/Tablet%20(Galaxy%20Tab%20A)/Tablet_Homepage.jpg" width="550" />

**Login**

<img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/screenshots/Responsiveness/Tablet%20(Galaxy%20Tab%20A)/Tablet_Login.jpg" width="550" />

**Authors**

<img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/screenshots/Responsiveness/Tablet%20(Galaxy%20Tab%20A)/Tablet_Authors.jpg" width="550" />

**Books**

<img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/screenshots/Responsiveness/Tablet%20(Galaxy%20Tab%20A)/Tablet_Books.jpg" width="550" />


#### **Mobile** 

**Sign in page**

<img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/screenshots/Responsiveness/Mobile%20(Samsung%20S21)/Mobile_SignIn_Page.jpg" width="500" />

**Home page**

<img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/screenshots/Responsiveness/Mobile%20(Samsung%20S21)/Mobile_Homepage.jpg" width="500" />

**Authors**

<img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/screenshots/Responsiveness/Mobile%20(Samsung%20S21)/Mobile_Authors.jpg" width="500" />

**Sign up page**

<img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/screenshots/Responsiveness/Mobile%20(Samsung%20S21)/Mobile_SignUp_Page.jpg" width="500" />

**Sign in Success**

<img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/screenshots/Responsiveness/Mobile%20(Samsung%20S21)/Mobile_SignIn_%20Success.jpg" width="500" />

**Book**

<img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/screenshots/Responsiveness/Mobile%20(Samsung%20S21)/Mobile_Book.jpg" width="500" />








### Lighthouse Audit: 
 
Book Delete

<img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/screenshots/valid%202/Perf_Book_Delete.png" width="500" />, 

Edit Author 

<img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/screenshots/valid%202/Perf_Edit_Author.png" width="500" />, 

Author Delete

<img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/screenshots/valid%202/Perf_Author_Delete.png" width="500" />, 

Edit Book

<img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/screenshots/valid%202/Perf_Book_Edit.png" width="500" />, 

Books

<img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/screenshots/valid%202/Perf_Book_List.png" width="500" />, 

Sign in page

<img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/screenshots/valid%202/Perf_login.png" width="500" />, 

Sign up page

<img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/screenshots/valid%202/Perf_SignUp.png" width="500" />, 

Author List

<img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/screenshots/valid%202/Perf_Author_List.png" width="500" />, 

Homepage

<img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/screenshots/valid%202/Perf_Home.png" width="500" />, 




### **Testing Table**


| Feature | Expected Outcome | Result | Screenshots |
| ------- | ---------------- | ------ | ----------- |
|  Sign Up       |  New users can access a sign up form from the "Register" link	                |   Pass: No Errors     | <img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/screenshots/Testing/Testing_SignUp.png" width="650" /> |
|  Sign In Page       |  Users can log in using a form after clicking "Log in"           |      Pass  | <img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/screenshots/Testing/Testing_SignIn_Page.png" width="650" /> |
|  Sign In Successfull       |    Text displays the user logged in with their username	              |     Pass   | <img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/screenshots/Testing/Testing_SignIn_Amir.png" width="650" /> |
|  Sign Out Successfull       |    Users successfully log out after clicking "Log out"              |    Pass   | <img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/screenshots/Testing/Testing_SignOut_Success.png" width="650" /> |
|  Author Create Successfull       |    Acknowledgement of author created	successfully                 |   Pass     | <img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/screenshots/Testing/Testing_Author_Create_Success.png" width="650" /> |
|  Book Create Successfull       |   Acknowledgement of book created	successfully	              |      Pass  | <img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/screenshots/Testing/Testing_Book_Create_success.png" width="650" /> |
|  Delete Author       |   Confirmation screen pops-up for deletion of author              |    Pass   | <img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/screenshots/Testing/Testing_Delete_Author.png" width="650" /> |
|  Delete Book       |   Confirmation screen pops-up for deletion of book 	               |     Pass | <img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/screenshots/Testing/Testing_Delete_Book.png" width="650" /> |
|  Author Delete Successfull       |  Acknowledgement of author deleted	successfully                |    Pass   | <img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/screenshots/Testing/Testing_Delete_Author_Success.png" width="650" /> |
|  Book Delete Successfull       |   Acknowledgement of book deleted	successfully              |     Pass  | <img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/screenshots/Testing/Testing_Delete_Book_Success.png" width="650" /> |




**Unfixed Bugs**<a id="unfixed-bugs"></a>

The **Exclusive Classics Bookstore App** has been thoroughly tested and refined to provide a reliable and user-friendly experience for bookstore staff. The testing process ensured that all features work as intended and that the application is accessible across various devices and browsers. As of the latest testing, there are no known major bugs in the **Exclusive Classics Bookstore App** project. While time constraints and initial implementation challenges were encountered, all issues were ultimately resolved through thorough testing and debugging.

### Testing and Functionality

Extensive testing has been conducted on the application, utilizing a sample dataset of 13 authors and 26 book titles. The following features were tested rigorously:

- **Record Creation**: New author and book records can be created without issues.
- **Record Deletion**: Records can be deleted, with a confirmation modal to prevent accidental deletions.
- **Record Listing**: Authors and books are listed alphabetically.
- **Record Editing**: Existing records can be edited and updated correctly.

### Cross-Browser and Device Compatibility

The application has been tested on multiple devices and browsers to ensure consistent functionality and appearance. The following points highlight the compatibility results:

- **Devices Tested**:
  - **Laptop**: Full functionality with all features accessible and usable.
  - **Tablet**: Responsive design adapts well, with navigation and record management features intact.
  - **Mobile**: Elements rearrange for convenience, maintaining usability and readability.

- **Browsers Tested**:
  - **Google Chrome**: No issues found, full compatibility.
  - **Mozilla Firefox**: No issues found, full compatibility.
  - **Safari**: No issues found, full compatibility.
  - **Microsoft Edge**: No issues found, full compatibility.

### Design and User Experience Enhancements

To improve user experience and application performance, the following enhancements were made:

- **Alphabetical Listing**: Ensured authors and books are listed alphabetically for easy navigation.
- **Delete Confirmation Modal**: Added a confirmation popup to prevent accidental deletions.
- **Responsive Design**: Navigation bar reduces to a burger icon on smaller screens, with dropdown lists for easy access.
- **Z-Index Adjustment**: Success and failure messages now appear correctly above the hero image, thanks to appropriate z-index and margin adjustments.
- **Optimized Hero Image**: Compressed original image and provided smaller versions for different screen sizes, maintaining aspect ratio and reducing load times.
- **Message Display Fix**: Initially, no messages were being displayed during login and registeration. This was remedied by using the `@login_required_message` decorator available as part of Django's extensive login features.

### Interesting Bugs and Problems Encountered

During the testing phase, a few interesting issues were identified and resolved:

- **Non-Alphabetic Listing**: Initially, records were not listed alphabetically, which was promptly fixed to enhance user navigation.
- **Accidental Deletions**: The delete button initially removed records immediately. This was addressed by implementing a confirmation modal.
- **Message Display**: Success and failure messages were obscured by the hero image. Adjustments to z-index and top margin resolved this issue.
- **Hero Image Load Time**: The loading time of the hero image was optimized by compressing the image and creating smaller versions for different screen sizes.
- **Initial Message Display Issue**: Initially, no messages were being displayed during login and registeration. This was remedied by using the `@login_required_message` decorator available as part of Django's extensive login features.


**Validator Testing**<a id="validator-testing"></a>

- HTML

  - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcode-institute-org.github.io%2Flove-running-2.0%2Findex.html)

- CSS

  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fvalidator.w3.org%2Fnu%2F%3Fdoc%3Dhttps%253A%252F%252Fcode-institute-org.github.io%252Flove-running-2.0%252Findex.html\&profile=css3svg\&usermedium=all\&warning=1\&vextwarning=\&lang=en#css)



## **Deployment**

<img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/Kanban-board.png" width="500" />, 

<img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/Milestone-V2-0.png" width="500" />, 


I used the steps used when deploying our Django blog to deploy this application. The instructions for this mainly came from the follow-along videos and text-steps provided on the Code Institute LMS.
Using a Kanban board, issues, labels, and milestones in my bookstore project for my final assessment has been incredibly beneficial for organizing and tracking my work efficiently. The Kanban board provided me with a clear visual overview of my project's progress, allowing me to see the status of tasks at a glance and quickly identify any bottlenecks in my workflow. By creating issues for each task, I could ensure that every work item was documented and systematically addressed. Labels were invaluable for categorizing and prioritizing these issues, making it easier to filter and focus on specific tasks or areas that needed attention. Additionally, setting milestones helped me stay on track with my goals, providing clear targets and deadlines to measure my progress against. Overall, these tools enhanced my productivity and ensured that I stayed organized and aware of my project's status and priorities throughout the development process

**Content**
* The records for Authors and Books were generated by searching the internet and using ChatGPT.
* Extensive reference to LMS and personal notes were made to complete all coding parts of the project. From creating views and models to deployment on Heroku.
* Code Copilot was instrumental in understanding coding problems and debugging.  

**Media**

* The Hero Image was generated using DALL-E
* Cwep Utility was used to compress and resize the Hero Image.



## Tools and Technologies Used

The technologies implemented in this application included HTML5, CSS, Bootstrap, Python, and Django.

- **Python**: Used as the back-end programming language.
- **Git**: Used for version control. (git add, git commit, git push)
- **GitHub**: Used for secure online code storage.
- **Heroku**: Used for hosting the deployed front-end and back-end site.
- **Gitpod**: Used as a cloud-based IDE for development.
- **Bootstrap**: Used as the front-end CSS framework for modern responsiveness and pre-built components.
- **Code Institute Hosted Postgres Database**: Used to store records.
- **Balsamiq**: Used for wireframes.
- **Google and Stack Overflow**: Utilized for general research or solving a bug, information gathering, and various online tools.
- **Slack (Code Institute Channels)**: Used for understanding and debugging issues.
- **Webp CLI**: Utility used to compress and resize hero images.
- **TinyPNG**: Used extensively for images included in README.md.
- **ChatGPT**: Used throughout the application including generating records.
- **Code Copilot**: Used to understand code and debugging.

## Languages Used
- HTML5
- CSS
- Python


## **Future features**

The intention was to produce a minimal viable product but below are a list of future enhacements:
* Add book covers 
* Add about page
* Add search facility for Authors and Books
* Add email verification
* Add additional fields to database and views for more information on books and authors
* Add a contact page
* Add social media links

## **Credits**
To create the README.md I used https://github.com/hiboibrahim/thebookbooth readme as an example. It followed my project very closely. I must thank Hibo Ibrahim for that.

The support, help, and guidance given by Iris Smoke, Martin, and Kevin, our facilitator and tutors, were invaluable and helped me enormously in producing the code and debugging my application. I am enormously grateful to them for all their patience and hard work, especially Iris.

## **Known Bugs**

* There are no major bugs.

