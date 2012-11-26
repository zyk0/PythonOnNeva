##Результаты профилирования.##


map:
--
    15000  167.553    0.011  167.553    0.011 map.py:24(<lambda>)   <== mymap
    15000  173.713    0.012  173.713    0.012 map.py:25(<lambda>)   <== built-in function
--
не понятно. Может быть неудачные данные для теста...

zip:
--
        1    2.019    0.000    2.350    0.000 zip.py:12(myzip)     <== myZip
        1    1.366    1.366    1.366    1.366 {zip}                <== built-in function
--

filter:
--
        1    4.933    0.000    7.159    0.000 filter.py:12(myfilter)     <== myFilter
        1    3.447    3.447    5.516    5.516 {filter}                   <== built-in function
--

reduce:
--
        1    0.120    0.120   26.871   26.871 reduce.py:12(myreduce)
        1   26.749    0.000   26.749    0.000 reduce.py:19(<lambda>)      <== myreduce
        1   26.573    0.000   26.573    0.000 reduce.py:20(<lambda>)      <== build-in 
--

