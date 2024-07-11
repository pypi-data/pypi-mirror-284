
# Indonesia Latest Earthquake Detection Application
This package will get the latest earthquake data from [ BMKG ](https://bmkg.go.id) |  Badan Meteorologi, Klimatologi, dan Geofisika



## HOW IT WORK ?



> The package will use BeautifulSoup4 and Requests, to produce output in the from of JSON that is ready to be used in web or mobile phone


## How to use
___

```python
import recent_earthquake


if __name__ == '__main__':
    
    result = recent_earthquake.ekstraksi_data()
    recent_earthquake.tampilkan_data(result)


```