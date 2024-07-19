
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
| Home |         <img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/Home_HTML.png" width="650" />  | Pass: No Errors |
| Author List |  <img src="https://drive.google.com/uc?export=view&id=1jtmRDqd6hTvefzrGdDsjamjoXZTI9m-d" width="750" /> | Pass: No Errors |
| Author Form |  <img src="https://drive.google.com/uc?export=view&id=1GuFMphiiA2CAnKpDeXQh_fFkjCfKxL1Q" width="750" />   | Pass: but there are extraneous newline characters (↩) these characters are not valid in HTML and can cause validation errors. |
| Author Detail |<img src="https://drive.google.com/uc?export=view&id=1ucnFGjgKRYGIN6jG3-asF9OjRQG91ZOM" width="750" />   | Pass: but there are extraneous newline characters (↩) these characters are not valid in HTML and can cause validation errors. |
| Author Confirm Delete |<img src="https://drive.google.com/uc?export=view&id=15PUQ24YHHTpBiaIV_zP8kKetFZ2wtJzx" width="750" />  | Pass: No Errors |
| Book List |    <img src="https://drive.google.com/uc?export=view&id=10U9tDA1H1hygVOKE0fmDLgjkXIuWrFzA" width="750" />  | Pass: No Errors |
| Book Form |    <img src="https://drive.google.com/uc?export=view&id=1gcW94ZajuFSAUn8BwQvDmEw9J44NXEuv" width="750" />  | Pass: No Errors |
|Book Detail |          <img src="https://drive.google.com/uc?export=view&id=1wt3y_k2PwK3830DfAhl9qz-tKfzQsxSx" width="750" />  | Pass: No Errors |
|Book Confirm Delete |  <img src="https://drive.google.com/uc?export=view&id=1bddBkIkFw8iPkJ_rEjaXRscis4etESfd" width="750" />  | Pass: No Errors |

**CSS code Validation using W3C validator** 

| File | Screenshot | Notes |
| ---- | ---------- | ----- |
| style.css| <img src="https://drive.google.com/uc?export=view&id=1egYf3FvcEPMMUYG8CyTYXqS4c0C0mT4o" width="750" /> | Pass: No Errors|






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

<img src="https://drive.google.com/uc?export=view&id=1MM9yIDkaIE8M9BJZCSdAnqgQgU2C0gVb" />


* Microsoft Edge

<img src="https://drive.google.com/uc?export=view&id=1OWZjcZ2ZcQ4OJCjCtH6tuQ3JcedT7EbR" />

I can confirm that the site is responsive and looks as expected on different screen sizes.


#### **Tablet** 


**Homepage**

<img src="https://drive.google.com/uc?export=view&id=1amgW4qK88_AjqHzXmo2SJ01bOeBE5x5j" width="550" />

**Login**

<img src="https://drive.google.com/uc?export=view&id=1hL1E1DxXDjyvX7E1pIAEeFFfP4I4fPmY" width="550" />

**Authors**

<img src="https://drive.google.com/uc?export=view&id=1LnpZvZODJ1FNQw16YnLVOL5tJJfbnOad" width="550" />

**Books**

<img src="https://drive.google.com/uc?export=view&id=1t6reZcEUbu_PZn2pFksfKlzrrgHTNi_7" width="550" />


#### **Mobile** 

**Sign in page**

<img src="https://drive.google.com/uc?export=view&id=1qrXEce3CvewauorKbm8SwOaOAVy-5aUR" width="500" />

**Home page**

<img src="https://drive.google.com/uc?export=view&id=1iM_zAxCnJfzRHIHSsRzXc8V74p5en--N" width="500" />

**Authors**

<img src="https://drive.google.com/uc?export=view&id=19UpwiEySSht_L9baNIjRw1zrq2w0YCtW" width="500" />

**Sign up page**

<img src="https://drive.google.com/uc?export=view&id=1nkTBMGkivmdMiNjs8XdG362h5Uf_vs2H" width="500" />

**Sign in Success**

<img src="https://drive.google.com/uc?export=view&id=16tMyuXNcvxzlr4VoEEraSbZ087jig3V1" width="500" />

**Book**

<img src="https://drive.google.com/uc?export=view&id=169D0Dq-sEmC2SnthVzu-cH7vaB20k7FM" width="500" />

### Lighthouse Audit: 
 
Book Delete

<img src="https://drive.google.com/uc?export=view&id=17zysQ6Q-S60OwH9qUkrasQ1B0DuWXe_P" width="500" />, 

Edit Author 

<img src="https://drive.google.com/uc?export=view&id=18lFz1BOETLV56Q0UDrOmIkyDzrPF8yEK" width="500" />, 

Author Delete

<img src="https://drive.google.com/uc?export=view&id=11Cyz3MSwxyPlV5QUPD60d0DnVg-KqU5H" width="500" />, 

Edit Book

<img src="https://drive.google.com/uc?export=view&id=1z7N8Rc91gn8mmYCPBJnFRjsBdid8NcXd" width="500" />, 

Books

<img src="https://drive.google.com/uc?export=view&id=1jJacpsWyGd-xLT6H1dTuvDh7s19t8JjP" width="500" />, 

Sign in page

<img src="https://drive.google.com/uc?export=view&id=1B3pkCd90XEpqvvzSPZa3_Wliehve5A9d" width="500" />, 

Sign up page

<img src="https://drive.google.com/uc?export=view&id=1FC50PYX6wj3TSHagFfMQopYI3gIixF_O" width="500" />, 

Author List

<img src="https://drive.google.com/uc?export=view&id=1VD6AKAWRJNEo1aMY40hdRQUTlpp_gaSO" width="500" />, 

Homepage

<img src="https://drive.google.com/uc?export=view&id=14A6xq7TtzSXKyP9EJDKVxEbAV9anhwlx" width="500" />, 




### **Testing Table**


| Feature | Expected Outcome | Result | Screenshots |
| ------- | ---------------- | ------ | ----------- |
|  Sign Up       |  New users can access a sign up form from the "Register" link	                |   Pass: No Errors     | <img src="https://drive.google.com/uc?export=view&id=1Pgi5Ok0SV4f9VPgIS9Pps9W_rgUTGiJY" width="650" /> |
|  Sign In Page       |  Users can log in using a form after clicking "Log in"           |      Pass  | <img src="https://drive.google.com/uc?export=view&id=1r2GZC8oI1poaxo16zNnG75MXMEKdJ5Bv" width="650" /> |
|  Sign In Successfull       |    Text displays the user logged in with their username	              |     Pass   | <img src="https://drive.google.com/uc?export=view&id=19sr1mR1eahVmjA9paXi0NcZKbr_cs62S" width="650" /> |
|  Sign Out Successfull       |    Users successfully log out after clicking "Log out"              |    Pass   | <img src="https://drive.google.com/uc?export=view&id=1oeYET3IrlEY6gRKBo1RncS-QlMulag-k" width="650" /> |
|  Author Create Successfull       |    Acknowledgement of author created	successfully                 |   Pass     | <img src="https://drive.google.com/uc?export=view&id=18JGOy9xSNCmN_7HQaVjOQK5XdnelR2jX" width="650" /> |
|  Book Create Successfull       |   Acknowledgement of book created	successfully	              |      Pass  | <img src="https://drive.google.com/uc?export=view&id=1rliMtqTKEE4gpSfILAcfQWMXNPjTOC0N" width="650" /> |
|  Delete Author       |   Confirmation screen pops-up for deletion of author              |    Pass   | <img src="https://drive.google.com/uc?export=view&id=1vXop7QcLFbwhJV2Fkrq8hEu-9j-BmtBD" width="650" /> |
|  Delete Book       |   Confirmation screen pops-up for deletion of book 	               |     Pass | <img src="https://drive.google.com/uc?export=view&id=103MYcPTFVvgR-5OyUsD7rPl_nPKUJ0MN" width="650" /> |
|  Author Delete Successfull       |  Acknowledgement of author deleted	successfully                |    Pass   | <img src="https://drive.google.com/uc?export=view&id=1zjYCANrPH6w89ZurZYoJ2-ueKMloUl-k" width="650" /> |
|  Book Delete Successfull       |   Acknowledgement of book deleted	successfully              |     Pass  | <img src="https://drive.google.com/uc?export=view&id=14f97FjqxlyWwtkBXGbCuYJp3IEJzCvfN" width="650" /> |



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


Kanban board!

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub)

- The site was deployed to GitHub pages. The steps to deploy are as follows:

  - In the GitHub repository, navigate to the Settings tab

  - From the source section drop-down menu, select the Master Branch

  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.

The live link can be found here - <https://code-institute-org.github.io/love-running-2.0/index.html>


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

## Deployment
I used the steps used when deploying our Django blog to deploy this application. The instructions for this mainly came from the follow-along videos and text-steps provided on the Code Institute LMS.


**Content**
* The records for Authors and Books were generated by searching the internet and using ChatGPT.
* Extensive reference to LMS and personal notes were made to complete all coding parts of the project. From creating views and models to deployment on Heroku.
* Code Copilot was instrumental in understanding coding problems and debugging.  

**Media**

* The Hero Image was generated using DALL-E
* Cwep Utility was used to compress and resize the Hero Image.


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
To create the README.md I used https://github.com/hiboibrahim/thebookbooth readme as an example. It followed my project very closely.
The support, help and guidence given by Iris Smoke, Martin and Kevin was invaluable and help me enormously in producing the code and debugging my application.

## **Known Bugs**

* There are no major bugs.

