• First, I'm making an empty git repository inside my chosen directory, then I create a new repository on github. After I connect the local repository to the remote repository on github, I create a python virtual environment. After I activate the virtual environment, then I install the dependencies required by the software to function. Then, I can create a django project. In the django project file, there exist a file named 'settings.py' to setting the project and I set the value of 'ALLOWED_HOST' inside the file to ['*'] so it can be accessed by any host, which will make the application accessible widely. Then I add a .gitignore file to the repository that is used to specify files and directories that should be ignored by git. 

After that, I create a django application. I make sure to register the django application to the django project by adding the name of the django application in the variable 'INSTALLED_APPS' on the 'settings.py' file. Then I create a model on the django application with three attributes, name as the name of the item with type CharField, amount as the amount/count of the item with type IntegerField, and description as the description of the item with type TextField. The model is used to providing a structured and organized way to work with the data. Then I create a function in 'views.py' named 'show_main'. The function includes a list of datas and a dictionary so it can be called in my html template. After that, I create an html template to create the structure and appearance of my data content on web pages. In the template, I call the data retrieved from the dictionary to the template. Then I create a routing in urls in the django application to configure the URL related to the application and urls in the django project to configure the top-level project URL. After that I create a basic testing to check the accessibility of the urls and if the page is rendered by using the html template or not. After I successfully run the tests, I can deploy the application

I use the internet to get references and chatgpt to help me with syntax error and server error

• Client request -----> urls.py -----> views.py <-----> models.py
                                           I
                                           I
                                           V
                                          HTML

The URL that is requested by the client must be matched to the urls in 'urls.py', then 'views.py' take the client request. 'views.py' may interact with 'models.py' to retrieve data. After that, 'views.py' renders the HTML template then return that as an output or response to the request

• The virtual environment is used to isolate packages and dependencies of a python project, preventing conflicts with other versions on the computer.

We can create a django web app without a virtual environment but it might create a dependencies conflicts if different projects require different versions of django or other packages.

• MVC (Model-View-Controller) is an architectural concept that separates the key components of an application into the model, the view, and the controller. MVT (Model-View-Template) is is an architectural concept used in web development to separate the key components of an application into the model, the view, and the template. MVVM (Model-View-ViewModel) is an architectural pattern that separates an application into three main logical components: the model, the view, and the view model

Differences between the three are ways to bridge between the model that represents the data and the view that represents the user interface. MVC use controller which receives user input from the view, processes it using the model, and updates the view accordingly. MVT use template which defines the structure and presentation of the user interface. It separates the HTML markup from Python code. MVVM use view model which exposes data and commands that the view can bind to. This separation of concerns can make the UI more testable and maintainable.
