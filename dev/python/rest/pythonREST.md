# Python Dev Notes for REST

My notes for Python REST development is listed herein.

<br/>

## Development Setup

Refer to [Python Dev Notes](../pythonREADME.md#develoment_setup) for information about general setup.

### Setup a JSON server

One option for a JSON server is the free and open package named **json-server**, implemented on top of the **Node.js** environment. As Node.js itself is an open-source, cross-platform JavaScript run-time environment that executes JavaScript code outside of a browser.

The procedure to set up Node.js is as follows:

1. Download Node.js from its [download page](https://nodejs.org/en/download/). Select the platform (Windows, Linux, or macOS). Select the latest LTS version at the time of your download. Install it on your target system.
1. For Windows platform, open a `command prompt` window. Run one of the following:

```
node --version

npm --version
```

You should see the version that matches your downloaded and installed Node.js image.

3. Install `json-server` for Node.js

```
npm install -g json-server
```

4. Run `json-server` for Node.js

```
json-server --watch a_json_file
```

<br/>

## Tutorials and Resources

- [Python Requests library](https://requests.readthedocs.io/en/latest/)
- [Working with RESTful APIs](https://edube.org/study/pcpp1-4) by [OpenEDG](https://openedg.org/)
- [Python Requests Tutorial](https://www.geeksforgeeks.org/python-requests-tutorial/) by Geeks for Geeks

## Notes

Possible exceptions (source: Sec. \*\*1.6.1.10 Making life easier with the requests module
, Working with RESTful APIs, OpenEDG)

```
RequestException
|___HTTPError
|___ConnectionError
|   |___ProxyError
|   |___SSLError
|___Timeout
|   |___ConnectTimeout
|   |___ReadTimeout
|___URLRequired
|___TooManyRedirects
|___MissingSchema
|___InvalidSchema
|___InvalidURL
|   |___InvalidProxyURL
|___InvalidHeader
|___ChunkedEncodingError
|___ContentDecodingError
|___StreamConsumedError
|___RetryError
|___UnrewindableBodyError
```

<br/>

## Practices and Exercises

Note the files `src/cars.json` and `src/nyse.xml` are sample input data from the online course [**Working with RESTful APIs**](https://edube.org/study/pcpp1-4) at [OpenEDG](https://openedg.org/).

<br/>
