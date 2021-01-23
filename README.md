# Dynamic Website Design for a Manufacturing Company
## AIM:
To design a dynamic website for a chip manufacturing company.

## DESIGN STEPS:
### Step 1: 
Requirement collection.
### Step 2:
Creating the layout using HTML and CSS.
### Step 3:
Updating the sample content.
### Step 4:
Choose the appropriate style and color scheme.
### Step 5:
Validate the layout in various browsers.
### Step 6:
Validate the HTML code.
### Step 7:
Create a database model and migrate the database.
### Step 8:
Retrieve data from database and display it in a dynamic webpage.
### Step 9:
Publish the website in the given URL.

## PROGRAM:
### base.html
```
{% load static %}
<!DOCTYPE html>
<html lang="en">

<head>
    <title>Stark Private Limited</title>
    <link rel="stylesheet" href="{% static 'css/layout.css' %}">
    <link rel = "icon" href ="{% static 'img/2.png' %}" type = "image/x-icon"> 
              
</head>

<body>
    <div class="container">
    <div class="banner">
    <h1 id="title">
        Stark Private Limited
    </h1>
    </div>
    <div class="menu">
        <div class="menuitem"><a class="a" href="/home">Home</a></div> 
        <div class="menuitem"><a class="a" href="/products">Products</a></div> 
        <div class="menuitem"><a class="a" href="/people">People</a></div>
        <div class="menuitem"><a href="/contact">Contact Us</a></div> 
    </div><div class="content">
    {% block content %}    
    {% endblock  %}
    </div>
    <div class="footer">
        Copyright © 2021 Stark Private Limited, Developed by Ragav.
    </div>
    </div>
</body>

</html>
```

### home.html
```
{% extends "website/base.html" %}

{% block content %}
    <div class="homecontent">    
    <h1>About Us</h1>
    <img src="/static/img/stark.jpeg" alt="Building">
    <div class="contenttext">
    Silicon Pvt Ltd, provides a broad range of semiconductor and infrastructure software applications that serve the data center, networking, software, broadband, wireless, and storage and industrial markets. Common applications for its products include: data center networking, home connectivity, broadband access, telecommunications equipment, smartphones, base stations, data center servers and storage, factory automation, power generation and alternative energy systems, displays, and mainframe operations and management, and application software development. Some of Silicon's core technologies and products include:
    <ul>
        <li>Memory Chips</li>
        <li>Sata hdd</li>
        <li>Sata ssd </li>
        <li>Broadband Modems</li>
        <li>Wifi Devices</li>
        <li>Switching Devices</li>
        <li>Optical Sensors</li>
    </ul> 
    </div>
    </div>
{% endblock  %}
```
### products.html
```
{% extends "website/base.html" %}

{% block content %}
<div class="productcontent">
    <h1>Our Premium Products</h1>
    <div class="productitems">
        {% for products in productss %}
        <div class="productitem">
            <div class="itemimage">
                <img src="{{ products.photo.url }}" alt="product image" height="200" width="200">
            </div>
            <div class="productsname"><strong>PRODUCT NAME:</strong>{{ products.name }}</div>
            <div class="productsprice"><strong>PRODUCT PRICE:</strong>{{ products.price }}</div>
        </div>
        {% endfor %}
    </div>
</div>
{% endblock  %}
```
### people
```
{% extends "website/base.html" %}

{% block content %}
    <h1 id="Ex">Executives</h1>
        <div class="row">
        {% for people in peoples %}
            <div class="column">
                <img src="{{ people.photo.url }}" alt="executive image" width="250" height="200">
                <div class="membername"><strong><u>EXECUTIVE</u>:{{ people.name }}</strong></div>
                <div class="designation"><strong><u>DESIGNATION</u>:{{ people.designation }}</strong></div>
            </div>
            {% endfor %}
        </div>
{% endblock  %}
```

### contact.html
```
{% extends "website/base.html" %}

{% block content %}
   <img src="/static/img/4.png" alt="contact">
    <h1 class="contact">
        <strong><u>CONTACT US</u></strong> 
    </h1>
    <hr>
    <h2 class="contact">
        ADDRESS:© Stark pvt,Mountain View, California, United-States
            <br/>
        EMAIL ID:starkprivatelimited@gmail.com
            <br/>
        CONTACT NO:9876543217
    </h2>
    <hr>
{% endblock  %}
```

### models.py
```
from django.db import models
from django.contrib import admin
# Create your models here.
class people(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/', blank=True)

class peopleAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'photo')

class products(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='photos/', blank=True)
class productsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'photo')
```

### admin.py
```
from django.contrib import admin
from .models import people,peopleAdmin
from .models import products,productsAdmin


# Register your models here.

admin.site.register(people,peopleAdmin)

admin.site.register(products,productsAdmin)
```

## OUTPUT:
![output](./static/img/output1.png)

![output](./static/img/output2.png)

![output](./static/img/output3.png)

![output](./static/img/output4.png)

## admin page
![output](./static/img/admin-products.png)

![output](./static/img/admin-people.png)

## CODE VALIDATION REPORT:
![output](./static/img/validate1.png)

![output](./static/img/validate2.png)

![output](./static/img/validate3.png)

![output](./static/img/validate4.png)


## RESULT:
Thus a website is designed for the chip manufacturing company and is hosted in the URL http://ragav.student.saveetha.in:8000/ HTML code is validated.