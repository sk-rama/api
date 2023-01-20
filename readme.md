# Python API from @rama

## Counter

You can set or update counter for any string (e.g. full website name like https://example/directory/filename)

For set or update counter you must call url

<code>
https://api.pyapi.org/api/counter/set/?id=test&step=1
</code>



* **id** is required and it is any string value
* **step** is optional parameter and default is 1

In html web pages you can use this call in **```<img>```** tag.

Example:

<code>
<img src="https://api.pyapi.org/api/counter/set/?id=https%3A%2F%2Fwww.mybluelinux.com%2Fwhat-is-email-envelope-and-email-header%2F" style="opacity: 0.0;">
</code>



