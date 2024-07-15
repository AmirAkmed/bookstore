

<img src="https://drive.google.com/uc?export=view&id=1Tqg0yJPeIFMMwB5N2ZfchMcd7HRtU71Q" />


### **Project overview**

This website is for a small exclusive bookstore holding classical literature by well known authors over the centuries. The staff are interested in holding a list of authors that are of particular interest to them and the books that they have published. Guests can view these authors and books but cannot update or create any records only staff can. The bookstore website is targeted to book sellers and book readers who enjoy books.

### **List of features**

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

Staff are required to login to be able to create, delete and edit records. ****They can simply register with an username and password.


### **UX/UI**


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


***Planning and wireframe design***

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


![](h)



Book


<img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/view%20book%20details.png " width="650" />


<img src="h " width="650" />

<img src="https://github.com/AmirAkmed/bookstore/blob/main/static/img/book%20title.png" width="650" />


### **Testing**

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your project’s features and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.


**Validator Testing**<a id="validator-testing"></a>

- HTML

  - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcode-institute-org.github.io%2Flove-running-2.0%2Findex.html)

- CSS

  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fvalidator.w3.org%2Fnu%2F%3Fdoc%3Dhttps%253A%252F%252Fcode-institute-org.github.io%252Flove-running-2.0%252Findex.html\&profile=css3svg\&usermedium=all\&warning=1\&vextwarning=\&lang=en#css)

## **HTML** 

| Page | Screenshot | Notes |
| ---- | ---------- | ----- |
| Home |         <img src="https://drive.google.com/uc?export=view&id=1GnTdTjI_lyIjFuTJjRUn6xK8EXxQuJuv" width="650" />  | Pass: No Errors |
| Author List |  <img src="https://drive.google.com/uc?export=view&id=1jtmRDqd6hTvefzrGdDsjamjoXZTI9m-d" width="750" /> | Pass: No Errors |
| Author Form |  <img src="https://drive.google.com/uc?export=view&id=1GuFMphiiA2CAnKpDeXQh_fFkjCfKxL1Q" width="750" />   | Pass: but there are extraneous newline characters (↩) these characters are not valid in HTML and can cause validation errors. |
| Author Detail |<img src="https://drive.google.com/uc?export=view&id=1ucnFGjgKRYGIN6jG3-asF9OjRQG91ZOM" width="750" />   | Pass: but there are extraneous newline characters (↩) these characters are not valid in HTML and can cause validation errors. |
| 0000 Author Confirm Delete |<img src="https://drive.google.com/uc?export=view&id=15PUQ24YHHTpBiaIV_zP8kKetFZ2wtJzx" width="750" />  | Pass: No Errors |
| Book List |    <img src="https://drive.google.com/uc?export=view&id=10U9tDA1H1hygVOKE0fmDLgjkXIuWrFzA" width="750" />  | Pass: No Errors |
| Book Form |    <img src="https://drive.google.com/uc?export=view&id=1gcW94ZajuFSAUn8BwQvDmEw9J44NXEuv" width="750" />  | Pass: No Errors |
|0000 Book Detail |          <img src="https://drive.google.com/uc?export=view&id=1wt3y_k2PwK3830DfAhl9qz-tKfzQsxSx" width="750" />  | Pass: No Errors |
|0000 Book Confirm Delete |  <img src="https://drive.google.com/uc?export=view&id=1bddBkIkFw8iPkJ_rEjaXRscis4etESfd" width="750" />  | Pass: No Errors |

## **CSS** 

| File | Screenshot | Notes |
| ---- | ---------- | ----- |
| style.css| <img src="https://drive.google.com/uc?export=view&id=1egYf3FvcEPMMUYG8CyTYXqS4c0C0mT4o" width="750" /> | Pass: No Errors|

**TABLE**


| Feature | Expected Outcome | Result | Screenshots |
| ------- | ---------------- | ------ | ----------- |
|  Sign Up       |                  |   Pass: No Errors     | <img src="https://drive.google.com/uc?export=view&id=1Pgi5Ok0SV4f9VPgIS9Pps9W_rgUTGiJY" width="650" /> |
|  Sign In Page       |                  |      Pass  | <img src="https://drive.google.com/uc?export=view&id=1r2GZC8oI1poaxo16zNnG75MXMEKdJ5Bv" width="650" /> |
|  Sign In Success       |                  |     Pass   | <img src="https://drive.google.com/uc?export=view&id=19sr1mR1eahVmjA9paXi0NcZKbr_cs62S" width="650" /> |
|  Sign Out Success       |                  |    Pass   | <img src="https://drive.google.com/uc?export=view&id=1oeYET3IrlEY6gRKBo1RncS-QlMulag-k" width="650" /> |
|  Author Create Success       |                  |   Pass     | <img src="https://drive.google.com/uc?export=view&id=18JGOy9xSNCmN_7HQaVjOQK5XdnelR2jX" width="650" /> |
|  Book Create Success       |                  |      Pass  | <img src="https://drive.google.com/uc?export=view&id=1rliMtqTKEE4gpSfILAcfQWMXNPjTOC0N" width="650" /> |
|  Delete Author       |                  |    Pass   | <img src="https://drive.google.com/uc?export=view&id=1vXop7QcLFbwhJV2Fkrq8hEu-9j-BmtBD" width="650" /> |
|  Delete Book       |                  |     Pass | <img src="https://drive.google.com/uc?export=view&id=103MYcPTFVvgR-5OyUsD7rPl_nPKUJ0MN" width="650" /> |
|  Author Delete Success       |                  |    Pass   | <img src="https://drive.google.com/uc?export=view&id=1zjYCANrPH6w89ZurZYoJ2-ueKMloUl-k" width="650" /> |
|  Book Delete Success       |                  |     Pass  | <img src="https://drive.google.com/uc?export=view&id=14f97FjqxlyWwtkBXGbCuYJp3IEJzCvfN" width="650" /> |

### **Responsiveness**
Development tools were used to test responsiveness on varying devices including laptop, mobile.

Full testing was performed on the following devices:

Laptop:

* Lenovo Thinkpad Yoga 14" screen 

Mobile Devices:

* Samsung S21

Browser Compatibility:

I have tested the site using the following browsers:

* Google Chrome

<img src="https://drive.google.com/uc?export=view&id=1MM9yIDkaIE8M9BJZCSdAnqgQgU2C0gVb" />


* Microsoft Edge




**Unfixed Bugs**<a id="unfixed-bugs"></a>

You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.




### **Deployment**


Kanban board!

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub)

- The site was deployed to GitHub pages. The steps to deploy are as follows:

  - In the GitHub repository, navigate to the Settings tab

  - From the source section drop-down menu, select the Master Branch

  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.

The live link can be found here - <https://code-institute-org.github.io/love-running-2.0/index.html>


### **Citation of ALL sources(code,images, text)**


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


### **Future features**

book covers 

Features you did not add yet

● You ran out of time

● You weren’t sure if it was viable

● Weren’t comfortable implementing


### **Known Bugs**



