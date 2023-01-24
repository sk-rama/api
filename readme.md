# Python API from @rama

## Counter

### 1. set counter

You can set or update counter for any string or full website name like https://www.mybluelinux.com/what-is-email-envelope-and-email-header/

For set or update counter you must call url with **id** parameter

```
curl -X 'GET' 'https://api.pyapi.org/api/counter/set/?id=test&step=1'

# output:
{"counter":28}
```
* **id** is required and it is any string value. "test" is string for set up a counter
* **step** is optional parameter and default is 1


Set up counter for string 'https://www.mybluelinux.com/what-is-email-envelope-and-email-header/'

```
curl -X 'GET' 'https://api.pyapi.org/api/counter/set/?id=https%3A%2F%2Fwww.mybluelinux.com%2Fwhat-is-email-envelope-and-email-header%2F'

# output:
{"counter":68}
```
* **step** parameter is missing - it is optional parameter and default is 1

In html web pages you can use this call in **```<img>```** tag.

```
<img src="https://api.pyapi.org/api/counter/set/?id=https%3A%2F%2Fwww.mybluelinux.com%2Fwhat-is-email-envelope-and-email-header%2F" style="opacity: 0.0;">
```
* **```style="opacity: 0.0;"```** make img full opacity

### 2. Retrieve counter

For retrieve counter you can use a GET method:

**example with curl:**

```
curl -X 'GET' 'https://api.pyapi.org/api/counter/get/as_json/?id=test'

# output:
{"counter":28}
```
* **id** is required and it is any string value. "test" is string for get a counter

Example - recive counter for string "https://www.mybluelinux.com/what-is-email-envelope-and-email-header/"

```
curl -X 'GET' 'https://api.pyapi.org/api/counter/get/as_json/?id=https%3A%2F%2Fwww.mybluelinux.com%2Fwhat-is-email-envelope-and-email-header%2F'

# output:
{"counter":67}
```


### Hugo Static Site Generator

For usage in Hugo static site generator you must add this to your single page template:

```
<img src="https://api.pyapi.org/api/counter/set/?id={{ $.Page.Permalink }}" style="opacity: 0.0;" />
```
* **```style="opacity: 0.0;"```** make img full opacity

For retrieve counter you can use a hugo **getJSON** function in template:

```
{{ $data_view := getJSON "https://api.pyapi.org/api/counter/get/as_json/?" (querify "id" $.Page.Permalink | safeURL) }}
{{ index $data_view "counter" }}
```





