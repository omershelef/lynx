lynx
====

Simple python configuration library and format. The format is very similar to YAML with the enhancment of sections.

##Installation

Install the ``lynx`` package with [pip](<https://pypi.python.org/pypi/lynx>):

    pip install lynx





##Example use

Configuration example:
```
# section example
section {
	# fields
	field1: myfield1 value
	field2: Another field value
	
	# lists
	mylist: [5, mystr, value, 8]
}


# Another section
section2 {
	
	# sub section example
	my_section {
		name: lynx
	}

	# sections can have same name.	
	my_section {
		Library description: Python configuration library
	}
}

```

Load the configuration:
```
>>> import lynx

# Load file
>>> with open("config.conf", "r") as fp:
...     config = lynx.load(fp)

# Get the first section
>>> config[0].name()
'section'
>>> config[0].fields()
{'field2': 'Another field value', 'field1': 'myfield1 value', 'mylist': ['5', ' mystr', ' value', ' 8']}

# Get sub sections
>>> config[1].sub_sections()
[<lynx.Section object at 0x7f4ab28dfdd0>, <lynx.Section object at 0x7f4ab28dfe10>]
>>> config[1].sub_sections()[0].name()
'my_section'
```



## Features

Features include:
* Sections
* Sub sections
* String fields
* Lists

