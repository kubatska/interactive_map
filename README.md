# interactive_map

This program generates an interactive map on which there are three layers with different markers.
A user chooses a year when movies were released, and a number of them.

The first and second layers show locations where the films and serials were filmed.
The third layer paints the map according to the population level of the countries.

To use the program you must download:
1) world.json;
2) location.csv;
Also, you must install folium and geopy libraries on your computer.

An example of the program's work results for 2015, with the limit of 100 movies, 
you can see by opening the main_map.html file.



During the program, the file "Main_map.html" with the following tags and attributes was generated:
```<```!DOCTYPE```>``` - document type declaration;
```<```html```>``` - tells the browser that this is an HTML document and represents the root of an HTML document;
```<```head```>``` -  is a container for all the head elements, can include a title for the document, scripts, styles, 
   meta information, and more;
```<```meta```>``` - provides metadata about the HTML document;
   attribute http-equiv provides an HTTP header for the information/value of the content attribute;
   content - gives the value associated with the http-equiv or name attribute;
   name - specifies a name for the metadata;
```<```script```>``` - is used to define a client-side script (JavaScript);
   src - specifies the URL of an external script file;
```<```var```>``` - is a phrase tag, define a variable;
```<```link```>``` - is used to link to external style sheets;
   rel - specifies the relationship between the current document and the linked document;
   href - specifies the location of the linked document;
```<```style```>``` - is used to define style information for an HTML document;
```<```body```>``` - defines the document's body, contains all the contents of an HTML document,
   such as text, hyperlinks, images, tables, lists, etc;
```<```div```>``` - defines a division or a section in an HTML document, is often used as a container for other HTML elements to style them with CSS or to perform certain tasks with JavaScript.


Analyzing the map, we can conclude that most films and movies were filmed in the European countries and USA.
