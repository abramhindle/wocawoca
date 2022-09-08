# WOCaWOCa

Dumb utilities for working with World of Code (WOC)

## choosen.py

From a stream sample n elements without knowing the length of the stream.

```
seq 1 1000000 | python3 choosen.py 100 > /tmp/100elements.txt
```

Use only the memory of N elements.
