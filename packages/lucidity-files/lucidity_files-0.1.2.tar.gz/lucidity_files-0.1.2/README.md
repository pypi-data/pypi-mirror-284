
#  Lucidity Files

Lucidity Files is a project for listing files and folders using the popular Lucidity templating module.

Made this for another project called Lucidity Browser (Aka Browser) that handles files listing and contextual actions across many folders and templates. This was tested with good results in the production Bad Dinos at [Able & Baker studios](https://ableandbakerstudios.com/). Since the focus was on the Browser part, this end up not being a great thing, but it works.

Have not tested this in Mac or Linux, although I plan to do it.




## Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

![Python 2.7](https://img.shields.io/badge/Python-2-blue)

![Python 3.7](https://img.shields.io/badge/Python-3-blue)

![Windows](https://img.shields.io/badge/OS-Windows-blue)

![Windows](https://img.shields.io/badge/Status-Beta-yellow)


## Installation

Install module with pip

```bash
  python -m pip install lucidity_files
```

You can also target a folder like this (a pip thing, not anything i did)

```bash
  python -m pip install --target=P:\my\path lucidity_files
```

## Usage/Examples

```python
import os
import lucidity_files

# create 'asset' file template -------

# define roots for files (useful for different os or the farm)
roots = {'root': 'C:'}

# define a relative path from the root
pattern = '{root:[\w_.\-:]+}/{project}/{entitytype}/{entity}/{step}/{task}/{entity}_{step}_{task}_{name}_v{version}.{ext}'
lf_template = lucidity_files.TemplateFile.create('assets', pattern, roots=roots)

# lets create a file to be listed
path = r"C:\test\asset\car\mod\hi\car_mod_hi_default_v001.txt"

# we could also use the template to do this!
input_data = {'entity': 'car', 'entitytype': 'asset', 'ext': 'txt', 'name': 'default',
    'project': 'test', 'root': 'C:', 'step': 'mod', 'task': 'hi', 'version': '001'}
path2 = lf_template.format(input_data)
print(path == path2)
# will print True

os.makedirs(os.path.dirname(path), exist_ok=True)
with open(path, 'w'):
    pass


# list all assets in project 'test'
paths_found = lf_template.getPaths({'project': 'test'})

# now get each path's data
for path in paths_found:
    data = lf_template.parse(path)
    print(path)
    print('\t', data)

# # will print something like
# C:\test\asset\car\mod\hi\car_mod_hi_default_v001.txt
#          {'entity': 'car', 'entitytype': 'asset', 'ext': 'txt', 'name': 'default',
#  'project': 'test', 'root': 'C:', 'step': 'mod', 'task': 'hi', 'version': '001'}

# lets get a partial template to the entity folder
partial_template = lf_template.getPartialTemplateFile('entity')

# list all entity folders. Will use the strict check to make sure that what get listed
# is parsable with the same template (some other folders might match the glob but
# not the specifics of the template, and we want to avoid those)
paths_found = partial_template.getPaths({'project': 'test'}, strict_check=True)

# now get each path's data
for path in paths_found:
    print(path)
    data = partial_template.parse(path)
    print('\t', data)

# # will print something like
# C:\test\asset\car
#          {'entity': 'car', 'entitytype': 'asset', 'project': 'test', 'root': 'C:'}
# ...


```


## Documentation

[Documentation on Read The Docs](https://lucidity-files.readthedocs.io/en/latest/)




## Environment Variables

To run this project, you can add the following environment variables to your .env file

`LUCIDITY_TEMPLATE_PATH` 
Where you store files defining your lucidity templates.



## Acknowledgements

 - Thanks to Jordi Amposta, Angel Galindo and Marco Sancho for the patience while testing this in production!
 - This depends on the [Lucidity Project](https://pypi.org/project/Lucidity/), please check it out!

## Authors

- [eduardograna](https://gitlab.com/eduardograna)


## License

[MIT](https://choosealicense.com/licenses/mit/)


## Used By

This project is used by the following companies:

- [Able & Baker studios](https://ableandbakerstudios.com/)


## Roadmap

- Make module pip installable -> Done!

- Test on Linux (Ubuntu) -> Done!


## Support

For questions, email eduardo@eduardograna.com.

