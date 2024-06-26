> [Python Snippets](../README.md) / [각종 조각코드 모음](README.md) / 구글드라이브 다루기 - Google Drive with PyDrive.md
## 구글드라이브 다루기 - Google Drive with PyDrive
https://github.com/gsuitedevs/PyDrive

```
PyDrive
PyDrive is a wrapper library of google-api-python-client that simplifies many common Google Drive API tasks.

Project Info
Homepage: https://pypi.python.org/pypi/PyDrive
Documentation: Official documentation on GitHub pages
GitHub: https://github.com/gsuitedevs/PyDrive
Features of PyDrive
Simplifies OAuth2.0 into just few lines with flexible settings.
Wraps Google Drive API into classes of each resource to make your program more object-oriented.
Helps common operations else than API calls, such as content fetching and pagination control.
How to install
You can install PyDrive with regular pip command.

$ pip install PyDrive
To install the current development version from GitHub, use:

$  pip install git+https://github.com/gsuitedevs/PyDrive.git#egg=PyDrive
OAuth made easy
Download client_secrets.json from Google API Console and OAuth2.0 is done in two lines. You can customize behavior of OAuth2 in one settings file settings.yaml.

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)
File management made easy
Upload/update the file with one method. PyDrive will do it in the most efficient way.

file1 = drive.CreateFile({'title': 'Hello.txt'})
file1.SetContentString('Hello')
file1.Upload() # Files.insert()

file1['title'] = 'HelloWorld.txt'  # Change title of the file
file1.Upload() # Files.patch()

content = file1.GetContentString()  # 'Hello'
file1.SetContentString(content+' World!')  # 'Hello World!'
file1.Upload() # Files.update()

file2 = drive.CreateFile()
file2.SetContentFile('hello.png')
file2.Upload()
print('Created file %s with mimeType %s' % (file2['title'],
file2['mimeType']))
# Created file hello.png with mimeType image/png

file3 = drive.CreateFile({'id': file2['id']})
print('Downloading file %s from Google Drive' % file3['title']) # 'hello.png'
file3.GetContentFile('world.png')  # Save Drive file as a local file

# or download Google Docs files in an export format provided.
# downloading a docs document as an html file:
docsfile.GetContentFile('test.html', mimetype='text/html')
File listing pagination made easy
PyDrive handles file listing pagination for you.

# Auto-iterate through all files that matches this query
file_list = drive.ListFile({'q': "'root' in parents"}).GetList()
for file1 in file_list:
    print('title: {}, id: {}'.format(file1['title'], file1['id']))

# Paginate file lists by specifying number of max results
for file_list in drive.ListFile({'maxResults': 10}):
    print('Received {} files from Files.list()'.format(len(file_list))) # <= 10
    for file1 in file_list:
        print('title: {}, id: {}'.format(file1['title'], file1['id']))
Concurrent access made easy
All calls made are thread-safe. The underlying implementation in the google-api-client library is not thread-safe, which means that every request has to re-authenticate an http object. You can avoid this overhead by creating your own http object for each thread and re-use it for every call.

This can be done as follows:

# Create httplib.Http() object.
http = drive.auth.Get_Http_Object()

# Create file object to upload.
file_obj = drive.CreateFile()
file_obj['title'] = "file name"

# Upload the file and pass the http object into the call to Upload.
file_obj.Upload(param={"http": http})
You can specify the http-object in every access method which takes a param parameter.
```