# Python API from @rama

## Counter

You can set or update counter for any string or full website name like https://www.mybluelinux.com/what-is-email-envelope-and-email-header/

For set or update counter you must call url

```
https://api.pyapi.org/api/counter/set/?id=test&step=1
```



* **id** is required and it is any string value
* **step** is optional parameter and default is 1

In html web pages you can use this call in **```<img>```** tag.

Example:

```
<img src="https://api.pyapi.org/api/counter/set/?id=https%3A%2F%2Fwww.mybluelinux.com%2Fwhat-is-email-envelope-and-email-header%2F" style="opacity: 0.0;">
```
* **```style="opacity: 0.0;"```** make img full opacity

### Hugo

For usage in Hugo static site generator you must add this to your single page template:

```
<img src="https://api.pyapi.org/api/counter/set/?id={{ $.Page.Permalink }}" style="opacity: 0.0;" />
```





