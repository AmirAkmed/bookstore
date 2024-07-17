
<img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/banner.png" />


# **Project overview**

## Introduction

 to the **Exclusive Classics Bookstore App** repository. This project is designed for a small, specialist bookstore that prides itself on its collection of classical literature. The bookstore focuses on exclusive prints and antique editions with historical significance, curated from popular and famous authors over the centuries.

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

The guest users are able to view the list of authors and a little biography on them.

The bookstore staff are able to see the list of authors as well as being able to edit or delete authors.

****![](https://github.com/AmirAkmed/bookstore/blob/main/static/img/books.png)****

**Books** 

The guest users are able to see the book names as well as authors alongside when the book was published. 

The bookstore staff are able to see the book names and authors as well as being able to edit the books too.

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


**HTML** 

| Page | Screenshot | Notes |
| ---- | ---------- | ----- |
| Home |         <img src="https://drive.google.com/uc?export=view&id=1GnTdTjI_lyIjFuTJjRUn6xK8EXxQuJuv" width="650" />  | Pass: No Errors |
| Author List |  <img src="https://drive.google.com/uc?export=view&id=1jtmRDqd6hTvefzrGdDsjamjoXZTI9m-d" width="750" /> | Pass: No Errors |
| Author Form |  <img src="https://drive.google.com/uc?export=view&id=1GuFMphiiA2CAnKpDeXQh_fFkjCfKxL1Q" width="750" />   | Pass: but there are extraneous newline characters (↩) these characters are not valid in HTML and can cause validation errors. |
| Author Detail |<img src="https://drive.google.com/uc?export=view&id=1ucnFGjgKRYGIN6jG3-asF9OjRQG91ZOM" width="750" />   | Pass: but there are extraneous newline characters (↩) these characters are not valid in HTML and can cause validation errors. |
| Author Confirm Delete |<img src="https://drive.google.com/uc?export=view&id=15PUQ24YHHTpBiaIV_zP8kKetFZ2wtJzx" width="750" />  | Pass: No Errors |
| Book List |    <img src="https://drive.google.com/uc?export=view&id=10U9tDA1H1hygVOKE0fmDLgjkXIuWrFzA" width="750" />  | Pass: No Errors |
| Book Form |    <img src="https://drive.google.com/uc?export=view&id=1gcW94ZajuFSAUn8BwQvDmEw9J44NXEuv" width="750" />  | Pass: No Errors |
|Book Detail |          <img src="https://drive.google.com/uc?export=view&id=1wt3y_k2PwK3830DfAhl9qz-tKfzQsxSx" width="750" />  | Pass: No Errors |
|Book Confirm Delete |  <img src="https://drive.google.com/uc?export=view&id=1bddBkIkFw8iPkJ_rEjaXRscis4etESfd" width="750" />  | Pass: No Errors |

**CSS** 

| File | Screenshot | Notes |
| ---- | ---------- | ----- |
| style.css| <img src="https://drive.google.com/uc?export=view&id=1egYf3FvcEPMMUYG8CyTYXqS4c0C0mT4o" width="750" /> | Pass: No Errors|






### **Responsiveness**
Development tools were used to test responsiveness on varying devices including laptop, mobile.

Full testing was performed on the following devices:

#### Laptop:


* Lenovo Thinkpad Yoga 14" screen 

Mobile Devices:

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
|  Sign In Success       |    Text displays the user logged in with their username	              |     Pass   | <img src="https://drive.google.com/uc?export=view&id=19sr1mR1eahVmjA9paXi0NcZKbr_cs62S" width="650" /> |
|  Sign Out Success       |    Users successfully log out after clicking "Log out"              |    Pass   | <img src="https://drive.google.com/uc?export=view&id=1oeYET3IrlEY6gRKBo1RncS-QlMulag-k" width="650" /> |
|  Author Create Success       |    Acknowledgement of author created	successfully                 |   Pass     | <img src="https://drive.google.com/uc?export=view&id=18JGOy9xSNCmN_7HQaVjOQK5XdnelR2jX" width="650" /> |
|  Book Create Success       |   Acknowledgement of book created	successfully	              |      Pass  | <img src="https://drive.google.com/uc?export=view&id=1rliMtqTKEE4gpSfILAcfQWMXNPjTOC0N" width="650" /> |
|  Delete Author       |   Confirmation of deletion of author              |    Pass   | <img src="https://drive.google.com/uc?export=view&id=1vXop7QcLFbwhJV2Fkrq8hEu-9j-BmtBD" width="650" /> |
|  Delete Book       |   Confirmation of deletion of book 	               |     Pass | <img src="https://drive.google.com/uc?export=view&id=103MYcPTFVvgR-5OyUsD7rPl_nPKUJ0MN" width="650" /> |
|  Author Delete Success       |  Acknowledgement of author deleted	successfully                |    Pass   | <img src="https://drive.google.com/uc?export=view&id=1zjYCANrPH6w89ZurZYoJ2-ueKMloUl-k" width="650" /> |
|  Book Delete Success       |   Acknowledgement of book deleted	successfully              |     Pass  | <img src="https://drive.google.com/uc?export=view&id=14f97FjqxlyWwtkBXGbCuYJp3IEJzCvfN" width="650" /> |



**Unfixed Bugs**<a id="unfixed-bugs"></a>

You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your project’s features and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.


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


## **Credits**


GitHub 
Django 
Gitpod
Heroku
Code Institute LMS
Slack Cod Institute
Webp
Tinypng
ChatGPT
Code Copilot
Python used as the back-end programming language.


* Git used for version control. (git add, git commit, git push)


* GitHub used for secure online code storage.


* GitHub Pages used for hosting the deployed front-end site.


* Gitpod used as a cloud-based IDE for development.

* Bootstrap used as the front-end CSS framework for modern responsiveness and pre-built components.


**Content**
* The records for Authors and Books were generated by searching the internet and using ChatGPT.
* Extensive reference to LMS and personal notes were made to complete all coding parts of the project. From creating views and models to deployment on Heroku.
* Code Copilot was instrumental in understanding coding problems and debugging.  


	https://amirbooks-d3222602a6af.herokuapp.com/

**Media**


* The Hero Image was generated using DALL-E
* Cwep Utility was used to compress and resize the Hero Image.



In this section you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism.

You can break the credits section up into Content and Media, depending on what you have included in your project.

 **Content**<a id="content"></a>

- The text for the Home page was taken from Wikipedia Article A

- Instructions on how to implement form validation on the Sign Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)

- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

 **Media**<a id="media"></a>

- The photos used on the home and sign up page are from This Open Source site

- The images used for the gallery page were taken from this other open source site

Congratulations on completing your Readme, you have made another big stride in the direction of being a developer!









## **Future features**

* book covers 

* The about page but ran out of time

* Add search facility for Authors and Books
* Add email verification
* Add additional fields to the models for more information on books and authors
* Add a contact page




Features you did not add yet

● You ran out of time

● You weren’t sure if it was viable

● Weren’t comfortable implementing


## **Known Bugs**

* There are no major bugs.


