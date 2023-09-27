## Assignment 2

### • How do you implement the tasks in the checklist? Explain in a step-by-step manner (not just copy-paste from the tutorial).

First, I'm making an empty git repository inside my chosen directory, then I create a new repository on github. After I connect the local repository to the remote repository on github, I create a python virtual environment. After I activate the virtual environment, then I install the dependencies required by the software to function. Then, I can create a django project. In the django project file, there exist a file named 'settings.py' to setting the project and I set the value of 'ALLOWED_HOST' inside the file to ['*'] so it can be accessed by any host, which will make the application accessible widely. Then I add a .gitignore file to the repository that is used to specify files and directories that should be ignored by git. 

After that, I create a django application. I make sure to register the django application to the django project by adding the name of the django application in the variable 'INSTALLED_APPS' on the 'settings.py' file. Then I create a model on the django application with three attributes, name as the name of the item with type CharField, amount as the amount/count of the item with type IntegerField, and description as the description of the item with type TextField. The model is used to providing a structured and organized way to work with the data. Then I create a function in 'views.py' named 'show_main'. The function includes a list of datas and a dictionary so it can be called in my html template. After that, I create an html template to create the structure and appearance of my data content on web pages. In the template, I call the data retrieved from the dictionary to the template. Then I create a routing in urls in the django application to configure the URL related to the application and urls in the django project to configure the top-level project URL. After that I create a basic testing to check the accessibility of the urls and if the page is rendered by using the html template or not. After I successfully run the tests, I can deploy the application

### • Create a diagram explaining the flow of client requests to a Django web app and its response. Also in the diagram, explain the connections between urls.py, views.py, models.py, and the HTML file(s).

![](./diagram.drawio.svg)

The URL that is requested by the client must be matched to the urls in 'urls.py', then 'views.py' take the client request. 'views.py' may interact with 'models.py' to retrieve data. After that, 'views.py' renders the HTML template then return that as an output or response to the request

### • What is the purpose of a virtual environment? Can we create a Django web app without a virtual environment? 

The virtual environment is used to isolate packages and dependencies of a python project, preventing conflicts with other versions on the computer.

We can create a django web app without a virtual environment but it might create a dependencies conflicts if different projects require different versions of django or other packages.

### • What is MVC, MVT, and MVVM? Explain the differences between the three.

MVC (Model-View-Controller) is an architectural concept that separates the key components of an application into the model, the view, and the controller. MVT (Model-View-Template) is is an architectural concept used in web development to separate the key components of an application into the model, the view, and the template. MVVM (Model-View-ViewModel) is an architectural pattern that separates an application into three main logical components: the model, the view, and the view model

Differences between the three are ways to bridge between the model that represents the data and the view that represents the user interface. MVC use controller which receives user input from the view, processes it using the model, and updates the view accordingly. MVT use template which defines the structure and presentation of the user interface. It separates the HTML markup from Python code. MVVM use view model which exposes data and commands that the view can bind to. This separation of concerns can make the UI more testable and maintainable.

## Assignment 3

### • What is the difference between POST form and GET form in Django?

Post method sends new data to an application programming interface to be processed or stored. Get method retrieves data from an application programming interface.

### • What are the main differences between XML, JSON, and HTML in the context of data delivery?

HTML is used for creating web pages and web content. The browser requests an HTML page and the server will returns an HTML file. XMl is a markup language that uses tags to represent data in a hierarchical and structured manner. It is often used for configuration files, data interchange between heterogeneous systems, and defining document structures. JSON is a lightweight data interchange format that represents data as key-value pairs or arrays. It is widely used for data exchange between web services and APIs, configuration files, and storing structured data in databases. For XML and JSON, the browser requests data then the server returns data (in XML or JSON).

### • Why is JSON often used in data exchange between modern web applications?

Because JSON is highly readable and often preferred for configuration files and APIs due to its simplicity and compactness. JSON's structure is also simpler compared to XML, which makes it more concise for data transmission.

### • Explain how you implemented the checklist above step-by-step (not just following the tutorial).

First, I change one of the path in urlpatterns list in urls.py inside my django project folder named 'main/' to ''. Then, I create a folder in the root directory named templates and create an HTML file inside it named 'base.html'. The HTML will function as base template that can be used as a general structure for the website's page. Then I adjust the base directory in settings.py as 'templates'. Then, I change my 'main.html' as an extension of 'base.html'. Then I create a forms.py file in my django app folder to create a form structure that accepts new item data. After that, I add a function in views.py to to automatically add a new product when the form is submitted. I also change the show main function to make an object that can fetch all item object from my application database. Then, I create a 'create_product.html' inside the same folder as 'main.html' and also modified the 'main.html' file so it can add a 'add new product' button.

Then I modify my views.py and urls.py inside the django app folder so I can return data as XML and JSON. I create a function to fetch and return data as XML and JSON. Then I add the new urls path in urls.py inside the django app folder. I also modify it to retrieve data based on ID in XML and JSON. I did the same thing as I did to XML and JSON but I create a variable in the function to store the query result of data with a specific ID.

### • Access the five URLs using Postman, take screenshots of the results in Postman, and add them to README.md.

Screenshot HTML
[![Screenshot-58.png](https://i.postimg.cc/FHQqj4mh/Screenshot-58.png)](https://postimg.cc/JGPPLSGF)

Screenshot XML
[![Screenshot-59.png](https://i.postimg.cc/zf4TgJZj/Screenshot-59.png)](https://postimg.cc/Tyqy8vPL)

Screenshot JSON
[![Screenshot-60.png](https://i.postimg.cc/sgvB9tJ0/Screenshot-60.png)](https://postimg.cc/dhctJNp8)

Screenshot XML by ID
[![Screenshot-61.png](https://i.postimg.cc/SxF0D9LF/Screenshot-61.png)](https://postimg.cc/KRNsYRsJ)

Screenshot JSON by ID
[![Screenshot-62.png](https://i.postimg.cc/0QFxvBSr/Screenshot-62.png)](https://postimg.cc/k6QLFwfd)

## Assignment 4

### • Create two user accounts with three dummy data entries for each account using the model previously created in the application.

First account
[![Screenshot-65.png](https://i.postimg.cc/Hs3SRbsB/Screenshot-65.png)](https://postimg.cc/4m7bh7c9)

Second account
[![Screenshot-66.png](https://i.postimg.cc/W1C7c8R6/Screenshot-66.png)](https://postimg.cc/gxyhvv2n)

### • What is UserCreationForm in Django? Explain its advantages and disadvantages.

In Django, UserCreationForm is a built-in form class provided by the Django authentication system that simplifies the process of creating new user accounts. It is part of Django's contribution to user authentication and registration, making it easier for developers to create registration forms for their web applications. It can save development time and help ensure that user data is collected and validated correctly. However, for more complex registration and authentication requirements, or for highly customized user experiences, developers may need to build their own forms and views.

### • What is the difference between authentication and authorization in Django application? Why are both important?

In Django, authentication is often handled by the built-in authentication system, which includes user accounts, login views, and password management. Authorization, on the other hand, is typically managed through Django's permissions and the use of decorators or middleware to restrict access to specific views or functionality.

By implementing both authentication and authorization correctly, developers can create web applications that are secure, protect user data, and provide a smooth and controlled user experience.

### • What are cookies in website? How does Django use cookies to manage user session data?

Cookies are small pieces of data that a website sends to a user's web browser and are stored on the user's device. They are commonly used to track user behavior, store session information, and personalize the user experience on websites. Cookies play a crucial role in web development, especially in managing user sessions.

When a user visits a Django-powered website, Django generates a unique session ID for that user's session. This session ID is typically stored as a cookie in the user's browser. It's often named something like "sessionid". The session ID acts as a reference to the user's session data, which is stored server-side.

### • Are cookies secure to use? Is there potential risk to be aware of?

Cookies are a valuable tool for web development but should be used thoughtfully and securely to protect user data and privacy. Cookies can be used for tracking user behavior across websites, which can raise privacy concerns. Users may be uncomfortable with the idea of being tracked without their consent.

### • Explain how you implemented the checklist above step-by-step (not just following the tutorial).

First, after adding new necessary imports in 'views.py' inside the main folder I create a function called register. The function will create a registration form automatically. If a registration data is submitted, a user account will be created. Then, I create a new html file inside the template folder inside the main folder called 'register.hmtl'. It serves as a template of the registration form. Then, I import the register function inside 'urls.py' inside the main app folder. Then, add a new url path to 'urlpatterns' list to access the imported function. Next, I'll create a login and logout function to complete the authentication system. Add another new necessary imports in 'views.py for the login and logout function. Then, I create function called 'login_user' and 'logout_user'. to apply the login and logout mechanism. For the login mechanism, I create a a new html file inside the template folder inside the main folder called 'login.hmtl'. It serves as a template of user login form. For the logout mechanism, add a new button inside 'main.html' named 'logout'. Then, I import the login and logout function inside 'urls.py' inside the main app folder. Then, add the new urls path to 'urlpatterns' list to access the imported function. Now, to restrict access to the main page only to authenticated users, import 'login_required' inside 'views.py' and add '@login_required(login_url='/login')' code above the 'show_main' function. 

To add a last login feature and displaying it on the main page, we have to add the necessary imports in 'views.py' then modify the 'login_user', 'logout_user', and 'show_main' functions to create a last login cookie data to the response which will be displayed in the main page and delete the last login cookie when the user logs out. Then, modify the 'main.html' to display the last login data. At last, to connect the item model to the user model, modifiy 'models.py' by adding import user and add user in the item class. Then, modify the 'create_product' function in 'views.py' to set the user field to the user object associated with the currently logged-in user, indicating that the product belongs to that user. Then, also modify the 'show_main' function to change the hardcoded username with the username of the logged-in user on the main page. Because I changed something in 'models.py', I have to make a migration.

I use the internet to get references and chatgpt to help me with syntax error and server error